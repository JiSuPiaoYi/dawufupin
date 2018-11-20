from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.db import connection

from user_center import models as user_models
from weixin_xcx import form_verify
from app_common import repositories as common_repositories
from app_common import models as common_models
from app_common import common
from report_form import models as report_models
from health_data import models as health_models

import json,urllib,uuid,re,os,math
from operator import itemgetter

# Create your views here.


# 判断是否完成了微信帐号绑定
@csrf_exempt
def is_account_bind(request):
    code = request.POST.get('code','')

    appid = settings.APPID
    secret = settings.APPSECRET

    if code == '':
        return JsonResponse({"code": "-1", "message": "code错误"})

    url = "https://api.weixin.qq.com/sns/jscode2session?appid=" + appid + "&secret=" + secret + "&js_code=" + code + "&grant_type=authorization_code"

    # json_obj = requests.get(url)
    try:
        json_obj = urllib.request.urlopen(url).read()
        json_obj = json.loads(str(json_obj, encoding="utf-8"))
    except:
        return JsonResponse({"code": "-1", "message": "登录失败！"})
    else:
        if "errcode" in json_obj.keys():
            return JsonResponse({"code": json_obj['errcode'], "message": json_obj['errmsg']})
        else:
            openid = json_obj['openid']
            session_key = json_obj['session_key']

            try:
                userinfo = user_models.UserExtra.objects.get(openid=openid)
            except user_models.UserExtra.DoesNotExist:
                # 如果微信帐号没有和本系统中用户绑定
                return JsonResponse({"code": "40001", "message": "微信登录成功，现在绑定账号！", "data": {"openid": openid}})
            else:
                # 如果微信帐号已经和本系统中用户绑定了，则登录成功
                userinfo.token = get_uuid()
                userinfo.save()

                data = {
                    "name": userinfo.name,
                    "mobile": userinfo.mobile,
                    "department_name": userinfo.department.name,
                    "department_id": userinfo.department.id,
                    "token": userinfo.token
                }
                return JsonResponse(
                    {"code": "200", "message": "登录成功！", "data": data})


# 小程序微信登录后帐号绑定
@csrf_exempt
def account_bind(request):
    post = request.POST
    verifier = form_verify.VerifyAccountBind(post, auto_id=False)
    if verifier.is_valid():
        try:
            userobj = user_models.UserExtra.objects.get(mobile=verifier.cleaned_data['mobile'])
        except:
            res = {'code': '-1', 'message': "手机号未注册", 'data': []}
        else:
            user = auth.authenticate(username=userobj.about.username, password=verifier.cleaned_data['passwd'])
            if user is not None:
                if user.is_active:
                    #user_models.UserExtra.objects.filter(openid=verifier.cleaned_data['openid']).update(unionid='')#删除以往绑定记录

                    if userobj.department.id not in [10,28]:
                        res = {'code': '-1', 'message': "非扶贫办或帮扶人账号，没有权限", 'data': []}
                    else:
                        userobj.openid = verifier.cleaned_data['openid']
                        userobj.token = get_uuid()
                        userobj.save()

                        data = {
                            "name": userobj.name,
                            "mobile": userobj.mobile,
                            "department_name": userobj.department.name,
                            "department_id":userobj.department.id,
                            "token": userobj.token
                        }
                        res = {'code': '200', 'message': "登录成功",'data': data}
                else:
                    res = {'code': '-1', 'message': "用户未激活", 'data': []}
            else:
                print(user)
                res = {'code': '-1', 'message': "用户不存在或密码错误", 'data': []}
    else:
        one_error = list(json.loads(verifier.errors.as_json()).items())[0][1][0]['message']
        res = {'code': '-1', 'message': one_error, 'data': []}
    return JsonResponse(res, safe=False)

def annunciate_list(request):
    annunciates = list(common_models.Annunciate.objects.all().values())
    for key, value in enumerate(annunciates):
        annunciates[key]['short_content'] = value['content'][:50]
        annunciates[key]['create_time'] = value['create_time'].strftime('%Y-%m-%d %H:%M:%S')

    annunciates.sort(key=itemgetter('create_time'), reverse=True)

    res = {'code': '200', 'message': '成功', 'data': annunciates}
    return JsonResponse(res, safe=False)

def annunciate_info(request):
    data_id = request.GET.get('id')
    obj = common_models.Annunciate.objects.get(id=data_id)
    data = {
        "title":obj.title,
        "content":obj.content.replace(os.linesep,'\n'),
        "create_time":obj.create_time.strftime('%Y-%m-%d %H:%M:%S')
    }
    # pattern = re.compile(r'hello', re.I)
    # match = pattern.match('hello world!')
    # print(match.group())

    res = {'code': '200', 'message': '成功', 'data': data}
    return JsonResponse(res, safe=False)

