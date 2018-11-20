from django.db import models


# Create your models here.


#1 “产业扶起来”
class IndustryLedgerForm(models.Model):    #“产业扶起来”政策落实调查汇总表(台账表)

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡镇（区）

    administrative_village=models.CharField(max_length=50,db_column='administrative_village',blank=True)    #行政村

    householder_name=models.CharField(max_length=30,db_column='householder_name',blank=True)    #户主姓名

    householder_id=models.CharField(max_length=20,db_column='householder_id',blank=True)    #户主身份证号

    family_number=models.CharField(max_length=10,db_column='family_number',blank=True)    #家庭人数

    project_category=models.CharField(max_length=50,db_column='project_category',blank=True)    #发展项目-类别

    project_name=models.CharField(max_length=50,db_column='project_name',blank=True)    #发展项目-名称

    project_scale=models.CharField(max_length=50,db_column='project_scale',blank=True)    #发展项目-规模

    project_standard=models.CharField(max_length=50,db_column='project_standard',blank=True)    #发展项目-拟定享受标准

    cardholder_name=models.CharField(max_length=30,db_column='cardholder_name',blank=True)    #卡主-姓名

    cardholder_relationship=models.CharField(max_length=20,db_column='cardholder_relationship',blank=True)    #卡主-与户主的关系

    cardholder_id=models.CharField(max_length=20,db_column='cardholder_id',blank=True)    #卡主-身份证号

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #开户行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #银行卡号

    def __str__(self):
        return self.town_name


#2 “教育扶起来”
class EducationLedgerForm(models.Model):    #“教育扶起来”政策落实调查汇总表（台账表）

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡镇（区）

    administrative_village=models.CharField(max_length=50,db_column='administrative_village',blank=True)    #行政村

    householder_name=models.CharField(max_length=30,db_column='householder_name',blank=True)    #户主-姓名

    householder_id=models.CharField(max_length=20,db_column='householder_id',blank=True)    #户主-身份证号

    student_name=models.CharField(max_length=30,db_column='student_name',blank=True)    #学生-姓名

    student_relationship=models.CharField(max_length=20,db_column='student_relationship',blank=True)    #学生-与户主的关系

    student_id=models.CharField(max_length=20,db_column='student_id',blank=True)    #学生-身份证号

    student_school=models.CharField(max_length=50,db_column='student_school',blank=True)    #学生-学校

    student_agegroup=models.CharField(max_length=50,db_column='student_agegroup',blank=True)    #学生—年龄段

    subsidy_standard=models.CharField(max_length=50,db_column='subsidy_standard',blank=True)    #拟补助标准

    cardholder_name=models.CharField(max_length=30,db_column='cardholder_name',blank=True)    #卡主-姓名

    cardholder_relationship=models.CharField(max_length=20,db_column='cardholder_relationship',blank=True)    #卡主-与户主的关系

    cardholder_id=models.CharField(max_length=20,db_column='cardholder_id',blank=True)    #卡主-身份证号

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #开户行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #银行卡号

    def __str__(self):
        return self.town_name


#3 “生活保起来”
class LifeMinimumLedgerForm(models.Model):    #“生活保起来”政策落实情况统计表（低保台账表）

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡镇（区）

    administrative_village=models.CharField(max_length=50,db_column='administrative_village',blank=True)    #行政村

    householder_name=models.CharField(max_length=30,db_column='householder_name',blank=True)    #户主姓名

    householder_id=models.CharField(max_length=20,db_column='householder_id',blank=True)    #身份证号

    family_number=models.CharField(max_length=10,db_column='family_number',blank=True)    #家庭人口数

    beneficiary_name=models.CharField(max_length=30,db_column='beneficiary_name',blank=True)    #享受低保人-姓名

    beneficiary_id=models.CharField(max_length=20,db_column='beneficiary_id',blank=True)    #享受低保人-身份证号

    beneficiary_standard=models.CharField(max_length=50,db_column='beneficiary_standard',blank=True)    #享受低保人-年标准

    cardholder_name=models.CharField(max_length=30,db_column='cardholder_name',blank=True)    #卡主姓名

    cardholder_id=models.CharField(max_length=20,db_column='cardholder_id',blank=True)    #卡主身份证号

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #开户行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #银行卡号

    def __str__(self):
        return self.town_name


