from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect,QueryDict
from django.conf import settings
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.db.models import Max,Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from app_common import common
from app_common import models as common_models
from app_common.config import VIEW_DICT,VIEW_DIR,DOWNLOAD_URL_PR,DELETE_DIR
from app_common import config as app_config
from department import models as department_models
from excel_view import models as excel_models
from user_center import models as user_models

from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
from excel_view.ChineseAnalyzer import ChineseAnalyzer
from excel_view import repositories as excel_repos
from report_form import models as report_models
from health_data import models as health_models

from pytz import timezone
from operator import itemgetter
from itertools import groupby
from operator import itemgetter
import os,datetime,threading,xlrd,xlwt,collections,copy,json,math,locale,shutil

locale.setlocale(locale.LC_ALL, '')

# Create your views here.

#http://127.0.0.1:8000/excel_view/index/?id=10
@login_required()
def index(request):
    id = request.GET.get('id')

    if id == '2':
        #农办
        nav_list = common_models.Nav.objects.filter(pid_id = 15)
        print(nav_list)
        return render(request,'excel_view/nongban.html',{"nav_list":nav_list})

    if id not in VIEW_DICT.keys():
        return HttpResponse(status=404)

    department_info = department_models.Department.objects.get(id=id)
    department_view_dir = VIEW_DICT.get(str(id), '')
    dirpath = request.path.replace('/excel_view/index','')

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


    view_dir = os.path.join(VIEW_DIR, department_view_dir)
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

                file_path = os.path.join((curr_request_dir or ''), f).replace('\\', '/')
                if (os.path.isdir(dir_path + '/' + f)):
                    # 排除隐藏文件夹。因为隐藏文件夹过多
                    if (f[0] == '.'):
                        pass
                    else:
                        # 添加非隐藏文件夹
                        dirlist.append({"name":f,"update_time":file_update_time,"path":file_path})
                if (os.path.isfile(dir_path + '/' + f)):
                    if (f[0] == '.'):
                        pass
                    else:
                        # 添加文件
                        filelist.append({
                            "name":f,
                            "update_time":file_update_time,
                            "path":file_path,
                            "full_path":os.path.join(department_view_dir,file_path).replace('\\','/')
                        })

        diy_filelist = [value['full_path'] for value in filelist]
        diy_objs = excel_models.ExcelApprove.objects.filter(path__in=diy_filelist)
        for key,value in enumerate(filelist):
            for val in diy_objs:
                if value['full_path'] == val.path:
                    filelist[key]['approve_obj'] = val

        return render(request, 'excel_view/index.html', {
            "department_info": department_info,
            "dirlist": dirlist,
            "filelist": filelist,
            "curr_request_dir":curr_request_dir if curr_request_dir != None else None,
            "prev_request_dir":prev_request_dir if prev_request_dir != None else None,
            "ol_path_list":ol_path_list
        })
    else:
        return render(request, 'app_common/error.html', {"msg": "目录不存在！"})

@login_required()
def create_dir(request):  # 创建文件
    id = request.GET.get('id')
    name = request.GET.get('name')

    if id not in VIEW_DICT.keys():
        return HttpResponse(status=404)

    department_view_dir = VIEW_DICT.get(str(id), '')
    dirpath = request.path.replace('/excel_view/create_dir','')

    if dirpath[::-1][0] == '/':
        dirpath = dirpath[:-1]

    request_dir = dirpath.split('/')
    request_dir = [v for v in request_dir if v != '']

    if len(request_dir) > 0:
        curr_request_dir = '/'.join(request_dir)
    else:
        curr_request_dir = None


    view_dir = os.path.join(VIEW_DIR, department_view_dir)
    dir_path = os.path.join(view_dir, (curr_request_dir or '')).replace('\\','/')
    need_create_dir = os.path.join(dir_path,name)
    if os.path.exists(need_create_dir):
        pass
    else:
        os.mkdir(need_create_dir)

    if curr_request_dir:
        url = '/excel_view/index/'+curr_request_dir+'/?id='+id
    else:
        url = '/excel_view/index/?id='+id
    return HttpResponseRedirect(url)

@login_required()
def guoban(request):
    department_view_dir = VIEW_DICT.get('国办', '')

    dirpath = request.path.replace('/excel_view/guoban', '')

    if dirpath[::-1][0] == '/':
        dirpath = dirpath[:-1]

    request_dir = dirpath.split('/')
    request_dir = [v for v in request_dir if v != '']

    ol_path_list = []
    ol_path = ''
    for v in request_dir:
        ol_path += v + '/'
        ol_path_list.append([v, ol_path])
    # print(ol_path_list)

    if len(request_dir) > 0:
        if len(request_dir) > 1:
            join_request_dir = request_dir[:-1]
            prev_request_dir = '/'.join(join_request_dir)
        else:
            prev_request_dir = ''
        curr_request_dir = '/'.join(request_dir)
    else:
        prev_request_dir = None
        curr_request_dir = None

    view_dir = os.path.join(VIEW_DIR, department_view_dir).replace('\\', '/')
    dir_path = os.path.join(view_dir, (curr_request_dir or '')).replace('\\', '/')

    # print(dir_path)
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
                file_update_time = datetime.datetime.utcfromtimestamp(file_update_time) + datetime.timedelta(hours=8)

                file_path = os.path.join((curr_request_dir or ''), f).replace('\\', '/')
                # print(file_path,os.path.isdir(dir_path + '/' + f))
                if (os.path.isdir(dir_path + '/' + f)):
                    # 排除隐藏文件夹
                    if (f[0] == '.'):
                        pass
                    else:
                        # 添加非隐藏文件夹
                        dirlist.append({"name": f, "update_time": file_update_time, "path": file_path})
                if (os.path.isfile(dir_path + '/' + f)):
                    if (f[0] == '.'):
                        pass
                    else:
                        # 添加文件
                        filelist.append({"name": f, "update_time": file_update_time, "path": file_path})
        return render(request, 'excel_view/guoban.html', {
            "guoban_childs_dir":['贫困村数据','贫困户数据','贫困人口数据'],
            "dirlist": dirlist,
            "filelist": filelist,
            "curr_request_dir": curr_request_dir if curr_request_dir != None else None,
            "prev_request_dir": prev_request_dir if prev_request_dir != None else None,
            "ol_path_list": ol_path_list
        })
    else:
        return render(request, 'app_common/error.html', {"msg": "文件不存在！"})


@login_required()
def file_view(request):  # 文件状况
    id = request.GET.get('id','')
    if id:
        try:
            department_info = department_models.Department.objects.get(id=id)
        except:
            department_info = {}
    else:
        department_info = {}
    department_view_dir = VIEW_DICT.get(str(id), '')
    dirpath = request.path.replace('/excel_view/file_view','')

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


    view_dir = os.path.join(VIEW_DIR, department_view_dir)
    dir_path = os.path.join(view_dir, (curr_request_dir or '')).replace('\\','/')
    if os.path.isfile(dir_path):
        approve_path = os.path.join(department_view_dir,(curr_request_dir or '')).replace('\\','/')
        is_approve = False  # 是否正在审核中
        try:
            excel_models.ExcelApprove.objects.get(path=approve_path,status=2)
        except:
            is_approve = False
        else:
            is_approve = True



        print(dir_path)
        download_url = os.path.join(DOWNLOAD_URL_PR,department_view_dir)
        download_url = os.path.join(download_url, (curr_request_dir or '')).replace('\\','/')
        #return HttpResponseRedirect('/static/repositories/'+id+'/'+(curr_request_dir or ''))
        ext = os.path.splitext(os.path.basename(dir_path))[1]
        file_name = os.path.splitext(os.path.basename(dir_path))[0]
        if ext.lower() in ['.pdf','.svg','.png','.jpg','.jpeg','.gif','.mp3','.mp4']:
            #可以打开的文件
            is_can_open = '0'
            file_content = None
        elif ext.lower() in ['.txt','.css','.html','.md','.py','.php','.java','.c','.sh','.sql','.conf','.ini']:
            #可以读取的文件
            is_can_open = '2'
            file_content = common.read_file(dir_path)
        elif ext.lower() in ['.doc','.docx','.xls','.xlsx','.ppt','.pptx']:
            is_can_open = '3'
            file_content = None

            #将office文件转换成pdf,然后显示
            # switch_path = os.path.join(settings.BASE_DIR,'common/excelview/' + department_view_dir).replace('\\','/')
            # if os.path.isdir(switch_path) == False:
            #     os.makedirs(switch_path)
            #
            # print(os.path.join(view_dir,(curr_request_dir or '')), switch_path)
            # is_switch_sucess = common.office2pdf(dir_path,switch_path)
            # print(is_switch_sucess)
            # if is_switch_sucess == 1:
            #     #如果转换pdf成功
            #     is_can_open = '3'
            #     file_content = '/common/excelview/' + department_view_dir + '/' +file_name +'.pdf'
            # else:
            #     is_can_open = '0'
            #     file_content = None
        else:
            is_can_open = '0'
            file_content = None

        return render(request,'excel_view/fileinfo.html',{
            "department_info":department_info,
            "curr_file_path":(curr_request_dir or ''),
            "file_path":'/common/excelview/'+id+'/'+(curr_request_dir or ''),
            "is_can_open":is_can_open,
            "file_content":file_content,
            "ol_path_list":ol_path_list,
            "file_name":file_name,
            "download_url":download_url,
            "dirpath":dirpath,
            "is_approve":is_approve
        })
    else:
        return render(request, 'app_common/error.html', {"msg": "文件不存在！"})

@login_required
def file_del(request):  #删除文件
    id = request.POST.get('id','')
    dirpath = request.POST.get('dirpath','')
    if dirpath[::-1][0] == '/':
        dirpath = dirpath[:-1]

    # if id:
    #     try:
    #         department_info = department_models.Department.objects.get(id=id)
    #     except:
    #         department_info = {}
    # else:
    #     department_info = {}
    department_view_dir = VIEW_DICT.get(str(id), '')

    request_dir = dirpath.split('/')
    request_dir = [v for v in request_dir if v != '']

    if len(request_dir) > 0:
        curr_request_dir = '/'.join(request_dir)
    else:
        curr_request_dir = None

    delete_dir = os.path.join(DELETE_DIR, department_view_dir)
    delete_dir_path = os.path.join(delete_dir, (curr_request_dir or '')).replace('\\','/')

    view_dir = os.path.join(VIEW_DIR, department_view_dir)
    dir_path = os.path.join(view_dir, (curr_request_dir or '')).replace('\\','/')
    print(dir_path)

    delete_dir_path_parse = os.path.splitext(delete_dir_path)
    dir_path_parse_file = request_dir[-1]
    delete_dir_path_parse_path = delete_dir_path.replace(dir_path_parse_file,'')

    if os.path.isdir(delete_dir_path_parse_path) != True:
        os.makedirs(delete_dir_path_parse_path)

    shutil.move(dir_path,delete_dir_path_parse_path)

    return JsonResponse({"code":"200","message":"删除成功","data":{"curr_request_dir":curr_request_dir}})