def governmentdecree_list(request):
    governmentdecrees = list(common_models.GovernmentDecree.objects.all().values())
    for key, value in enumerate(governmentdecrees):
        governmentdecrees[key]['short_content'] = value['content'][:50]
        governmentdecrees[key]['create_time'] = value['create_time'].strftime('%Y-%m-%d %H:%M:%S')

    governmentdecrees.sort(key=itemgetter('create_time'), reverse=True)

    res = {'code': '200', 'message': '成功', 'data': governmentdecrees}
    return JsonResponse(res, safe=False)

def governmentdecree_info(request):
    data_id = request.GET.get('id')
    obj = common_models.GovernmentDecree.objects.get(id=data_id)
    data = {
        "title":obj.title,
        "content":obj.content.replace(os.linesep,'\n'),
        "create_time":obj.create_time.strftime('%Y-%m-%d %H:%M:%S')
    }

    res = {'code': '200', 'message': '成功', 'data': data}
    return JsonResponse(res, safe=False)

def user_info(request):
    token = request.GET.get('token')
    user_obj = user_models.UserExtra.objects.get(token=token)

    data = {
        "name":user_obj.name,
        "mobile":user_obj.mobile,
        "department_name":user_obj.department.name
    }
    res = {'code': '200', 'message': '成功', 'data': data}
    return JsonResponse(res, safe=False)

@csrf_exempt
def change_password(request):
    post = request.POST
    verifier = form_verify.VerifyPassword(post, auto_id=False)

    if verifier.is_valid():
        userobj = user_models.UserExtra.objects.get(token=verifier.cleaned_data['token'])
        if verifier.cleaned_data['new_password'] != verifier.cleaned_data['qr_new_password']:
            res = {'code': '-1', 'message': "两次密码不一致", 'data': []}
        else:
            user = auth.authenticate(username=userobj.about.username, password=verifier.cleaned_data['old_password'])
            if user is not None:
                auth_user = userobj.about
                auth_user.password = make_password(verifier.cleaned_data['new_password'])
                auth_user.save()
                res = {'code': '200', 'message': '修改成功', 'data': []}
            else:
                res = {'code': '-1', 'message': "旧密码错误", 'data': []}
    else:
        one_error = list(json.loads(verifier.errors.as_json()).items())[0][1][0]['message']
        res = {'code': '-1', 'message': one_error, 'data': []}
    return JsonResponse(res, safe=False)

def poorhouse_list(request):
    page = request.GET.get('page', 1)
    name = request.GET.get('name', '').strip()
    idcard = request.GET.get('idcard', '').strip()
    token = request.GET.get('token')
    user_obj = user_models.UserExtra.objects.get(token=token)

    # 搜索-start
    search_condition = ''
    if user_obj.department.id == 28:
        #帮扶人查询
        house_identifiers = report_models.HelperDataForm.objects.filter(mobile_phone=user_obj.mobile).values_list('household_identifier',flat=True)
        house_identifiers = ["'"+value+"'" for value in house_identifiers]
        house_identifier_s = ','.join(house_identifiers)

        if house_identifier_s == '':
            search_condition += "1 = 2 and "
        else:
            search_condition += "householder_id in (" + house_identifier_s + ") and "
    elif user_obj.department.id == 10:
        #扶贫办查询
        if name != '':
            house_identifiers = report_models.PoorPeopleDataForm.objects.filter(people_name=name).values_list('house_identifier', flat=True)
            house_identifiers = ["'" + value + "'" for value in house_identifiers]
            house_identifier_s = ','.join(house_identifiers)
            if house_identifier_s == '':
                search_condition += "1 = 2 and "
            else:
                search_condition += "house_identifier in (" + house_identifier_s + ") and "

        if idcard != '':
            house_identifiers = report_models.PoorPeopleDataForm.objects.filter(people_id=idcard).values_list('house_identifier', flat=True)
            house_identifiers = ["'" + value + "'" for value in house_identifiers]
            house_identifier_s = ','.join(house_identifiers)
            if house_identifier_s == '':
                search_condition += "1 = 2 and "
            else:
                search_condition += "house_identifier in (" + house_identifier_s + ") and "
    else:
        #其他部分查询，没有权限，查询不到数据
        search_condition += "1 = 2 and "
    # 搜索-end

    if search_condition == '':
        #如果搜索条件为空，那么查询所有
        search_condition = '1=1'
    else:
        search_condition += '1=1'

    count_sql = "SELECT count(id) FROM report_form_poorhousedataform WHERE "+search_condition+";"
    print(count_sql)
    count_res = list(report_models.PoorHouseDataForm.objects.raw(count_sql).query)
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

    sql = "SELECT *,(SELECT CONCAT_WS('',town_name,now_administrative_village) FROM report_form_administrativevillagedataform WHERE now_village_identifier = basic.now_village_identifier LIMIT 1) as home_location FROM report_form_poorhousedataform AS basic WHERE "+ search_condition + " LIMIT "+limit_start+","+str(every_page_number)+";"
    obj_list = report_models.PoorHouseDataForm.objects.raw(sql)
    obj_list = list(obj_list)

    #转json数据-start
    models_fields = [v.column for v in report_models.PoorHouseDataForm._meta.get_fields()]  # 表中所有字段
    for key,value in enumerate(obj_list):
        value_data = {}
        for field in models_fields:
            value_data[field] = getattr(value,field)
            value_data['home_location'] = value.home_location
        obj_list[key] = value_data
    #转json数据-end

    return JsonResponse({
        "page": page,
        "count": count,
        "num_pages":num_pages,
        "every_page_number":every_page_number,
        "poorhouse_list": obj_list
    }, safe=False)

