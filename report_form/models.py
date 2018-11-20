from django.db import models


# Create your models here.


#1
class AdministrativeVillageDataForm(models.Model):    #行政村基本信息表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡（镇）

    past_administrative_village=models.CharField(max_length=50,db_column='past_administrative_village',blank=True)    #行政村曾用名

    now_administrative_village=models.CharField(max_length=50,db_column='now_administrative_village',blank=True)    #行政村现用名

    past_village_identifier=models.CharField(max_length=30,db_column='past_village_identifier',blank=True)    #过去村编号

    now_village_identifier=models.CharField(max_length=30,db_column='now_village_identifier',blank=True)    #现在村编号

    past_is_poor=models.CharField(max_length=10,db_column='past_is_poor',blank=True)    #是否曾为贫困村

    now_is_poor=models.CharField(max_length=10,db_column='now_is_poor',blank=True)    #是否现为贫困村

    is_merge=models.CharField(max_length=10,db_column='is_merge',blank=True)    #是否参与合并

    is_rename=models.CharField(max_length=10,db_column='is_rename',blank=True)    #是否更名

    past_home_number=models.CharField(max_length=20,db_column='past_home_number',blank=True)    #过去总户数

    now_home_number=models.CharField(max_length=20,db_column='now_home_number',blank=True)    #现在总户数

    past_poor_home=models.CharField(max_length=20,db_column='past_poor_home',blank=True)    #过去贫困户数

    now_poor_home=models.CharField(max_length=20,db_column='now_poor_home',blank=True)    #现在贫困户数

    past_people_number=models.CharField(max_length=20,db_column='past_people_number',blank=True)    #过去人口总数

    now_people_number=models.CharField(max_length=20,db_column='now_people_number',blank=True)    #现在人口总数

    past_poor_people=models.CharField(max_length=20,db_column='past_poor_people',blank=True)    #过去贫困人口数

    now_poor_people=models.CharField(max_length=20,db_column='now_poor_people',blank=True)    #现在贫困人口数

    past_responsible_person=models.CharField(max_length=100,db_column='past_responsible_person',blank=True)    #过去负责人

    now_responsible_person=models.CharField(max_length=100,db_column='now_responsible_person',blank=True)    #现在负责人

    past_telephone_number=models.CharField(max_length=100,db_column='past_telephone_number',blank=True)    #过去村办公电话

    now_telephone_number=models.CharField(max_length=100,db_column='now_telephone_number',blank=True)    #现在村办公电话

    past_development_direction=models.CharField(max_length=30,db_column='past_development_direction',blank=True)    #过去发展方向

    now_development_direction=models.CharField(max_length=30,db_column='now_development_direction',blank=True)    #现在发展方向

    past_village_officer=models.CharField(max_length=20,db_column='past_village_officer',blank=True)    #过去村官人数

    now_village_officer=models.CharField(max_length=20,db_column='now_village_officer',blank=True)    #现在村官人数

    past_party_member=models.CharField(max_length=20,db_column='past_party_member',blank=True)    #过去中共党员数

    now_party_member=models.CharField(max_length=20,db_column='now_party_member',blank=True)    #现在中共党员数

    past_terrain_physiognomy=models.CharField(max_length=30,db_column='past_terrain_physiognomy',blank=True)    #过去地形地貌

    now_terrain_physiognomy=models.CharField(max_length=30,db_column='now_terrain_physiognomy',blank=True)    #现在地形地貌

    past_dimension=models.CharField(max_length=30,db_column='past_dimension',blank=True)    #过去纬度

    now_dimension=models.CharField(max_length=30,db_column='now_dimension',blank=True)    #现在纬度

    past_longitude=models.CharField(max_length=30,db_column='past_longitude',blank=True)    #过去经度

    now_longitude=models.CharField(max_length=30,db_column='now_longitude',blank=True)    #现在经度

    past_minimum_home=models.CharField(max_length=20,db_column='past_minimum_home',blank=True)    #过去低保户数

    now_minimum_home=models.CharField(max_length=20,db_column='now_minimum_home',blank=True)    #现在低保户数

    past_minimum_people=models.CharField(max_length=20,db_column='past_minimum_people',blank=True)    #过去低保人口数

    now_minimum_people=models.CharField(max_length=20,db_column='now_minimum_people',blank=True)    #现在低保人口数

    past_five_home=models.CharField(max_length=20,db_column='past_five_home',blank=True)    #过去五保户数

    now_five_home=models.CharField(max_length=20,db_column='now_five_home',blank=True)    #现在五保户数

    past_five_people=models.CharField(max_length=20,db_column='past_five_people',blank=True)    #过去五保人口数

    now_five_people=models.CharField(max_length=20,db_column='now_five_people',blank=True)    #现在五保人口数

    past_nation_people=models.CharField(max_length=20,db_column='past_nation_people',blank=True)    #过去少数民族人口数

    now_nation_people=models.CharField(max_length=20,db_column='now_nation_people',blank=True)    #现在少数民族人口数

    past_woman_people=models.CharField(max_length=20,db_column='past_woman_people',blank=True)    #过去妇女人口数

    now_woman_people=models.CharField(max_length=20,db_column='now_woman_people',blank=True)    #现在妇女人口数

    past_handicapped_people=models.CharField(max_length=20,db_column='past_handicapped_people',blank=True)    #过去残疾人口数

    now_handicapped_people=models.CharField(max_length=20,db_column='now_handicapped_people',blank=True)    #现在残疾人口数

    past_labor_people=models.CharField(max_length=20,db_column='past_labor_people',blank=True)    #过去劳动力人数

    now_labor_people=models.CharField(max_length=20,db_column='now_labor_people',blank=True)    #现在劳动力人数

    past_egression_people=models.CharField(max_length=20,db_column='past_egression_people',blank=True)    #过去外出务工人数

    now_egression_people=models.CharField(max_length=20,db_column='now_egression_people',blank=True)    #现在外出务工人数

    year_date=models.CharField(max_length=10,db_column='year_date',blank=True)    #年度

    past_help_people=models.CharField(max_length=50,db_column='past_help_people',blank=True)    #过去帮扶人员

    now_help_people=models.CharField(max_length=50,db_column='now_help_people',blank=True)    #现在帮扶人员

    past_help_unit=models.CharField(max_length=50,db_column='past_help_unit',blank=True)    #过去帮扶单位

    now_help_unit=models.CharField(max_length=50,db_column='now_help_unit',blank=True)    #现在帮扶单位

    past_help_way=models.CharField(max_length=50,db_column='past_help_way',blank=True)    #过去帮扶方式

    now_help_way=models.CharField(max_length=50,db_column='now_help_way',blank=True)    #现在帮扶方式

    past_help_phone=models.CharField(max_length=100,db_column='past_help_phone',blank=True)    #过去帮扶人员电话号码

    now_help_phone=models.CharField(max_length=100,db_column='now_help_phone',blank=True)    #现在帮扶人员电话号码

    village_tag=models.CharField(max_length=5,db_column='village_tag',blank=True)    #区分合并后行政村名称相同的数据

    town_tag=models.CharField(max_length=5,db_column='town_tag',blank=True)    #区分乡镇名称相同的数据

    def __str__(self):
        return self.town_name

    class Meta:
        verbose_name = '贫困村'


