from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F, Q, Count
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.db import connection

from user_center import models as user_models
from department import models as department_models
from app_common.tree import tree
from user_center.forms_verify import VerifyUser
from app_common.common import diy_permission_required
from app_common.common import log as common_log

import json,copy,math

# Create your views here.
def login_in(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        if all([account,password]):
            user = auth.authenticate(username=account, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    common_log(user_id=user.id,type='login')#记录日志
                    res = {'code': '200', 'message': "登录成功", 'data': []}
                else:
                    res = {'code': '-1', 'message': "用户未激活", 'data': []}
            else:
                try:
                    userextra = user_models.UserExtra.objects.get(mobile=account)
                except user_models.UserExtra.DoesNotExist:
                    res = {'code': '-1', 'message': "用户不存在或密码错误", 'data': []}
                else:
                    userobj = auth.authenticate(username=userextra.about.username, password=password)
                    if userobj is not None:
                        if userobj.is_active:
                            auth.login(request, userobj)
                            res = {'code': '200', 'message': "登录成功", 'data': []}
                        else:
                            res = {'code': '-1', 'message': "用户未激活", 'data': []}
                    else:
                        res = {'code': '-1', 'message': "用户不存在或密码错误", 'data': []}
            return JsonResponse(res, safe=False)
        else:
            return JsonResponse({"code":"-1","message":"账号或密码不能为空"},safe=False)
    else:
        return render(request,'user_center/login.html')

def login_out(request):
    logout(request)
    return redirect(reverse('login_in'))

def user_list(request):
    page = request.GET.get('page',1)
    keyword = request.GET.get('keyword','')
    if keyword:
        search_condition = "mobile like '%%"+keyword+"%%' or name like '%%"+keyword+"%%'"
    else:
        search_condition = '1=1'
    count_sql = "SELECT count(user_id) FROM user_center_userextra WHERE "+search_condition+";"
    print(count_sql)
    count_res = list(user_models.UserExtra.objects.raw(count_sql).query)
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

    sql = "select * from user_center_userextra WHERE "+search_condition+" LIMIT "+limit_start+","+str(every_page_number)+";"
    users = list(user_models.UserExtra.objects.raw(sql))
    return render(request,'user_center/user_list.html',{
        "page": page,
        "count": count,
        "num_pages":num_pages,
        "every_page_number":every_page_number,
        "users": users
    })

@login_required
def add_user(request):
    if request.method == 'POST':
        data = request.POST.dict()
        verifier = VerifyUser(data, auto_id=False)
        if verifier.is_valid():
            try:
                user_models.UserExtra.objects.get(Q(mobile=verifier.cleaned_data['mobile']))
            except user_models.UserExtra.DoesNotExist:
                user = get_user_model().objects.create_user(verifier.cleaned_data['mobile'], '123456@vip.com',data.get('password'))

                user_extra = user_models.UserExtra.objects.create(name=verifier.cleaned_data['name'],
                                                     mobile=verifier.cleaned_data['mobile'],
                                                     department_id=verifier.cleaned_data['department_id'],
                                                     about=user)

                update_obj = copy.deepcopy(user_extra)
                common_log(user_id=request.user.id, model_path='user_center.models.UserExtra', type='add',update_obj=update_obj)  # 记录日志

                # group_obj = Group.objects.get(name=user_extra.department.name)
                # cursor = connection.cursor()
                # cursor.execute("insert into auth_user_groups(user_id,group_id) values(%s,%s);", [user.id,group_obj.id])
                # row = cursor.fetchone()

                user.groups = [user_extra.department.group]
                return JsonResponse({"code": "200", "message": "添加成功", "data": []})
            else:
                return JsonResponse({"code": "-1", "message": "手机号被占用", "data": []})

        else:
            one_error = list(json.loads(verifier.errors.as_json()).items())[0][1][0]['message']
            return JsonResponse({"code": "-1", "message": one_error, "data": []})
    else:
        data = department_models.Department.objects.all().values()
        department_list = tree(data).to_tree(pid_id=None, level=0, html='')
        return render(request,'user_center/add.html',{"department_list":department_list})

@login_required
@transaction.atomic
def edit_user(request):
    curr_mobile = request.GET.get('mobile')#当前手机号
    about_id = request.GET.get('about_id')
    if request.method == 'POST':
        data = request.POST.dict()
        verifier = VerifyUser(data, auto_id=False)
        if verifier.is_valid():
            try:
                user_models.UserExtra.objects.get(Q(mobile=verifier.cleaned_data['mobile']) , ~Q(about_id=about_id))
            except user_models.UserExtra.DoesNotExist:
                obj = user_models.UserExtra.objects.get(mobile=curr_mobile)
                print(obj.about_id)
                old_obj = copy.deepcopy(obj)

                obj.name = verifier.cleaned_data['name']
                obj.mobile = verifier.cleaned_data['mobile']
                obj.department_id = verifier.cleaned_data['department_id']
                obj.save()

                update_obj = copy.deepcopy(obj)

                user_obj = obj.about
                user_obj.username = verifier.cleaned_data['mobile']
                if data.get('password').strip() != '':
                    user_obj.password = make_password(data.get('password').strip())
                user_obj.save()

                # group_obj = Group.objects.get(name=obj.department.name)
                # cursor = connection.cursor()
                # cursor.execute("UPDATE auth_user_groups SET group_id = %s WHERE user_id = %s", [group_obj.id,user_id])
                # row = cursor.fetchone()

                user_obj.groups = [obj.department.group]

                common_log(user_id=request.user.id, model_path='user_center.models.UserExtra', type='update',old_obj=old_obj,update_obj=update_obj)  # 记录日志

                return JsonResponse({"code": "200", "message": "修改成功", "data": []})
            else:
                return JsonResponse({"code": "-1", "message": "手机号被占用", "data": []})

        else:
            one_error = list(json.loads(verifier.errors.as_json()).items())[0][1][0]['message']
            return JsonResponse({"code": "-1", "message": one_error, "data": []})
    else:
        info = user_models.UserExtra.objects.get(mobile=curr_mobile)
        data = department_models.Department.objects.all().values()
        department_list = tree(data).to_tree(pid_id=None, level=0, html='')
        return render(request,'user_center/add.html',{"department_list":department_list,"info":info})

@login_required
def delete_user(request):
    mobile = request.GET.get('mobile')
    obj = user_models.UserExtra.objects.get(mobile=mobile)

    old_obj = copy.deepcopy(obj)

    obj.about.delete()
    #obj.delete()

    common_log(user_id=request.user.id, model_path='user_center.models.UserExtra', type='delete',old_obj=old_obj)  # 记录日志
    return JsonResponse({"code": "200", "message": "删除成功", "data": []})