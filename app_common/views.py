from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import F, Q, Count
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection
from django.utils.decorators import method_decorator

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import permission_required
from django.db import transaction
from django.views.generic import View
from django.contrib.auth import get_user_model

from user_center import models as user_models
from app_common import models as common_models
from app_common import common
from department import models as department_models
from report_form import models as report_models
from app_common.tree import tree
from app_common.forms_verify import VerifyNav
from app_common import repositories as common_repositories
from app_common import config

import json,collections,xlrd,os,re,datetime,itertools,math,copy,time,pickle,locale

from dateutil.relativedelta import relativedelta
from pytz import timezone
from operator import itemgetter

from django.conf import settings
import sys,xlwt,threading
# Create your views here.


@login_required
def index(request):
    print(sys.stdout.encoding)
    data = common_repositories.get_annunciate()
    return render(request,'app_common/index.html',{"data":data})

@login_required
def nav(request):
    data = common_models.Nav.objects.all().order_by('sort').values()
    nav_list = tree(data).to_tree(pid_id=None, level=0, html='')
    return render(request,'app_common/nav.html',{"nav_list":nav_list})

@login_required
def add_nav(request):
    if request.method == "POST":
        data = request.POST.dict()
        is_show = True if data.get('is_show') == '1' else False
        pid = None if data.get('pid') == '0' else data.get('pid')
        verifier = VerifyNav(data, auto_id=False)  # 审核
        if verifier.is_valid():
            try:
                common_models.Nav.objects.get(name=verifier.cleaned_data['name'],pid_id=pid)
            except common_models.Nav.DoesNotExist:
                if pid:
                    p_info = common_models.Nav.objects.get(id=pid)
                    permission_name = p_info.name+'_'+verifier.cleaned_data['name']
                else:
                    permission_name = verifier.cleaned_data['name']
                content_type = ContentType.objects.get_for_model(common_models.Nav)
                permission = Permission.objects.create(codename=permission_name, name=permission_name,content_type=content_type)

                common_models.Nav.objects.create(name=verifier.cleaned_data['name'],pid_id=pid,is_show=is_show,icon=data.get('icon',''),sort=verifier.cleaned_data['sort'],url=data.get('url','#'),permission=permission)

                return JsonResponse({"code": "200", "message": "添加成功", "data": []})
            else:
                return JsonResponse({"code": "-1", "message": "导航名称已经存在", "data": []})
        else:
            one_error = list(json.loads(verifier.errors.as_json()).items())[0][1][0]['message']
            return JsonResponse({"code": "-1", "message": one_error, "data": []})
    else:
        #top_navs = common_models.Nav.objects.filter(pid__isnull=True).values()
        data = common_models.Nav.objects.all().values()
        nav_list = tree(data).to_tree(pid_id=None, level=0, html='')
        return render(request, 'app_common/add_nav.html',{"nav_list":nav_list})

@login_required
@transaction.atomic
def edit_nav(request):  # 编辑
    nav_id = request.GET.get('id')
    if request.method == "POST":
        data = request.POST.dict()
        is_show = True if data.get('is_show') == '1' else False
        pid = None if data.get('pid') == '0' else data.get('pid')
        verifier = VerifyNav(data, auto_id=False)
        if verifier.is_valid():
            try:
                common_models.Nav.objects.get(Q(name=verifier.cleaned_data['name']) & ~Q(id=nav_id) & Q(pid_id=pid))
            except common_models.Nav.DoesNotExist:
                obj = common_models.Nav.objects.get(id=nav_id)
                obj.name=verifier.cleaned_data['name']
                obj.pid_id=pid
                obj.is_show=is_show
                obj.icon=data.get('icon','')
                obj.sort = verifier.cleaned_data['sort']
                obj.url=data.get('url','#')
                obj.save()

                if obj.pid:
                    permission_name = obj.pid.name+'_'+verifier.cleaned_data['name']
                else:
                    permission_name = verifier.cleaned_data['name']

                obj.permission.name = permission_name
                obj.permission.codename = permission_name
                obj.permission.save()
                return JsonResponse({"code": "200", "message": "编辑成功", "data": []})
            else:
                return JsonResponse({"code": "-1", "message": "导航名称已经存在", "data": []})
        else:
            one_error = list(json.loads(verifier.errors.as_json()).items())[0][1][0]['message']
            return JsonResponse({"code": "-1", "message": one_error, "data": []})
    else:
        #top_navs = common_models.Nav.objects.filter(Q(pid__isnull=True) & ~Q(id=nav_id)).values()
        nav_info = common_models.Nav.objects.get(id=nav_id)
        data = common_models.Nav.objects.filter(~Q(id=nav_id)).values()
        nav_list = tree(data).to_tree(pid_id=None, level=0, html='')
        return render(request, 'app_common/add_nav.html',{"nav_list":nav_list,"nav_info":nav_info})

@login_required
def del_nav(request):
    nav_id = request.GET.get('id')
    obj = common_models.Nav.objects.get(id=nav_id)

    permission_ids = list(obj.nav_set.all().values_list('permission_id', flat=True))
    print(permission_ids)
    Permission.objects.filter(id__in=permission_ids).delete()

    obj.permission.delete()
    obj.delete()
    return JsonResponse({"code": "200", "message": "删除成功", "data": []})

@login_required
def group_auth(request):  # 用户组
    department_id = request.GET.get('id')
    obj = department_models.Department.objects.get(id=department_id)
    if request.method == 'POST':
        permission_ids = request.POST.getlist('permission')
        group = obj.group
        if group == None or group == '':
            messages.error(request, '用户组不存在')
            return HttpResponseRedirect('/app_common/group_auth/?id='+department_id)
        else:
            permission_list = list(Permission.objects.filter(id__in=permission_ids))
            group.permissions = permission_list
            return HttpResponseRedirect('/app_common/group_auth/?id=' + department_id)
    else:
        permission_ids = obj.group.permissions.all().values_list('id',flat=True)
        data = common_models.Nav.objects.all().order_by('sort').values()
        nav_list = tree(data).to_tree(pid_id=None, level=0, html='')
        print(permission_ids)
        return render(request,'app_common/group_auth.html',{"nav_list":nav_list,"permission_ids":permission_ids,"obj":obj})