#4 “生活保起来”
class LifeOrphanLedgerForm(models.Model):    #“生活保起来”政策落实情况统计表（孤儿台账表）

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡镇（区）

    administrative_village=models.CharField(max_length=50,db_column='administrative_village',blank=True)    #行政村

    householder_name=models.CharField(max_length=30,db_column='householder_name',blank=True)    #户主姓名

    householder_id=models.CharField(max_length=20,db_column='householder_id',blank=True)    #身份证号

    family_number=models.CharField(max_length=10,db_column='family_number',blank=True)    #家庭人口数

    orphan_name=models.CharField(max_length=30,db_column='orphan_name',blank=True)    #孤儿-姓名

    orphan_id=models.CharField(max_length=20,db_column='orphan_id',blank=True)    #孤儿-身份证号

    orphan_type=models.CharField(max_length=5,db_column='orphan_type',blank=True)    #孤儿-类型（集中/分散）

    orphan_standard=models.CharField(max_length=50,db_column='orphan_standard',blank=True)    #孤儿-标准

    cardholder_name=models.CharField(max_length=30,db_column='cardholder_name',blank=True)    #卡主姓名

    cardholder_id=models.CharField(max_length=20,db_column='cardholder_id',blank=True)    #卡主身份证号

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #开户行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #银行卡号

    def __str__(self):
        return self.town_name


#5 “生活保起来”
class LifeGuaranteeLedgerForm(models.Model):    #“生活保起来”政策落实情况统计表（五保台账表）

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡镇（区）

    administrative_village=models.CharField(max_length=50,db_column='administrative_village',blank=True)    #行政村

    householder_name=models.CharField(max_length=30,db_column='householder_name',blank=True)    #户主姓名

    householder_id=models.CharField(max_length=20,db_column='householder_id',blank=True)    #身份证号

    family_number=models.CharField(max_length=10,db_column='family_number',blank=True)    #家庭人口数

    beneficiary_name=models.CharField(max_length=30,db_column='beneficiary_name',blank=True)    #享受五保人-姓名

    beneficiary_id=models.CharField(max_length=20,db_column='beneficiary_id',blank=True)    #享受五保人-身份证号

    beneficiary_type=models.CharField(max_length=5,db_column='beneficiary_type',blank=True)    #享受五保人-类型（集中/分散）

    beneficiary_standard=models.CharField(max_length=50,db_column='beneficiary_standard',blank=True)    #享受五保人-标准

    cardholder_name=models.CharField(max_length=30,db_column='cardholder_name',blank=True)    #卡主姓名

    cardholder_id=models.CharField(max_length=20,db_column='cardholder_id',blank=True)    #卡主身份证号

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #开户行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #银行卡号

    def __str__(self):
        return self.town_name


#6 “医疗保起来”
class MedicalLedgerForm(models.Model):    #“医疗保起来”政策落实情况统计表（台账表）

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡镇（区）

    administrative_village=models.CharField(max_length=50,db_column='administrative_village',blank=True)    #行政村

    householder_name=models.CharField(max_length=30,db_column='householder_name',blank=True)    #户主姓名

    patient_name=models.CharField(max_length=30,db_column='patient_name',blank=True)    #患者-姓名

    patient_id=models.CharField(max_length=20,db_column='patient_id',blank=True)    #患者-身份证号

    medical_institution=models.CharField(max_length=50,db_column='medical_institution',blank=True)    #医疗机构名称

    visit_type=models.CharField(max_length=50,db_column='visit_type',blank=True)    #就诊类型

    disease_name=models.CharField(max_length=50,db_column='disease_name',blank=True)    #疾病名称

    hospital_time=models.CharField(max_length=50,db_column='hospital_time',blank=True)    #入院时间

    settlement_date=models.CharField(max_length=50,db_column='settlement_date',blank=True)    #结算日期

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #本次总费用①=②+③+④

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付②-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付②-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付②-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付②-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付②-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担③

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费④

    def __str__(self):
        return self.town_name


