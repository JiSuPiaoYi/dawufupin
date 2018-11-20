from django.conf import settings
from django.shortcuts import render
from django.template.loader import render_to_string

from app_common import models as common_models
from user_center import models as user_models
from excel_view import models as excel_models

from app_common import config as app_config
from app_common.tree import tree

import os,uuid,json
try:
    from app_common import sms1
except:
    pass

def setting(request):
    navs = common_models.Nav.objects.filter(is_show=True).order_by('sort')
    permissions = request.user.get_all_permissions()
    nav_list = []
    CODENAMES = []
    for nav in navs:
        permission_name = 'app_common.'+nav.permission.codename
        if permission_name in permissions:
            CODENAMES.append(nav.permission.codename)

            nav_info = nav.__dict__
            nav_list.append(nav_info)

    NAVLIST = tree(nav_list).to_be_tree(None)
    #print(CODENAMES)
    try:
        USERINFO = user_models.UserExtra.objects.get(about_id=request.user.id)
    except:
        USERINFO = None

    return {
        "STATIC_URL":settings.STATIC_URL,
        "STATIC_ROOT":settings.STATIC_ROOT,
        "MEDIA_ROOT":settings.MEDIA_ROOT,
        "NAVLIST":NAVLIST,
        "USERINFO":USERINFO,
        "CODENAMES":CODENAMES
    }

'''
用自定义的权限认证装饰器，而不用django自带的，管理起来更方便
这里根据url来验证权限
'''
def diy_permission_required(func):
    def wrapper(*args, **kwargs):
        url = args[0].get_full_path()
        print(url)
        permissions = args[0].user.get_all_permissions()#获取用户所有权限

        #permissions = list(map(lambda x:x[x.find('.')+1:],permissions))
        permissions = list(permissions)
        #print(permissions)
        nav_objects = common_models.Nav.objects.all()
        urls = []
        for nav in nav_objects:
            # if nav.pid:
            #     permission_name = 'app_common.'+nav.pid.name+'_'+nav.name
            # else:
            #     permission_name = 'app_common.'+nav.name

            permission_name = 'app_common.'+nav.permission.name

            if permission_name in permissions:
                urls.append(nav.url)

        if url in urls:
            return func(*args, **kwargs)
        else:
            return render(args[0],'app_common/auth_error.html')
    return wrapper


def get_xlsx_num():
    path = "E:/job/data"
    files = scandir(path)
    print(files)
    num = 0
    for file in files:
        file_info = os.path.splitext(os.path.basename(file))
        if file_info[1] in ['.xls','.xlsx']:
            num += 1
    return num


def scandir(path):
    dir_list = os.listdir(path)
    files = []
    for file in dir_list:
        if os.path.isdir(path+os.sep+file) and file[0] != '.':
            files += scandir(path+os.sep+file)
        elif file[0] != '.':
            files.append(path+os.sep+file)
    return files

#读取文件
def read_file(path):
    with open(path,'r') as f:
        result = f.read()
        # f_charInfo = chardet.detect(result)
        # res = result.decode(encoding=f_charInfo['encoding'])
    return result

#获取目录下的所有文件xlsx,xls文件，不包含子孙级目录
def get_child_dir_by_path(path):
    file_paths = []
    if os.path.isdir(path):
        child_list_path = os.listdir(path)
        for child in child_list_path:
            file_path = os.path.join(path, child).replace('\\', '/')
            if os.path.isfile(file_path):
                file_path_info = os.path.splitext(file_path)
                if file_path_info[1] in ['.xlsx','.xls']:
                    file_paths.append(file_path)
    else:
        file_paths = []

    return file_paths

# 将office常用文件格式转换成为pdf格式比便于预览
def office2pdf(source_path, target_path):
    """

    :param source_path: 源文件路径
    :param target_path: 转换后文件的路径
    :return: 1表示成功，0表示失败
    调用方法如 office2pdf('common/repository/34/abc.docx', 'common/repository_preview/34)
    """
    import subprocess
    # source_path = os.path.join(settings.BASE_DIR, source_path)
    # target_path = os.path.join(settings.BASE_DIR, target_path)
    print("sudo libreoffice  --invisible --convert-to pdf " + source_path + "  --outdir " + target_path)
    # temp_path = source_path.split('.')[0] + '.pdf'
    # subprocess.check_call( ["who"],shell=True)
    try:
        subprocess.check_call(
            ["sudo libreoffice5.4  --invisible --convert-to pdf " + source_path + "  --outdir " + target_path], shell=True)


    # os.system("sudo libreoffice  --invisible --convert-to pdf " + source_path+"  --outdir "+target_path )
    except subprocess.CalledProcessError:
        return 0
    else:
        return 1
        # try:
        #     subprocess.check_call(["mv -f " + temp_path + " " + target_path], shell=True)
        # except subprocess.CalledProcessError:
        #     return 0
        # else:
        #     return 1

#上传文件
def upload_file(path,file_name,file_obj):
    if os.path.isdir(path) == False:
        os.mkdir(path)

    axt = os.path.splitext(file_obj.name)[0]

    ext = os.path.splitext(file_obj.name)[1]
    inputfile_name = file_name + ext#保存的文件名称
    upload_path = os.path.join(path , inputfile_name).replace('\\','/')
    destination = open(upload_path, 'wb+')
    for chunk in file_obj.chunks():
        destination.write(chunk)
    destination.close()
    inputfilename = axt + ext#上传的文件名称
    return inputfilename,inputfile_name