def upload_data(request):  # 上传文件
    dirpath = request.path.replace('/app_common/upload_data','')

    if dirpath[::-1][0] == '/':
        dirpath = dirpath[:-1]

    request_dir = dirpath.split('/')
    request_dir = [v for v in request_dir if v != '']

    ol_path_list = []
    ol_path = ''
    for v in request_dir:
        ol_path += v+'/'
        ol_path_list.append([v,ol_path])
    #print(ol_path_list)

    if len(request_dir) > 0:
        if len(request_dir) >1:
            join_request_dir = request_dir[:-1]
            prev_request_dir = '/'.join(join_request_dir)
        else:
            prev_request_dir = ''
        curr_request_dir = '/'.join(request_dir)
    else:
        prev_request_dir = None
        curr_request_dir = None

    department_view_dir = "政策落实按部门分类数据"
    view_dir = os.path.join("E:/job/data", department_view_dir)
    dir_path = os.path.join(view_dir, (curr_request_dir or '')).replace('\\','/')

    print(dir_path)
    if os.path.isdir(dir_path):
        try:
            res = os.listdir(dir_path)
        except:
            dirlist = []
            filelist = []
        else:
            dirlist = []
            filelist = []
            for f in res:
                file_update_time = os.path.getmtime(dir_path + '/' + f)
                file_update_time = datetime.datetime.utcfromtimestamp(file_update_time)+datetime.timedelta(hours=8)

                if (os.path.isdir(dir_path + '/' + f)):
                    # 排除隐藏文件夹。因为隐藏文件夹过多
                    if (f[0] == '.'):
                        pass
                    else:
                        # 添加非隐藏文件夹
                        dirlist.append({"name":f,"update_time":file_update_time})
                if (os.path.isfile(dir_path + '/' + f)):
                    if (f[0] == '.'):
                        pass
                    else:
                        # 添加文件
                        filelist.append({"name":f,"update_time":file_update_time})
        print(curr_request_dir,dirlist)
        return render(request, 'app_common/upload_data.html', {
            "dirlist": dirlist,
            "filelist": filelist,
            "curr_request_dir":curr_request_dir if curr_request_dir != None else None,
            "prev_request_dir":prev_request_dir if prev_request_dir != None else None,
            "ol_path_list":ol_path_list
        })
    else:
        return render(request, 'app_common/error.html', {"msg": "目录不存在！"})

class Annunciate(View):  # 通告
    def get(self,request):
        id = request.GET.get('id')
        if id:
            obj = common_models.Annunciate.objects.get(id=id)
            attach_path = obj.attach_path[32:]
            return render(request,'app_common/annunciate/get.html',{"data":obj,"attach_path":attach_path})
        else:
            return render(request, 'app_common/annunciate/get.html')

    def post(self,request):
        form_type = request.POST.get('form_type')
        path = os.path.join(settings.BASE_DIR, 'common/upload/attachments/').replace('\\', '/')
        if form_type == 'add':
            title = request.POST.get('title')
            content = request.POST.get('content')
            attach_obj = request.FILES.get('file',None)
            attach_path = ''
            if attach_obj != None:
                axt = os.path.splitext(attach_obj.name)[0]
                ext = os.path.splitext(attach_obj.name)[1]
                file_name = common.get_uuid()+axt
                _, attach_path = common.upload_file(path,file_name,attach_obj)

            obj = common_models.Annunciate.objects.create(title=title,content=content,attach_path=attach_path)

            update_obj = copy.deepcopy(obj)
            common.log(user_id=request.user.id, model_path='app_common.models.Annunciate', type='add',update_obj=update_obj)  # 记录日志
            return render(request,'app_common/annunciate/get.html',{"message":"add success","obj":obj})
        elif form_type == 'edit':
            id = request.POST.get('id')
            attach_obj = request.FILES.get('file', None)
            obj = common_models.Annunciate.objects.get(id=id)

            old_obj = copy.deepcopy(obj)

            attach_path = None
            if attach_obj != None:
                path = os.path.join(settings.BASE_DIR,'common/upload/attachments/').replace('\\','/')
                axt = os.path.splitext(attach_obj.name)[0]
                ext = os.path.splitext(attach_obj.name)[1]
                file_name = common.get_uuid()+axt
                _, attach_path = common.upload_file(path,file_name,attach_obj)

                old_attach_path = os.path.join(path,obj.attach_path)
                if os.path.isfile(old_attach_path):
                    os.remove(old_attach_path)

            obj.title = request.POST.get('title')
            obj.content = request.POST.get('content')
            if attach_path != None:
                obj.attach_path = attach_path
            obj.save()

            update_obj = copy.deepcopy(obj)
            common.log(user_id=request.user.id, model_path='app_common.models.Annunciate', type='update',old_obj=old_obj,
                       update_obj=update_obj) # 记录日志
            return HttpResponseRedirect('/app_common/annunciate_info/?id='+id)

def annunciate_info(request): # 通告信息
    id = request.GET.get('id')
    obj = common_models.Annunciate.objects.get(id=id)
    attach_path = obj.attach_path[32:]  # 附加
    return render(request,'app_common/annunciate/info.html',{"obj":obj,"attach_path":attach_path})

def annunciate_delete(request):  # 删除通告
    id = request.GET.get('id')
    path = os.path.join(settings.BASE_DIR, 'common/upload/attachments/').replace('\\', '/')
    obj = common_models.Annunciate.objects.get(id=id)

    old_obj = copy.deepcopy(obj)

    old_attach_path = os.path.join(path, obj.attach_path)
    if os.path.isfile(old_attach_path):
        os.remove(old_attach_path)

    obj.delete()
    common.log(user_id=request.user.id, model_path='app_common.models.Annunciate', type='delete', old_obj=old_obj)  # 记录日志
    return JsonResponse({"code":"200","message":"删除成功！"})