#2
class AdministrativeVillageAdditionalForm(models.Model):    #行政村附加表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    past_village_identifier=models.CharField(max_length=30,db_column='past_village_identifier',blank=True)    #过去村编号

    now_village_identifier=models.CharField(max_length=30,db_column='now_village_identifier',blank=True)    #现在村编号

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #接受扶持款的卡的银行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #接受扶持款的卡的账号

    card_people=models.CharField(max_length=30,db_column='card_people',blank=True)    #卡主姓名

    people_id=models.CharField(max_length=20,db_column='people_id',blank=True)    #卡主身份证号

    policy_number=models.CharField(max_length=30,db_column='policy_number',blank=True)    #应享政策编号

    policy_multiplier=models.CharField(max_length=20,db_column='policy_multiplier',blank=True)    #该政策编号乘以数量

    plan_money=models.CharField(max_length=20,db_column='plan_money',blank=True)    #应享政策编号对应的钱金额

    fact_money=models.CharField(max_length=20,db_column='fact_money',blank=True)    #实际享受到政策编号对应的钱金额

    date_year=models.CharField(max_length=20,db_column='date_year',blank=True)    #截止时间年

    date_month=models.CharField(max_length=20,db_column='date_month',blank=True)    #截止时间月

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

    subsidy_standard=models.CharField(max_length=300,db_column='subsidy_standard',blank=True)    #补助标准

    def __str__(self):
        return self.now_village_identifier


