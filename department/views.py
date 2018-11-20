from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import F, Q, Count
from django.db import transaction
from django.contrib.auth.models import Group
from app_common.common import diy_permission_required

from department import models as department_models
from app_common.tree import tree
# Create your views here.

@login_required
@diy_permission_required
def index(request):
    data = department_models.Department.objects.all().values()

    department_list = tree(data).to_tree(pid_id=None, level=0, html='┗━━━')
    return render(request,'department/index.html',{"department_list":department_list})

@login_required
@transaction.atomic
def add(request):
    if request.method == 'POST':
        data = request.POST.dict()
        if data.get('name','').strip() == '':
            return JsonResponse({"code":"-1","message":"部门名称不能为空"})

        try:
            department_models.Department.objects.get(name=data.get('name'))
        except department_models.Department.DoesNotExist:
            group = Group.objects.create(name=data.get('name'))
            department_models.Department.objects.create(name=data.get('name'),pid_id=data.get('pid'),group=group)
            return JsonResponse({"code": "200", "message": "添加部门成功"})
        else:
            return JsonResponse({"code": "-1", "message": "部门已经存在"})
    else:
        data = department_models.Department.objects.all().values()
        department_list = tree(data).to_tree(pid_id=None, level=0, html='')
        return render(request,'department/add.html',{"department_list":department_list})

@login_required
def edit(request): # 编辑
    department_id = request.GET.get('id')
    info = department_models.Department.objects.get(id=department_id)
    if request.method == 'POST':
        data = request.POST.dict()
        if data.get('name', '').strip() == '':
            return JsonResponse({"code": "-1", "message": "部门名称不能为空"})

        try:
            department_models.Department.objects.get(Q(name=data.get('name')) & ~Q(id=department_id))
        except department_models.Department.DoesNotExist:
            obj = department_models.Department.objects.get(id=department_id)
            obj.name = data.get('name')
            obj.pid_id = data.get('pid')
            obj.save()

            obj.group.name = data.get('name')
            obj.group.save()
            return JsonResponse({"code": "200", "message": "修改部门成功"})
        else:
            return JsonResponse({"code": "-1", "message": "部门名称已经存在"})
    else:
        data = department_models.Department.objects.filter(~Q(id=department_id)).values()
        department_list = tree(data).to_tree(pid_id=None, level=0, html='')
        return render(request,'department/add.html',{"info":info,"department_list":department_list})

@login_required
@transaction.atomic
def delete(request):
    department_id = request.GET.get('id')
    obj = department_models.Department.objects.get(id=department_id)
    obj.group.delete()
    obj.delete()
    return JsonResponse({"code": "200", "message": "删除成功", "data": []})