class GovernmentDecree(View): #  政令
    def get(self,request):
        id = request.GET.get('id')
        if id:
            obj = common_models.GovernmentDecree.objects.get(id=id)
            attach_path = obj.attach_path[32:]
            return render(request,'app_common/governmentdecree/get.html',{"data":obj,"attach_path":attach_path})
        else:
            return render(request, 'app_common/governmentdecree/get.html')

    def post(self,request):
        form_type = request.POST.get('form_type')
        if form_type == 'add':
            title = request.POST.get('title')
            content = request.POST.get('content')
            attach_obj = request.FILES.get('file',None)
            attach_path = ''
            if attach_obj != None:
                path = os.path.join(settings.BASE_DIR,'common/upload/attachments/').replace('\\','/')
                axt = os.path.splitext(attach_obj.name)[0]
                ext = os.path.splitext(attach_obj.name)[1]
                file_name = common.get_uuid()+axt
                _, attach_path = common.upload_file(path,file_name,attach_obj)

            obj = common_models.GovernmentDecree.objects.create(title=title,content=content,attach_path=attach_path)

            update_obj = copy.deepcopy(obj)
            common.log(user_id=request.user.id, model_path='app_common.models.GovernmentDecree', type='add',old_obj=None,update_obj=update_obj)  # 记录日志
            return render(request,'app_common/governmentdecree/get.html',{"message":"add success","obj":obj})
        elif form_type == 'edit': # 编辑
            id = request.POST.get('id')
            attach_obj = request.FILES.get('file', None)
            obj = common_models.GovernmentDecree.objects.get(id=id)
            old_obj = copy.deepcopy(obj)

            attach_path = None
            if attach_obj != None:
                path = os.path.join(settings.BASE_DIR,'common/upload/attachments/').replace('\\','/')
                axt = os.path.splitext(attach_obj.name)[0]
                ext = os.path.splitext(attach_obj.name)[1]
                file_name = common.get_uuid()+axt
                _, attach_path = common.upload_file(path,file_name,attach_obj)

                old_attach_path = os.path.join(path,obj.attach_path)
                if os.path.isfile(old_attach_path):
                    os.remove(old_attach_path)

            obj.title = request.POST.get('title')
            obj.content = request.POST.get('content')
            if attach_path != None:
                obj.attach_path = attach_path
            obj.save()

            update_obj = copy.deepcopy(obj)
            common.log(user_id=request.user.id, model_path='app_common.models.GovernmentDecree', type='update',old_obj=old_obj,update_obj=update_obj)  # 记录日志
            return HttpResponseRedirect('/app_common/governmentdecree_info/?id='+id)

@login_required()
def governmentdecree_info(request): # 政令信息
    id = request.GET.get('id')
    obj = common_models.GovernmentDecree.objects.get(id=id)
    attach_path = obj.attach_path[32:]
    return render(request,'app_common/governmentdecree/info.html',{"obj":obj,"attach_path":attach_path})

def governmentdecree_delete(request):
    id = request.GET.get('id')
    path = os.path.join(settings.BASE_DIR, 'common/upload/attachments/').replace('\\', '/')
    obj = common_models.GovernmentDecree.objects.get(id=id)
    old_obj = copy.deepcopy(obj)

    old_attach_path = os.path.join(path, obj.attach_path)
    if os.path.isfile(old_attach_path):
        os.remove(old_attach_path)

    obj.delete()

    common.log(user_id=request.user.id, model_path='app_common.models.GovernmentDecree', type='delete', old_obj=old_obj,update_obj=None)  # 记录日志
    return JsonResponse({"code":"200","message":"删除成功！"})

@login_required()
def log_list(request):  # 日志及审计
    page = request.GET.get('page', 1)

    count_sql = "select count(id) from app_common_logs;"
    count_res = list(common_models.Logs.objects.raw(count_sql).query)
    count = count_res[0][0]

    # ***分页start
    every_page_number = 15
    try:
        page = int(page)
    except:
        page = 1

    num_pages = math.ceil(count / every_page_number)
    if page > num_pages:
        page = num_pages
    if page <= 0:
        page = 1
    # ***分页end
    limit_start = str(int((page - 1) * 15))

    sql = "select *,(select name from user_center_userextra where user_id = app_common_logs.user_id limit 1) as user_name from app_common_logs order by action_time desc LIMIT "+limit_start+","+str(every_page_number)+";"
    logs = common_models.Logs.objects.raw(sql)

    data = list(logs)

    return render(request,'app_common/logs/list.html',{
        "page": page,
        "count": count,
        "data":data
    })

def log_detail(request):  # 详情
    log_id = request.GET.get('id')
    info = common_models.Logs.objects.get(id=log_id)
    return render(request,'app_common/logs/detail.html',{
        "info":info
    })

#意见反馈
@login_required()
def feedback_list(request):
    page = request.GET.get('page', 1)
    keyword = request.GET.get('keyword','')
    if keyword:
        user_ids = user_models.UserExtra.objects.filter(Q(name__contains=keyword)|Q(mobile__contains=keyword)).values_list('about_id',flat=True)
        user_ids = [str(value) for value in user_ids]
        user_join_ids = ','.join(user_ids)
        print(user_join_ids)
        search_condition = "user_id in ("+user_join_ids+")"
    else:
        search_condition = '1=1'
    count_sql = "select count(id) from app_common_feedbacks WHERE "+search_condition+";"
    count_res = list(common_models.Logs.objects.raw(count_sql).query)
    count = count_res[0][0]

    # ***分页start
    every_page_number = 10
    try:
        page = int(page)
    except:
        page = 1

    num_pages = math.ceil(count / every_page_number)
    if page > num_pages:
        page = num_pages
    if page <= 0:
        page = 1
    # ***分页end
    limit_start = str(int((page - 1) * every_page_number))

    sql = "select *,(select name from user_center_userextra where user_id = app_common_feedbacks.user_id limit 1) as user_name,(select mobile from user_center_userextra where user_id = app_common_feedbacks.user_id limit 1) as mobile from app_common_feedbacks WHERE "+search_condition+" order by create_time desc LIMIT "+limit_start+","+str(every_page_number)+";"
    feedbacks = common_models.Feedbacks.objects.raw(sql)

    data = list(feedbacks)

    return render(request,'app_common/feedbacks/list.html',{
        "page": page,
        "count": count,
        "data":data
    })

