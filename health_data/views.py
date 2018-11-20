from django.shortcuts import render

from report_form import models as report_models
from health_data import models as health_models

import math,collections,json

#
# import locale
# locale.setlocale(locale.LC_ALL,'en')
#

# Create your views here.

def four_one(request):  # 四位一体
    # 乡镇-行政村数据 start
    village_all = report_models.AdministrativeVillageDataForm.objects.all().values('town_name','now_village_identifier','now_administrative_village')
    village_data = collections.defaultdict(dict)
    for value in village_all:
        village_data[value['town_name']][value['now_village_identifier']] = value['now_administrative_village']
    # 乡镇-行政村数据 end

    page = request.GET.get('page', 1)
    policy_id = request.GET.get('policy_id')
    policy_obj = report_models.PolicyStaticForm.objects.get(id=policy_id)

    # 搜索-start
    # now_village_identifier = request.GET.get('now_village_identifier', '').strip()
    people_id = request.GET.get('people_id', '').strip()
    search_condition = ''
    # if now_village_identifier != '':
    #     house_identifiers = report_models.PoorHouseDataForm.objects.filter(now_village_identifier=now_village_identifier).values_list('house_identifier', flat=True)
    #     house_identifier_s = ','.join(house_identifiers)
    #     search_condition += "house_identifier in (" + house_identifier_s + ") and "
    if people_id != '':
        search_condition += "people_id = '" + people_id + "' "
    # 搜索-end

    if search_condition == '':
        #如果搜索条件为空，那么查询所有
        search_condition = '1=1'

    count_sql = "SELECT count(id) FROM health_data_fourinoneadditionalform WHERE "+search_condition+" ;"
    count_res = list(health_models.FourInOneAdditionalForm.objects.raw(count_sql).query)
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

    sql = "SELECT * FROM health_data_fourinoneadditionalform WHERE "+ search_condition + " LIMIT "+limit_start+","+str(every_page_number)+";"
    obj_list = health_models.FourInOneAdditionalForm.objects.raw(sql)

    print(sql)
    return render(request,'health_data/four_one.html',{
        "page": page,
        "count": count,
        "policy_id": policy_id,
        "every_page_number": every_page_number,
        "policy_obj": policy_obj,
        "data": obj_list,
        "village_data": village_data,
        "village_data_str": json.dumps(village_data)
    })