#1
class PoorHouseDataForm(models.Model):    #贫困户基本信息表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡（镇）

    past_village_identifier=models.CharField(max_length=30,db_column='past_village_identifier',blank=True,db_index = True)    #过去村编号

    now_village_identifier=models.CharField(max_length=30,db_column='now_village_identifier',blank=True,db_index = True)    #现在村编号

    house_identifier=models.CharField(max_length=30,db_column='house_identifier',blank=True)    #户编号

    house_group=models.CharField(max_length=20,db_column='house_group',blank=True)    #所在组

    householder_identifier=models.CharField(max_length=30,db_column='householder_identifier',blank=True)    #户主个人编号

    householder_name=models.CharField(max_length=30,db_column='householder_name',blank=True)    #户主姓名

    householder_id=models.CharField(max_length=20,db_column='householder_id',blank=True,db_index=True)    #户主身份证号

    family_number=models.CharField(max_length=10,db_column='family_number',blank=True)    #人数

    people_nation=models.CharField(max_length=20,db_column='people_nation',blank=True)    #民族

    education_degree=models.CharField(max_length=30,db_column='education_degree',blank=True)    #文化程度

    school_situation=models.CharField(max_length=30,db_column='school_situation',blank=True)    #在校生状况

    health_situation=models.CharField(max_length=30,db_column='health_situation',blank=True)    #健康状况

    labor_ability=models.CharField(max_length=30,db_column='labor_ability',blank=True)    #劳动技能

    work_situation=models.CharField(max_length=30,db_column='work_situation',blank=True)    #务工状况

    work_time=models.CharField(max_length=10,db_column='work_time',blank=True)    #务工时间（月）

    join_medical=models.CharField(max_length=10,db_column='join_medical',blank=True)    #参加大病医疗

    offpoor_attribute=models.CharField(max_length=30,db_column='offpoor_attribute',blank=True)    #脱贫属性

    offpoor_year=models.CharField(max_length=20,db_column='offpoor_year',blank=True)    #脱贫年度

    poor_attribute=models.CharField(max_length=30,db_column='poor_attribute',blank=True)    #贫困户属性

    poor_reason=models.CharField(max_length=30,db_column='poor_reason',blank=True)    #主要致贫原因

    danger_house=models.CharField(max_length=10,db_column='danger_house',blank=True)    #危房户

    water_safe=models.CharField(max_length=10,db_column='water_safe',blank=True)    #饮水安全

    water_hard=models.CharField(max_length=10,db_column='water_hard',blank=True)    #饮水困难

    is_minimum=models.CharField(max_length=30,db_column='is_minimum',blank=True)    #是否享受低保

    average_income=models.CharField(max_length=20,db_column='average_income',blank=True)    #人均纯收入

    telephone=models.CharField(max_length=20,db_column='telephone',blank=True)    #户主联系电话

    address=models.CharField(max_length=100,db_column='address',blank=True)    #住址

    year_date=models.CharField(max_length=10,db_column='year_date',blank=True)    #年度

    first_identify=models.CharField(max_length=50,db_column='first_identify',blank=True)    #首次识别时间

    help_people=models.CharField(max_length=50,db_column='help_people',blank=True)    #帮扶人员

    help_unit=models.CharField(max_length=50,db_column='help_unit',blank=True)    #帮扶单位

    help_way=models.CharField(max_length=50,db_column='help_way',blank=True)    #帮扶方式

    help_phone=models.CharField(max_length=100,db_column='help_phone',blank=True)    #帮扶人员电话号码

    house_classification=models.CharField(max_length=100,db_column='house_classification',blank=True)    #贫困户分类

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

    def __str__(self):
        return self.house_identifier

    class Meta:
        verbose_name = '贫困户'