@login_required()
def feedback_export(request):  # 基层反馈
    date_start = request.GET.get('date_start')
    date_end = request.GET.get('date_end')

    search_condition = "create_time between '"+date_start+"' and '"+date_end+"'"
    sql = "select *,(select name from user_center_userextra where user_id = app_common_feedbacks.user_id limit 1) as user_name,(select mobile from user_center_userextra where user_id = app_common_feedbacks.user_id limit 1) as mobile from app_common_feedbacks WHERE " + search_condition + " order by create_time asc;"

    feedbacks = common_models.Feedbacks.objects.raw(sql)
    data = [['反馈人','反馈人电话','反馈时间','反馈内容','处理结果']]
    for value in feedbacks:
        data.append([value.user_name,value.mobile,value.create_time.strftime('%Y-%m-%d'),value.content,value.remarks])

    path = os.path.join(settings.BASE_DIR,'common/export/').replace('\\','/')
    if os.path.isdir(path) == False:
        os.mkdir(path)
    file_name = '基层反馈处理.xls'

    wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)  ##第二参数用于确认同一个cell单元是否可以重设值。


    style_common = xlwt.easyxf('font: name Times New Roman, color-index black,height 0x0012c;align: wrap on, vert centre, horiz center;')

    for key,value in enumerate(data):
        for k,v in enumerate(value):
            sheet.write(key+1, k, v, style_common)

    for k,v in enumerate(data):
        sheet.col(k).width = 0x0d00 + 250*len(v[0])

    title = date_start+'至'+date_end+' 基层反馈处理'
    sheet.write_merge(0, 0, 0, len(data[0])-1, title, xlwt.easyxf('font: name Times New Roman, color-index black,bold on,height 0x0012c;align: wrap on, vert centre, horiz center;'))

    wbk.save(path+file_name)  ##该文件路径必须存在
    return HttpResponseRedirect('/common/export/' + file_name)

@login_required()
def affirm_feedback(request):  # 确认反馈
    obj_id = request.GET.get('obj_id')
    obj = common_models.Feedbacks.objects.get(id=obj_id)
    obj.status = 1
    obj.save()
    return JsonResponse({"code":"200"})

@login_required()
def edit_remarks(request):  # 编辑评论
    remarks = request.POST.get('remarks','')
    obj_id = request.POST.get('obj_id','')

    if remarks.strip() == '':
        return JsonResponse({"code":"-1","message":"不能为空"})
    else:
        obj = common_models.Feedbacks.objects.get(id=obj_id)
        obj.remarks = remarks
        obj.save()
        return JsonResponse({"code": "200", "message": "编辑成功"})

#短信通知
@login_required()
def sms_inform(request):
    department_list = department_models.Department.objects.all()
    return render(request,'app_common/sms_inform.html',{"department_list":department_list})

#通知个人
@login_required()
def sms_inform_people(request):
    mobile = request.POST.get('mobile')
    content = request.POST.get('content')

    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeStruct = time.localtime(now)
    date = time.strftime("%Y-%m-%d", timeStruct)

    params = {
        "time": date,
        "content":content
    }
    param_str = json.dumps(params, separators=(',', ':'))

    res = common.send_sms(str(mobile), "阿里云短信测试专用", "SMS_140735959",param_str)

    return JsonResponse(res,safe=False)

#通知部门
@login_required()
def sms_inform_department(request):
    department_id = request.POST.get('department_id')
    content = request.POST.get('content')

    mobile_list = user_models.UserExtra.objects.filter(department_id=department_id).values_list('mobile',flat=True)
    mobile_list = [v for v in mobile_list if len(str(v)) == 11]
    if len(mobile_list) == 0:
        return JsonResponse({"code":"200","message":"发送成功"}, safe=False)
    else:
        mobile_list_join = ','.join(mobile_list)

        # 获得当前时间时间戳
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeStruct = time.localtime(now)
        date = time.strftime("%Y-%m-%d", timeStruct)

        params = {
            "time": date,
            "content":content
        }
        param_str = json.dumps(params, separators=(',', ':'))

        res = common.send_sms(mobile_list_join, "阿里云短信测试专用", "SMS_140735959",param_str)
        return JsonResponse(res, safe=False)

@login_required()
def screen_common(request):  # 扶贫数据概况
    return render(request,'app_common/screen_common.html')

@login_required()
def screen(request):  #大屏显示
    return render(request,'app_common/screen.html')