#7 “住房保起来”
class HousingLedgerForm(models.Model):    #“住房保起来”政策落实情况统计表（台账表）

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    town_name=models.CharField(max_length=50,db_column='town_name',blank=True)    #乡镇（区）

    administrative_village=models.CharField(max_length=50,db_column='administrative_village',blank=True)    #行政村

    householder_name=models.CharField(max_length=30,db_column='householder_name',blank=True)    #户主-姓名

    householder_id=models.CharField(max_length=20,db_column='householder_id',blank=True)    #户主-身份证号

    family_number=models.CharField(max_length=10,db_column='family_number',blank=True)    #家庭人数

    implementation_year=models.CharField(max_length=30,db_column='implementation_year',blank=True)    #实施年度

    gather_proportion=models.CharField(max_length=20,db_column='gather_proportion',blank=True)    #易地扶贫搬迁安置-集中安置-建筑面积（m²）

    gather_location=models.CharField(max_length=50,db_column='gather_location',blank=True)    #易地扶贫搬迁安置-集中安置-安置地点

    gather_whether=models.CharField(max_length=10,db_column='gather_whether',blank=True)    #易地扶贫搬迁安置-集中安置-是否入住

    nearby_proportion=models.CharField(max_length=20,db_column='nearby_proportion',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-建筑面积（m²）

    nearby_location=models.CharField(max_length=50,db_column='nearby_location',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置地点

    nearby_whether=models.CharField(max_length=10,db_column='nearby_whether',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-是否入住

    city_proportion=models.CharField(max_length=20,db_column='city_proportion',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-建筑面积（m²）

    city_location=models.CharField(max_length=50,db_column='city_location',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-安置地点

    city_whether=models.CharField(max_length=10,db_column='city_whether',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-是否入住

    danger_rank=models.CharField(max_length=5,db_column='danger_rank',blank=True)    #危房改造-危房等级（C级/D级）

    danger_batch=models.CharField(max_length=10,db_column='danger_batch',blank=True)    #危房改造-审定危改批次（第一批/第二批）

    danger_standard=models.CharField(max_length=50,db_column='danger_standard',blank=True)    #危房改造-补助标准

    danger_situation=models.CharField(max_length=50,db_column='danger_situation',blank=True)    #危房改造-进展情况

    danger_acceptance=models.CharField(max_length=10,db_column='danger_acceptance',blank=True)    #危房改造-是否验收

    def __str__(self):
        return self.town_name


#1 “产业扶起来”
class PasturageIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-产业-畜牧

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#2 “产业扶起来”
class ForestryIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-产业-林业

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#3 “产业扶起来”
class AgricultureIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-产业-农业

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#4 “产业扶起来”
class AquacultureIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-产业-水产

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#5 “产业扶起来”
class CommerceIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-农村电商

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#6 “产业扶起来”
class EntertainmentIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-农家乐

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#7 “产业扶起来”
class TrainIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-培训人次

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#8 “产业扶起来”
class OneIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-一大员

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#9 “产业扶起来”
class TwoIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-二大员

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#10 “产业扶起来”
class ThreeIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-三大员

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#11 “产业扶起来”
class FourIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-四大员

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#12 “产业扶起来”
class FiveIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-五大员

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#13 “产业扶起来”
class SixIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-六大员

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#14 “产业扶起来”
class HelpIndustryOutputForm(models.Model):    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-其他方式帮助就业

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    people_number=models.CharField(max_length=20,db_column='people_number',blank=True)    #人数

    breeding_type=models.CharField(max_length=50,db_column='breeding_type',blank=True)    #特色种养业-申报类型（畜牧、林业、农业、水产...）

    breeding_class=models.CharField(max_length=30,db_column='breeding_class',blank=True)    #特色种养业-类别（油茶、青茶、养牛、养猪、养鸡、养鱼）

    breeding_scale=models.CharField(max_length=50,db_column='breeding_scale',blank=True)    #特色种养业-申报规模

    breeding_home=models.CharField(max_length=20,db_column='breeding_home',blank=True)    #特色种养业-户数

    breeding_bankroll=models.CharField(max_length=20,db_column='breeding_bankroll',blank=True)    #特色种养业-目前落实资金（元）

    tourism_home=models.CharField(max_length=20,db_column='tourism_home',blank=True)    #特色旅游业-户数

    tourism_people=models.CharField(max_length=20,db_column='tourism_people',blank=True)    #特色旅游业-人数

    tourism_bankroll=models.CharField(max_length=20,db_column='tourism_bankroll',blank=True)    #特色旅游业-目前落实资金（元）

    internet_home=models.CharField(max_length=20,db_column='internet_home',blank=True)    #“互联网+扶贫”-户数

    internet_people=models.CharField(max_length=20,db_column='internet_people',blank=True)    #“互联网+扶贫”-人数

    internet_bankroll=models.CharField(max_length=20,db_column='internet_bankroll',blank=True)    #“互联网+扶贫”-目前落实资金（元）

    train_type=models.CharField(max_length=50,db_column='train_type',blank=True)    #贫困人口就业-培训-类型

    train_people=models.CharField(max_length=20,db_column='train_people',blank=True)    #贫困人口就业-培训-人次

    enterprise_number=models.CharField(max_length=20,db_column='enterprise_number',blank=True)    #贫困人口就业-企业带动就业-企业个数

    enterprise_people=models.CharField(max_length=20,db_column='enterprise_people',blank=True)    #贫困人口就业-企业带动就业-带动贫困户人数

    enterprise_allowance=models.CharField(max_length=20,db_column='enterprise_allowance',blank=True)    #贫困人口就业-企业带动就业-补贴人数

    six_type=models.CharField(max_length=50,db_column='six_type',blank=True)    #贫困人口就业-六大员-类型

    six_home=models.CharField(max_length=20,db_column='six_home',blank=True)    #贫困人口就业-六大员-贫困户户数

    six_people=models.CharField(max_length=20,db_column='six_people',blank=True)    #贫困人口就业-六大员-贫困户人数

    six_bankroll=models.CharField(max_length=20,db_column='six_bankroll',blank=True)    #贫困人口就业-六大员-目前落实资金（元）

    other_home=models.CharField(max_length=20,db_column='other_home',blank=True)    #贫困人口就业-其他方式帮助就业-户数

    other_people=models.CharField(max_length=20,db_column='other_people',blank=True)    #贫困人口就业-其他方式帮助就业-人数

    def __str__(self):
        return self.date


#1 “产业扶起来”
class ChengGuanMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-城关镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#2 “产业扶起来”
class DaXinMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-大新镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#3 “产业扶起来”
class DongXinMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-东新乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#4 “产业扶起来”
class FangFanMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-芳畈镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#5 “产业扶起来”
class FengDianMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-丰店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#6 “产业扶起来”
class GaoDianMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-高店乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#7 “产业扶起来”
class GaoTieMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-高铁新区

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#8 “产业扶起来”
class HeKouMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-河口镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#9 “产业扶起来”
class HuangZhanMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-黄站镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#10 “产业扶起来”
class KaiFaMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-开发区

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#11 “产业扶起来”
class LiuJiMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-刘集镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#12 “产业扶起来”
class LvWangMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-吕王镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#13 “产业扶起来”
class PengDianMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-彭店乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#14 “产业扶起来”
class SanLiMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-三里城镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#15 “产业扶起来”
class SiGuMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-四姑镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#16 “产业扶起来”
class WuFengMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-悟峰山管委会

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#17 “产业扶起来”
class XiaDianMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-夏店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#18 “产业扶起来”
class XinChengMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-新城镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#19 “产业扶起来”
class XuanHuaMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-宣化店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#20 “产业扶起来”
class YangPingMicroOutputForm(models.Model):    #扶贫小额信贷工作进展情况统计表（输出表）-阳平镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    poverty_number=models.CharField(max_length=20,db_column='poverty_number',blank=True)    #贫困户直贷-贫困户户数

    poverty_loan=models.CharField(max_length=20,db_column='poverty_loan',blank=True)    #贫困户直贷-贷款金额

    poverty_date=models.CharField(max_length=50,db_column='poverty_date',blank=True)    #贫困户直贷-发放贷款日期

    poverty_bank=models.CharField(max_length=50,db_column='poverty_bank',blank=True)    #贫困户直贷-贷款银行

    management_number=models.CharField(max_length=20,db_column='management_number',blank=True)    #经营主体贷款-经营主体贷款-个数

    management_loan=models.CharField(max_length=20,db_column='management_loan',blank=True)    #经营主体贷款-经营主体贷款-总额

    management_pattern=models.CharField(max_length=50,db_column='management_pattern',blank=True)    #经营主体贷款-经营主体贷款-贷款方式

    management_term=models.CharField(max_length=50,db_column='management_term',blank=True)    #经营主体贷款-经营主体贷款-贷款期限

    management_date=models.CharField(max_length=50,db_column='management_date',blank=True)    #经营主体贷款-经营主体贷款-发放贷款日期

    management_bank=models.CharField(max_length=50,db_column='management_bank',blank=True)    #经营主体贷款-经营主体贷款-承贷银行

    lead_pattern=models.CharField(max_length=50,db_column='lead_pattern',blank=True)    #经营主体贷款-带动贫困户-就业帮扶方式

    lead_mode=models.CharField(max_length=50,db_column='lead_mode',blank=True)    #经营主体贷款-带动贫困户-现金给付方式

    lead_home=models.CharField(max_length=20,db_column='lead_home',blank=True)    #经营主体贷款-带动贫困户-户数

    def __str__(self):
        return self.date


#1 “教育扶起来”
class ChengGuanEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-城关镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#2 “教育扶起来”
class DaXinEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-大新镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#3 “教育扶起来”
class DongXinEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-东新乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#4 “教育扶起来”
class FangFanEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-芳畈镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#5 “教育扶起来”
class FengDianEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-丰店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#6 “教育扶起来”
class GaoDianEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-高店乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#7 “教育扶起来”
class GaoTieEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-高铁新区

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#8 “教育扶起来”
class HeKouEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-河口镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#9 “教育扶起来”
class HuangZhanEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-黄站镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#10 “教育扶起来”
class KaiFaEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-开发区

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#11 “教育扶起来”
class LiuJiEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-刘集镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#12 “教育扶起来”
class LvWangEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-吕王镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#13 “教育扶起来”
class PengDianEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-彭店乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#14 “教育扶起来”
class SanLiEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-三里城镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#15 “教育扶起来”
class SiGuEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-四姑镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#16 “教育扶起来”
class WuFengEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-悟峰山管委会

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#17 “教育扶起来”
class XiaDianEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-夏店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#18 “教育扶起来”
class XinChengEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-新城镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#19 “教育扶起来”
class XuanHuaEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-宣化店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#20 “教育扶起来”
class YangPingEducationOutputForm(models.Model):    #“教育扶起来”政策落实情况统计表（输出表）-阳平镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    student_number=models.CharField(max_length=20,db_column='student_number',blank=True)    #学生数

    card_time=models.CharField(max_length=50,db_column='card_time',blank=True)    #打卡时间

    preschool_progress=models.CharField(max_length=50,db_column='preschool_progress',blank=True)    #学前教育（3200元/生/年）-进展

    preschool_capital=models.CharField(max_length=20,db_column='preschool_capital',blank=True)    #学前教育（3200元/生/年）-落实资金

    primary_progress=models.CharField(max_length=50,db_column='primary_progress',blank=True)    #小学教育（4400元/生/年）-进展

    primary_capital=models.CharField(max_length=20,db_column='primary_capital',blank=True)    #小学教育（4400元/生/年）-落实资金

    middle_progress=models.CharField(max_length=50,db_column='middle_progress',blank=True)    #初中教育（5200元/生/年）-进展

    middle_capital=models.CharField(max_length=20,db_column='middle_capital',blank=True)    #初中教育（5200元/生/年）-落实资金

    high_progress=models.CharField(max_length=50,db_column='high_progress',blank=True)    #高中/中职（5200元/生/年）-进展

    high_capital=models.CharField(max_length=20,db_column='high_capital',blank=True)    #高中/中职（5200元/生/年）-落实资金

    college_progress=models.CharField(max_length=50,db_column='college_progress',blank=True)    #大学（5200元/生/年）-进展

    college_capital=models.CharField(max_length=20,db_column='college_capital',blank=True)    #大学（5200元/生/年）-落实资金

    def __str__(self):
        return self.date


#1 “生活保起来”
class CountyLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-全县合计

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#2 “生活保起来”
class ChengGuanLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-城关镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#3 “生活保起来”
class DaXinLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-大新镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#4 “生活保起来”
class DongXinLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-东新乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#5 “生活保起来”
class FangFanLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-芳畈镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#6 “生活保起来”
class FengDianLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-丰店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#7 “生活保起来”
class GaoDianLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-高店乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#8 “生活保起来”
class GaoTieLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-高铁新区

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#9 “生活保起来”
class HeKouLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-河口镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#10 “生活保起来”
class HuangZhanLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-黄站镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#11 “生活保起来”
class KaiFaLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-开发区

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#12 “生活保起来”
class LiuJiLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-刘集镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#13 “生活保起来”
class LvWangLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-吕王镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#14 “生活保起来”
class PengDianLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-彭店乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#15 “生活保起来”
class SanLiLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-三里城镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#16 “生活保起来”
class SiGuLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-四姑镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#17 “生活保起来”
class WuFengLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-悟峰山管委会

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#18 “生活保起来”
class XiaDianLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-夏店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#19 “生活保起来”
class XinChengLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-新城镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#20 “生活保起来”
class XuanHuaLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-宣化店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#21 “生活保起来”
class YangPingLifeOutputForm(models.Model):    #“生活保起来”政策落实情况统计表（输出表）-阳平镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    fivefocus_people=models.CharField(max_length=20,db_column='fivefocus_people',blank=True)    #五保-集中供养-人数

    fivefocus_capital=models.CharField(max_length=20,db_column='fivefocus_capital',blank=True)    #五保-集中供养-落实资金

    fivedisperse_people=models.CharField(max_length=20,db_column='fivedisperse_people',blank=True)    #五保-分散供养-人数

    fivedisperse_capital=models.CharField(max_length=20,db_column='fivedisperse_capital',blank=True)    #五保-分散供养-落实资金

    orphanfocus_people=models.CharField(max_length=20,db_column='orphanfocus_people',blank=True)    #孤儿-集中-人数

    orphanfocus_capital=models.CharField(max_length=20,db_column='orphanfocus_capital',blank=True)    #孤儿-集中-落实资金

    orphandisperse_people=models.CharField(max_length=20,db_column='orphandisperse_people',blank=True)    #孤儿-分散-人数

    orphandisperse_capital=models.CharField(max_length=20,db_column='orphandisperse_capital',blank=True)    #孤儿-分散-落实资金

    minimum_home=models.CharField(max_length=20,db_column='minimum_home',blank=True)    #低保-户数

    minimum_people=models.CharField(max_length=20,db_column='minimum_people',blank=True)    #低保-人数

    minimum_capital=models.CharField(max_length=20,db_column='minimum_capital',blank=True)    #低保-落实资金

    def __str__(self):
        return self.date


#1 “医疗保起来”
class ChengGuanMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-城关镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#2 “医疗保起来”
class DaXinMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-大新镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#3 “医疗保起来”
class DongXinMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-东新乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#4 “医疗保起来”
class FangFanMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-芳畈镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#5 “医疗保起来”
class FengDianMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-丰店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#6 “医疗保起来”
class GaoDianMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-高店乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#7 “医疗保起来”
class GaoTieMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-高铁新区

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#8 “医疗保起来”
class HeKouMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-河口镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#9 “医疗保起来”
class HuangZhanMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-黄站镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#10 “医疗保起来”
class KaiFaMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-开发区

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#11 “医疗保起来”
class LiuJiMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-刘集镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#12 “医疗保起来”
class LvWangMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-吕王镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#13 “医疗保起来”
class PengDianMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-彭店乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#14 “医疗保起来”
class SanLiMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-三里城镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#15 “医疗保起来”
class SiGuMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-四姑镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#16 “医疗保起来”
class WuFengMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-悟峰山管委会

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#17 “医疗保起来”
class XiaDianMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-夏店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#18 “医疗保起来”
class XinChengMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-新城镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#19 “医疗保起来”
class XuanHuaMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-宣化店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#20 “医疗保起来”
class YangPingMedicalOutputForm(models.Model):    #“医疗保起来”政策落实情况统计表（输出表）-阳平镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    home_number=models.CharField(max_length=20,db_column='home_number',blank=True)    #户数

    treat_people=models.CharField(max_length=20,db_column='treat_people',blank=True)    #治疗人次

    total_cost=models.CharField(max_length=20,db_column='total_cost',blank=True)    #总费用

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位-体统筹支付-总额

    payment_reimbursement=models.CharField(max_length=20,db_column='payment_reimbursement',blank=True)    #四位一体统筹支付-基本医疗报销

    payment_indemnity=models.CharField(max_length=20,db_column='payment_indemnity',blank=True)    #四位-体统筹支付-大病保险赔付

    payment_defrayal=models.CharField(max_length=20,db_column='payment_defrayal',blank=True)    #四位-体统筹支付-民政救助支付

    payment_insurance=models.CharField(max_length=20,db_column='payment_insurance',blank=True)    #四位-体统筹支付-大病补充保险

    institution_undertake=models.CharField(max_length=20,db_column='institution_undertake',blank=True)    #医疗机构超范围承担

    personal_cost=models.CharField(max_length=20,db_column='personal_cost',blank=True)    #个人自费

    def __str__(self):
        return self.date


#1 “住房保起来”
class CountyHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-全县合计

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#2 “住房保起来”
class ChengGuanHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-城关镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#3 “住房保起来”
class DaXinHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-大新镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#4 “住房保起来”
class DongXinHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-东新乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#5 “住房保起来”
class FangFanHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-芳畈镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#6 “住房保起来”
class FengDianHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-丰店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#7 “住房保起来”
class GaoDianHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-高店乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#8 “住房保起来”
class GaoTieHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-高铁新区

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#9 “住房保起来”
class HeKouHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-河口镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#10 “住房保起来”
class HuangZhanHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-黄站镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#11 “住房保起来”
class KaiFaHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-开发区

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#12 “住房保起来”
class LiuJiHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-刘集镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#13 “住房保起来”
class LvWangHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-吕王镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#14 “住房保起来”
class PengDianHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-彭店乡

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#15 “住房保起来”
class SanLiHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-三里城镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#16 “住房保起来”
class SiGuHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-四姑镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#17 “住房保起来”
class WuFengHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-悟峰山管委会

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#18 “住房保起来”
class XiaDianHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-夏店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#19 “住房保起来”
class XinChengHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-新城镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#20 “住房保起来”
class XuanHuaHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-宣化店镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#21 “住房保起来”
class YangPingHousingOutputForm(models.Model):    #“住房保起来”政策落实情况统计表（输出表）-阳平镇

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    date=models.CharField(max_length=50,db_column='date',blank=True)    #日期

    gather_settlement=models.CharField(max_length=20,db_column='gather_settlement',blank=True)    #易地扶贫搬迁安置-集中安置-安置点个数

    gather_home=models.CharField(max_length=20,db_column='gather_home',blank=True)    #易地扶贫搬迁安置-集中安置-规划户数

    gather_family=models.CharField(max_length=20,db_column='gather_family',blank=True)    #易地扶贫搬迁安置-集中安置-入住户数

    nearby_settlement=models.CharField(max_length=20,db_column='nearby_settlement',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-安置点个数

    nearby_home=models.CharField(max_length=20,db_column='nearby_home',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-规划户数

    nearby_family=models.CharField(max_length=20,db_column='nearby_family',blank=True)    #易地扶贫搬迁安置-分散安置-就近就地安置-入住户数

    city_plan=models.CharField(max_length=20,db_column='city_plan',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-规划户数

    city_implement=models.CharField(max_length=20,db_column='city_implement',blank=True)    #易地扶贫搬迁安置-分散安置-进城购房-落实户数

    dangerc_home=models.CharField(max_length=20,db_column='dangerc_home',blank=True)    #危房改造-危房等级（C级/D级）-C级-户数

    dangerc_capital=models.CharField(max_length=20,db_column='dangerc_capital',blank=True)    #危房改造-危房等级（C级/D级）-C级-补助资金

    dangerd_home=models.CharField(max_length=20,db_column='dangerd_home',blank=True)    #危房改造-危房等级（C级/D级）-D级-户数

    dangerd_capital=models.CharField(max_length=20,db_column='dangerd_capital',blank=True)    #危房改造-危房等级（C级/D级）-D级-补助资金

    danger_plan=models.CharField(max_length=20,db_column='danger_plan',blank=True)    #危房改造-规划户数

    danger_implement=models.CharField(max_length=20,db_column='danger_implement',blank=True)    #危房改造-已验收户数

    def __str__(self):
        return self.date


#1
class FlexibleLedgerForm(models.Model):    #灵活台账表类型

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    coarse_class=models.CharField(max_length=50,db_column='coarse_class',blank=True)    #粗类（产业扶起来、教育扶起来、...）

    subdivided_capacitor=models.CharField(max_length=1000,db_column='subdivided_capacitor',blank=True)    #细类（“产业扶起来”政策落实调查汇总表、“教育扶起来”政策落实调查汇总表、...）

    def __str__(self):
        return self.coarse_class


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

    village_tag=models.CharField(max_length=10,db_column='village_tag',blank=True)    #区分合并后行政村名称相同的数据

    town_tag=models.CharField(max_length=10,db_column='town_tag',blank=True)    #区分乡镇名称相同的数据

    def __str__(self):
        return self.town_name


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

    date=models.CharField(max_length=50,db_column='date',blank=True)    #截止时间

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

    def __str__(self):
        return self.now_village_identifier


#1
class PoorHouseDataForm(models.Model):    #贫困户基本信息表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    past_village_identifier=models.CharField(max_length=30,db_column='past_village_identifier',blank=True)    #过去村编号

    now_village_identifier=models.CharField(max_length=30,db_column='now_village_identifier',blank=True)    #现在村编号

    house_identifier=models.CharField(max_length=30,db_column='house_identifier',blank=True)    #户编号

    house_group=models.CharField(max_length=20,db_column='house_group',blank=True)    #所在组

    householder_identifier=models.CharField(max_length=30,db_column='householder_identifier',blank=True)    #户主个人编号

    householder_name=models.CharField(max_length=30,db_column='householder_name',blank=True)    #户主姓名

    householder_id=models.CharField(max_length=20,db_column='householder_id',blank=True)    #户主身份证号

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

    average_income=models.CharField(max_length=20,db_column='average_income',blank=True)    #人均纯收入

    telephone=models.CharField(max_length=20,db_column='telephone',blank=True)    #户主联系电话

    address=models.CharField(max_length=100,db_column='address',blank=True)    #住址

    is_minimum=models.CharField(max_length=30,db_column='is_minimum',blank=True)    #是否享受低保

    year_date=models.CharField(max_length=10,db_column='year_date',blank=True)    #年度

    first_identify=models.CharField(max_length=50,db_column='first_identify',blank=True)    #首次识别时间

    help_people=models.CharField(max_length=50,db_column='help_people',blank=True)    #帮扶人员

    help_unit=models.CharField(max_length=50,db_column='help_unit',blank=True)    #帮扶单位

    help_way=models.CharField(max_length=50,db_column='help_way',blank=True)    #帮扶方式

    def __str__(self):
        return self.house_identifier


#2
class PoorHouseAdditionalForm(models.Model):    #贫困户附加表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    past_village_identifier=models.CharField(max_length=30,db_column='past_village_identifier',blank=True)    #过去村编号

    now_village_identifier=models.CharField(max_length=30,db_column='now_village_identifier',blank=True)    #现在村编号

    house_identifier=models.CharField(max_length=30,db_column='house_identifier',blank=True)    #户编号

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #接受扶持款的卡的银行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #接受扶持款的卡的账号

    card_people=models.CharField(max_length=30,db_column='card_people',blank=True)    #卡主姓名

    people_id=models.CharField(max_length=20,db_column='people_id',blank=True)    #卡主身份证号

    policy_number=models.CharField(max_length=30,db_column='policy_number',blank=True)    #应享政策编号

    policy_multiplier=models.CharField(max_length=20,db_column='policy_multiplier',blank=True)    #该政策编号乘以数量

    plan_money=models.CharField(max_length=20,db_column='plan_money',blank=True)    #应享政策编号对应的钱金额

    fact_money=models.CharField(max_length=20,db_column='fact_money',blank=True)    #实际享受到政策编号对应的钱金额

    date=models.CharField(max_length=50,db_column='date',blank=True)    #截止时间

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

    def __str__(self):
        return self.house_identifier


#1
class PoorPeopleDataForm(models.Model):    #贫困人口基本信息表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    house_identifier=models.CharField(max_length=30,db_column='house_identifier',blank=True)    #户编号

    people_identifier=models.CharField(max_length=30,db_column='people_identifier',blank=True)    #人编号

    people_name=models.CharField(max_length=30,db_column='people_name',blank=True)    #姓名

    people_id=models.CharField(max_length=20,db_column='people_id',blank=True)    #证件号码

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

    is_minimum=models.CharField(max_length=30,db_column='is_minimum',blank=True)    #是否享受低保

    year_date=models.CharField(max_length=10,db_column='year_date',blank=True)    #年度

    first_identify=models.CharField(max_length=50,db_column='first_identify',blank=True)    #首次识别时间

    help_people=models.CharField(max_length=50,db_column='help_people',blank=True)    #帮扶人员

    help_unit=models.CharField(max_length=50,db_column='help_unit',blank=True)    #帮扶单位

    help_way=models.CharField(max_length=50,db_column='help_way',blank=True)    #帮扶方式

    def __str__(self):
        return self.people_identifier


#2
class PoorPeopleAdditionalForm(models.Model):    #贫困人口附加表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    house_identifier=models.CharField(max_length=30,db_column='house_identifier',blank=True)    #户编号

    people_identifier=models.CharField(max_length=30,db_column='people_identifier',blank=True)    #人编号

    bank_name=models.CharField(max_length=50,db_column='bank_name',blank=True)    #用来接受扶持款的银行

    bank_number=models.CharField(max_length=50,db_column='bank_number',blank=True)    #该银行账号

    policy_number=models.CharField(max_length=30,db_column='policy_number',blank=True)    #应享政策编号

    policy_multiplier=models.CharField(max_length=20,db_column='policy_multiplier',blank=True)    #该政策编号乘以数量

    plan_money=models.CharField(max_length=20,db_column='plan_money',blank=True)    #应享政策编号对应的钱金额

    fact_money=models.CharField(max_length=20,db_column='fact_money',blank=True)    #实际享受到政策编号对应的钱金额

    date=models.CharField(max_length=50,db_column='date',blank=True)    #截止时间

    remarks=models.CharField(max_length=300,db_column='remarks',blank=True)    #备注

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

    def __str__(self):
        return self.policy_number


#1
class HelperDataForm(models.Model):    #帮扶人基本信息表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    unit_name=models.CharField(max_length=50,db_column='unit_name',blank=True)    #帮扶人-单位名称

    helper_name=models.CharField(max_length=30,db_column='helper_name',blank=True)    #帮扶人-姓名

    helper_sex=models.CharField(max_length=10,db_column='helper_sex',blank=True)    #帮扶人-性别

    helper_post=models.CharField(max_length=50,db_column='helper_post',blank=True)    #帮扶人-职务

    helper_type=models.CharField(max_length=30,db_column='helper_type',blank=True)    #帮扶人-队长/队员/结对帮扶责任人

    poor_town=models.CharField(max_length=50,db_column='poor_town',blank=True)    #贫困户-乡镇

    past_administrative_village=models.CharField(max_length=50,db_column='past_administrative_village',blank=True)    #贫困户-行政村曾用名

    now_administrative_village=models.CharField(max_length=50,db_column='now_administrative_village',blank=True)    #贫困户-行政村现用名

    past_village_identifier=models.CharField(max_length=30,db_column='past_village_identifier',blank=True)    #贫困户-过去村编号

    now_village_identifier=models.CharField(max_length=30,db_column='now_village_identifier',blank=True)    #贫困户-现在村编号

    poor_home=models.CharField(max_length=20,db_column='poor_home',blank=True)    #贫困户-户数

    poor_name=models.CharField(max_length=30,db_column='poor_name',blank=True)    #贫困户-户主姓名

    poor_group=models.CharField(max_length=20,db_column='poor_group',blank=True)    #贫困户-户主姓名-组别

    household_identifier=models.CharField(max_length=20,db_column='household_identifier',blank=True)    #贫困户-户主身份证号码

    office_phone=models.CharField(max_length=100,db_column='office_phone',blank=True)    #帮扶干部电话-办公电话

    mobile_phone=models.CharField(max_length=100,db_column='mobile_phone',blank=True)    #帮扶干部电话-手机

    year_date=models.CharField(max_length=10,db_column='year_date',blank=True)    #年度

    def __str__(self):
        return self.helper_name