#2
class PoorHouseAdditionalForm(models.Model):    #贫困户附加表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    past_village_identifier=models.CharField(max_length=30,db_column='past_village_identifier',blank=True)    #过去村编号

    now_village_identifier=models.CharField(max_length=30,db_column='now_village_identifier',blank=True)    #现在村编号

    house_identifier=models.CharField(max_length=30,db_column='house_identifier',blank=True)    #户编号

    householder_name=models.CharField(max_length=30,db_column='householder_name',blank=True)    #贫困户户主姓名

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #接受扶持款的卡的银行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #接受扶持款的卡的账号

    card_people=models.CharField(max_length=30,db_column='card_people',blank=True)    #卡主姓名

    people_id=models.CharField(max_length=20,db_column='people_id',blank=True)    #卡主身份证号

    householder_id=models.CharField(max_length=20,db_column='householder_id',blank=True)    #户主身份证号

    policy_number=models.CharField(max_length=30,db_column='policy_number',blank=True)    #应享政策编号

    policy_multiplier=models.CharField(max_length=20,db_column='policy_multiplier',blank=True)    #该政策编号乘以数量

    plan_money=models.CharField(max_length=20,db_column='plan_money',blank=True)    #应享政策编号对应的钱金额

    fact_money=models.CharField(max_length=20,db_column='fact_money',blank=True)    #实际享受到政策编号对应的钱金额

    date_year=models.CharField(max_length=20,db_column='date_year',blank=True)    #截止时间年

    date_month=models.CharField(max_length=20,db_column='date_month',blank=True)    #截止时间月

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

    subsidy_standard=models.CharField(max_length=300,db_column='subsidy_standard',blank=True)    #补助标准

    def __str__(self):
        return self.house_identifier