def main1(request):

    # sql = 'select count(id),offpoor_year from report_form_poorhousedataform  GROUP BY offpoor_year'
    # cursor = connection.cursor()
    # cursor.execute(sql)
    # house_by_offpoor_year = cursor.fetchall()  # 读取所有
    # print(house_by_offpoor_year)
    #
    # house_by_offpoor_year_item = {}
    # for key,value in house_by_offpoor_year:
    #     if len(value) >= 4:
    #         house_by_offpoor_year_item[value[:4]] = key


    sql1 = "select sum(fact_money),date_year from (select policy_number,fact_money,date_year from report_form_administrativevillageadditionalform UNION ALL select policy_number,fact_money,date_year from report_form_poorhouseadditionalform UNION ALL select policy_number,fact_money,date_year from report_form_poorpeopleadditionalform) as staticstics_table GROUP BY date_year;"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    fact_moneys = cursor1.fetchall()  # 读取所有
    # print('---------------------------------1111111111111111')
    # print(fact_moneys)

    pol_money_dict_list = collections.defaultdict(list)
    for money, year in fact_moneys:
        if len(year) >= 4:
            try:
                money = float(money)
            except:
                money = 0
            pol_money_dict_list[year[:4]].append(money)

    pol_money_dict = {}
    for key,value in pol_money_dict_list.items():
        pol_money_dict[key] = sum(value)/1000

    years = list(pol_money_dict.keys())#+list(house_by_offpoor_year_item.keys())
    years = list(set(years))
    years.sort()

    path = os.path.join(settings.BASE_DIR, 'common/data/' + config.DATA_DICT['overcome_poverty'])
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            overcome_poverty_dict = pickle.load(f)
        if isinstance(overcome_poverty_dict,dict):
            is_nothave_overcome_poverty_data = False
        else:
            is_nothave_overcome_poverty_data = True
    else:
        overcome_poverty_dict = {}
        is_nothave_overcome_poverty_data = True

    pol_money_list = []
    #house_by_offpoor_count_list = []
    overcome_poverty_list = []
    for value in years:
        pol_money_list.append(pol_money_dict.get(value,0))
        #house_by_offpoor_count_list.append(house_by_offpoor_year_item.get(value,0))
        if is_nothave_overcome_poverty_data == False:
            overcome_poverty_list.append(overcome_poverty_dict.get(value,0))

    print(pol_money_list)
    #print(house_by_offpoor_count_list)
    # pol_money_dict_item = sorted(pol_money_dict.items(),key=lambda x:x[0])
    # for key,value in pol_money_dict_item:
    #     pol_money_list.append(value)

    return JsonResponse({
        #"pol_money_dict":dict(pol_money_dict),
        "is_nothave_overcome_poverty_data":is_nothave_overcome_poverty_data,
        "overcome_poverty_list":overcome_poverty_list,
        "pol_money_list":pol_money_list,
        "years":years,
        #"house_by_offpoor_count_list":house_by_offpoor_count_list,
        #"house_by_offpoor_year_list":house_by_offpoor_year_list
    },safe=False)

def main2(request):
    sql = "select group_concat(policy_number),policy_first_layer from report_form_policystaticform GROUP BY policy_first_layer"
    cursor = connection.cursor()
    cursor.execute(sql)
    policys = cursor.fetchall()  # 读取所有

    pol_ids = {}
    for key, value in policys:
        pol_ids[value] = key.split(',')
    # print(pol_ids)

    sql1 = "select policy_number,sum(fact_money),date_year from (select policy_number,fact_money,date_year from report_form_administrativevillageadditionalform UNION ALL select policy_number,fact_money,date_year from report_form_poorhouseadditionalform UNION ALL select policy_number,fact_money,date_year from report_form_poorpeopleadditionalform) as staticstics_table GROUP BY policy_number,date_year;"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    fact_moneys = cursor1.fetchall()  # 读取所有
    # print(fact_moneys)

    pol_money_dict = {}
    for p_id, money, year in fact_moneys:
        pol_money_dict[year[:4]] = collections.defaultdict(list)
        pol_money_dict['all'] = collections.defaultdict(list)
    for p_id, money,year in fact_moneys:
        for pol, ids in pol_ids.items():
            if p_id in ids:
                try:
                    money = float(money)
                except:
                    money = 0
                pol_money_dict[year[:4]][pol].append(money)
                pol_money_dict['all'][pol].append(money)

    pol_money_dict_item = collections.defaultdict(list)
    for year, pol_data in pol_money_dict.items():
        for pol,money_list in pol_data.items():
            pol_money_dict_item[year].append({"name":pol,"value":sum(money_list)})

    years = list(pol_money_dict_item.keys())
    years.sort()
    return JsonResponse({
        "pol_money_dict_item":dict(pol_money_dict_item),
        "policys":list(pol_ids.keys()),
        "years":years
    },safe=False)

def main3(request):
    sql = "select group_concat(now_village_identifier),town_name from report_form_administrativevillagedataform GROUP BY town_name"
    cursor = connection.cursor()
    cursor.execute(sql)
    towns = cursor.fetchall()  # 读取所有

    town_ids = {}
    for key, value in towns:
        town_ids[value] = key.split(',')
    # print(village_ids)

    sql1 = "select now_village_identifier,count(id) as count_num from report_form_poorhousedataform GROUP BY now_village_identifier;"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    village_count = cursor1.fetchall()  # 读取所有


    village_count_dict = collections.defaultdict(list)
    for now_village_identifier, count_num in village_count:
        for town, ids in town_ids.items():
            if now_village_identifier in ids:
                village_count_dict[town].append(count_num)

    town_count_dict = []
    for town,count_list in village_count_dict.items():
        town_count_dict.append({"name": town, "value": sum(count_list)})

    return JsonResponse({
        "town_count_dict":town_count_dict,
        "towns":list(town_ids.keys()),
    },safe=False)

def main4(request):
    sql = "select group_concat(now_village_identifier),town_name from report_form_administrativevillagedataform GROUP BY town_name"
    cursor = connection.cursor()
    cursor.execute(sql)
    towns = cursor.fetchall()  # 读取所有

    town_ids = {}
    for key, value in towns:
        town_ids[value] = key.split(',')
    # print(village_ids)

    sql1 = "select house_identifier,count(id) as count_num from report_form_poorpeopledataform GROUP BY house_identifier;"
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    house_count = cursor1.fetchall()  # 读取所有

    sql2 = "select group_concat(house_identifier),now_village_identifier from report_form_poorhousedataform GROUP BY now_village_identifier;"
    cursor2 = connection.cursor()
    cursor2.execute(sql2)
    village_house_ids= cursor2.fetchall()  # 读取所有

    town_house_ids = collections.defaultdict(list)
    for town,ids in town_ids.items():
        for house_ids,village in village_house_ids:
            if village in ids:
                town_house_ids[town] += house_ids.split(',')

    #print(town_house_ids)
    town_count_dict = collections.defaultdict(list)
    for town,ids in town_house_ids.items():
        for house_id,count_num in house_count:
            if house_id in ids:
                town_count_dict[town].append(count_num)

    town_count_dict_item = []
    for town,count_num_list in town_count_dict.items():
        town_count_dict_item.append({"name":town,"value":sum(count_num_list)})

    return JsonResponse({
        "town_count_dict":town_count_dict_item,
        "towns":list(town_ids.keys()),
    },safe=False)