def poorhouse_detail(request):
    data_id = request.GET.get('id','')
    obj = report_models.PoorHouseDataForm.objects.get(id=data_id)

    models_fields = [v.column for v in report_models.PoorHouseDataForm._meta.get_fields()]  # 表中所有字段
    detail = {}
    for field in models_fields:
        detail[field] = getattr(obj, field)

    field_tuple = ("policy_multiplier","plan_money","fact_money","date_year","date_month","policy_data","take_obj")
    sql = "SELECT policy_multiplier,plan_money,fact_money,date_year,date_month,(SELECT CONCAT_WS(',',policy_first_layer,policy_second_layer,policy_third_layer,subsidy_one) FROM report_form_policystaticform WHERE policy_number = report_form_poorhouseadditionalform.policy_number) as policy_data,(SELECT CONCAT('"+obj.householder_name+"','（户主）')) as take_obj FROM report_form_poorhouseadditionalform WHERE householder_id = '"+obj.householder_id+"' UNION ALL SELECT policy_multiplier,plan_money,fact_money,date_year,date_month,(SELECT CONCAT_WS(',',policy_first_layer,policy_second_layer,policy_third_layer,subsidy_one) FROM report_form_policystaticform WHERE policy_number = report_form_poorpeopleadditionalform.policy_number) as policy_data,(SELECT CONCAT(people_name,'（',people_relationship,'）') FROM report_form_poorpeopledataform WHERE people_id = report_form_poorpeopleadditionalform.people_id) as take_obj FROM report_form_poorpeopleadditionalform WHERE people_id IN (SELECT people_id FROM report_form_poorpeopledataform WHERE house_identifier = '"+obj.house_identifier+"')"
    print(sql)

    cursor = connection.cursor()
    cursor.execute(sql)
    policys = cursor.fetchall()  # 读取所有

    policy_list = []
    for value in policys:
        policy_list.append(dict(zip(field_tuple,value)))

    for key,value in enumerate(policy_list):
        policy_data = value['policy_data'].split(',')
        policy_list[key]['policy_first_layer'] = policy_data[0]
        policy_list[key]['policy_second_layer'] = policy_data[1]
        policy_list[key]['policy_third_layer'] = policy_data[2]
        policy_list[key]['subsidy_one'] = policy_data[3]


    four_one_sql = "select * from health_data_fourinoneadditionalform where people_id IN (SELECT people_id FROM report_form_poorpeopledataform WHERE house_identifier = '"+obj.house_identifier+"')"
    four_one_list_raw = list(health_models.FourInOneAdditionalForm.objects.raw(four_one_sql))
    four_one_models_fields = [v.column for v in health_models.FourInOneAdditionalForm._meta.get_fields()]  # 表中所有字段
    four_one_list = []
    for value in four_one_list_raw:
        four_one_detail = {}
        for field in four_one_models_fields:
            four_one_detail[field] = getattr(value, field)
        four_one_list.append(four_one_detail)

    res = {'code': '200', 'message': "成功", 'data': {
        "detail":detail,
        "policy_list":policy_list,
        "four_one_list":four_one_list
    }}
    return JsonResponse(res, safe=False)

#账号解绑
@csrf_exempt
def relieve_bind(request):
    token = request.POST.get('token')
    userobj = user_models.UserExtra.objects.get(token=token)
    userobj.openid = None
    userobj.save()
    return JsonResponse({"code":"200","message":"解绑成功","data":[]})

#意见反馈
@csrf_exempt
def feedback(request):
    token = request.POST.get('token')
    type = request.POST.get('type')
    content = request.POST.get('content')
    about_object = request.POST.get('about_object')
    about_object_content = request.POST.get('about_object_content')
    my_file = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
    userobj = user_models.UserExtra.objects.get(token=token)

    if my_file:
        path = os.path.join(settings.BASE_DIR, 'common/upload/images/').replace('\\', '/')
        curr_uuid_name = common.get_uuid()
        inputfilename, inputfile_name = common.upload_file(path, curr_uuid_name, my_file)  # 上传文件
    else:
        inputfile_name = None

    common_models.Feedbacks.objects.create(
        user_id=userobj.about.id,
        type=type,
        content=content,
        about_object=about_object,
        about_object_content=about_object_content,
        img_path=inputfile_name
    )
    return JsonResponse({"code": "200", "message": "成功", "data": []})

def get_uuid():
    uuid_str = uuid.uuid1()
    uuid_str = str(uuid_str).replace('-','')
    return uuid_str