#1
class PoorPeopleDataForm(models.Model):    #贫困人口基本信息表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡（镇）

    house_identifier=models.CharField(max_length=30,db_column='house_identifier',blank=True)    #户编号

    people_identifier=models.CharField(max_length=30,db_column='people_identifier',blank=True)    #人编号

    people_name=models.CharField(max_length=30,db_column='people_name',blank=True)    #姓名

    people_id=models.CharField(max_length=20,db_column='people_id',blank=True)    #证件号码

    poor_attribute=models.CharField(max_length=30,db_column='poor_attribute',blank=True)    #贫困人口属性

    family_number=models.CharField(max_length=10,db_column='family_number',blank=True)    #人数

    people_relationship=models.CharField(max_length=20,db_column='people_relationship',blank=True)    #与户主的关系

    people_nation=models.CharField(max_length=20,db_column='people_nation',blank=True)    #民族

    education_degree=models.CharField(max_length=30,db_column='education_degree',blank=True)    #文化程度

    school_situation=models.CharField(max_length=30,db_column='school_situation',blank=True)    #在校生状况

    health_situation=models.CharField(max_length=30,db_column='health_situation',blank=True)    #健康状况

    labor_ability=models.CharField(max_length=30,db_column='labor_ability',blank=True)    #劳动技能

    work_time=models.CharField(max_length=10,db_column='work_time',blank=True)    #务工时间（月）

    join_medical=models.CharField(max_length=10,db_column='join_medical',blank=True)    #参加大病医疗

    offpoor_attribute=models.CharField(max_length=30,db_column='offpoor_attribute',blank=True)    #脱贫属性

    poor_reason=models.CharField(max_length=30,db_column='poor_reason',blank=True)    #主要致贫原因

    telephone=models.CharField(max_length=20,db_column='telephone',blank=True)    #联系电话

    address=models.CharField(max_length=100,db_column='address',blank=True)    #住址

    birth_date=models.CharField(max_length=30,db_column='birth_date',blank=True)    #出生日期

    is_five=models.CharField(max_length=30,db_column='is_five',blank=True)    #是否为五保户

    year_date=models.CharField(max_length=10,db_column='year_date',blank=True)    #年度

    first_identify=models.CharField(max_length=50,db_column='first_identify',blank=True)    #首次识别时间

    help_people=models.CharField(max_length=50,db_column='help_people',blank=True)    #帮扶人员

    help_unit=models.CharField(max_length=50,db_column='help_unit',blank=True)    #帮扶单位

    help_way=models.CharField(max_length=50,db_column='help_way',blank=True)    #帮扶方式

    help_phone=models.CharField(max_length=100,db_column='help_phone',blank=True)    #帮扶人员电话号码

    special_people=models.CharField(max_length=50,db_column='special_people',blank=True)    #特殊照顾人群

    people_classification=models.CharField(max_length=100,db_column='people_classification',blank=True)    #贫困人口分类

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

    offpoor_year=models.CharField(max_length=20,db_column='offpoor_year',blank=True)    #脱贫年度

    poorhouse_attribute=models.CharField(max_length=30,db_column='poorhouse_attribute',blank=True)    #贫困户属性

    def __str__(self):
        return self.people_identifier

    class Meta:
        verbose_name = '贫困人口'


#2
class PoorPeopleAdditionalForm(models.Model):    #贫困人口附加表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    house_identifier=models.CharField(max_length=30,db_column='house_identifier',blank=True)    #户编号

    people_identifier=models.CharField(max_length=30,db_column='people_identifier',blank=True)    #人编号

    people_id=models.CharField(max_length=20,db_column='people_id',blank=True)    #个人身份证号

    people_name=models.CharField(max_length=30,db_column='people_name',blank=True)    #贫困人口姓名

    householder_id=models.CharField(max_length=20,db_column='householder_id',blank=True)    #户主身份证号

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #接受扶持款的卡的银行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #接受扶持款的卡的账号

    card_people=models.CharField(max_length=30,db_column='card_people',blank=True)    #卡主姓名

    card_id=models.CharField(max_length=20,db_column='card_id',blank=True)    #卡主身份证号

    policy_number=models.CharField(max_length=30,db_column='policy_number',blank=True)    #应享政策编号

    policy_multiplier=models.CharField(max_length=20,db_column='policy_multiplier',blank=True)    #该政策编号乘以数量

    plan_money=models.CharField(max_length=20,db_column='plan_money',blank=True)    #应享政策编号对应的钱金额

    fact_money=models.CharField(max_length=20,db_column='fact_money',blank=True)    #实际享受到政策编号对应的钱金额

    date_year=models.CharField(max_length=20,db_column='date_year',blank=True)    #截止时间年

    date_month=models.CharField(max_length=20,db_column='date_month',blank=True)    #截止时间月

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

    subsidy_standard=models.CharField(max_length=300,db_column='subsidy_standard',blank=True)    #补助标准

    def __str__(self):
        return self.people_identifier