@login_required
def upload_view(request):  # 文件提交信息
    return render(request,'excel_view/upload_view.html')

@csrf_exempt
def upload_excel(request):
    id = request.POST.get('id','')
    my_file = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
    curr_request_dir = request.POST.get('curr_request_dir','')
    curr_request_dir = curr_request_dir.strip('/')

    if my_file == None:
        return JsonResponse({"code": "-1", "message": "请选择文件", "data": []})
    else:
        axt = os.path.splitext(my_file.name)[0]
        ext = os.path.splitext(my_file.name)[1]
        if ext not in ['.xlsx', '.xls']:
            return JsonResponse({"code": "-1", "message": "请上传Excel文件！", "data": []})

        path = os.path.join(settings.BASE_DIR, 'common/upload/').replace('\\', '/')
        curr_uuid = common.get_uuid()
        inputfilename, inputfile_name = common.upload_file(path, curr_uuid, my_file)  # 上传文件

        read_result = read_excel(path,inputfile_name)
        print(read_result)
        print(inputfilename, inputfile_name)

        tem_is_true,unknown_fields = common.verify_excel(read_result,curr_request_dir)

        if curr_request_dir in ['贫困村数据','贫困户数据','贫困人口数据']:
            to_path = os.path.join(VIEW_DICT.get('国办', ''), (curr_request_dir or '')).replace('\\', '/')
        elif id != '':
            tem_is_true = True
            to_path = os.path.join(VIEW_DICT.get(id, ''), (curr_request_dir or '')).replace('\\', '/')
        else:
            return JsonResponse({"code":-1},safe=False)

        if tem_is_true == False:
            file_path = os.path.join(path, inputfile_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

        return JsonResponse({
            "code":200,
            "message":"",
            "data":{
                "tem_is_true": tem_is_true,
                "unknown_fields":unknown_fields,
                "inputfilename":inputfilename,
                "inputfile_name": inputfile_name,
                "path": to_path
            }
        },safe=False)



def read_excel(path,inputfile_name):
    file_path = os.path.join(path,inputfile_name)
    if os.path.isfile(file_path):
        excel = xlrd.open_workbook(file_path)
        # sheet = excel.sheet_by_index(0)

        excel_names = excel.sheet_names()
        data = []
        for excel_name in excel_names:
            sheet = excel.sheet_by_name(excel_name)

            nrows = sheet.nrows  # 行总数
            ncols = sheet.ncols  # 列总数

            print(nrows,ncols)
            for i in range(nrows):
                row_data = sheet.row_values(i)
                data.append(row_data)

        return data

def upload_excel_to(request):
    inputfile_name = request.POST.get('inputfile_name')
    inputfilename = request.POST.get('inputfilename')
    upload_path = os.path.join(settings.BASE_DIR, 'common/upload/'+inputfile_name).replace('\\', '/')
    path = request.POST.get('path')
    path = os.path.join(VIEW_DIR,path)
    path = os.path.join(path,inputfilename)
    print('-----',path)
    if os.path.isfile(upload_path):
        with open(upload_path, 'rb') as f:
            data = f.read()
        with open(path, 'wb') as p:
            p.write(data)
        os.remove(upload_path)
    return JsonResponse({"code":200})

@csrf_exempt
def upload_excel_zc(request):
    user_id = request.user.id
    id = request.POST.get('id','')
    if id == '':
        return JsonResponse({"code": "-1", "message": "未知的部门", "data": []})

    my_file = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
    curr_request_dir = request.POST.get('curr_request_dir','')
    curr_request_dir = curr_request_dir.strip('/')

    to_path = os.path.join(VIEW_DICT.get(id, ''), (curr_request_dir or '')).replace('\\', '/')
    path = os.path.join(VIEW_DIR, to_path)

    if my_file == None:
        return JsonResponse({"code": "-1", "message": "请选择文件", "data": []})
    else:
        axt = os.path.splitext(my_file.name)[0]
        ext = os.path.splitext(my_file.name)[1]
        if ext not in ['.xlsx', '.xls']:
            return JsonResponse({"code": "-1", "message": "请上传Excel文件！", "data": []})

        #path = os.path.join(settings.BASE_DIR, 'common/upload/').replace('\\', '/')
        #curr_uuid = common.get_uuid()

        inputfilename, inputfile_name = common.upload_file(path, axt, my_file)  # 上传文件

        read_result = read_excel(path,inputfile_name)
        #print(read_result)
        print(inputfilename, inputfile_name)

        tem_is_true,tem_data = common.verify_excel_zc(read_result)

        if tem_is_true == False:
            file_path = os.path.join(path, inputfile_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        else:
            a_to_path = os.path.join(to_path,my_file.name).replace("\\","/")
            excel_models.ExcelApprove.objects.create(upload_user_id=user_id,path=a_to_path,department_id=id)

        return JsonResponse({
            "code":200,
            "message":"",
            "data":{
                "tem_is_true": tem_is_true,
                "tem_data":tem_data,
                "inputfilename":inputfilename,
                "inputfile_name": inputfile_name,
                "path": to_path
            }
        },safe=False)

class SyncMysql(View):
    guoban_childs_dir = ['贫困村数据', '贫困户数据', '贫困人口数据']
    village_dir = '贫困村数据'#国办数据目录中，存放贫困村数据的目录名
    family_dir = '贫困户数据'
    man_dir = '贫困人口数据'
    # def __init__(self):
    #     pass

    # 国办数据同步到MySQL
    def get(self,request):
        department_view_dir = VIEW_DICT.get('国办', '')

        dirpath = request.path.replace('/excel_view/sync_mysql', '')

        if dirpath[::-1][0] == '/':
            dirpath = dirpath[:-1]

        request_dir = dirpath.split('/')
        request_dir = [v for v in request_dir if v != '']

        if len(request_dir) > 0:
            curr_request_dir = '/'.join(request_dir)
        else:
            curr_request_dir = ''

        if curr_request_dir == '贫困村数据':
            self.sync_village()
        elif curr_request_dir == '贫困户数据':
            self.sync_family()
        elif curr_request_dir == '贫困人口数据':
            self.sync_man()
        elif curr_request_dir == '帮扶人':
            self.sync_helper()

        return HttpResponseRedirect('/excel_view/guoban/'+curr_request_dir+'?id=国办')


    #贫困村数据同步到MySQL
    #国办-行政村
    def sync_village(self):
        poverty_village = app_config.POVERTY_VILLAGE
        path = os.path.join(VIEW_DIR, VIEW_DICT.get('国办') + '/' + self.village_dir)  # 国办数据目录中，存放贫困村数据的目录路径
        file_paths = common.get_child_dir_by_path(path)  # 存放“国办数据/贫困村数据”目录下的所有文件xlsx和xls文件

        administrative_village = app_config.ADMINISTRATIVE_VILLAGE
        administrative_village_path = os.path.join(VIEW_DIR, VIEW_DICT.get('其他') + '/行政村基本信息表.xls')  # 行政村基本信息表路径
        administrative_village_data = read_excel('', administrative_village_path) or []  # 行政村基本信息表excel数据

        models_fields = [v.column for v in report_models.AdministrativeVillageDataForm._meta.get_fields()]#表中所有字段
        models_fields.remove('id')#移除id字段，因为id字段自增
        in_models_not_in_administrative_fields = {v:'' for v in models_fields if v not in administrative_village.values()}#在表中，却不在administrative_village中的字段
        in_models_not_in_poverty_fields = {v: '' for v in models_fields if v not in poverty_village.values()}  # 在表中，却不在poverty_village中的字段

        administrative_data_dict = []
        administrative_names = []  # administrative_village_data中存在的村庄名列表
        for value in administrative_village_data:
            if value == list(administrative_village.keys()) or value.count('') >= (len(value) - 1):
                pass
            else:
                administrative_my_dict = dict(zip(administrative_village.values(), value))
                administrative_my_dict.update(in_models_not_in_administrative_fields)
                administrative_data_dict.append(administrative_my_dict)

                administrative_names.append(administrative_my_dict['past_administrative_village']+administrative_my_dict['town_name'])


        poverty_data = []  # 贫困村excel数据
        for file in file_paths:
            excel_result = read_excel('', file) or []
            poverty_data += excel_result
        poverty_data_dict = []
        in_poverty_not_in_administrative_dict = []  # 在poverty_data，却不在administrative_village_data中的村庄数据
        for value in poverty_data:
            if value == list(poverty_village.keys()) or value.count('') >= (len(value) - 1) or '是否参与合并' in value:
                pass
            else:
                poverty_my_dict = dict(zip(poverty_village.values(), value))
                poverty_my_dict = {k: v for k, v in poverty_my_dict.items() if k.strip() != ''}

                if poverty_my_dict['past_administrative_village']+poverty_my_dict['town_name'] not in administrative_names:
                    models_fields_copy = copy.deepcopy(models_fields)
                    models_fields_copy_dict = {v:'' for v in models_fields_copy}
                    models_fields_copy_dict.update({"past_administrative_village": poverty_my_dict['past_administrative_village'],"town_name":poverty_my_dict['town_name']})
                    in_poverty_not_in_administrative_dict.append(models_fields_copy_dict)
                poverty_data_dict.append(poverty_my_dict)

        administrative_data_dict += in_poverty_not_in_administrative_dict

        data_list = []
        for value in administrative_data_dict:
            value_copy = copy.deepcopy(value)
            for v in poverty_data_dict:
                if v['past_administrative_village'].strip() == value['past_administrative_village'].strip() and v['town_name'].strip() == value['town_name']:
                    value_copy.update(v)
                    break
            data_list.append(value_copy)

        for key, value in enumerate(data_list):  # 去空格
            data_list[key] = {k: self.get_true_value(v) for k, v in value.items()}

        for key,value in enumerate(data_list):
            #对于未合并的村，过去村编号和现在村编号一样
            if value['is_merge'] == '未合并':
                data_list[key]['past_village_identifier'] = value['now_village_identifier']

        ##---统计合村后字段start---##
        data_list_group = groupby(data_list, key=itemgetter('now_administrative_village'))  # 根据合并后的村名将数据分组
        sum_some_fields = {}
        for key, value in data_list_group:
            sum_some_fields[key.strip()] = {
                "now_poor_home": str(int(sum([self.get_float_value(v['past_poor_home']) for v in value])) or ''),
            # 贫困户数
                "now_poor_people": str(int(sum([self.get_float_value(v['past_poor_people']) for v in value])) or ''),
            # 贫困人口数
                "now_minimum_people": str(
                    int(sum([self.get_float_value(v['past_minimum_people']) for v in value])) or ''),  # 低保人口数
                "now_minimum_home": str(int(sum([self.get_float_value(v['past_minimum_home']) for v in value])) or ''),
            # 低保户数
                "now_five_people": str(int(sum([self.get_float_value(v['past_five_people']) for v in value])) or ''),
            # 五保人口数
                "now_five_home": str(int(sum([self.get_float_value(v['past_five_home']) for v in value])) or ''),
            # 五保户数
                "now_nation_people": str(
                    int(sum([self.get_float_value(v['past_nation_people']) for v in value])) or ''),  # 少数民族人口数
                "now_woman_people": str(int(sum([self.get_float_value(v['past_woman_people']) for v in value])) or ''),
            # 妇女人口数
                "now_handicapped_people": str(
                    int(sum([self.get_float_value(v['past_handicapped_people']) for v in value])) or ''),  # 残疾人口数
                "now_labor_people": str(int(sum([self.get_float_value(v['past_labor_people']) for v in value])) or ''),
            # 劳动力人数
                "now_egression_people": str(
                    int(sum([self.get_float_value(v['past_egression_people']) for v in value])) or '')  # 外出务工人数
            }

        print(sum_some_fields)

        for key, value in enumerate(data_list):
            data_list[key]['now_poor_home'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_poor_home']
            data_list[key]['now_poor_people'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_poor_people']
            data_list[key]['now_minimum_people'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_minimum_people']
            data_list[key]['past_minimum_home'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_minimum_home']
            data_list[key]['past_five_people'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_five_people']
            data_list[key]['past_five_home'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_five_home']
            data_list[key]['past_nation_people'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_nation_people']
            data_list[key]['past_woman_people'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_woman_people']
            data_list[key]['past_handicapped_people'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_handicapped_people']
            data_list[key]['past_labor_people'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_labor_people']
            data_list[key]['past_egression_people'] = sum_some_fields[value['now_administrative_village'].strip()][
                'now_egression_people']
        ##---统计合村后字段end---##


        ##---按照字段顺序排序start---##
        data = []  # 按照in_administrative_and_poverty_fields_keys排序后的数据
        for value in data_list:
            value_sort = []
            for v in models_fields:
                value_sort.append(value[v])
            data.append(value_sort)
        print(data)
        ##---按照字段顺序排序end---##

        drop_sql = "Delete from report_form_administrativevillagedataform"

        field_str = ','.join(models_fields)
        sql = 'insert into report_form_administrativevillagedataform (' + field_str + ') VALUES '
        sql_values = []
        for value in data:
            i_values = ['\'' + str(v).strip() + '\'' for v in value]
            sql_values.append('(' + (','.join(i_values)) + ')')

        sql += ','.join(sql_values)
        sql += ';'

        if len(sql_values) > 0:
            cursor = connection.cursor()
            cursor.execute(drop_sql)
            cursor.execute(sql)
            row = cursor.fetchone()

    #贫困户数据同步到MySQL
    #国办-贫困户
    def sync_family(self):
        poverty_family = app_config.POVERTY_FAMILY
        path = os.path.join(VIEW_DIR, VIEW_DICT.get('国办') + '/' + self.family_dir)  # 国办数据目录中，存放贫困村数据的目录路径
        file_paths = common.get_child_dir_by_path(path)  # 存放“国办数据/贫困户数据”目录下的所有文件xlsx和xls文件

        models_fields = [v.column for v in report_models.PoorHouseDataForm._meta.get_fields()]#表中所有字段
        models_fields.remove('id')#移除id字段，因为id字段自增
        in_models_not_in_poverty_fields = {v:'' for v in models_fields if v not in poverty_family.values()}#在表中，却不在poverty_family中的字段

        poverty_data = []  # 贫困户excel数据
        for file in file_paths:
            excel_result = read_excel('', file) or []
            poverty_data += excel_result

        poverty_data_dict = []
        for value in poverty_data:
            if value == list(poverty_family.keys()) or value.count('') >= (len(value) - 1) or value[10].strip() != '户主':
                pass
            else:
                poverty_my_dict = dict(zip(poverty_family.values(), value))
                poverty_my_dict = {k: v for k, v in poverty_my_dict.items() if k.strip() != ''}
                poverty_my_dict.update(in_models_not_in_poverty_fields)
                poverty_data_dict.append(poverty_my_dict)

        village_data = report_models.AdministrativeVillageDataForm.objects.all().values('past_village_identifier','past_administrative_village','now_village_identifier','town_name')
        data_list = []
        for value in poverty_data_dict:
            value_copy = copy.deepcopy(value)
            for v in village_data:
                if v['past_administrative_village'] == value['行政村'].strip() and v['town_name'] == value['乡(镇)']:
                    value_copy.update(v)
                    del value_copy['行政村']
                    del value_copy['乡(镇)']
                    del value_copy['town_name']
                    break
            data_list.append(value_copy)

        for key, value in enumerate(data_list):  # 去空格
            data_list[key] = {k: self.get_true_value(v) for k, v in value.items()}

        ##---按照字段顺序排序start---##
        data = []  # 按照in_administrative_and_poverty_fields_keys排序后的数据
        for value in data_list:
            value_sort = []
            for v in models_fields:
                if v == 'householder_id':
                    # if '420922193004017728' in value[v]:
                    #     print('---',value)
                    value_sort.append(value[v][:18])
                else:
                    value_sort.append(value[v])
            data.append(value_sort)
        #print(data)
        ##---按照字段顺序排序end---##

        drop_sql = "Delete from report_form_poorhousedataform"
        field_str = ','.join(models_fields)
        sql = 'insert into report_form_poorhousedataform (' + field_str + ') VALUES '
        print(field_str)
        sql_values = []
        for value in data:
            i_values = ['\'' + str(v).strip() + '\'' for v in value]
            sql_values.append('(' + (','.join(i_values)) + ')')

        sql += ','.join(sql_values)
        sql += ';'

        if len(sql_values) > 0:
            cursor = connection.cursor()
            cursor.execute(drop_sql)
            cursor = connection.cursor()
            cursor.execute(sql)
            row = cursor.fetchone()

    # 贫困人口数据同步到MySQL
    # 国办-贫困人口
    def sync_man(self):
        poverty_man = app_config.POVERTY_MAN
        path = os.path.join(VIEW_DIR, VIEW_DICT.get('国办') + '/' + self.man_dir)  # 国办数据目录中，存放贫困村数据的目录路径
        file_paths = common.get_child_dir_by_path(path)  # 存放“国办数据/贫困户数据”目录下的所有文件xlsx和xls文件

        models_fields = [v.column for v in report_models.PoorPeopleDataForm._meta.get_fields()]#表中所有字段
        models_fields.remove('id')#移除id字段，因为id字段自增
        in_models_not_in_poverty_fields = {v:'' for v in models_fields if v not in poverty_man.values()}#在表中，却不在poverty_man中的字段

        poverty_data = []  # 贫困人口excel数据
        for file in file_paths:
            excel_result = read_excel('', file) or []
            poverty_data += excel_result

        poverty_data_dict = []
        for value in poverty_data:
            if value == list(poverty_man.keys()) or value.count('') >= (len(value) - 1):
                pass
            else:
                poverty_my_dict = dict(zip(poverty_man.values(), value))
                poverty_my_dict = {k: v for k, v in poverty_my_dict.items() if k.strip() != ''}
                poverty_my_dict.update(in_models_not_in_poverty_fields)
                poverty_data_dict.append(poverty_my_dict)

        for key, value in enumerate(poverty_data_dict):  # 去空格
            poverty_data_dict[key] = {k: self.get_true_value(v) for k, v in value.items()}

        ##---按照字段顺序排序start---##
        data = []  # 按照in_administrative_and_poverty_fields_keys排序后的数据
        for value in poverty_data_dict:
            value_sort = []
            for v in models_fields:
                if v == 'people_id':
                    value_sort.append(value[v][:18])
                else:
                    value_sort.append(value[v])
            data.append(value_sort)
        #print(data)
        ##---按照字段顺序排序end---##

        drop_sql = "Delete from report_form_poorpeopledataform"
        field_str = ','.join(models_fields)
        sql = 'insert into report_form_poorpeopledataform (' + field_str + ') VALUES '
        print(field_str)
        sql_values = []
        for value in data:
            i_values = ['\'' + str(v).strip() + '\'' for v in value]
            sql_values.append('(' + (','.join(i_values)) + ')')

        sql += ','.join(sql_values)
        sql += ';'

        if len(sql_values) > 0:
            cursor = connection.cursor()
            cursor.execute(drop_sql)
            cursor = connection.cursor()
            cursor.execute(sql)
            row = cursor.fetchone()

    def sync_helper(self):
        poverty_helper = app_config.POVERTY_HELPER
        path = os.path.join(VIEW_DIR, VIEW_DICT.get('其他') + '/2018年4月29日（打开隐藏版）.xlsx')  # 帮扶人文件路径

        models_fields = [v.column for v in report_models.HelperDataForm._meta.get_fields()]  # 表中所有字段
        models_fields.remove('id')  # 移除id字段，因为id字段自增
        in_models_not_in_poverty_fields = {v: '' for v in models_fields if
                                           v not in poverty_helper.values()}  # 在表中，却不在POVERTY_HELPER中的字段

        poverty_data = read_excel('', path) or []
        print(path)
        # wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
        # sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)  ##第二参数用于确认同一个cell单元是否可以重设值。
        # style_common = xlwt.easyxf(
        #     'font: name Times New Roman, color-index black,height 0x0012c;align: wrap on, vert centre, horiz center;')
        # mydata = []
        # for k, v in enumerate(poverty_data):
        #     if v.count('') >= (len(v) - 1) or '帮扶人' in v:
        #         pass
        #     else:
        #         if str(v[10]).strip() == '':
        #             mydata.append(v)
        # mydata.insert(0,list(poverty_helper.keys()))
        # print(mydata)
        # for key, value in enumerate(mydata):
        #     for k, v in enumerate(value):
        #         if k == 8:
        #             sheet.col(k).width = 12000
        #         else:
        #             sheet.col(k).width = 5555
        #         sheet.write(key, k, v,style_common)
        # wbk.save("C:/Users/xzw/Documents/其他数据/aaa.xls")  ##该文件路径必须存在

        poverty_data_dict = []
        for value in poverty_data:
            if value == list(poverty_helper.keys()) or value.count('') >= (
                    len(value) - 1) or '帮扶人' in value or '队长/队员/结对帮扶责任人' in value:
                pass
            else:
                poverty_my_dict = dict(zip(poverty_helper.values(), value))
                poverty_my_dict = {k: v for k, v in poverty_my_dict.items() if k.strip() != ''}
                poverty_my_dict.update(in_models_not_in_poverty_fields)
                poverty_data_dict.append(poverty_my_dict)
        #print(poverty_data_dict)
        poverty_data_dict_split = []
        for value in poverty_data_dict:
            if value['poor_town'] == '新城镇':
                value['poor_name'] = value['poor_name'].replace('(', '（').replace(')', '）').replace('）', '）、')

            poor_name_split = re.split(r'[、]', value['poor_name'])
            for v in poor_name_split:
                if v.strip() != '':
                    if v.find('（') == -1:
                        poor_name = v
                        poor_group = ''
                    else:
                        poor_name = v[:v.find('（')]
                        poor_group = v[v.find('（') + 1:v.find('）')]
                    value_copy = copy.deepcopy(value)
                    value_copy.update({"poor_name": poor_name, 'poor_group': poor_group})
                    poverty_data_dict_split.append(value_copy)

        # join_sql = "select a.past_administrative_village,a.past_village_identifier,a.now_village_identifier,b.householder_id from report_form_administrativevillagedataform as a INNER JOIN report_form_poorhousedataform as b ON a.past_village_identifier = b.past_village_identifier"
        # print(join_sql)
        # join_data = list(report_models.AdministrativeVillageDataForm.objects.raw(join_sql))
        # field_tup = ('past_administrative_village','past_village_identifier','now_village_identifier','householder_id')
        # village_data = list(map(lambda x: dict(zip(field_tup, x)), join_data))
        #

        # village_data = report_models.AdministrativeVillageDataForm.objects.all().values('past_administrative_village','now_administrative_village','past_village_identifier','now_village_identifier','town_name')
        # village_data = report_models.PoorHouseDataForm.objects.all().values('householder_id','past_village_identifier')
        # print(village_data)
        # data_list = []
        # for value in poverty_data_dict_split:
        #     value_copy = copy.deepcopy(value)
        #     for v in village_data:
        #         if v['past_village_identifier'] == value['行政村'].strip() and v['town_name'] == value['乡(镇)']:
        #             value_copy.update(v)
        #             del value_copy['行政村']
        #             del value_copy['乡(镇)']
        #             del value_copy['town_name']
        #             break
        #     data_list.append(value_copy)
        #

        # 单元格中的数据进行正确转换
        def get_true_value(value):
            # try:
            #     true_value = float(value)
            # except:
            #     true_value = str(value).strip()
            # else:
            #     true_value = str(int(true_value))
            #
            # return true_value

            try:
                true_value = str(int(value))
            except:
                true_value = str(value).strip()

            return true_value

        for key, value in enumerate(poverty_data_dict_split):  # 去空格
            poverty_data_dict_split[key] = {k: get_true_value(v) for k, v in value.items()}

        print(models_fields)
        ##---按照字段顺序排序start---##
        data = []  # 按照in_administrative_and_poverty_fields_keys排序后的数据
        for value in poverty_data_dict_split:
            # if value['poor_town'] == '新城镇':
            #     print(value)
            value_sort = []
            for v in models_fields:
                value_sort.append(value[v])
            data.append(value_sort)
        #print(data)
        ##---按照字段顺序排序end---##

        drop_sql = "Delete from report_form_helperdataform"
        field_str = ','.join(models_fields)
        sql = 'insert into report_form_helperdataform (' + field_str + ') VALUES '
        print(field_str)

        sql_values = []
        for value in data:
            if len(value) < 5:
                print(value)
            i_values = ['\'' + str(v).strip() + '\'' for v in value]
            sql_values.append('(' + (','.join(i_values)) + ')')

        sql += ','.join(sql_values)
        sql += ';'
        # print(sql)
        print(len(sql_values))
        if len(sql_values) > 0:
            cursor = connection.cursor()
            cursor.execute(drop_sql)
            cursor = connection.cursor()
            cursor.execute(sql)
            row = cursor.fetchone()



    def get_float_value(self,value):
        # try:
        #     float_value = float(value)
        # except:
        #     float_value = 0
        # return float_value

        try:
            int_value = int(value)
        except:
            int_value = 0

        return int_value

    #单元格中的数据进行正确转换
    def get_true_value(self,value):
        # try:
        #     true_value = float(value)
        # except:
        #     true_value = str(value).strip()
        # else:
        #     true_value = str(int(true_value))
        #
        # return true_value

        try:
            true_value = str(int(value))
        except:
            true_value = str(value).strip()

        return true_value

def data_correct(request):  # 基础数据修正
    return render(request,'excel_view/data_correct.html')

class SearchCorrect(View):
    tems = {
        "village":"excel_view/forms/village.html",
        "family":"excel_view/forms/family.html",
        "man": "excel_view/forms/man.html",
        "helper": "excel_view/forms/helper.html",
    }

    def get(self,request):
        type = request.GET.get('type')
        number = request.GET.get('number')

        if type == 'village':
            res = report_models.AdministrativeVillageDataForm.objects.filter(now_village_identifier=number)
            if len(res) > 0:
                result = res[0]
            else:
                result = None
        elif type == 'family':
            try:
                result = report_models.PoorHouseDataForm.objects.filter(householder_id=number)
            except report_models.AdministrativeVillageDataForm.DoesNotExist:
                result = None
        elif type == 'man':
            try:
                result = report_models.PoorPeopleDataForm.objects.filter(people_id=number)
            except report_models.AdministrativeVillageDataForm.DoesNotExist:
                result = None
        elif type == 'helper':
            res = report_models.HelperDataForm.objects.filter(mobile_phone=number)
            if len(res) > 0:
                result = res[0]
            else:
                result = None
        else:
            result = None


        if result:
            return render(request, self.tems[type], {"result": result})
        else:
            return render(request, 'excel_view/forms/no_result.html')

    def post(self,request):
        # data = request.POST.get('data')
        # post = QueryDict(data).dict()
        post = request.POST.dict()
        type = post.get('type')
        number = post.get('number')

        del post['type']
        del post['number']
        del post['csrfmiddlewaretoken']
        #print(post)

        if type == 'village':
            self.update_village(post,number)
            model_path = 'report_form.models.AdministrativeVillageDataForm'
        elif type == 'family':
            self.update_family(post)
            model_path = 'report_form.models.PoorHouseDataForm'
        elif type == 'man':
            self.update_man(post)
            model_path = 'report_form.models.PoorPeopleDataForm'
        elif type == 'helper':
            self.update_helper(post,number)
            model_path = 'report_form.models.HelperDataForm'
        else:
            model_path = None
        common.log(user_id=request.user.id, model_path=model_path,type='update', old_obj=None, update_obj=None)  # 记录日志

        return JsonResponse({"code":"200","message":"修改成功"},safe=False)

    def update_village(self,post,number):
        report_models.AdministrativeVillageDataForm.objects.filter(now_village_identifier=number).update(**post)

    def update_family(self, post):
        auto_id = post.get('id')
        del post['id']
        obj = report_models.PoorHouseDataForm.objects.get(id=auto_id)
        for key, value in post.items():
            setattr(obj, key, value)
        obj.save()

    def update_man(self, post):
        auto_id = post.get('id')
        del post['id']
        obj = report_models.PoorPeopleDataForm.objects.get(id=auto_id)
        for key, value in post.items():
            setattr(obj, key, value)
        obj.save()

    def update_helper(self,post,number):
        # data = {
        #     'helper_name': post.get('helper_name'),
        #     'helper_sex': post.get('helper_sex'),
        #     'unit_name': post.get('unit_name'),
        #     'helper_post': post.get('helper_post'),
        #     'helper_type': post.get('helper_type'),
        #     'office_phone': post.get('office_phone'),
        #     'mobile_phone': post.get('mobile_phone'),
        # }
        report_models.HelperDataForm.objects.filter(mobile_phone=number).update(**post)

class DataCorrectAdd(View):  # 贫困人员数据
    tems = {
        "village":"excel_view/forms/village.html",
        "family":"excel_view/forms/family.html",
        "man": "excel_view/forms/man.html",
        "helper": "excel_view/forms/helper.html",
    }

    def get(self,request):
        type = request.GET.get('type')
        return render(request, self.tems[type], {"result": '1'})

    def post(self,request):
        post = request.POST.dict()
        type = post.get('type')
        number = post.get('number')

        del post['type']
        del post['number']
        del post['csrfmiddlewaretoken']

        if type == 'village':
            obj = report_models.AdministrativeVillageDataForm.objects.create(**post)
            model_path = 'report_form.models.AdministrativeVillageDataForm'
        elif type == 'family':
            obj = report_models.PoorHouseDataForm.objects.create(**post)
            model_path = 'report_form.models.PoorHouseDataForm'
        elif type == 'man':
            obj = report_models.PoorPeopleDataForm.objects.create(**post)
            model_path = 'report_form.models.PoorPeopleDataForm'
        elif type == 'helper':
            obj = report_models.HelperDataForm.objects.create(**post)
            model_path = 'report_form.models.HelperDataForm'
        else:
            return render(request, 'app_common/error.html', {"msg": "页面不存在！"})

        update_obj = copy.deepcopy(obj)
        common.log(user_id=request.user.id, model_path=model_path,
                   type='add', old_obj=None, update_obj=update_obj)  # 记录日志
        return JsonResponse({"code":"200","message":"添加成功"},safe=False)

def data_correct_delete(request):
    type = request.GET.get('type')
    data_id = request.GET.get('data_id')
    if type == 'village':
        model_path = 'report_form.models.AdministrativeVillageDataForm'
        obj = report_models.AdministrativeVillageDataForm.objects.get(id=data_id)
        number = obj.now_village_identifier
        old_obj = copy.deepcopy(obj)
        obj.delete()
    elif type == 'family':
        model_path = 'report_form.models.PoorHouseDataForm'
        obj = report_models.PoorHouseDataForm.objects.get(id=data_id)
        number = obj.householder_id
        old_obj = copy.deepcopy(obj)
        obj.delete()
    elif type == 'man':
        model_path = 'report_form.models.PoorPeopleDataForm'
        obj = report_models.PoorPeopleDataForm.objects.get(id=data_id)
        number = obj.people_id
        old_obj = copy.deepcopy(obj)
        obj.delete()
    elif type == 'helper':
        model_path = 'report_form.models.HelperDataForm'
        obj = report_models.HelperDataForm.objects.get(id=data_id)
        number = obj.mobile_phone
        old_obj = copy.deepcopy(obj)
        obj.delete()
    else:
        return render(request, 'app_common/error.html', {"msg": "页面不存在！"})

    common.log(user_id=request.user.id, model_path=model_path,
               type='delete', old_obj=old_obj, update_obj=None)  # 记录日志
    return HttpResponseRedirect('/excel_view/search_correct/?type='+type+'&number='+number)

def ceshi(request):

    return HttpResponse('')

#扶起来汇总
class HelpUp(View):
    policy_first_layer_list = ['产业扶起来','教育扶起来','健康扶起来','生活保起来','住房保起来','残疾人专项','保险类专项','创业类专项']

    def __init__(self):
        village_all = report_models.AdministrativeVillageDataForm.objects.all().values('town_name','now_village_identifier','now_administrative_village').order_by('now_village_identifier')

        village_data = collections.defaultdict(dict)
        for value in village_all:
            village_data[value['town_name']][value['now_village_identifier']] = value['now_administrative_village']

        self.village_data = village_data

        super(HelpUp, self).__init__()


    def get(self,request):
        dirpath = request.path.replace('/excel_view/help_up', '')

        if dirpath[::-1][0] == '/':
            dirpath = dirpath[:-1]

        request_dir = dirpath.split('/')
        request_dir = [v for v in request_dir if v != '']

        if len(request_dir) > 0:
            curr_request_dir = '/'.join(request_dir)
        else:
            curr_request_dir = ''

        print(curr_request_dir)

        #搜索-start
        now_village_identifier = request.GET.get('now_village_identifier','').strip()
        date_start = request.GET.get('date_start','').strip()
        date_end = request.GET.get('date_end', '').strip()
        search_condition = ''
        search_condition_house = ''
        search_condition_people = ''
        search_condition_industry_agritainment = ''
        if now_village_identifier != '':
            village_list_obj = report_models.AdministrativeVillageDataForm.objects.filter(now_village_identifier=now_village_identifier)
            householder_id_identifier = report_models.PoorHouseDataForm.objects.filter(now_village_identifier=now_village_identifier).values('householder_id','house_identifier')

            householder_ids = [v['householder_id'] for v in householder_id_identifier]
            householder_ids = ["'" + value + "'" for value in householder_ids]
            householder_ids_s = ','.join(householder_ids)
            if householder_ids_s == '':
                search_condition_house += "1 = 2 and "
            else:
                search_condition_house += "householder_id in ("+householder_ids_s+") and "

            house_identifiers = [v['house_identifier'] for v in householder_id_identifier]
            people_ids = report_models.PoorPeopleDataForm.objects.filter(house_identifier__in=house_identifiers).values_list('people_id', flat=True)
            people_ids = ["'" + value + "'" for value in people_ids]
            people_ids_s = ','.join(people_ids)
            if people_ids_s == '':
                search_condition_people += "1 = 2 and "
            else:
                search_condition_people += "people_id in ("+people_ids_s+") and "

            if len(village_list_obj) > 0:
                village_obj = village_list_obj[0]
                search_condition_industry_agritainment += "town_name = '"+village_obj.town_name+"' and administrative_village = '"+village_obj.now_administrative_village+"' and "

            search_condition += "now_village_identifier = '"+now_village_identifier+"' and "

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


        if search_condition_industry_agritainment == '':
            search_condition_industry_agritainment = '1=1'

        policy_first_layer = curr_request_dir.replace('汇总','')

        if policy_first_layer in self.policy_first_layer_list:
            #data = report_models.PolicyStaticForm.objects.filter(policy_first_layer=policy_first_layer)

            sql = "SELECT *,(case when policy_object = '贫困村' then (SELECT concat_ws(',',ifnull(SUM(policy_multiplier),0),ifnull(SUM(plan_money),0),ifnull(SUM(fact_money),0),concat_ws(',',count(id),'村')) FROM report_form_administrativevillageadditionalform WHERE "+search_condition+"policy_number = basic.policy_number) when policy_object = '农家乐吸纳就业' then (SELECT concat_ws(',',ifnull(SUM(subsidy_multiplier),0),ifnull(SUM(plan_subsidy),0),ifnull(SUM(fact_subsidy),0),concat_ws(',',count(id),'户')) FROM report_form_industryagritainmentdataform where "+search_condition_industry_agritainment+") when policy_object = '贫困户' then (SELECT concat_ws(',',ifnull(SUM(policy_multiplier),0),ifnull(SUM(plan_money),0),ifnull(SUM(fact_money),0),concat_ws(',',count(id),'户')) FROM report_form_poorhouseadditionalform WHERE "+search_condition_house+"policy_number = basic.policy_number) when policy_object = '贫困人口' then (SELECT concat_ws(',',ifnull(SUM(policy_multiplier),0),ifnull(SUM(plan_money),0),ifnull(SUM(fact_money),0),concat_ws(',',count(id),'人')) FROM report_form_poorpeopleadditionalform WHERE "+search_condition_people+"policy_number = basic.policy_number) end) AS sum_data FROM report_form_policystaticform AS basic WHERE policy_first_layer = '"+policy_first_layer+"' ORDER BY policy_number;"
            print(sql)

            data = list(report_models.PolicyStaticForm.objects.raw(sql))

            # for key,value in enumerate(data):
            #     if value.id == 32:
            #         sum_data_sql = 'select sum(payment_amount) from '
            #         print(111)

            sum_data_sum = {
                "fact_money":0,
                "plan_money":0,
                "policy_multiplier":0,
                "count_村":0,
                "count_户":0,
                "count_人":0
            }
            for key,value in enumerate(data):
                # print(value.__dict__)
                # print(value.sum_data)
                sum_data_split = str(value.sum_data, encoding = "utf8").split(',')
                #print(sum_data_split)
                sum_data = []
                for v in sum_data_split:
                    try:
                        float(v)
                    except:
                        sum_data.append(0.00)
                    else:
                        sum_data.append(float(v))
                #print(sum_data)
                sum_data_sum['policy_multiplier'] += sum_data[0]
                sum_data_sum['plan_money'] += sum_data[1]
                sum_data_sum['fact_money'] += sum_data[2]
                sum_data_sum['count_' + str(sum_data_split[4])] += int(sum_data[3])

                data[key].sum_data = [locale.format("%.2f", float(v_), 1) for v_ in sum_data]
        else:
            data = []
            sum_data_sum = {}

        print(sum_data_sum)
        return render(request,'excel_view/help_up.html',{
            "data":data,
            "page":curr_request_dir,
            "village_data":self.village_data,
            "village_data_str":json.dumps(self.village_data),
            "sum_data_sum":sum_data_sum
        })

class HelpUpDetail(View):  # 扶起来数据汇总
    def __init__(self):
        #乡镇-行政村数据 start
        village_all = report_models.AdministrativeVillageDataForm.objects.all().values('town_name','now_village_identifier','now_administrative_village')

        village_data = collections.defaultdict(dict)
        for value in village_all:
            village_data[value['town_name']][value['now_village_identifier']] = value['now_administrative_village']

        self.village_data = village_data
        # 乡镇-行政村数据 end


        super(HelpUpDetail, self).__init__()

    def get(self,request):
        page = request.GET.get('page',1)
        policy_id = request.GET.get('policy_id')

        #搜索-start
        now_village_identifier = request.GET.get('now_village_identifier','').strip()
        idcard = request.GET.get('idcard','').strip()
        date_start = request.GET.get('date_start','').strip()
        date_end = request.GET.get('date_end', '').strip()
        search_condition = ''
        search_condition_house = ''
        search_condition_people = ''
        if now_village_identifier != '':
            #village_list_obj = report_models.AdministrativeVillageDataForm.objects.filter(now_village_identifier=now_village_identifier)
            householder_id_identifier = report_models.PoorHouseDataForm.objects.filter(now_village_identifier=now_village_identifier).values('householder_id','house_identifier')

            householder_ids = [v['householder_id'] for v in householder_id_identifier]
            householder_ids = ["'" + value + "'" for value in householder_ids]
            householder_ids_s = ','.join(householder_ids)
            if householder_ids_s == '':
                search_condition_house += "1 = 2 and "
            else:
                search_condition_house += "householder_id in ("+householder_ids_s+") and "

            house_identifiers = [v['house_identifier'] for v in householder_id_identifier]
            people_ids = report_models.PoorPeopleDataForm.objects.filter(house_identifier__in=house_identifiers).values_list('people_id', flat=True)
            people_ids = ["'" + value + "'" for value in people_ids]
            people_ids_s = ','.join(people_ids)
            if people_ids_s == '':
                search_condition_people += "1 = 2 and "
            else:
                search_condition_people += "people_id in ("+people_ids_s+") and "

            # if len(village_list_obj) > 0:
            #     village_obj = village_list_obj[0]
            #     search_condition_industry_agritainment += "town_name = '"+village_obj.town_name+"' and administrative_village = '"+village_obj.now_administrative_village+"' and "

            search_condition += "now_village_identifier = '"+now_village_identifier+"' and "

        if idcard != '':
            search_condition_house += "householder_id = '" + idcard + "' and "
            search_condition_people += "people_id = '" + idcard + "' and "
        if date_start != '':
            date_start_list = date_start.split('-')
            date_start_sql = "(date_year > "+date_start_list[0]+" or (date_year = "+date_start_list[0]+" and date_month > "+date_start_list[1]+")) and "
            search_condition += date_start_sql
            search_condition_house += date_start_sql
            search_condition_people += date_start_sql
        if date_end != '':
            date_end_list = date_end.split('-')
            date_end_sql = "(date_year < " + date_end_list[0] + " or (date_year = " + date_end_list[0] + " and date_month < " + date_end_list[1] + ")) and "
            search_condition += date_end_sql
            search_condition_house += date_end_sql
            search_condition_people += date_end_sql
        #搜索-end

        print(search_condition_house)

        policy_obj = report_models.PolicyStaticForm.objects.get(id=policy_id)
        policy_object = policy_obj.policy_object
        if policy_object == '贫困村':
            count_sql = "select count(id),ifnull(sum(policy_multiplier),0) as sum_policy_multiplier,ifnull(sum(plan_money),0) as sum_plan_money,ifnull(sum(fact_money),0) as sum_fact_money from report_form_administrativevillageadditionalform WHERE "+search_condition+"policy_number = "+policy_obj.policy_number
            count_res = list(report_models.AdministrativeVillageAdditionalForm.objects.raw(count_sql).query)
            count = count_res[0][0]

            group_count_sql = "select count(*) from (SELECT count(id) from report_form_administrativevillageadditionalform WHERE "+search_condition+"policy_number = "+policy_obj.policy_number+" GROUP BY now_village_identifier) as a"
            group_count_res = list(report_models.AdministrativeVillageAdditionalForm.objects.raw(group_count_sql).query)
            group_count = group_count_res[0][0]
        elif policy_object == '贫困户':
            count_sql = "select count(id),ifnull(sum(policy_multiplier),0) as sum_policy_multiplier,ifnull(sum(plan_money),0) as sum_plan_money,ifnull(sum(fact_money),0) as sum_fact_money from report_form_poorhouseadditionalform WHERE " + search_condition_house + "policy_number = " + policy_obj.policy_number
            count_res = list(report_models.PoorHouseAdditionalForm.objects.raw(count_sql).query)
            count = count_res[0][0]

            group_count_sql = "select count(*) from (SELECT count(id) from report_form_poorhouseadditionalform WHERE " + search_condition_house + "policy_number = " + policy_obj.policy_number+" GROUP BY people_id) as a"
            group_count_res = list(report_models.PoorHouseAdditionalForm.objects.raw(group_count_sql).query)
            group_count = group_count_res[0][0]
        elif policy_object == '贫困人口':
            count_sql = "select count(id),ifnull(sum(policy_multiplier),0) as sum_policy_multiplier,ifnull(sum(plan_money),0) as sum_plan_money,ifnull(sum(fact_money),0) as sum_fact_money from report_form_poorpeopleadditionalform WHERE " + search_condition_people + "policy_number = " + policy_obj.policy_number
            count_res = list(report_models.PoorPeopleAdditionalForm.objects.raw(count_sql).query)
            count = count_res[0][0]

            group_count_sql = "select count(*) from (SELECT count(id) from report_form_poorpeopleadditionalform WHERE " + search_condition_people + "policy_number = " + policy_obj.policy_number+" GROUP BY people_id) as a"
            group_count_res = list(report_models.PoorPeopleAdditionalForm.objects.raw(group_count_sql).query)
            group_count = group_count_res[0][0]
        else:
            count = 0
            count_res = []
            group_count = 0
        #print(count_res)
        # ***分页start
        every_page_number = 15
        try:
            page = int(page)
        except:
            page = 1

        num_pages = math.ceil(count/every_page_number)
        if page > num_pages:
            page = num_pages
        if page <= 0:
            page = 1
        # ***分页end

        limit_start = str(int((page-1)*15))
        if policy_object == '贫困村':
            sql = "SELECT basic.*,(SELECT now_administrative_village FROM report_form_administrativevillagedataform WHERE now_village_identifier = basic.now_village_identifier LIMIT 1) AS someone_name FROM report_form_administrativevillageadditionalform AS basic WHERE " + search_condition + "policy_number='" + policy_obj.policy_number + "' LIMIT "+limit_start+","+str(every_page_number)+";"
            #sql = "SELECT basic.*,extra.now_administrative_village as someone_name FROM report_form_administrativevillageadditionalform AS basic LEFT JOIN report_form_administrativevillagedataform AS extra ON basic.now_village_identifier = extra.now_village_identifier WHERE policy_number='" +policy_obj.policy_number + "';"
            obj_list = report_models.AdministrativeVillageAdditionalForm.objects.raw(sql)
            #obj_list = report_models.AdministrativeVillageAdditionalForm.objects.filter(policy_number=policy_obj.policy_number)
        elif policy_object == '贫困户':
            sql = "SELECT basic.*,(SELECT householder_name FROM report_form_poorhousedataform WHERE householder_id = basic.householder_id  LIMIT 1) AS someone_name FROM report_form_poorhouseadditionalform AS basic WHERE " + search_condition_house + "policy_number='" + policy_obj.policy_number + "' LIMIT "+limit_start+","+str(every_page_number)+";"
            #sql = "SELECT basic.*,extra.householder_name as someone_name FROM report_form_poorhouseadditionalform AS basic LEFT JOIN report_form_poorhousedataform AS extra ON basic.householder_id = extra.householder_id WHERE policy_number='"+policy_obj.policy_number+"';"
            obj_list = report_models.PoorHouseAdditionalForm.objects.raw(sql)
            #obj_list = report_models.PoorHouseAdditionalForm.objects.filter(policy_number=policy_obj.policy_number)
        elif policy_object == '贫困人口':
            sql = "SELECT basic.*,(SELECT people_name FROM report_form_poorpeopledataform WHERE people_id = basic.people_id  LIMIT 1) AS someone_name FROM report_form_poorpeopleadditionalform AS basic WHERE " + search_condition_people + "policy_number='" + policy_obj.policy_number + "' LIMIT "+limit_start+","+str(every_page_number)+";"

            #sql = "SELECT basic.*,extra.people_name as someone_name FROM report_form_poorpeopleadditionalform AS basic LEFT JOIN report_form_poorpeopledataform AS extra ON basic.people_id = extra.people_id WHERE policy_number='" + policy_obj.policy_number + "';"
            obj_list = report_models.PoorPeopleAdditionalForm.objects.raw(sql)
            #obj_list = report_models.PoorPeopleAdditionalForm.objects.filter(policy_number=policy_obj.policy_number)
        else:
            obj_list = []

        data = list(obj_list)

        return render(request,'excel_view/help_up_detail.html',{
            "page":page,
            "count":count,
            "policy_id":policy_id,
            "every_page_number":every_page_number,
            "policy_obj":policy_obj,
            "data":data,
            "village_data": self.village_data,
            "village_data_str": json.dumps(self.village_data),
            "sum_data_sum":count_res[0],
            "group_count":group_count
        })

# 主线程函数
def create_index_excel_func(request):
    dir_list = VIEW_DICT

    # 存放线程的实例
    t_objs = []
    for dep_id,adir in dir_list.items():
        path = os.path.join(VIEW_DIR, adir).replace('\\', '/')
        t = threading.Thread(target=create_index_excel, args=(path,dep_id))
        t.start()
        # 为了不让后面的子线程阻塞，把当前的子线程放入到一个列表中
        t_objs.append(t)



    # 循环所有子线程实例，等待所有子线程执行完毕
    # for t in t_objs:
    #     t.join()


    #return True    # 所有子进程结束后返回True

def create_index_excel(path,dep_id):
    # from jieba.analyse import ChineseAnalyzer
    #
    # analyzer = ChineseAnalyzer()

    myschema = Schema(path=ID(unique=True, stored=True), time=STORED, content=TEXT(analyzer=ChineseAnalyzer()),
           title=TEXT(analyzer=ChineseAnalyzer(), stored=True),url=STORED)

    if os.path.isdir(path):
        file_list = common.scandir(path)
        print(file_list)
        init_path = VIEW_DIR

        index_path = os.path.join(settings.BASE_DIR, "common/excel_index/" + dep_id).replace('\\', '/')
        if os.path.isdir(index_path) == False:
            os.makedirs(index_path)

        # Always create the index from scratch
        ix = create_in(index_path, schema=myschema)
        writer = ix.writer()

        # Assume we have a function that gathers the filenames of the
        # documents to be indexed
        for file_path in file_list:
            file_path = file_path.replace('\\','/')
            file_size = os.path.getsize(file_path)/1048576
            if file_size < 25:
                file_type = os.path.splitext(file_path)[-1]
                title = os.path.basename(file_path)
                print(file_path)
                if file_type == '.docx':
                    content = excel_repos.word_parse(file_path)
                elif file_type in ['.xls', '.xlsx']:
                    content = excel_repos.excel_parse(file_path)
                elif file_type in ['.ppt', '.pptx']:
                    content = excel_repos.ppt_parse2(file_path)
                elif file_type == '.pdf':
                    content = excel_repos.pdf_parse(file_path)
                elif file_type == '.txt':
                    content = excel_repos.txt_parse(file_path)
                else:
                    content = ''

                writer.add_document(path=file_path, content=content+title, title=title, time=os.path.getmtime(file_path),
                                    url=file_path.replace(path, ''))
        writer.commit()

def search(request):  # 搜索
    id = request.GET.get('id')
    keyword = request.GET.get('keyword')

    department_obj = department_models.Department.objects.get(id=id)
    #init_path = os.path.join(settings.BASE_DIR, "common/repositories/"+str(repository_obj.id)).replace('\\', '/')
    try:
        results = search_excel(id,keyword)
        print('---',results)
    except:
        results = []
        print('报错了')

    return render(request,'excel_view/search.html',{"results":results,"department_obj":department_obj})

def search_excel(id, keyword):
    path = os.path.join(settings.BASE_DIR, "common/excel_index/"+str(id)).replace('\\', '/')
    print(path)
    ix = open_dir(path)  # 打开索引
    with ix.searcher() as searcher:
        searcher = ix.searcher()
        results = searcher.find('content', keyword)

    return results

def template_list(request):
    template_list = excel_models.Template.objects.all().order_by('title')
    return render(request,'excel_view/template_list.html',{"template_list":template_list})

def template_add(request):
    user_id = request.user.id
    if request.method == 'POST':
        post = request.POST.dict()
        title = post.get('title')
        #rows = request.POST.getlist('rows[]', [])

        rows = json.loads(post.get('rows_str', '[]'))
        rows = [[str(v).strip(), str(v1).strip()] for v, v1 in rows]

        if re.search(r'[\[~@#$&()^%!,;:\'‘’"“”。.\]]', title, re.M | re.I):
            res = {'code': '-1', 'message': '标题不能包含“[~@#$&()^%!,;:\'‘’"“”]”等特殊字符', 'data': []}
            return JsonResponse(res, safe=False)

        excel_models.Template.objects.create(user_id=user_id,title=title,row=json.dumps(rows))
        return JsonResponse({"code": "200", "message": "添加成功", "data": []}, safe=False)
    else:
        return render(request, 'excel_view/template_add.html')

def template_edit(request):
    template_id = request.GET.get('id')
    template_info = excel_models.Template.objects.get(id=template_id)
    if request.method == 'POST':
        post = request.POST.dict()
        title = post.get('title','').strip()
        #rows = request.POST.getlist('rows[]',[])

        rows = json.loads(post.get('rows_str','[]'))
        rows = [[str(v).strip(),str(v1).strip()] for v,v1 in rows]


        if re.search(r'[\[~@#$&()^%!,;:\'‘’"“”。.\]]', title, re.M | re.I):
            res = {'code': '-1', 'message': '标题不能包含“[~@#$&()^%!,;:\'‘’"“”]”等特殊字符', 'data': []}
            return JsonResponse(res, safe=False)

        template_info.title = title
        template_info.row = json.dumps(rows)
        template_info.save()
        return JsonResponse({"code":"200","message":"编辑成功","data":[]},safe=False)
    else:
        template_info.row = json.loads(template_info.row)
        return render(request, 'excel_view/template_add.html',{"template_info":template_info})

def template_delete(request):
    template_id = request.GET.get('id')
    obj = excel_models.Template.objects.get(id=template_id)
    obj.delete()
    return JsonResponse({"code": "200", "message": "删除成功", "data": []}, safe=False)

def template_download(request):
    template_id = request.GET.get('id')
    obj = excel_models.Template.objects.get(id=template_id)

    path = os.path.join(settings.BASE_DIR,'common/excel_template/').replace('\\','/')
    if os.path.isdir(path) == False:
        os.mkdir(path)
    file_name = obj.title+'.xls'

    template_data = json.loads(obj.row)#获取模板数据

    wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)  ##第二参数用于确认同一个cell单元是否可以重设值。


    style_common = xlwt.easyxf('font: name Times New Roman, color-index black,height 0x0012c;align: wrap on, vert centre, horiz center;')

    for k,v in enumerate(template_data):
        sheet.write(1, k, v[0], style_common)

    for k,v in enumerate(template_data):
        sheet.col(k).width = 0x0d00 + 250*len(v[0])

    sheet.write_merge(0, 0, 0, len(template_data)-1, str(obj.title), xlwt.easyxf('font: name Times New Roman, color-index black,bold on,height 0x0012c;align: wrap on, vert centre, horiz center;'))

    wbk.save(path+file_name)  ##该文件路径必须存在
    return HttpResponseRedirect('/common/excel_template/' + file_name)

@login_required
def excel_approve1(request):  # 审核
    user_id = request.user.id
    user_obj = user_models.UserExtra.objects.get(about_id=user_id)
    user_ids = list(user_obj.department.userextra_set.all().values_list('about_id', flat=True))
    user_ids = [str(v) for v in user_ids]
    user_list_join = ','.join(user_ids)
    if user_list_join != '':
        condition = "upload_user_id in ("+user_list_join+")"
    else:
        condition = '1=2'

    page = request.GET.get('page')

    count_sql = "SELECT count(id) FROM excel_view_excelapprove WHERE "+condition+";"
    count_res = list(excel_models.ExcelApprove.objects.raw(count_sql).query)
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
    limit_start = str(int((page - 1) * every_page_number))

    sql = "SELECT *,(select max(id) from excel_view_excelapprove WHERE path = basis.path) as max_id FROM excel_view_excelapprove as basis WHERE "+condition+" order by create_time desc LIMIT " + limit_start + "," + str(every_page_number) + ";"
    obj_list = excel_models.ExcelApprove.objects.raw(sql)
    objs = []
    for i in obj_list:
        i_path = i.path.split('/')
        if len(i_path) > 0:
            i.excel_path = i_path[-1]

        i.path = os.path.join(DOWNLOAD_URL_PR,i.path)

        objs.append(i)
    return render(request,'excel_view/excel_approve1.html',{
        "page": page,
        "every_page_number": every_page_number,
        "count": count,
        "obj_list":objs
    })

@login_required
#审核文件列表
def excel_approve(request):
    user_id = request.user.id
    user_obj = user_models.UserExtra.objects.get(about_id=user_id)
    department_list = list(user_obj.department.department_set.all().values_list('id',flat=True))
    if user_obj.department_id == 10:
        department_list.append(user_obj.department_id)
    department_list = [str(v) for v in department_list]
    department_list_join = ','.join(department_list)

    if department_list_join != '':
        condition = "department_id in ("+department_list_join+")"
    else:
        condition = '1=2'

    page = request.GET.get('page')

    count_sql = "SELECT count(id) FROM excel_view_excelapprove WHERE "+condition+";"
    count_res = list(excel_models.ExcelApprove.objects.raw(count_sql).query)
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
    limit_start = str(int((page - 1) * every_page_number))

    sql = "SELECT *,(select max(id) from excel_view_excelapprove WHERE path = basis.path) as max_id FROM excel_view_excelapprove as basis WHERE "+condition+" order by create_time desc LIMIT " + limit_start + "," + str(every_page_number) + ";"
    print(sql)
    obj_list = excel_models.ExcelApprove.objects.raw(sql)
    objs = []
    for i in obj_list:
        i_path = i.path.split('/')
        if len(i_path) > 0:
            i.excel_path = i_path[-1]

        i.path = os.path.join(DOWNLOAD_URL_PR,i.path)

        objs.append(i)

    return render(request,'excel_view/excel_approve.html',{
        "page":page,
        "every_page_number":every_page_number,
        "count":count,
        "obj_list":objs
    })

@login_required
def approve_reject(request):  # 审核被拒
    remark = request.POST.get('remark','') # 备注
    obj_id = request.POST.get('id')

    obj = excel_models.ExcelApprove.objects.get(id=obj_id)
    obj.remark = remark
    obj.status = 0
    obj.save()
    return JsonResponse({"code":"200"})

@login_required
def approve_agree(request):  # 审核通过
    obj_id = request.POST.get('id')
    remark = request.POST.get('remark', '')
    obj = excel_models.ExcelApprove.objects.get(id=obj_id)

    path = os.path.join(VIEW_DIR,obj.path)
    print(path)
    data = read_excel('',path)
    tem_is_true, tem_data = common.verify_excel_zc(data)
    #tem_data_dict = dict(tem_data)

    tem_fields = []
    tem_excel_fields = []
    for value in tem_data:
        tem_fields.append(value[1])
        tem_excel_fields.append(value[0])
    print(tem_is_true, tem_data)
    print(tem_excel_fields)

    if tem_is_true:
        data_list = []
        for key,value in enumerate(data):
            if key >= 2:
                data_list.append(list(zip(tem_fields,value)))

        _str = ''
        for value in tem_data:
            _str += value[0]
        #用于处理畜牧局-start
        if '猪' in _str and '牛' in _str and '鸡' in _str and '鸭' in _str:  # 是否为畜牧局Excel
            tem_excel_fields_find_zhu = tem_excel_fields.index('猪')
            tem_excel_fields_find_niu = tem_excel_fields.index('牛')
            tem_excel_fields_find_ji = tem_excel_fields.index('鸡')
            tem_excel_fields_find_ya = tem_excel_fields.index('鸭')
            tem_excel_fields_find_e = tem_excel_fields.index('鹅')
            tem_excel_fields_find_tu = tem_excel_fields.index('兔')
            tem_excel_fields_find_feng = tem_excel_fields.index('蜂')
            b_data_list = []
            for key, value in enumerate(data_list):
                b_list = []
                for k, v in enumerate(value):
                    if v[0] != 'policy_multiplier' and v[0] != 'subsidy_standard' and v[0] != 'plan_money':
                        b_list.append(v)
                b_data_list.append(b_list)
            # print(len(b_data_list),b_data_list)
            # print(len(data_list), data_list)
            c_data_list = []
            for key, value in enumerate(data_list):
                for k, v in enumerate(value):
                    if v[0] == 'policy_multiplier':
                        c_list = []
                        c_list.append(value[k])
                        c_list.append(value[k + 1])
                        c_list.append(value[k + 2])

                        if k == tem_excel_fields_find_zhu:
                            c_list.append(('policy_number','010104'))
                        elif k == tem_excel_fields_find_niu:
                            c_list.append(('policy_number', '010108'))
                        elif k == tem_excel_fields_find_ji:
                            c_list.append(('policy_number', '01010501'))
                        elif k == tem_excel_fields_find_ya:
                            c_list.append(('policy_number', '01010502'))
                        elif k == tem_excel_fields_find_e:
                            c_list.append(('policy_number', '01010503'))
                        elif k == tem_excel_fields_find_tu:
                            c_list.append(('policy_number', '01010504'))
                        elif k == tem_excel_fields_find_feng:
                            c_list.append(('policy_number', '010107'))

                        c_list = c_list + b_data_list[key]
                        c_data_list.append(c_list)

            data_list = c_data_list
        # 用于处理畜牧局-end

        # 用于处理残联-start
        if '残疾人证号' in _str and '生活补贴（金额）' in _str and '护理补贴（金额）' in _str:  # 是否为残联Excel
            tem_excel_fields_find_1 = tem_excel_fields.index('生活补贴（金额）')
            tem_excel_fields_find_2 = tem_excel_fields.index('护理补贴（金额）')
            b_data_list = []
            for key, value in enumerate(data_list):
                b_list = []
                for k, v in enumerate(value):
                    if v[0] != 'fact_money':
                        b_list.append(v)
                b_data_list.append(b_list)
            c_data_list = []
            for key, value in enumerate(data_list):
                for k, v in enumerate(value):
                    if v[0] == 'fact_money':
                        c_list = []
                        c_list.append(value[k])

                        if k == tem_excel_fields_find_1:
                            c_list.append(('policy_number', '06010101'))
                        elif k == tem_excel_fields_find_2:
                            c_list.append(('policy_number', '06010102'))

                        c_list = c_list + b_data_list[key]
                        c_data_list.append(c_list)

            data_list = c_data_list
        # 用于处理残联-end

        # 用于处理教育局-start
        if '学生在读类别' in _str:  # 是否为教育局Excel
            tem_excel_fields_find = tem_excel_fields.index('学生在读类别')
            print(tem_excel_fields_find)
            for key, value in enumerate(data_list):
                tem_excel_fields_policy_number_dict = {
                    "学前教育":"020101",
                    "小学阶段":"020201",
                    "初中":"02030101",
                    "高中":"02030102",
                    "中职":"02030103",
                    "高职高专":"02030104",
                    "大学":"02030105"
                }
                data_list[key].append(('policy_number', tem_excel_fields_policy_number_dict.get(value[tem_excel_fields_find][1],'')))
        # 用于处理教育局-end

        # 用于处理建设局（危房改造）-start
        if '贫困户类别' in _str and '危房等级' in _str:  # 是否为建设局（危房改造）Excel
            tem_excel_fields_find_1 = tem_excel_fields.index('贫困户类别')
            tem_excel_fields_find_2 = tem_excel_fields.index('危房等级')
            for key, value in enumerate(data_list):
                if value[tem_excel_fields_find_1][1] == '建档立卡贫困户' and value[tem_excel_fields_find_2][1] == 'C级':
                    data_list[key].append(('policy_number', '05020101'))
                elif value[tem_excel_fields_find_1][1] == '建档立卡贫困户' and value[tem_excel_fields_find_2][1] == 'D级':
                    data_list[key].append(('policy_number', '05020201'))
                elif value[tem_excel_fields_find_1][1] == '低保户' and value[tem_excel_fields_find_2][1] == 'C级':
                    data_list[key].append(('policy_number', '05020102'))
                elif value[tem_excel_fields_find_1][1] == '低保户' and value[tem_excel_fields_find_2][1] == 'D级':
                    data_list[key].append(('policy_number', '05020202'))
                elif value[tem_excel_fields_find_1][1] == '农村分散供养特困人员' and value[tem_excel_fields_find_2][1] == 'C级':
                    data_list[key].append(('policy_number', '05020103'))
                elif value[tem_excel_fields_find_1][1] == '农村分散供养特困人员' and value[tem_excel_fields_find_2][1] == 'D级':
                    data_list[key].append(('policy_number', '05020203'))
                elif value[tem_excel_fields_find_1][1] == '贫困残疾人家庭' and value[tem_excel_fields_find_2][1] == 'C级':
                    data_list[key].append(('policy_number', '05020104'))
                elif value[tem_excel_fields_find_1][1] == '贫困残疾人家庭' and value[tem_excel_fields_find_2][1] == 'D级':
                    data_list[key].append(('policy_number', '05020204'))
        # 用于处理建设局（危房改造）-end

        # 用于处理建设局（易地搬迁）-start
        if '安置方式' in _str and '安置点名称' in _str:  # 是否为教育局Excel
            tem_excel_fields_find = tem_excel_fields.index('安置方式')
            print(tem_excel_fields_find)
            for key, value in enumerate(data_list):
                tem_excel_fields_policy_number_dict = {
                    "集中安置": "050101",
                    "进镇购房": "050102",
                    "分散安置": "050103"
                }
                data_list[key].append(
                    ('policy_number', tem_excel_fields_policy_number_dict.get(value[tem_excel_fields_find][1], '')))
        # 用于处理建设局（易地搬迁）-end

        # 用于处理民政局（农村低保）-start
        if '邮局账号' in _str and '家庭人口' in _str and '家庭人均纯收入' in _str:  # 是否为民政局（农村低保）Excel
            for key, value in enumerate(data_list):
                data_list[key].append(('bank_name', '邮政银行'))
                data_list[key].append(('policy_number', '040301'))
        # 用于处理民政局（农村低保）-end

        # 用于民政局（农村特困_社会散住）Excel 或 民政局（农村特困_在院供养）Excel-start
        if "生活补助" in _str and "护理标准" in _str and "供养方式" in _str:  # 是否为民政局（农村特困_社会散住）Excel 或 民政局（农村特困_在院供养）Excel
            tem_excel_fields_find_1 = tem_excel_fields.index('生活补助')
            tem_excel_fields_find_2 = tem_excel_fields.index('护理标准')
            b_data_list = []
            for key, value in enumerate(data_list):
                b_list = []
                for k, v in enumerate(value):
                    if v[0] != 'fact_money':
                        b_list.append(v)
                b_data_list.append(b_list)
            c_data_list = []
            for key, value in enumerate(data_list):
                for k, v in enumerate(value):
                    if v[0] == 'fact_money':
                        c_list = []
                        c_list.append(value[k])

                        c_list = c_list + b_data_list[key]
                        c_data_list.append(c_list)

            data_list = c_data_list
        # 用于民政局（农村特困_社会散住）Excel 或 民政局（农村特困_在院供养）Excel-end

        # 用于民政局（农村孤儿）Excel-start
        if '孤儿姓名' in _str and '儿童编号' in _str:
            tem_excel_fields_find = tem_excel_fields.index('补助类型（在院供养2018/社会散住2018）')
            print(tem_excel_fields_find)
            for key, value in enumerate(data_list):
                tem_excel_fields_policy_number_dict = {
                    "社会散住2018": "04020202",
                    "在院供养2018": "04020102"
                }
                data_list[key].append(
                    ('policy_number', tem_excel_fields_policy_number_dict.get(value[tem_excel_fields_find][1], '')))
        # 用于民政局（农村孤儿）Excel-end




        field_data_list = []
        for value in data_list:
            item = {}
            for val1,val2 in value:
                if val1 != '':
                    if val1 == 'date_yeardate_month':
                        item['date_year'] = str(val2)[:4]
                        item['date_month'] = str(val2)[4:]
                    elif val1 == 'householder_id' or val1 == 'people_id':
                        item[str(val1)] = str(val2)[:18]
                    else:
                        item[str(val1)] = str(val2)

            field_data_list.append(item)

        tem_obj = excel_models.Template.objects.filter(row=json.dumps(tem_data))[0]

        if tem_obj.id != 36 and tem_obj.policy_object != '农家乐吸纳就业' and tem_obj.policy_object != '企业吸纳就业' and ('猪' in _str and '牛' in _str and '鸡' in _str and '鸭' in _str) == False and ('残疾人证号' in _str and '生活补贴（金额）' in _str and '护理补贴（金额）' in _str) == False and ('学生在读类别' in _str) == False and ('贫困户类别' in _str and '危房等级' in _str) == False and ('安置方式' in _str and '安置点名称' in _str) == False and ('邮局账号' in _str and '家庭人口' in _str and '家庭人均纯收入' in _str) == False and ('孤儿姓名' in _str and '儿童编号' in _str) == False:
            policystatic_list = list(report_models.PolicyStaticForm.objects.all().values('policy_number', 'policy_first_layer','policy_second_layer', 'policy_third_layer'))

            file_name = os.path.split(path)[1]
            file_name_policys = file_name.split('_')

            flag_intersection = False
            policy_number = None
            for value in policystatic_list:
                policystatic_names = list(value.values())
                intersection_names = set(policystatic_names) & set(file_name_policys)
                if len(intersection_names) >= 3:
                    flag_intersection = True
                    policy_number = value['policy_number']

            if flag_intersection == False:
                return JsonResponse({"code": "-1", 'message': '文件名格式不正确'}, safe=False)


            for key,value in enumerate(field_data_list):
                field_data_list[key]['policy_number'] = policy_number



        table_data_list = []
        if tem_obj.policy_object == '四位一体':
            for value in field_data_list:
                table_data_list.append(health_models.FourInOneAdditionalForm(**value))
            if len(table_data_list) > 0:
                health_models.FourInOneAdditionalForm.objects.bulk_create(table_data_list)
        elif tem_obj.policy_object == '贫困村':
            for value in field_data_list:
                table_data_list.append(report_models.AdministrativeVillageAdditionalForm(**value))
            if len(table_data_list) > 0:
                report_models.AdministrativeVillageAdditionalForm.objects.bulk_create(table_data_list)
        elif tem_obj.policy_object == '贫困户':
            for value in field_data_list:
                table_data_list.append(report_models.PoorHouseAdditionalForm(**value))
            if len(table_data_list) > 0:
                report_models.PoorHouseAdditionalForm.objects.bulk_create(table_data_list)
        elif tem_obj.policy_object == '贫困人口':
            for value in field_data_list:
                table_data_list.append(report_models.PoorPeopleAdditionalForm(**value))
            if len(table_data_list) > 0:
                report_models.PoorPeopleAdditionalForm.objects.bulk_create(table_data_list)
        elif tem_obj.policy_object == '农家乐吸纳就业':
            for value in field_data_list:
                table_data_list.append(report_models.IndustryAgritainmentDataForm(**value))
            if len(table_data_list) > 0:
                report_models.IndustryAgritainmentDataForm.objects.bulk_create(table_data_list)
        elif tem_obj.policy_object == '企业吸纳就业':
            for value in field_data_list:
                table_data_list.append(report_models.IndustryEnterpriseDataForm(**value))
            if len(table_data_list) > 0:
                report_models.IndustryEnterpriseDataForm.objects.bulk_create(table_data_list)

        print(tem_obj)
        #print(field_data_list)

        obj.status = 1
        obj.remark = remark
        obj.save()

        return JsonResponse({"code": "200", 'message': '成功'}, safe=False)
    else:
        return JsonResponse({"code":"-1",'message':'excel格式不正确'},safe=False)