def main5(request):
    sql = 'select count(id),poor_reason from report_form_poorpeopledataform GROUP BY poor_reason'
    cursor = connection.cursor()
    cursor.execute(sql)
    poor_reason_group = cursor.fetchall()  # 读取所有
    print(poor_reason_group)

    poor_reason_item = []
    poor_reason_list = []
    for key,value in poor_reason_group:
        poor_reason_item.append({"name":value,"value":key})
        poor_reason_list.append(value)

    return JsonResponse({
        "poor_reason_item":poor_reason_item,
        "poor_reason_list":poor_reason_list
    },safe=False)

def save_overcome_poverty(request):
    years = request.POST.getlist('years[]')
    overcome_poverty_list = request.POST.getlist('overcome_poverty_list[]')
    data = dict(zip(years,overcome_poverty_list))

    path = os.path.join(settings.BASE_DIR, 'common/data/'+config.DATA_DICT['overcome_poverty'])
    with open(path, 'wb') as f:
        pickle.dump(data, f)

    return JsonResponse(overcome_poverty_list,safe=False)

@login_required
def help_list(request):  # 帮助中心
    helps = common_models.HelpCenter.objects.all()
    return render(request,'app_common/help_list.html',{"helps":helps})

class DataView(View):  # 乡镇数据概况
    def __init__(self):
        village_all = report_models.AdministrativeVillageDataForm.objects.all().values('town_name','now_village_identifier','now_administrative_village').order_by('now_village_identifier')
        policys = report_models.PolicyStaticForm.objects.all().order_by('policy_first_layer')
        self.policys = policys

        village_data = collections.defaultdict(dict)
        for value in village_all:
            village_data[value['town_name']][value['now_village_identifier']] = value['now_administrative_village']

        self.village_data = village_data

        super(DataView, self).__init__()

    @method_decorator(login_required)
    def get(self,request):
        town_name = request.GET.get('town_name', '')
        policy_number = request.GET.get('policy_number', '')
        now_village_identifier = request.GET.get('now_village_identifier', '').strip()
        date_start = request.GET.get('date_start', '').strip()
        date_end = request.GET.get('date_end', '').strip()

        if policy_number == '':
            return render(request, 'app_common/data_view.html', {
                "policys": self.policys,
                "village_data": self.village_data,
                "village_data_str": json.dumps(self.village_data)
            })

        policy_obj = report_models.PolicyStaticForm.objects.get(policy_number=policy_number)

        #搜索-start
        search_condition = ''
        search_condition_house = ''
        search_condition_people = ''
        search_condition_industry_agritainment = ''
        main_sql = ''
        #if town_name != '':
            #main_sql = " where town_name='"+town_name+"'"
            # if now_village_identifier != '':
            #     main_sql += " and now_village_identifier = '"+now_village_identifier+"'"

        # search_condition_house += "householder_id in (select householder_id from report_form_poorhousedataform where now_village_identifier=b.now_village_identifier) and "
        # search_condition_people += "people_id in (select people_id from report_form_poorpeopledataform where house_identifier in (select house_identifier from report_form_poorhousedataform where now_village_identifier=b.now_village_identifier)) and "
        #search_condition_people += "people_id in (select people_id from report_form_poorpeopledataform as people_table join report_form_poorhousedataform as house_table on people_table.house_identifier = house_table.house_identifier where house_table.now_village_identifier=b.now_village_identifier) and "




        if date_start != '':
            date_start_list = date_start.split('-')
            search_condition += "(date_year > "+date_start_list[0]+" or (date_year = "+date_start_list[0]+" and date_month > "+date_start_list[1]+")) and "
            search_condition_house += "(date_year > " + date_start_list[0] + " or (date_year = " + date_start_list[
                0] + " and date_month > " + date_start_list[1] + ")) and "
            search_condition_people += "(date_year > "+date_start_list[0]+" or (date_year = "+date_start_list[0]+" and date_month > "+date_start_list[1]+")) and "

        if date_end != '':
            date_end_list = date_end.split('-')
            search_condition += "(date_year < " + date_end_list[0] + " or (date_year = " + date_end_list[0] + " and date_month < " + date_end_list[1] + ")) and "
            search_condition_house += "(date_year < " + date_end_list[0] + " or (date_year = " + date_end_list[
                0] + " and date_month < " + date_end_list[1] + ")) and "
            search_condition_people += "(date_year < " + date_end_list[0] + " or (date_year = " + date_end_list[0] + " and date_month < " + date_end_list[1] + ")) and "
        if date_start != '' and date_end != '':
            search_condition_industry_agritainment += "grant_date > "+(date_start_list[0]+date_start_list[1])+" and grant_date < "+(date_end_list[0]+date_end_list[1])
        #搜索-end

        village_data_dict = {}
        if town_name != '':
            main_sql = " where town_name='" + town_name + "'"
            village_list = list(report_models.AdministrativeVillageDataForm.objects.filter(town_name=town_name).values('now_village_identifier','now_administrative_village'))
            village_list = [v['now_village_identifier']+'_'+v['now_administrative_village'] for v in village_list]
            village_list_set = set(village_list)
            villages = [v.split('_') for v in village_list_set]
            for value in villages:
                search_condition_copy = copy.deepcopy(search_condition)
                search_condition_house_copy = copy.deepcopy(search_condition_house)
                search_condition_people_copy = copy.deepcopy(search_condition_people)
                search_condition_industry_agritainment_copy = copy.deepcopy(search_condition_industry_agritainment)
                village_list_obj = report_models.AdministrativeVillageDataForm.objects.filter(
                    now_village_identifier=value[0])
                householder_id_identifier = report_models.PoorHouseDataForm.objects.filter(
                    now_village_identifier=value[0]).values('householder_id', 'house_identifier')

                householder_ids = [v['householder_id'] for v in householder_id_identifier]
                householder_ids = ["'" + v + "'" for v in householder_ids]
                householder_ids_s = ','.join(householder_ids)
                if householder_ids_s == '':
                    search_condition_house_copy += "1 = 2 and "
                else:
                    search_condition_house_copy += "householder_id in (" + householder_ids_s + ") and "

                house_identifiers = [v['house_identifier'] for v in householder_id_identifier]
                people_ids = report_models.PoorPeopleDataForm.objects.filter(
                    house_identifier__in=house_identifiers).values_list('people_id', flat=True)
                people_ids = ["'" + v + "'" for v in people_ids]
                people_ids_s = ','.join(people_ids)
                if people_ids_s == '':
                    search_condition_people_copy += "1 = 2 and "
                else:
                    search_condition_people_copy += "people_id in (" + people_ids_s + ") and "

                if len(village_list_obj) > 0:
                    village_obj = village_list_obj[0]
                    search_condition_industry_agritainment_copy += "town_name = '" + village_obj.town_name + "' and administrative_village = '" + village_obj.now_administrative_village + "' and "

                search_condition += "now_village_identifier = '" + value[0] + "' and "

                search_condition_copy += "policy_number="+policy_number
                search_condition_house_copy += "policy_number=" + policy_number
                search_condition_people_copy += "policy_number=" + policy_number


                if policy_obj.policy_object == '贫困村':
                    search_ = search_condition_copy
                    form = "report_form_administrativevillageadditionalform"
                    group_by = "now_village_identifier"
                elif policy_obj.policy_object == '贫困户':
                    search_ = search_condition_house_copy
                    form = "report_form_poorhouseadditionalform"
                    group_by = "householder_id"
                elif policy_obj.policy_object == '贫困人口':
                    search_ = search_condition_people_copy
                    form = "report_form_poorpeopleadditionalform"
                    group_by = "people_id"
                elif  policy_obj.policy_object == '农家乐吸纳就业':
                    search_ = search_condition_industry_agritainment_copy
                    form = "report_form_industryagritainmentdataform"
                    group_by = "agritainment_id"


                if policy_obj.policy_object == '农家乐吸纳就业':
                    concat_ws = "id,concat_ws(',',ifnull(SUM(subsidy_multiplier),0),ifnull(SUM(plan_subsidy),0),ifnull(SUM(fact_subsidy),0)) as sum_data"
                    sum_ws = "count(id) as count_id,ifnull(SUM(subsidy_multiplier),0) as policy_multiplier_,ifnull(SUM(plan_subsidy),0) as plan_money_,ifnull(SUM(fact_subsidy),0) as fact_money_"
                else:
                    concat_ws = "id,concat_ws(',',ifnull(SUM(policy_multiplier),0),ifnull(SUM(plan_money),0),ifnull(SUM(fact_money),0)) as sum_data"
                    sum_ws = "count(id) as count_id,ifnull(SUM(policy_multiplier),0) as policy_multiplier_,ifnull(SUM(plan_money),0) as plan_money_,ifnull(SUM(fact_money),0) as fact_money_"

                #,(select count(*) from (select id from "+form+" WHERE "+search_+" group by "+group_by+") as a) as count_id
                sql = "select count(*),ifnull(sum(policy_multiplier_),0),ifnull(sum(plan_money_),0),ifnull(sum(fact_money_),0) from (select "+sum_ws+" from "+form+" where "+search_+" group by "+group_by+") as a"
                #sql = "select "+concat_ws+" from "+form+" WHERE "+search_
                print(sql)
                #data = list(report_models.AdministrativeVillageAdditionalForm.objects.raw(sql))
                cursor = connection.cursor()
                cursor.execute(sql)
                data = cursor.fetchone()

                village_data_dict[value[1]] = data
                # print(len(data))
                # for key, value in enumerate(data):
                #     sum_data_split = value.sum_data.split(',')
                #     # print(sum_data_split)
                #     # sum_data = []
                #     # for v in sum_data_split:
                #     #     try:
                #     #         float(v)
                #     #     except:
                #     #         sum_data.append(0.00)
                #     #     else:
                #     #         sum_data.append(float(v))
                #     data[key].sum_data = sum_data_split
                #     print(sum_data_split)
        print(village_data_dict)
        village_data_dict_sum = [0,0,0,0]
        for key,value in village_data_dict.items():
            print(value)
            village_data_dict_sum[0] += value[0]
            village_data_dict_sum[1] += float(value[1])
            village_data_dict_sum[2] += float(value[2])
            village_data_dict_sum[3] += float(value[3])
        return render(request, 'app_common/data_view.html', {
            "village_data_dict":village_data_dict,
            "village_data_dict_sum":village_data_dict_sum,
            "policys":self.policys,
            "village_data": self.village_data,
            "village_data_str": json.dumps(self.village_data),
            "policy_object":policy_obj.policy_object
        })

    @method_decorator(login_required)
    def post(self,request):
        pass