#1
class PolicyStaticForm(models.Model):    #政策静态表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    policy_number=models.CharField(max_length=30,db_column='policy_number',blank=True)    #政策编号

    policy_first_layer=models.CharField(max_length=100,db_column='policy_first_layer',blank=True)    #政策类型第一层

    policy_second_layer=models.CharField(max_length=100,db_column='policy_second_layer',blank=True)    #政策类型第二层

    policy_third_layer=models.CharField(max_length=100,db_column='policy_third_layer',blank=True)    #政策类型第三层

    subsidy_one=models.CharField(max_length=100,db_column='subsidy_one',blank=True)    #补助1

    subsidy_two=models.CharField(max_length=100,db_column='subsidy_two',blank=True)    #补助2

    subsidy_three=models.CharField(max_length=100,db_column='subsidy_three',blank=True)    #补助3

    subsidy_limit=models.CharField(max_length=100,db_column='subsidy_limit',blank=True)    #补助上限

    limit_condition=models.CharField(max_length=200,db_column='limit_condition',blank=True)    #限制条件

    policy_object=models.CharField(max_length=10,db_column='policy_object',blank=True)    #政策针对对象（村/户/人）

    implement_department=models.CharField(max_length=50,db_column='implement_department',blank=True)    #落实部门

    department_tag=models.CharField(max_length=5,db_column='department_tag',blank=True)    #区分相同落实部门的数据

    def __str__(self):
        return self.policy_number

    class Meta:
        verbose_name = '政策'


#1
class HelperDataForm(models.Model):    #帮扶人基本信息表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    unit_name=models.CharField('单位',max_length=50,db_column='unit_name',blank=True)    #帮扶人-单位名称

    helper_name=models.CharField('姓名',max_length=30,db_column='helper_name',blank=True)    #帮扶人-姓名

    helper_sex=models.CharField('性别',max_length=10,db_column='helper_sex',blank=True)    #帮扶人-性别

    helper_post=models.CharField('职务',max_length=50,db_column='helper_post',blank=True)    #帮扶人-职务

    helper_type=models.CharField('类型',max_length=30,db_column='helper_type',blank=True)    #帮扶人-队长/队员/结对帮扶责任人

    poor_town=models.CharField('乡镇',max_length=50,db_column='poor_town',blank=True)    #贫困户-乡镇

    past_administrative_village=models.CharField(max_length=50,db_column='past_administrative_village',blank=True)    #贫困户-行政村曾用名

    now_administrative_village=models.CharField('行政村',max_length=50,db_column='now_administrative_village',blank=True)    #贫困户-行政村现用名

    past_village_identifier=models.CharField(max_length=30,db_column='past_village_identifier',blank=True)    #贫困户-过去村编号

    now_village_identifier=models.CharField('村编号',max_length=30,db_column='now_village_identifier',blank=True)    #贫困户-现在村编号

    poor_home=models.CharField('户数',max_length=20,db_column='poor_home',blank=True)    #贫困户-户数

    poor_name=models.CharField('户主姓名',max_length=30,db_column='poor_name',blank=True)    #贫困户-户主姓名

    poor_group=models.CharField(max_length=20,db_column='poor_group',blank=True)    #贫困户-户主姓名-组别

    household_identifier=models.CharField(max_length=20,db_column='household_identifier',blank=True)    #贫困户-户主身份证号码

    office_phone=models.CharField(max_length=100,db_column='office_phone',blank=True)    #帮扶干部电话-办公电话

    mobile_phone=models.CharField('手机',max_length=100,db_column='mobile_phone',blank=True)    #帮扶干部电话-手机

    year_date=models.CharField('年度',max_length=10,db_column='year_date',blank=True)    #年度

    helper_tag=models.CharField(max_length=5,db_column='helper_tag',blank=True)    #区分相同帮扶人的数据

    helper_id=models.CharField(max_length=20,db_column='helper_id',blank=True)    #帮扶人身份证号码

    def __str__(self):
        return self.helper_name

    class Meta:
        verbose_name = '帮扶人'


