import os,collections

#VIEW_DIR = "E:\job/新建文件夹"
VIEW_DIR = "E:/job/data"#文件存放路径
DELETE_DIR = "E:/job/delete_data"#删除文件存放路径
DOWNLOAD_URL_PR = "E:/job/download"#文件下载路径url前缀

DATA_DICT = {
    "overcome_poverty":"overcome_poverty.pick"#脱贫人数数据存放路径
}

#各部门数据存放路径，相对于VIEW_DIR
VIEW_DICT = {
    "1":"政策落实按部门分类数据/扶贫办",
    "2":"政策落实按部门分类数据/农办",
    "3":"政策落实按部门分类数据/教育局",
    "4":"政策落实按部门分类数据/民政局",
    "5":"政策落实按部门分类数据/人社局",
    "6":"政策落实按部门分类数据/易地扶贫搬迁指挥部",
    "7":"政策落实按部门分类数据/残联",
    "8":"政策落实按部门分类数据/发改局",
    "9":"政策落实按部门分类数据/老龄办",
    "10":"政策落实按部门分类数据/妇联",
    "11":"政策落实按部门分类数据/其他",
    "14":"政策落实按部门分类数据/农办/农业局",
    "15":"政策落实按部门分类数据/农办/林业局",
    "16":"政策落实按部门分类数据/农办/畜牧局",
    "17":"政策落实按部门分类数据/农办/水产局",
    "18":"政策落实按部门分类数据/农办/人社局",
    "19":"政策落实按部门分类数据/农办/经信局",
    "20":"政策落实按部门分类数据/农办/旅游局",
    "12":"政策落实按部门分类数据/金融办",
    "国办":"国办数据",
    "其他":"其他数据"

}

#行政村基本信息表 excel表格列与“AdministrativeVillageDataForm”表字段对应关系
ADMINISTRATIVE_VILLAGE = collections.OrderedDict([
    ('乡镇名称','town_name'),
    ('合并前村编号','past_village_identifier'),
    ('合并前村名称','past_administrative_village'),
    ('合并后村编号','now_village_identifier'),
    ('合并后村名称','now_administrative_village'),
    ('合并前是否为贫困村','past_is_poor'),
    ('合并后是否为贫困村','now_is_poor'),
    ('是否参与合并','is_merge'),
    ('是否更名','is_rename')
])


#国办数据-贫困村数据 excel表格列
# POVERTY_VILLAGE = ['序号', '行政区划编码', '县', '乡（镇）', '村', '负责人', '村办公电话', '村属性', '是否出列', '总户数', '总人口数', '自然村数', '贫困户数', '贫困人口数', '低保人口数', '低保户数', '五保人口数', '五保户数', '少数民族人口数', '妇女人口数', '残疾人口数', '劳动力人数', '外出务工人数', '省', '市（州）']

#国办数据-贫困村数据 excel表格列与“AdministrativeVillageDataForm”表字段对应关系
POVERTY_VILLAGE = collections.OrderedDict([
    ('序号', ''),
    ('行政区划编码', 'past_village_identifier'),
    ('县', ''),
    ('乡（镇）', 'town_name'),
    ('村', 'past_administrative_village'),
    ('负责人', 'past_responsible_person'),
    ('村办公电话', ''),
    ('村属性', 'past_is_poor'),
    ('是否出列', ''),
    ('总户数', 'past_home_number'),
    ('总人口数', 'past_people_number'),
    ('自然村数', ''),
    ('贫困户数', 'past_poor_home'),
    ('贫困人口数', 'past_poor_people'),
    ('低保人口数', 'past_minimum_people'),
    ('低保户数', 'past_minimum_home'),
    ('五保人口数', 'past_five_people'),
    ('五保户数', 'past_five_home'),
    ('少数民族人口数', 'past_nation_people'),
    ('妇女人口数', 'past_woman_people'),
    ('残疾人口数', 'past_handicapped_people'),
    ('劳动力人数', 'past_labor_people'),
    ('外出务工人数', 'past_egression_people'),
    ('省', ''),
    ('市（州）', '')
])