def get_uuid():
    return str(uuid.uuid1()).replace('-','')

#验证excel格式是否正确
def verify_excel(data,tem_type):
    if tem_type == '贫困村数据':
        tem_data = app_config.POVERTY_VILLAGE.keys()
    elif tem_type == '贫困户数据':
        tem_data = app_config.POVERTY_FAMILY.keys()
    elif tem_type == '贫困人口数据':
        tem_data = app_config.POVERTY_MAN.keys()
    else:
        tem_data = []

    if tem_data == []:
        return False,[]

    flag = False
    for value in data:
        if value == tem_data:
            flag = True

    return flag, tem_data

#验证部门扶贫政策excel格式是否正确
def verify_excel_zc(data):
    rows = excel_models.Template.objects.all().values_list('row',flat=True)
    rows = [json.loads(v) for v in rows]

    row_list = []
    for key,value in enumerate(rows):
        row_one = [v[0] for v in value]
        row_list.append(row_one)

    if len(data) < 2:
        return False,[]

    data_1 = [str(v).replace(os.linesep,'') for v in data[1]]
    #print(data)
    flag = False
    index = None
    for key,value in enumerate(row_list):
        v_1 = [str(v).replace(os.linesep,'') for v in value]
        # print(data_1)
        # print(v_1)
        if data_1 == v_1:
            flag = True
            index = key

    # tem_data = ['贫困对象名称（行政村名字或个人名字）', '贫困对象编号（村编号或个人身份证号码）', '归属乡镇', '归属行政村', '归属组', '补助标准', '补助数量（即补助标准的乘数）', '本期补助上限（元）', '应补助金额（元）', '实际补助金额（元）', '收款银行', '收款账号', '收款人名字', '收款人身份证号码（或者收款行政村编号）', '备注']

    try:
        tem_data = rows[index]
    except:
        tem_data = []

    return flag, tem_data


'''
:param user_id 操作人id
:param model_path 操作的表模型路径
:param type 类型（login，add，update，delete）
:param 旧数据对象，若type为add，则为None；
:param 更新后的数据对象，若type为delete，则为None
'''
def log(user_id=None,model_path=None,type=None,old_obj=None,update_obj=None):
    # type_dict = {
    #     "user_center.UserExtra":"用户账号",
    #     ""
    # }

    if type in ['login']:
        common_models.Logs.objects.create(user_id=user_id,message='登录了系统')
    else:
        model_obj = model_path.split('.')[-1]
        path = model_path.replace('.'+model_obj,'')
        # --import-- ()模块导入
        obj = __import__(path, fromlist=True)  # 注意fromlist参数
        if hasattr(obj, model_obj):
            model = getattr(obj, model_obj)
            fields = model._meta.fields
            field_list = []
            #field_names = []
            for value in fields:
                field_list.append({
                    "verbose_name":value.verbose_name,
                    "field_type":value,
                    "field_name":value.name
                })
                #field_names.append(value.name)
            # print(field_list)
            # print(model._meta.verbose_name)

            model_verbose_name = model._meta.verbose_name
            if type == 'add':
                message = '创建了'+model_verbose_name
            elif type == 'update':
                message = '修改了' + model_verbose_name
            elif type == 'delete':
                message = '删除了' + model_verbose_name
            else:
                message = None

            old_info = None
            update_info = None
            if old_obj:
                old_obj = old_obj.__dict__
                old_info = []
                for value in field_list:
                    if value['field_name'] in old_obj.keys():
                        value.update({"value":old_obj[value['field_name']]})
                        old_info.append(value)

            if update_obj:
                update_obj = update_obj.__dict__
                update_info = []
                for value in field_list:
                    if value['field_name'] in update_obj.keys():
                        value.update({"value": update_obj[value['field_name']]})
                        update_info.append(value)

            detail = None   # 日志
            if old_info or update_info:
                detail = render_to_string('app_common/log_tem/default.html', {
                    "type":type,
                    "model_verbose_name":model_verbose_name,
                    "old_info":old_info,
                    "update_info":update_info
                })

            #print(detail)

            common_models.Logs.objects.create(
                user_id=user_id,
                message=message,
                detail=detail
            )
        else:
            raise Exception("判断权限参数错误！")

#发送短信
def send_sms(mobile,SignName,TemplateCode,ParamString):
    content = sms1.send_sms(mobile,SignName,TemplateCode,ParamString)
    content = str(content,"utf-8")
    print('--------',content)
    try:
        content = json.loads(content)
    except:
        content = {}

    if content == {}:
        res = {"code": "-1", "message": "发送失败", "data": []}
    else:
        if content.get('d') == 'OK':
            #common_models.NoteSms.objects.create(mobile=mobile, verification_code=code)  # 插入数据库
            res = {"code": "200", "message": "发送成功", "data": []}
        else:
            res = {"code": "-1", "message": "发送失败:" + content.get('Message'), "data": []}
    print(res)
    return res

    # path = os.path.join(settings.BASE_DIR, 'app_common/sms.py')
    # print('11111111111111111111111111111','python {0} {1} {2} {3} {4}'.format(path, mobile, SignName, TemplateCode, ParamString))
    # res = os.popen(
    #     'python {0} {1} {2} {3} {4}'.format(path, mobile, SignName, TemplateCode, ParamString))
    #
    # try:
    #     result = json.loads(res.readline())
    # except:
    #     result = {}
    #
    # print('python {0} {1} {2} {3} {4}'.format(path, mobile, SignName, TemplateCode, ParamString))
    # print(result)
    # return result
    # pass