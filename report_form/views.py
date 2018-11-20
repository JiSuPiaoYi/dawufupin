from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json,datetime
# import xlrd


# Create your views here.


# def industryledgerform(request):
#     flexibleledgerform_list = FlexibleLedgerForm.objects.all()
#     for f in flexibleledgerform_list:
#         f.subdivided_capacitor=eval(f.subdivided_capacitor)
#
#     industryledgerform_list=IndustryLedgerForm.objects.all()
#     paginator=Paginator(industryledgerform_list,20)    #生成Paginator对象,定义每页显示20条记录
#     page=request.GET.get('page')    #从前端获取当前的页码数
#     try:
#         industryledgerform_list=paginator.page(page)    #获取当前页码的记录
#     except PageNotAnInteger:
#         industryledgerform_list=paginator.page(1)    #如果用户输入的页码不是整数,获取第1页的记录
#     except EmptyPage:
#         industryledgerform_list=paginator.page(paginator.num_pages)    #如果用户输入的页数不在页码列表范围中,获取最后一页的记录
#
#     return render(request,'report_form/ledgerform/industryledgerform.html',{'flexibleledgerform_list':flexibleledgerform_list,'industryledgerform_list':industryledgerform_list})

def poorvillage(request):
    town_list=AdministrativeVillageDataForm.objects.filter(town_tag="1")
    town_name=[]
    for t in town_list:
        town_name.append(t.town_name) #获取所有乡镇名称
    return render(request,'report_form/poorvillagedataform/poorvillage.html',{'town_name':town_name})

def poorvillagedataform(request):

    # edit_poorvillagedata_list=AdministrativeVillageDataForm.objects.all()
    # for e in edit_poorvillagedata_list:
    #     data=AdministrativeVillageDataForm.objects.filter(town_name=e.town_name,now_administrative_village=e.now_administrative_village,village_tag="1")
    #     if data.count()==0:
    #         e.village_tag="1"
    #         e.save()
    #
    #     moom=AdministrativeVillageDataForm.objects.filter(town_name=e.town_name,town_tag="1")
    #     if moom.count()==0:
    #         e.town_tag="1"
    #         e.save()

    now_village_identifier=request.GET.get('now_village_identifier')

    if now_village_identifier:
        poorvillagedata_list=AdministrativeVillageDataForm.objects.filter(now_village_identifier=now_village_identifier,village_tag='1')

    else:
        poorvillagedata_list=AdministrativeVillageDataForm.objects.filter(village_tag="1")

    data_number=len(poorvillagedata_list) #合并后村个数

    one_page_of_data=20

    curpage=1

    allpostcounts=poorvillagedata_list.count()
    allpage=allpostcounts//one_page_of_data
    remainpost=allpostcounts%one_page_of_data
    if remainpost>0:
        allpage=allpage+1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    poorvillagedata_list=poorvillagedata_list.all()[startpos:endpos] #分页

    for p in poorvillagedata_list:

        single_list=[]
        double_list=[]

        additional_data=AdministrativeVillageAdditionalForm.objects.filter(now_village_identifier=p.now_village_identifier)

        for a in additional_data:

            policy_data=PolicyStaticForm.objects.get(policy_number=a.policy_number)

            name_str=''
            if policy_data.policy_first_layer:
                name_str=policy_data.policy_first_layer
            if policy_data.policy_second_layer:
                name_str=name_str+"."+policy_data.policy_second_layer
            if policy_data.policy_third_layer:
                name_str=name_str+"."+policy_data.policy_third_layer
            single_list.append(name_str) #0

            subsidy_str=''
            if policy_data.subsidy_one:
                subsidy_str=policy_data.subsidy_one
            if policy_data.subsidy_two:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_two
            if policy_data.subsidy_three:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_three
            if a.subsidy_standard:
                subsidy_str=a.subsidy_standard
            single_list.append(subsidy_str) #1

            single_list.append(a.policy_multiplier) #2
            single_list.append(a.plan_money) #3
            single_list.append(a.fact_money) #4

            date=a.date_year+'-'+a.date_month
            single_list.append(date) #5

            color_str='b'
            if a.fact_money and a.plan_money:
                if float(a.fact_money)<float(a.plan_money):
                    color_str="o"
                else:
                    color_str="b"
            single_list.append(color_str) #6

            single_list.append(a.bank_name) #7
            single_list.append(a.bank_number) #8
            single_list.append(a.card_people) #9
            single_list.append(a.people_id) #10

            double_list.append(single_list)
            single_list=[]

        p.additionaldata=double_list #加上数据（贫困村享受政策数据）

    town_list=AdministrativeVillageDataForm.objects.filter(town_tag="1")
    town_name=[]
    for t in town_list:
        town_name.append(t.town_name) #获取所有乡镇名称

    return render(request,'report_form/poorvillagedataform/poorvillagedataform.html',{'poorvillagedata_list':poorvillagedata_list,'data_number':data_number,'town_name':town_name,'curpage':curpage,'allpage':allpage})