#国办数据-贫困户数据 excel表格列
# POVERTY_FAMILY = ['序号', '县(市、区、旗)', '乡(镇)', '行政村', '自然村', '户编号', '人编号', '姓名', '证件号码', '人数', '与户主关系', '民族', '文化程度', '在校生状况', '健康状况', '劳动技能', '务工状况', '务工时间（月）', '参加大病医疗', '脱贫属性', '脱贫年度', '贫困户属性', '主要致贫原因', '危房户', '饮水安全', '饮水困难', '人均纯收入', '联系电话']

#国办数据-贫困户数据 excel表格列与表“PoorHouseDataForm”字段对应关系
POVERTY_FAMILY = collections.OrderedDict([
    ('序号', ''),
    ('县(市、区、旗)', ''),
    #通过"乡(镇)"和"行政村"，获取村编号
    ('乡(镇)', '乡(镇)'),
    ('行政村', '行政村'),
    ('自然村', ''),
    ('户编号', 'house_identifier'),
    ('人编号', 'householder_identifier'),
    ('姓名', 'householder_name'),
    ('证件号码', 'householder_id'),
    ('人数', 'family_number'),
    ('与户主关系', ''),
    ('民族', 'people_nation'),
    ('文化程度', 'education_degree'),
    ('在校生状况', 'school_situation'),
    ('健康状况', 'health_situation'),
    ('劳动技能', 'labor_ability'),
    ('务工状况', 'work_situation'),
    ('务工时间（月）', 'work_time'),
    ('参加大病医疗', 'join_medical'),
    ('脱贫属性', 'offpoor_attribute'),
    ('脱贫年度', 'offpoor_year'),
    ('贫困户属性', 'poor_attribute'),
    ('主要致贫原因', 'poor_reason'),
    ('危房户', 'danger_house'),
    ('饮水安全', 'water_safe'),
    ('饮水困难', 'water_hard'),
    ('人均纯收入', 'average_income'),
    ('联系电话', 'telephone')
])


#国办数据-贫困人口数据 excel表格列
# POVERTY_MAN = ['序号', '县(市、区、旗)', '乡(镇)', '行政村', '自然村', '户编号', '人编号', '姓名', '证件号码', '人数', '与户主关系', '民族', '文化程度', '在校生状况', '健康状况', '劳动技能', '务工时间（月）', '参加大病医疗', '脱贫属性', '贫困户属性', '主要致贫原因']

#国办数据-贫困人口数据 excel表格列与表“PoorPeopleDataForm”字段对应关系
POVERTY_MAN = collections.OrderedDict([
    ('序号', ''),
    ('县(市、区、旗)', ''),
    ('乡(镇)', ''),
    ('行政村', ''),
    ('自然村', ''),
    ('户编号', 'house_identifier'),
    ('人编号', 'people_identifier'),
    ('姓名', 'people_name'),
    ('证件号码', 'people_id'),
    ('人数', 'family_number'),
    ('与户主关系', 'people_relationship'),
    ('民族', 'people_nation'),
    ('文化程度', 'education_degree'),
    ('在校生状况', 'school_situation'),
    ('健康状况', 'health_situation'),
    ('劳动技能', 'labor_ability'),
    ('务工时间（月）', 'work_time'),
    ('参加大病医疗', 'join_medical'),
    ('脱贫属性', 'offpoor_attribute'),
    ('贫困户属性', ''),
    ('主要致贫原因', 'poor_reason')
])

POVERTY_HELPER = collections.OrderedDict([
    ('单位名称','unit_name'),
    ('姓名','helper_name'),
    ('性别','helper_sex'),
    ('职务','helper_post'),
    ('队长/队员/结对帮扶责任人','helper_type'),
    ('乡镇','poor_town'),
    ('村','now_administrative_village'),
    ('户数','poor_home'),
    ('户主姓名（组别）','poor_name'),
    ('办公电话','office_phone'),
    ('手机','mobile_phone')
])