class IndustryEnterpriseDataForm(models.Model):    #人社局（就业）_产业扶起来.企业.吸纳就业补贴_落实工作反馈表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #企业归属乡镇

    administrative_village=models.CharField(max_length=50,db_column='administrative_village',blank=True)    #企业归属行政村

    ascription_group=models.CharField(max_length=20,db_column='ascription_group',blank=True)    #企业归属组

    enterprise_name=models.CharField(max_length=100,db_column='enterprise_name',blank=True)    #企业全称

    management_address=models.CharField(max_length=200,db_column='management_address',blank=True)    #经营地址

    institution_code=models.CharField(max_length=100,db_column='institution_code',blank=True)    #统一社会信用代码或组织机构代码

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #收款银行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #收款账号

    subsidy_name=models.CharField(max_length=200,db_column='subsidy_name',blank=True)    #发放补贴的名称

    subsidy_standard=models.CharField(max_length=300,db_column='subsidy_standard',blank=True)    #补助标准

    subsidy_multiplier=models.CharField(max_length=20,db_column='subsidy_multiplier',blank=True)    #补助数量（即补助标准的乘数）

    subsidy_limit=models.CharField(max_length=100,db_column='subsidy_limit',blank=True)    #本期补助上限（元）

    plan_subsidy=models.CharField(max_length=100,db_column='plan_subsidy',blank=True)    #应补助金额（元）

    fact_subsidy=models.CharField(max_length=100,db_column='fact_subsidy',blank=True)    #实际补助金额（元）

    grant_date=models.CharField(max_length=30,db_column='grant_date',blank=True)    #发放时间（年月格式为201809）

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

    def __str__(self):
        return self.enterprise_name


class IndustryAgritainmentDataForm(models.Model):    #人社局（就业）_产业扶起来.农家乐.吸纳就业补贴_落实工作反馈表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #归属乡镇

    administrative_village=models.CharField(max_length=50,db_column='administrative_village',blank=True)    #归属行政村

    ascription_group=models.CharField(max_length=20,db_column='ascription_group',blank=True)    #归属组

    agritainment_name=models.CharField(max_length=100,db_column='agritainment_name',blank=True)    #发放补贴的农家乐名称

    agritainment_holder=models.CharField(max_length=30,db_column='agritainment_holder',blank=True)    #该农家乐业主姓名

    agritainment_id=models.CharField(max_length=20,db_column='agritainment_id',blank=True)    #该农家乐业主身份证号码

    subsidy_standard=models.CharField(max_length=300,db_column='subsidy_standard',blank=True)    #补助标准

    subsidy_multiplier=models.CharField(max_length=20,db_column='subsidy_multiplier',blank=True)    #补助数量（即补助标准的乘数）

    subsidy_limit=models.CharField(max_length=100,db_column='subsidy_limit',blank=True)    #本期补助上限（元）

    plan_subsidy=models.CharField(max_length=100,db_column='plan_subsidy',blank=True)    #应补助金额（元）

    fact_subsidy=models.CharField(max_length=100,db_column='fact_subsidy',blank=True)    #实际补助金额（元）

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #收款银行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #收款账号

    receivables_name=models.CharField(max_length=30,db_column='receivables_name',blank=True)    #收款人名字

    receivables_id=models.CharField(max_length=20,db_column='receivables_id',blank=True)    #收款人身份证号码（或者收款行政村编号）

    grant_date=models.CharField(max_length=30,db_column='grant_date',blank=True)    #发放时间（年月格式为201809）

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

    def __str__(self):
        return self.agritainment_name


class IndustryFinanceDataForm(models.Model):    #金融办_产业扶起来_扶贫小额信贷_经营主体_落实工作反馈表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #银行名称

    management_name=models.CharField(max_length=30,db_column='management_name',blank=True)    #经营主体名称

    management_id=models.CharField(max_length=20,db_column='management_id',blank=True)    #经营主体身份证号

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡镇（区）

    administrative_village=models.CharField(max_length=50,db_column='administrative_village',blank=True)    #行政村

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #带动户数

    loan_money=models.CharField(max_length=20,db_column='loan_money',blank=True)    #贷款金额（万元）

    loan_begin=models.CharField(max_length=30,db_column='loan_begin',blank=True)    #贷款起始日期

    loan_end=models.CharField(max_length=30,db_column='loan_end',blank=True)    #贷款到期日期

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

    def __str__(self):
        return self.management_name