@csrf_exempt
def village_template_initial_paginator(request):
    poorvillagedata_list=AdministrativeVillageDataForm.objects.filter(village_tag="1")

    data_number=len(poorvillagedata_list) #合并后村个数

    one_page_of_data=20

    curpage=int(request.POST.get('curpage'))
    allpage=int(request.POST.get('allpage'))
    pagetype=str(request.POST.get('pagetype'))

    if pagetype=='pagenext':
        curpage=curpage+1
    elif pagetype=='pagelast':
        curpage=curpage-1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    middlepos=request.POST.get('gopage')
    if middlepos is not None:
        if int(middlepos)<=allpage:
            startpos=(int(middlepos)-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=int(middlepos)
        else:
            startpos=(allpage-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=allpage

    poorvillagedata_list=poorvillagedata_list.all()[startpos:endpos] #分页

    for p in poorvillagedata_list:

        single_list=[]
        double_list=[]

        additional_data=AdministrativeVillageAdditionalForm.objects.filter(now_village_identifier=p.now_village_identifier)

        for a in additional_data:

            policy_data=PolicyStaticForm.objects.get(policy_number=a.policy_number)

            name_str=''
            if policy_data.policy_first_layer:
                name_str=policy_data.policy_first_layer
            if policy_data.policy_second_layer:
                name_str=name_str+"."+policy_data.policy_second_layer
            if policy_data.policy_third_layer:
                name_str=name_str+"."+policy_data.policy_third_layer
            single_list.append(name_str) #0

            subsidy_str=''
            if policy_data.subsidy_one:
                subsidy_str=policy_data.subsidy_one
            if policy_data.subsidy_two:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_two
            if policy_data.subsidy_three:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_three
            if a.subsidy_standard:
                subsidy_str=a.subsidy_standard
            single_list.append(subsidy_str) #1

            single_list.append(a.policy_multiplier) #2
            single_list.append(a.plan_money) #3
            single_list.append(a.fact_money) #4

            date=a.date_year+'-'+a.date_month
            single_list.append(date) #5

            color_str='b'
            if a.fact_money and a.plan_money:
                if float(a.fact_money)<float(a.plan_money):
                    color_str="o"
                else:
                    color_str="b"
            single_list.append(color_str) #6

            single_list.append(a.bank_name) #7
            single_list.append(a.bank_number) #8
            single_list.append(a.card_people) #9
            single_list.append(a.people_id) #10

            double_list.append(single_list)
            single_list=[]

        p.additionaldata=double_list #加上数据（贫困村享受政策数据）

    template='report_form/poorvillagedataform/template_initial_paginator.html'

    return render(request,template,{'poorvillagedata_list':poorvillagedata_list,'data_number':data_number,'curpage':curpage,'allpage':allpage})


@csrf_exempt
def village_town_change(request):
    town=request.POST.get("town")
    village_list=AdministrativeVillageDataForm.objects.filter(town_name=town,village_tag="1")
    village_name=[]
    for v in village_list:
        village_name.append(v.now_administrative_village)
    res={'village_name':village_name}
    return HttpResponse(json.dumps(res),content_type='application/json')


@csrf_exempt
def village_template_query_paginator(request):

    town=request.POST.get("town")
    definition=request.POST.get("definition")
    responser=request.POST.get("responser")
    telephone=request.POST.get("telephone") #获取条件数据

    poorvillagedata=AdministrativeVillageDataForm.objects.filter(village_tag="1")

    if not town=="请选择":
        poorvillagedata=poorvillagedata.filter(town_name=town)
    if not definition=="请选择":
        poorvillagedata=poorvillagedata.filter(now_administrative_village=definition)
    if responser:
        poorvillagedata=poorvillagedata.filter(now_responsible_person=responser)
    if telephone:
        poorvillagedata=poorvillagedata.filter(now_telephone_number=telephone) #根据条件进行数据筛选

    data_number=len(poorvillagedata) #计算根据条件进行数据筛选后的数据个数

    one_page_of_data=20

    curpage=int(request.POST.get('curpage','1'))
    allpage=int(request.POST.get('allpage','1'))
    pagetype=str(request.POST.get('pagetype',''))

    if pagetype=='pagenext':
        curpage=curpage+1
    elif pagetype=='pagelast':
        curpage=curpage-1

    if curpage==1 and allpage==1:
        allpostcounts=poorvillagedata.count()
        allpage=allpostcounts//one_page_of_data
        remainpost=allpostcounts%one_page_of_data
        if remainpost>0:
            allpage=allpage+1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    middlepos=request.POST.get('gopage')
    if middlepos is not None:
        if int(middlepos)<=allpage:
            startpos=(int(middlepos)-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=int(middlepos)
        else:
            startpos=(allpage-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=allpage

    poorvillagedata=poorvillagedata.all()[startpos:endpos] #分页

    for p in poorvillagedata:

        single_list=[]
        double_list=[]

        additional_data=AdministrativeVillageAdditionalForm.objects.filter(now_village_identifier=p.now_village_identifier)

        for a in additional_data:

            policy_data=PolicyStaticForm.objects.get(policy_number=a.policy_number)

            name_str=''
            if policy_data.policy_first_layer:
                name_str=policy_data.policy_first_layer
            if policy_data.policy_second_layer:
                name_str=name_str+"."+policy_data.policy_second_layer
            if policy_data.policy_third_layer:
                name_str=name_str+"."+policy_data.policy_third_layer
            single_list.append(name_str) #0

            subsidy_str=''
            if policy_data.subsidy_one:
                subsidy_str=policy_data.subsidy_one
            if policy_data.subsidy_two:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_two
            if policy_data.subsidy_three:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_three
            if a.subsidy_standard:
                subsidy_str=a.subsidy_standard
            single_list.append(subsidy_str) #1

            single_list.append(a.policy_multiplier) #2
            single_list.append(a.plan_money) #3
            single_list.append(a.fact_money) #4

            date=a.date_year+'-'+a.date_month
            single_list.append(date) #5

            color_str='b'
            if a.fact_money and a.plan_money:
                if float(a.fact_money)<float(a.plan_money):
                    color_str="o"
                else:
                    color_str="b"
            single_list.append(color_str) #6

            single_list.append(a.bank_name) #7
            single_list.append(a.bank_number) #8
            single_list.append(a.card_people) #9
            single_list.append(a.people_id) #10

            double_list.append(single_list)
            single_list=[]

        p.additionaldata=double_list #加上数据（贫困村享受政策数据）

    template='report_form/poorvillagedataform/template_query_paginator.html'

    return render(request,template,{'poorvillagedata_list':poorvillagedata,'data_number':data_number,'curpage':curpage,'allpage':allpage})


def poorhouse(request):
    town_list=AdministrativeVillageDataForm.objects.filter(town_tag="1")
    town_name=[]
    for t in town_list:
        town_name.append(t.town_name) #获取所有乡镇名称
    return render(request,'report_form/poorhousedataform/poorhouse.html',{'town_name':town_name})


def poorhousedataform(request):
    house_identifier=request.GET.get('house_identifier')
    household_identifier=request.GET.get('household_identifier')

    if house_identifier:
        poorhousedata_list=PoorHouseDataForm.objects.filter(house_identifier=house_identifier)

    elif household_identifier:
        poorhousedata_list=PoorHouseDataForm.objects.filter(householder_id=household_identifier)

    else:
        poorhousedata_list=PoorHouseDataForm.objects.all()

    data_number=len(poorhousedata_list) #贫困户基本信息表所有数据的个数

    one_page_of_data=20

    curpage=1

    allpostcounts=poorhousedata_list.count()
    allpage=allpostcounts//one_page_of_data
    remainpost=allpostcounts%one_page_of_data
    if remainpost>0:
        allpage=allpage+1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    poorhousedata_list=poorhousedata_list.all()[startpos:endpos] #分页

    for p in poorhousedata_list:

        village_data=AdministrativeVillageDataForm.objects.filter(now_village_identifier=p.now_village_identifier)
        for v in village_data:
            p.now_village_name=v.now_administrative_village #加上数据（合并后村名称）
            p.town_name=v.town_name

        single_list=[]
        double_list=[]

        house_additional_data=PoorHouseAdditionalForm.objects.filter(householder_id=p.householder_id)

        for h in house_additional_data:

            policy_data=PolicyStaticForm.objects.filter(policy_number=h.policy_number)

            for po in policy_data:

                name_str=''
                if po.policy_first_layer:
                    name_str=po.policy_first_layer
                if po.policy_second_layer:
                    name_str=name_str+"."+po.policy_second_layer
                if po.policy_third_layer:
                    name_str=name_str+"."+po.policy_third_layer
                single_list.append(name_str) #0

                subsidy_str=''
                if po.subsidy_one:
                    subsidy_str=po.subsidy_one
                if po.subsidy_two:
                    subsidy_str=subsidy_str+"+"+po.subsidy_two
                if po.subsidy_three:
                    subsidy_str=subsidy_str+"+"+po.subsidy_two
                if h.subsidy_standard:
                    subsidy_str=h.subsidy_standard
                single_list.append(subsidy_str) #1

                single_list.append(h.policy_multiplier) #2
                single_list.append(h.plan_money) #3
                single_list.append(h.fact_money) #4

                date=h.date_year+'-'+h.date_month
                single_list.append(date) #5

                color_str='b'
                if h.fact_money and h.plan_money:
                    if float(h.fact_money)<float(h.plan_money):
                        color_str="o"
                    else:
                        color_str="b"
                single_list.append(color_str) #6

                single_list.append(h.bank_name) #7
                single_list.append(h.bank_number) #8
                single_list.append(h.card_people) #9
                single_list.append(h.people_id) #10
                single_list.append('户') #11
                single_list.append(h.householder_id) #12
                single_list.append(h.policy_number) #13

                double_list.append(single_list)
                single_list=[]

        family_data=PoorPeopleDataForm.objects.filter(house_identifier=p.house_identifier)

        for f in family_data:
            family_additional_data=PoorPeopleAdditionalForm.objects.filter(people_id=f.people_id)

            for fa in family_additional_data:

                policy_data=PolicyStaticForm.objects.get(policy_number=fa.policy_number)

                name_str=''
                if policy_data.policy_first_layer:
                    name_str=policy_data.policy_first_layer
                if policy_data.policy_second_layer:
                    name_str=name_str+"."+policy_data.policy_second_layer
                if policy_data.policy_third_layer:
                    name_str=name_str+"."+policy_data.policy_third_layer
                single_list.append(name_str) #0

                subsidy_str=''
                if policy_data.subsidy_one:
                    subsidy_str=policy_data.subsidy_one
                if policy_data.subsidy_two:
                    subsidy_str=subsidy_str+"+"+policy_data.subsidy_two
                if policy_data.subsidy_three:
                    subsidy_str=subsidy_str+"+"+policy_data.subsidy_three
                if fa.subsidy_standard:
                    subsidy_str=fa.subsidy_standard
                single_list.append(subsidy_str) #1

                single_list.append(fa.policy_multiplier) #2
                single_list.append(fa.plan_money) #3
                single_list.append(fa.fact_money) #4

                date=fa.date_year+'-'+fa.date_month
                single_list.append(date) #5

                color_str='b'
                if fa.fact_money and fa.plan_money:
                    if float(fa.fact_money)<float(fa.plan_money):
                        color_str="o"
                    else:
                        color_str="b"
                single_list.append(color_str)  #6

                single_list.append(fa.bank_name) #7
                single_list.append(fa.bank_number) #8
                single_list.append(fa.card_people) #9
                single_list.append(fa.card_id) #10
                single_list.append(f.people_name) #11
                single_list.append(f.people_id) #12
                single_list.append(fa.policy_number) #13

                double_list.append(single_list)
                single_list=[]

        p.additionaldata=double_list #加上数据（贫困户享受政策数据）

    town_list=AdministrativeVillageDataForm.objects.filter(town_tag="1")
    town_name=[]
    for t in town_list:
        town_name.append(t.town_name) #获取所有乡镇名称

    return render(request,'report_form/poorhousedataform/poorhousedataform.html',{'poorhousedata_list':poorhousedata_list,'data_number':data_number,'town_name':town_name,'curpage':curpage,'allpage':allpage})


@csrf_exempt
def house_template_initial_paginator(request):
    poorhousedata_list=PoorHouseDataForm.objects.all()

    data_number=len(poorhousedata_list)  #贫困户基本信息表所有数据的个数

    one_page_of_data=20

    curpage=int(request.POST.get('curpage'))
    allpage=int(request.POST.get('allpage'))
    pagetype=str(request.POST.get('pagetype'))

    if pagetype=='pagenext':
        curpage=curpage+1
    elif pagetype=='pagelast':
        curpage=curpage-1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    middlepos=request.POST.get('gopage')
    if middlepos is not None:
        if int(middlepos)<=allpage:
            startpos=(int(middlepos)-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=int(middlepos)
        else:
            startpos=(allpage-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=allpage

    poorhousedata_list=poorhousedata_list.all()[startpos:endpos] #分页

    for p in poorhousedata_list:

        village_data=AdministrativeVillageDataForm.objects.filter(now_village_identifier=p.now_village_identifier)
        for v in village_data:
            p.now_village_name=v.now_administrative_village #加上数据（合并后村名称）
            p.town_name=v.town_name

        single_list=[]
        double_list=[]

        house_additional_data=PoorHouseAdditionalForm.objects.filter(householder_id=p.householder_id)

        for h in house_additional_data:

            policy_data=PolicyStaticForm.objects.filter(policy_number=h.policy_number)

            for po in policy_data:

                name_str=''
                if po.policy_first_layer:
                    name_str=po.policy_first_layer
                if po.policy_second_layer:
                    name_str=name_str+"."+po.policy_second_layer
                if po.policy_third_layer:
                    name_str=name_str+"."+po.policy_third_layer
                single_list.append(name_str) #0

                subsidy_str=''
                if po.subsidy_one:
                    subsidy_str=po.subsidy_one
                if po.subsidy_two:
                    subsidy_str=subsidy_str+"+"+po.subsidy_two
                if po.subsidy_three:
                    subsidy_str=subsidy_str+"+"+po.subsidy_two
                if h.subsidy_standard:
                    subsidy_str=h.subsidy_standard
                single_list.append(subsidy_str) #1

                single_list.append(h.policy_multiplier) #2
                single_list.append(h.plan_money) #3
                single_list.append(h.fact_money) #4

                date=h.date_year+'-'+h.date_month
                single_list.append(date) #5

                color_str='b'
                if h.fact_money and h.plan_money:
                    if float(h.fact_money)<float(h.plan_money):
                        color_str="o"
                    else:
                        color_str="b"
                single_list.append(color_str) #6

                single_list.append(h.bank_name) #7
                single_list.append(h.bank_number) #8
                single_list.append(h.card_people) #9
                single_list.append(h.people_id) #10
                single_list.append('户') #11
                single_list.append(h.householder_id) #12
                single_list.append(h.policy_number) #13

                double_list.append(single_list)
                single_list=[]

        family_data=PoorPeopleDataForm.objects.filter(house_identifier=p.house_identifier)

        for f in family_data:
            family_additional_data=PoorPeopleAdditionalForm.objects.filter(people_id=f.people_id)

            for fa in family_additional_data:

                policy_data=PolicyStaticForm.objects.get(policy_number=fa.policy_number)

                name_str=''
                if policy_data.policy_first_layer:
                    name_str=policy_data.policy_first_layer
                if policy_data.policy_second_layer:
                    name_str=name_str+"."+policy_data.policy_second_layer
                if policy_data.policy_third_layer:
                    name_str=name_str+"."+policy_data.policy_third_layer
                single_list.append(name_str) #0

                subsidy_str=''
                if policy_data.subsidy_one:
                    subsidy_str=policy_data.subsidy_one
                if policy_data.subsidy_two:
                    subsidy_str=subsidy_str+"+"+policy_data.subsidy_two
                if policy_data.subsidy_three:
                    subsidy_str=subsidy_str+"+"+policy_data.subsidy_three
                if fa.subsidy_standard:
                    subsidy_str=fa.subsidy_standard
                single_list.append(subsidy_str) #1

                single_list.append(fa.policy_multiplier) #2
                single_list.append(fa.plan_money) #3
                single_list.append(fa.fact_money) #4

                date=fa.date_year+'-'+fa.date_month
                single_list.append(date) #5

                color_str='b'
                if fa.fact_money and fa.plan_money:
                    if float(fa.fact_money)<float(fa.plan_money):
                        color_str="o"
                    else:
                        color_str="b"
                single_list.append(color_str)  #6

                single_list.append(fa.bank_name) #7
                single_list.append(fa.bank_number) #8
                single_list.append(fa.card_people) #9
                single_list.append(fa.card_id) #10
                single_list.append(f.people_name) #11
                single_list.append(f.people_id) #12
                single_list.append(fa.policy_number) #13

                double_list.append(single_list)
                single_list=[]

        p.additionaldata=double_list #加上数据（贫困户享受政策数据）

    template='report_form/poorhousedataform/template_initial_paginator.html'

    return render(request,template,{'poorhousedata_list':poorhousedata_list,'data_number':data_number,'curpage':curpage,'allpage':allpage})


@csrf_exempt
def house_town_change(request):
    town=request.POST.get("town")
    village_list=AdministrativeVillageDataForm.objects.filter(town_name=town,village_tag="1")
    village_name=[]
    for v in village_list:
        village_name.append(v.now_administrative_village)
    res={'village_name':village_name}
    return HttpResponse(json.dumps(res),content_type='application/json')


@csrf_exempt
def house_template_query_paginator(request):

    town=request.POST.get("town")
    definition=request.POST.get("definition")
    householder=request.POST.get("householder")
    identity=request.POST.get("identity")
    helper=request.POST.get("helper")
    poor=request.POST.get("poor")
    number=request.POST.get("number")
    reason=request.POST.get("reason") #获取条件数据

    poorhousedata=PoorHouseDataForm.objects.all()

    if not town=="请选择":
        village_list=AdministrativeVillageDataForm.objects.filter(town_name=town,village_tag="1")
        now_village_identifier_list=[]
        for v in village_list:
            now_village_identifier_list.append(v.now_village_identifier)
        poorhousedata=poorhousedata.filter(now_village_identifier__in=now_village_identifier_list)
    if not definition=="请选择":
        village_list=AdministrativeVillageDataForm.objects.get(town_name=town,now_administrative_village=definition,village_tag="1")
        now_village_identifier=village_list.now_village_identifier
        poorhousedata=poorhousedata.filter(now_village_identifier=now_village_identifier)
    if householder:
        poorhousedata=poorhousedata.filter(householder_name=householder)
    if identity:
        poorhousedata=poorhousedata.filter(householder_id=identity)
    if helper:
        poorhousedata=poorhousedata.filter(help_people=helper)
    if not poor=="请选择":
        poorhousedata=poorhousedata.filter(poor_attribute=poor)
    if number:
        house_number=''
        people_data=PoorPeopleDataForm.objects.filter(people_id=number)
        for pe in people_data:
            house_number=pe.house_identifier
        poorhousedata=poorhousedata.filter(house_identifier=house_number)
    if not reason=="请选择":
        poorhousedata=poorhousedata.filter(poor_reason=reason) #根据条件进行数据筛选

    data_number=len(poorhousedata) #计算根据条件进行数据筛选后的数据个数

    one_page_of_data=20

    curpage=int(request.POST.get('curpage','1'))
    allpage=int(request.POST.get('allpage','1'))
    pagetype=str(request.POST.get('pagetype',''))

    if pagetype=='pagenext':
        curpage=curpage+1
    elif pagetype=='pagelast':
        curpage=curpage-1

    if curpage==1 and allpage==1:
        allpostcounts=poorhousedata.count()
        allpage=allpostcounts//one_page_of_data
        remainpost=allpostcounts%one_page_of_data
        if remainpost>0:
            allpage=allpage+1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    middlepos=request.POST.get('gopage')
    if middlepos is not None:
        if int(middlepos)<=allpage:
            startpos=(int(middlepos)-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=int(middlepos)
        else:
            startpos=(allpage-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=allpage

    poorhousedata=poorhousedata.all()[startpos:endpos] #分页

    for p in poorhousedata:

        village_data=AdministrativeVillageDataForm.objects.filter(now_village_identifier=p.now_village_identifier)
        for v in village_data:
            p.now_village_name=v.now_administrative_village #加上数据（合并后村名称）
            p.town_name=v.town_name

        single_list=[]
        double_list=[]

        house_additional_data=PoorHouseAdditionalForm.objects.filter(householder_id=p.householder_id)

        for h in house_additional_data:

            policy_data=PolicyStaticForm.objects.filter(policy_number=h.policy_number)

            for po in policy_data:

                name_str=''
                if po.policy_first_layer:
                    name_str=po.policy_first_layer
                if po.policy_second_layer:
                    name_str=name_str+"."+po.policy_second_layer
                if po.policy_third_layer:
                    name_str=name_str+"."+po.policy_third_layer
                single_list.append(name_str) #0

                subsidy_str=''
                if po.subsidy_one:
                    subsidy_str=po.subsidy_one
                if po.subsidy_two:
                    subsidy_str=subsidy_str+"+"+po.subsidy_two
                if po.subsidy_three:
                    subsidy_str=subsidy_str+"+"+po.subsidy_two
                if h.subsidy_standard:
                    subsidy_str=h.subsidy_standard
                single_list.append(subsidy_str) #1

                single_list.append(h.policy_multiplier) #2
                single_list.append(h.plan_money) #3
                single_list.append(h.fact_money) #4

                date=h.date_year+'-'+h.date_month
                single_list.append(date) #5

                color_str='b'
                if h.fact_money and h.plan_money:
                    if float(h.fact_money)<float(h.plan_money):
                        color_str="o"
                    else:
                        color_str="b"
                single_list.append(color_str) #6

                single_list.append(h.bank_name) #7
                single_list.append(h.bank_number) #8
                single_list.append(h.card_people) #9
                single_list.append(h.people_id) #10
                single_list.append('户') #11
                single_list.append(h.householder_id) #12
                single_list.append(h.policy_number) #13

                double_list.append(single_list)
                single_list=[]

        family_data=PoorPeopleDataForm.objects.filter(house_identifier=p.house_identifier)

        for f in family_data:
            family_additional_data=PoorPeopleAdditionalForm.objects.filter(people_id=f.people_id)

            for fa in family_additional_data:

                policy_data=PolicyStaticForm.objects.get(policy_number=fa.policy_number)

                name_str=''
                if policy_data.policy_first_layer:
                    name_str=policy_data.policy_first_layer
                if policy_data.policy_second_layer:
                    name_str=name_str+"."+policy_data.policy_second_layer
                if policy_data.policy_third_layer:
                    name_str=name_str+"."+policy_data.policy_third_layer
                single_list.append(name_str) #0

                subsidy_str=''
                if policy_data.subsidy_one:
                    subsidy_str=policy_data.subsidy_one
                if policy_data.subsidy_two:
                    subsidy_str=subsidy_str+"+"+policy_data.subsidy_two
                if policy_data.subsidy_three:
                    subsidy_str=subsidy_str+"+"+policy_data.subsidy_three
                if fa.subsidy_standard:
                    subsidy_str=fa.subsidy_standard
                single_list.append(subsidy_str) #1

                single_list.append(fa.policy_multiplier) #2
                single_list.append(fa.plan_money) #3
                single_list.append(fa.fact_money) #4

                date=fa.date_year+'-'+fa.date_month
                single_list.append(date) #5

                color_str='b'
                if fa.fact_money and fa.plan_money:
                    if float(fa.fact_money)<float(fa.plan_money):
                        color_str="o"
                    else:
                        color_str="b"
                single_list.append(color_str)  #6

                single_list.append(fa.bank_name) #7
                single_list.append(fa.bank_number) #8
                single_list.append(fa.card_people) #9
                single_list.append(fa.card_id) #10
                single_list.append(f.people_name) #11
                single_list.append(f.people_id) #12
                single_list.append(fa.policy_number) #13

                double_list.append(single_list)
                single_list=[]

        p.additionaldata=double_list #加上数据（贫困户享受政策数据）

    template='report_form/poorhousedataform/template_query_paginator.html'

    return render(request,template,{'poorhousedata_list':poorhousedata,'data_number':data_number,'curpage':curpage,'allpage':allpage})


def poorpeople(request):
    town_list=AdministrativeVillageDataForm.objects.filter(town_tag="1")
    town_name=[]
    for t in town_list:
        town_name.append(t.town_name) #获取所有乡镇名称
    return render(request,'report_form/poorpeopledataform/poorpeople.html',{'town_name':town_name})


def poorpeopledataform(request):
    house_identifier=request.GET.get('house_identifier')
    people_id=request.GET.get('people_id')

    if house_identifier:
        poorpeopledata_list=PoorPeopleDataForm.objects.filter(house_identifier=house_identifier)

    elif people_id:
        poorpeopledata_list=PoorPeopleDataForm.objects.filter(people_id=people_id)

    else:
        poorpeopledata_list=PoorPeopleDataForm.objects.all()

    data_number=len(poorpeopledata_list)  #贫困人口基本信息表所有数据的个数

    one_page_of_data=20

    curpage=1

    allpostcounts=poorpeopledata_list.count()
    allpage=allpostcounts//one_page_of_data
    remainpost=allpostcounts%one_page_of_data
    if remainpost>0:
        allpage=allpage+1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    poorpeopledata_list=poorpeopledata_list.all()[startpos:endpos] #分页

    for p in poorpeopledata_list:

        house_data=PoorHouseDataForm.objects.filter(house_identifier=p.house_identifier)
        for ho in house_data:
            p.now_village_identifier=ho.now_village_identifier #加上数据（合并后村编号）
            p.householder_name=ho.householder_name #加上数据（户主姓名）

            village_data=AdministrativeVillageDataForm.objects.filter(now_village_identifier=ho.now_village_identifier)
            for v in village_data:
                p.now_village_name=v.now_administrative_village #加上数据（合并后村名称）
                p.town_name=v.town_name

        year_time=datetime.date.today().year
        p.age=int(year_time)-int(p.birth_date[0:4]) #加上数据（贫困人口岁数）

        sex_number=int(p.people_id[16])
        if sex_number%2==0:
            p.sex="女"
        else:
            p.sex="男" #加上数据（加上贫困人口性别）

        single_list=[]
        double_list=[]

        additional_data=PoorPeopleAdditionalForm.objects.filter(people_id=p.people_id)

        for a in additional_data:

            policy_data=PolicyStaticForm.objects.get(policy_number=a.policy_number)

            name_str=''
            if policy_data.policy_first_layer:
                name_str=policy_data.policy_first_layer
            if policy_data.policy_second_layer:
                name_str=name_str+"."+policy_data.policy_second_layer
            if policy_data.policy_third_layer:
                name_str=name_str+"."+policy_data.policy_third_layer
            single_list.append(name_str) #0

            subsidy_str=''
            if policy_data.subsidy_one:
                subsidy_str=policy_data.subsidy_one
            if policy_data.subsidy_two:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_two
            if policy_data.subsidy_three:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_three
            if a.subsidy_standard:
                subsidy_str=a.subsidy_standard
            single_list.append(subsidy_str) #1

            single_list.append(a.policy_multiplier) #2
            single_list.append(a.plan_money) #3
            single_list.append(a.fact_money) #4

            date=a.date_year+'-'+a.date_month
            single_list.append(date) #5

            color_str='b'
            if a.fact_money and a.plan_money:
                if float(a.fact_money)<float(a.plan_money):
                    color_str="o"
                else:
                    color_str="b"
            single_list.append(color_str)  #6

            single_list.append(a.bank_name) #7
            single_list.append(a.bank_number) #8
            single_list.append(a.card_people) #9
            single_list.append(a.card_id) #10

            double_list.append(single_list)
            single_list=[]

        p.additionaldata=double_list #加上数据（贫困人口享受政策数据）

    town_list=AdministrativeVillageDataForm.objects.filter(town_tag="1")
    town_name=[]
    for t in town_list:
        town_name.append(t.town_name) #获取所有乡镇名称

    return render(request,'report_form/poorpeopledataform/poorpeopledataform.html',{'poorpeopledata_list':poorpeopledata_list,'data_number':data_number,'town_name':town_name,'curpage':curpage,'allpage':allpage})


@csrf_exempt
def people_template_initial_paginator(request):
    poorpeopledata_list=PoorPeopleDataForm.objects.all()

    data_number=len(poorpeopledata_list)  #贫困人口基本信息表所有数据的个数

    one_page_of_data=20

    curpage=int(request.POST.get('curpage'))
    allpage=int(request.POST.get('allpage'))
    pagetype=str(request.POST.get('pagetype'))

    if pagetype=='pagenext':
        curpage=curpage+1
    elif pagetype=='pagelast':
        curpage=curpage-1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    middlepos=request.POST.get('gopage')
    if middlepos is not None:
        if int(middlepos)<=allpage:
            startpos=(int(middlepos)-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=int(middlepos)
        else:
            startpos=(allpage-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=allpage

    poorpeopledata_list=poorpeopledata_list.all()[startpos:endpos] #分页

    for p in poorpeopledata_list:

        house_data=PoorHouseDataForm.objects.filter(house_identifier=p.house_identifier)
        for ho in house_data:
            p.now_village_identifier=ho.now_village_identifier #加上数据（合并后村编号）
            p.householder_name=ho.householder_name #加上数据（户主姓名）

            village_data=AdministrativeVillageDataForm.objects.filter(now_village_identifier=ho.now_village_identifier)
            for v in village_data:
                p.now_village_name=v.now_administrative_village #加上数据（合并后村名称）
                p.town_name=v.town_name

        year_time=datetime.date.today().year
        p.age=int(year_time)-int(p.birth_date[0:4]) #加上数据（贫困人口岁数）

        sex_number=int(p.people_id[16])
        if sex_number%2==0:
            p.sex="女"
        else:
            p.sex="男" #加上数据（加上贫困人口性别）

        single_list=[]
        double_list=[]

        additional_data=PoorPeopleAdditionalForm.objects.filter(people_id=p.people_id)

        for a in additional_data:

            policy_data=PolicyStaticForm.objects.get(policy_number=a.policy_number)

            name_str=''
            if policy_data.policy_first_layer:
                name_str=policy_data.policy_first_layer
            if policy_data.policy_second_layer:
                name_str=name_str+"."+policy_data.policy_second_layer
            if policy_data.policy_third_layer:
                name_str=name_str+"."+policy_data.policy_third_layer
            single_list.append(name_str) #0

            subsidy_str=''
            if policy_data.subsidy_one:
                subsidy_str=policy_data.subsidy_one
            if policy_data.subsidy_two:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_two
            if policy_data.subsidy_three:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_three
            if a.subsidy_standard:
                subsidy_str=a.subsidy_standard
            single_list.append(subsidy_str) #1

            single_list.append(a.policy_multiplier) #2
            single_list.append(a.plan_money) #3
            single_list.append(a.fact_money) #4

            date=a.date_year+'-'+a.date_month
            single_list.append(date) #5

            color_str='b'
            if a.fact_money and a.plan_money:
                if float(a.fact_money)<float(a.plan_money):
                    color_str="o"
                else:
                    color_str="b"
            single_list.append(color_str)  #6

            single_list.append(a.bank_name) #7
            single_list.append(a.bank_number) #8
            single_list.append(a.card_people) #9
            single_list.append(a.card_id) #10

            double_list.append(single_list)
            single_list=[]

        p.additionaldata=double_list #加上数据（贫困人口享受政策数据）

    template='report_form/poorpeopledataform/template_initial_paginator.html'

    return render(request,template,{'poorpeopledata_list':poorpeopledata_list,'data_number':data_number,'curpage':curpage,'allpage':allpage})


@csrf_exempt
def people_town_change(request):
    town=request.POST.get("town")
    village_list=AdministrativeVillageDataForm.objects.filter(town_name=town,village_tag="1")
    village_name=[]
    for v in village_list:
        village_name.append(v.now_administrative_village)
    res={'village_name':village_name}
    return HttpResponse(json.dumps(res),content_type='application/json')


@csrf_exempt
def people_template_query_paginator(request):

    town=request.POST.get("town")
    definition=request.POST.get("definition")
    householder=request.POST.get("householder")
    person=request.POST.get("person")
    identity=request.POST.get("identity")
    poor=request.POST.get("poor")
    year=request.POST.get("year") #获取条件数据

    poorpeopledata=PoorPeopleDataForm.objects.all()

    if not town=="请选择":
        village_list=AdministrativeVillageDataForm.objects.filter(town_name=town,village_tag="1")
        now_village_identifier_list=[]
        for v in village_list:
            now_village_identifier_list.append(v.now_village_identifier)
        house_list=PoorHouseDataForm.objects.filter(now_village_identifier__in=now_village_identifier_list)
        house_identifier_list=[]
        for h in house_list:
            house_identifier_list.append(h.house_identifier)
        poorpeopledata=poorpeopledata.filter(house_identifier__in=house_identifier_list)
    if not definition=="请选择":
        village_list=AdministrativeVillageDataForm.objects.get(town_name=town,now_administrative_village=definition,village_tag="1")
        now_village_identifier=village_list.now_village_identifier
        house_list=PoorHouseDataForm.objects.filter(now_village_identifier=now_village_identifier)
        house_identifier_list=[]
        for h in house_list:
            house_identifier_list.append(h.house_identifier)
        poorpeopledata=poorpeopledata.filter(house_identifier__in=house_identifier_list)
    if householder:
        house_list=PoorHouseDataForm.objects.filter(householder_name=householder)
        house_identifier_list=[]
        for h in house_list:
            house_identifier_list.append(h.house_identifier)
        poorpeopledata=poorpeopledata.filter(house_identifier__in=house_identifier_list)
    if person:
        poorpeopledata=poorpeopledata.filter(people_name=person)
    if identity:
        poorpeopledata=poorpeopledata.filter(people_id=identity)
    if not poor=="请选择":
        poorpeopledata=poorpeopledata.filter(poor_attribute=poor)
    if year:
        poorpeopledata=poorpeopledata.filter(year_date=year) #根据条件进行数据筛选

    data_number=len(poorpeopledata) #计算根据条件进行数据筛选后的数据个数

    one_page_of_data=20

    curpage=int(request.POST.get('curpage','1'))
    allpage=int(request.POST.get('allpage','1'))
    pagetype=str(request.POST.get('pagetype',''))

    if pagetype=='pagenext':
        curpage=curpage+1
    elif pagetype=='pagelast':
        curpage=curpage-1

    if curpage==1 and allpage==1:
        allpostcounts=poorpeopledata.count()
        allpage=allpostcounts//one_page_of_data
        remainpost=allpostcounts%one_page_of_data
        if remainpost>0:
            allpage=allpage+1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    middlepos=request.POST.get('gopage')
    if middlepos is not None:
        if int(middlepos)<=allpage:
            startpos=(int(middlepos)-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=int(middlepos)
        else:
            startpos=(allpage-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=allpage

    poorpeopledata=poorpeopledata.all()[startpos:endpos] #分页

    for p in poorpeopledata:

        house_data=PoorHouseDataForm.objects.filter(house_identifier=p.house_identifier)
        for ho in house_data:
            p.now_village_identifier=ho.now_village_identifier #加上数据（合并后村编号）
            p.householder_name=ho.householder_name #加上数据（户主姓名）

            village_data=AdministrativeVillageDataForm.objects.filter(now_village_identifier=ho.now_village_identifier)
            for v in village_data:
                p.now_village_name=v.now_administrative_village #加上数据（合并后村名称）
                p.town_name=v.town_name

        year_time=datetime.date.today().year
        p.age=int(year_time)-int(p.birth_date[0:4]) #加上数据（贫困人口岁数）

        sex_number=int(p.people_id[16])
        if sex_number%2==0:
            p.sex="女"
        else:
            p.sex="男" #加上数据（加上贫困人口性别）

        single_list=[]
        double_list=[]

        additional_data=PoorPeopleAdditionalForm.objects.filter(people_id=p.people_id)

        for a in additional_data:

            policy_data=PolicyStaticForm.objects.get(policy_number=a.policy_number)

            name_str=''
            if policy_data.policy_first_layer:
                name_str=policy_data.policy_first_layer
            if policy_data.policy_second_layer:
                name_str=name_str+"."+policy_data.policy_second_layer
            if policy_data.policy_third_layer:
                name_str=name_str+"."+policy_data.policy_third_layer
            single_list.append(name_str) #0

            subsidy_str=''
            if policy_data.subsidy_one:
                subsidy_str=policy_data.subsidy_one
            if policy_data.subsidy_two:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_two
            if policy_data.subsidy_three:
                subsidy_str=subsidy_str+"+"+policy_data.subsidy_three
            if a.subsidy_standard:
                subsidy_str=a.subsidy_standard
            single_list.append(subsidy_str) #1

            single_list.append(a.policy_multiplier) #2
            single_list.append(a.plan_money) #3
            single_list.append(a.fact_money) #4

            date=a.date_year+'-'+a.date_month
            single_list.append(date) #5

            color_str='b'
            if a.plan_money and a.fact_money:
                if float(a.fact_money)<float(a.plan_money):
                    color_str="o"
                else:
                    color_str="b"
            single_list.append(color_str)  #6

            single_list.append(a.bank_name) #7
            single_list.append(a.bank_number) #8
            single_list.append(a.card_people) #9
            single_list.append(a.card_id) #10

            double_list.append(single_list)
            single_list=[]

        p.additionaldata=double_list #加上数据（贫困人口享受政策数据）

    template='report_form/poorpeopledataform/template_query_paginator.html'

    return render(request,template,{'poorpeopledata_list':poorpeopledata,'data_number':data_number,'curpage':curpage,'allpage':allpage})


def helper(request):
    town_list=AdministrativeVillageDataForm.objects.filter(town_tag="1")
    town_name=[]
    for t in town_list:
        town_name.append(t.town_name) #获取所有乡镇名称
    return render(request,'report_form/helperdataform/helper.html',{'town_name':town_name})


def helperdataform(request):
    # edit_helperdata_list=HelperDataForm.objects.all()
    # for e in edit_helperdata_list:
    #     data=HelperDataForm.objects.filter(poor_town=e.poor_town,now_administrative_village=e.now_administrative_village,helper_tag="1",helper_name=e.helper_name,office_phone=e.office_phone,mobile_phone=e.mobile_phone)
    #     if data.count()==0:
    #         e.helper_tag="1"
    #         e.save()

    helperdata_list=HelperDataForm.objects.all()

    data_number=len(helperdata_list)

    people_number=(HelperDataForm.objects.filter(helper_tag="1")).count()

    one_page_of_data=20

    curpage=1

    allpostcounts=helperdata_list.count()
    allpage=allpostcounts//one_page_of_data
    remainpost=allpostcounts%one_page_of_data
    if remainpost>0:
        allpage=allpage+1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    helperdata_list=helperdata_list.all()[startpos:endpos] ###

    for h in helperdata_list:
        index01=(h.poor_home).find('.')
        if index01!=-1:
            h.poor_home=(h.poor_home)[:-2]
        index02=(h.office_phone).find('.')
        if index02!=-1:
            h.poor_home=(h.office_phone)[:-2]
        index03=(h.mobile_phone).find('.')
        if index03!=-1:
            h.mobile_phone=(h.mobile_phone)[:-2]

    town_list=AdministrativeVillageDataForm.objects.filter(town_tag="1")
    town_name=[]
    for t in town_list:
        town_name.append(t.town_name)

    return render(request,'report_form/helperdataform/helperdataform.html',{'helperdata_list':helperdata_list,'data_number':data_number,'town_name':town_name,'curpage':curpage,'allpage':allpage,'people_number':people_number})


@csrf_exempt
def helper_template_initial_paginator(request):
    helperdata_list=HelperDataForm.objects.all()

    data_number=len(helperdata_list)

    people_number=(HelperDataForm.objects.filter(helper_tag="1")).count()

    one_page_of_data=20

    curpage=int(request.POST.get('curpage'))
    allpage=int(request.POST.get('allpage'))
    pagetype=str(request.POST.get('pagetype'))

    if pagetype=='pagenext':
        curpage=curpage+1
    elif pagetype=='pagelast':
        curpage=curpage-1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    middlepos=request.POST.get('gopage')
    if middlepos is not None:
        if int(middlepos)<=allpage:
            startpos=(int(middlepos)-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=int(middlepos)
        else:
            startpos=(allpage-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=allpage

    helperdata_list=helperdata_list.all()[startpos:endpos] ###

    for h in helperdata_list:
        index01=(h.poor_home).find('.')
        if index01!=-1:
            h.poor_home=(h.poor_home)[:-2]
        index02=(h.office_phone).find('.')
        if index02!=-1:
            h.poor_home=(h.office_phone)[:-2]
        index03=(h.mobile_phone).find('.')
        if index03!=-1:
            h.mobile_phone=(h.mobile_phone)[:-2]

    template='report_form/helperdataform/template_initial_paginator.html'

    return render(request,template,{'helperdata_list':helperdata_list,'data_number':data_number,'curpage':curpage,'allpage':allpage,'people_number':people_number})


@csrf_exempt
def helper_town_change(request):
    town=request.POST.get("town")
    village_list=AdministrativeVillageDataForm.objects.filter(town_name=town,village_tag="1")
    village_name=[]
    for v in village_list:
        village_name.append(v.now_administrative_village)
    res={'village_name':village_name}
    return HttpResponse(json.dumps(res),content_type='application/json')


@csrf_exempt
def helper_template_query_paginator(request):
    town=request.POST.get("town")
    definition=request.POST.get("definition")
    householder=request.POST.get("householder")
    helper=request.POST.get("helper")

    helperdata=HelperDataForm.objects.all()
    if not town=="请选择":
        helperdata=helperdata.filter(poor_town=town)
    if not definition=="请选择":
        helperdata=helperdata.filter(now_administrative_village=definition)
    if householder:
        helperdata=helperdata.filter(poor_name=householder)
    if helper:
        helperdata=helperdata.filter(helper_name=helper)

    data_number=len(helperdata)

    one_page_of_data=20

    people_number=(helperdata.filter(helper_tag="1")).count()

    curpage=int(request.POST.get('curpage','1'))
    allpage=int(request.POST.get('allpage','1'))
    pagetype=str(request.POST.get('pagetype',''))

    if pagetype=='pagenext':
        curpage=curpage+1
    elif pagetype=='pagelast':
        curpage=curpage-1

    if curpage==1 and allpage==1:
        allpostcounts=helperdata.count()
        allpage=allpostcounts//one_page_of_data
        remainpost=allpostcounts%one_page_of_data
        if remainpost>0:
            allpage=allpage+1

    startpos=(curpage-1)*one_page_of_data
    endpos=startpos+one_page_of_data

    middlepos=request.POST.get('gopage')
    if middlepos is not None:
        if int(middlepos)<=allpage:
            startpos=(int(middlepos)-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=int(middlepos)
        else:
            startpos=(allpage-1)*one_page_of_data
            endpos=startpos+one_page_of_data
            curpage=allpage

    helperdata=helperdata.all()[startpos:endpos] ###

    for h in helperdata:
        index01=(h.poor_home).find('.')
        if index01!=-1:
            h.poor_home=(h.poor_home)[:-2]
        index02=(h.office_phone).find('.')
        if index02!=-1:
            h.office_phone=(h.office_phone)[:-2]
        index03=(h.mobile_phone).find('.')
        if index03!=-1:
            h.mobile_phone=(h.mobile_phone)[:-2]

    template='report_form/helperdataform/template_query_paginator.html'

    return render(request,template,{'helperdata_list':helperdata,'data_number':data_number,'curpage':curpage,'allpage':allpage,'people_number':people_number})

def policy(request):
    # edit_policydata_list=PolicyStaticForm.objects.all()
    # for e in edit_policydata_list:
    #     data=PolicyStaticForm.objects.filter(implement_department=e.implement_department,department_tag='1')
    #     if data.count()==0:
    #         e.department_tag="1"
    #         e.save()

    policystaticform_list=PolicyStaticForm.objects.order_by("policy_number")

    for p in policystaticform_list:
        policy_name=''
        if p.policy_first_layer:
            policy_name=p.policy_first_layer
        if p.policy_second_layer:
            policy_name=policy_name+"."+p.policy_second_layer
        if p.policy_third_layer:
            policy_name=policy_name+"."+p.policy_third_layer
        p.policy_name=policy_name

        policy_subsidy=''
        if p.subsidy_one:
            policy_subsidy=p.subsidy_one
        if p.subsidy_two:
            policy_subsidy=policy_subsidy+"+"+p.subsidy_two
        if p.subsidy_three:
            policy_subsidy=policy_subsidy+"+"+p.subsidy_three
        p.policy_subsidy=policy_subsidy

    department_list=PolicyStaticForm.objects.filter(department_tag="1")
    department_list=department_list.order_by("implement_department")
    department_name=[]
    for d in department_list:
        department_name.append(d.implement_department)

    return render(request,'report_form/policydataform/policy.html',{'policystaticform_list':policystaticform_list,'department_name':department_name})

@csrf_exempt
def policy_template_query(request):

    department=request.POST.get("department")

    policystaticform_list=PolicyStaticForm.objects.order_by("policy_number")

    if not department=="请选择":
        policystaticform_list=policystaticform_list.filter(implement_department=department)

    for p in policystaticform_list:
        policy_name=''
        if p.policy_first_layer:
            policy_name=p.policy_first_layer
        if p.policy_second_layer:
            policy_name=policy_name+"."+p.policy_second_layer
        if p.policy_third_layer:
            policy_name=policy_name+"."+p.policy_third_layer
        p.policy_name=policy_name

        policy_subsidy=''
        if p.subsidy_one:
            policy_subsidy=p.subsidy_one
        if p.subsidy_two:
            policy_subsidy=policy_subsidy+"+"+p.subsidy_two
        if p.subsidy_three:
            policy_subsidy=policy_subsidy+"+"+p.subsidy_three
        p.policy_subsidy=policy_subsidy

    template='report_form/policydataform/template_query.html'

    return render(request,template,{'policystaticform_list':policystaticform_list})

@csrf_exempt
def house_data_modify(request):

    object=request.POST.get("object")
    standard=request.POST.get("standard")
    number=request.POST.get("number")
    plan=request.POST.get("plan")
    fact=request.POST.get("fact")
    time=request.POST.get("time")
    bank=request.POST.get("bank")
    account=request.POST.get("account")
    receiver=request.POST.get("receiver")
    identification=request.POST.get("identification")
    id_code=request.POST.get("id_code")
    policy_number=request.POST.get("policy_number")
    date_year=request.POST.get("date_year")
    date_month=request.POST.get("date_month")

    if object=="户":
        poorhouse=PoorHouseAdditionalForm.objects.get(householder_id=id_code,policy_number=policy_number,date_year=date_year,date_month=date_month)
        poorhouse.subsidy_standard=standard
        poorhouse.policy_multiplier=number
        poorhouse.plan_money=plan
        poorhouse.fact_money=fact
        poorhouse.date_year=time[0:4]
        poorhouse.date_month=time[5:len(time)]
        poorhouse.bank_name=bank
        poorhouse.bank_number=account
        poorhouse.card_people=receiver
        poorhouse.people_id=identification
        poorhouse.save()
    else:
        poorpeople=PoorPeopleAdditionalForm.objects.get(people_id=id_code,policy_number=policy_number,date_year=date_year,date_month=date_month)
        poorpeople.subsidy_standard=standard
        poorpeople.policy_multiplier=number
        poorpeople.plan_money=plan
        poorpeople.fact_money=fact
        poorpeople.date_year=time[0:4]
        poorpeople.date_month=time[5:len(time)]
        poorpeople.bank_name=bank
        poorpeople.bank_number=account
        poorpeople.card_people=receiver
        poorpeople.card_id=identification
        poorpeople.save()

    res={'standard':standard,'number':number,'plan':plan,'fact':fact,'time':time,'bank':bank,'account':account,'receiver':receiver,'identification':identification}
    return HttpResponse(json.dumps(res),content_type='application/json')

@csrf_exempt
def house_data_delete(request):

    object=request.POST.get("object")
    id_code=request.POST.get("id_code")
    policy_number=request.POST.get("policy_number")
    date_year=request.POST.get("date_year")
    date_month=request.POST.get("date_month")

    if object=="户":
        poorhouse=PoorHouseAdditionalForm.objects.get(householder_id=id_code,policy_number=policy_number,date_year=date_year,date_month=date_month)
        poorhouse.delete()
    else:
        poorpeople=PoorPeopleAdditionalForm.objects.get(people_id=id_code,policy_number=policy_number,date_year=date_year,date_month=date_month)
        poorpeople.delete()

    res={'ok':'ok'}
    return HttpResponse(json.dumps(res),content_type='application/json')