def ceshi(request):  # 测试

    # all_obj = common_models.Nav.objects.all()
    #
    # for obj in all_obj:
    #     if obj.pid:
    #         permission_obj = obj.permission
    #         permission_obj.name = obj.pid.name+'_'+obj.name
    #         permission_obj.codename = obj.pid.name + '_' + obj.name
    #         permission_obj.save()




    # from django.contrib.auth.models import Permission
    # pers = Permission.objects.all()
    # for per in pers:
    #     try:
    #         obj = common_models.Nav.objects.get(name=per.name)
    #     except:
    #         pass
    #     else:
    #         obj.permission = per
    #         obj.save()

    # navs = common_models.Nav.objects.all().values()
    # content_type = ContentType.objects.get_for_model(common_models.Nav)
    # data = []
    # for nav in navs:
    #     data.append(Permission(codename=nav['name'],name=nav['name'],content_type=content_type))
    #
    # Permission.objects.bulk_create(data)
    # return JsonResponse({"navs":navs},safe=False)

    # print(request.user.id)
    # user_extra = user_models.UserExtra.objects.get(about_id=request.user.id)
    # common.log(user_id=request.user.id, model_path='user_center.models.UserExtra', type='add', update_obj=user_extra)  # 记录日志

    # users = get_user_model().objects.all()
    exise_mobiles = list(user_models.UserExtra.objects.filter(Q(name='')).values_list('mobile',flat=True))
    # print(exise_mobiles)
    # for user in users:
    #     if user.username not in exise_mobiles:
    #         try:
    #             user_models.UserExtra.objects.create(name='',mobile=user.username,department_id=28,about=user)
    #         except:
    #             pass

    #exise_mobiles = list(user_models.UserExtra.objects.all().values_list('mobile', flat=True))
    # helper_data = report_models.HelperDataForm.objects.all()
    # mobile_name_dict = {}
    # for value in helper_data:
    #     if value.mobile_phone and len(str(value.mobile_phone)) >= 4 and value.mobile_phone in exise_mobiles:
    #         mobile_name_dict[value.mobile_phone] = value.helper_name
    #
    # for mobile,name in mobile_name_dict.items():
    #     try:
    #         obj = user_models.UserExtra.objects.get(mobile=mobile)
    #         obj.name = name
    #         obj.save()
    #     except:
    #         pass

    # mobiles = []
    # for value in helper_data:
    #     if value.mobile_phone and len(str(value.mobile_phone)) >= 4 and value.mobile_phone not in exise_mobiles:
    #         mobiles.append(value.mobile_phone)
    #
    # mobile_list = list(set(mobiles))
    # print(len(mobile_list),mobile_list)
    # for value in mobile_list:
    #     try:
    #         user = get_user_model().object.get(username=value)
    #         user_models.UserExtra.objects.create_user(name='',mobile=value,department_id=28,about=user)
    #     except:
    #         pass

    # print(len(mobile_list),mobile_list)

    return HttpResponse()

class QuChong(View):  # 去重
    def get(self,request):
        t_poorhousedataform = threading.Thread(target=self.poorhousedataform)  # 定义线程
        t_poorhousedataform.start()  # 让线程开始工作

        t_poorhouseadditionalform = threading.Thread(target=self.poorhouseadditionalform)  # 定义线程
        t_poorhouseadditionalform.start()  # 让线程开始工作

        t_poorpeopledataform = threading.Thread(target=self.poorpeopledataform)  # 定义线程
        t_poorpeopledataform.start()  # 让线程开始工作

        t_poorpeopleadditionalform = threading.Thread(target=self.poorpeopleadditionalform)  # 定义线程
        t_poorpeopleadditionalform.start()  # 让线程开始工作

        return JsonResponse({"code": "200"})

    def poorhousedataform(self):
        models_fields = [v.column for v in report_models.PoorHouseDataForm._meta.get_fields() if v.column != 'id']  # 表中所有字段
        models_fields_split = ','.join(models_fields)
        sql = "select id,GROUP_CONCAT(id) as group_ids,count(id) as count_id from report_form_poorhousedataform GROUP BY " + models_fields_split + " HAVING count(id) > 1;"

        row = list(report_models.PoorHouseDataForm.objects.raw(sql))
        remove_ids = []
        for key,value in enumerate(row):
            group_ids = value.group_ids.split(',')
            remove_ids += group_ids[1:]

        if len(remove_ids) == len(set(remove_ids)):
            if len(remove_ids) > 0:
                report_models.PoorHouseDataForm.objects.filter(id__in=remove_ids).delete()

    def poorhouseadditionalform(self):
        models_fields = [v.column for v in report_models.PoorHouseAdditionalForm._meta.get_fields() if v.column != 'id']  # 表中所有字段
        models_fields_split = ','.join(models_fields)
        sql = "select id,GROUP_CONCAT(id) as group_ids,count(id) as count_id from report_form_poorhouseadditionalform GROUP BY " + models_fields_split + " HAVING count(id) > 1;"

        row = list(report_models.PoorHouseAdditionalForm.objects.raw(sql))
        remove_ids = []
        for key,value in enumerate(row):
            group_ids = value.group_ids.split(',')
            remove_ids += group_ids[1:]

        if len(remove_ids) == len(set(remove_ids)):
            if len(remove_ids) > 0:
                report_models.PoorHouseAdditionalForm.objects.filter(id__in=remove_ids).delete()

    def poorpeopledataform(self):
        models_fields = [v.column for v in report_models.PoorPeopleDataForm._meta.get_fields() if v.column != 'id']  # 表中所有字段
        models_fields_split = ','.join(models_fields)
        sql = "select id,GROUP_CONCAT(id) as group_ids,count(id) as count_id from report_form_poorpeopledataform GROUP BY "+models_fields_split+" HAVING count(id) > 1;"
        print(sql)
        row = list(report_models.PoorPeopleDataForm.objects.raw(sql))

        remove_ids = []
        for key,value in enumerate(row):
            group_ids = value.group_ids.split(',')
            remove_ids += group_ids[1:]

        if len(remove_ids) == len(set(remove_ids)):
            if len(remove_ids) > 0:
                print(remove_ids)
                report_models.PoorPeopleDataForm.objects.filter(id__in=remove_ids).delete()

    def poorpeopleadditionalform(self):
        models_fields = [v.column for v in report_models.PoorPeopleAdditionalForm._meta.get_fields() if v.column != 'id']  # 表中所有字段
        models_fields_split = ','.join(models_fields)
        sql = "select id,GROUP_CONCAT(id) as group_ids,count(id) as count_id from report_form_poorpeopleadditionalform GROUP BY "+models_fields_split+" HAVING count(id) > 1;"
        print(sql)
        row = list(report_models.PoorPeopleAdditionalForm.objects.raw(sql))

        remove_ids = []
        for key,value in enumerate(row):
            group_ids = value.group_ids.split(',')
            remove_ids += group_ids[1:]

        if len(remove_ids) == len(set(remove_ids)):
            if len(remove_ids) > 0:
                print(remove_ids)
                report_models.PoorPeopleAdditionalForm.objects.filter(id__in=remove_ids).delete()