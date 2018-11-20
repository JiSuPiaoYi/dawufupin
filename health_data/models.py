from django.db import models

# Create your models here.
class FourInOneDataForm(models.Model):    #四位一体表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    people_name=models.CharField(max_length=30,db_column='people_name',blank=True)    #姓名

    people_id=models.CharField(max_length=20,db_column='people_id',blank=True)    #证件号码

    people_attribute=models.CharField(max_length=50,db_column='people_attribute',blank=True)    #人员属性

    people_address=models.CharField(max_length=100,db_column='people_address',blank=True)    #住址

    people_diagnosis=models.CharField(max_length=100,db_column='people_diagnosis',blank=True)    #出院诊断

    institution_name=models.CharField(max_length=50,db_column='institution_name',blank=True)    #医疗机构名称

    hospitalization_number=models.CharField(max_length=30,db_column='hospitalization_number',blank=True)    #住院号

    in_time=models.CharField(max_length=50,db_column='in_time',blank=True)    #住院时间

    off_time=models.CharField(max_length=50,db_column='off_time',blank=True)    #住院时间

    medical_type=models.CharField(max_length=30,db_column='medical_type',blank=True)    #医疗类别

    medical_amount=models.CharField(max_length=20,db_column='medical_amount',blank=True)    #医疗费总额

    accord_range=models.CharField(max_length=20,db_column='accord_range',blank=True)    #符合范围

    payment_amount=models.CharField(max_length=20,db_column='payment_amount',blank=True)    #四位一体支付合计

    medical_reimbursement=models.CharField(max_length=20,db_column='medical_reimbursement',blank=True)    #基本医疗报销

    insurance_indemnity=models.CharField(max_length=20,db_column='insurance_indemnity',blank=True)    #大病保险赔付

    civil_rescue=models.CharField(max_length=20,db_column='civil_rescue',blank=True)    #民政救助

    supplement_indemnity=models.CharField(max_length=20,db_column='supplement_indemnity',blank=True)    #大病补充险赔付

    hospital_undertake=models.CharField(max_length=20,db_column='hospital_undertake',blank=True)    #医院承担

    plan_proportion=models.CharField(max_length=20,db_column='plan_proportion',blank=True)    #统筹比例

    hospital_reduction=models.CharField(max_length=20,db_column='hospital_reduction',blank=True)    #医院减免

    people_payment=models.CharField(max_length=20,db_column='people_payment',blank=True)    #个人自付

    year_date=models.CharField(max_length=20,db_column='year_date',blank=True)    #年份

    month_date=models.CharField(max_length=20,db_column='month_date',blank=True)    #月份

    def __str__(self):
        return self.people_name


class FourInOneAdditionalForm(models.Model):    #四位一体附加表

    id=models.AutoField(primary_key=True)    #区分表内不同数据的自增id

    people_id=models.CharField(max_length=20,db_column='people_id',blank=True)    #证件号码

    people_name=models.CharField(max_length=30,db_column='people_name',blank=True)    #姓名

    people_address=models.CharField(max_length=100,db_column='people_address',blank=True)    #住址

    bottom_property=models.CharField(max_length=50,db_column='bottom_property',blank=True)    #兜底属性

    institution_name=models.CharField(max_length=50,db_column='institution_name',blank=True)    #就医机构

    medical_type=models.CharField(max_length=30,db_column='medical_type',blank=True)    #就医类型

    people_diagnosis=models.CharField(max_length=100,db_column='people_diagnosis',blank=True)    #疾病

    in_time=models.CharField(max_length=50,db_column='in_time',blank=True)    #入院日期

    off_time=models.CharField(max_length=50,db_column='off_time',blank=True)    #出院日期

    medical_amount=models.CharField(max_length=20,db_column='medical_amount',blank=True)    #医疗总费

    inclusion_compensation=models.CharField(max_length=20,db_column='inclusion_compensation',blank=True)    #纳入补偿

    overall_payment=models.CharField(max_length=20,db_column='overall_payment',blank=True)    #统筹支付合计

    medical_compensation=models.CharField(max_length=20,db_column='medical_compensation',blank=True)    #医保补偿

    insurance_indemnity=models.CharField(max_length=20,db_column='insurance_indemnity',blank=True)    #大病保险

    civil_rescue=models.CharField(max_length=20,db_column='civil_rescue',blank=True)    #民政补助

    supplement_indemnity=models.CharField(max_length=20,db_column='supplement_indemnity',blank=True)    #补充保险

    people_payment=models.CharField(max_length=20,db_column='people_payment',blank=True)    #患者自付

    settlement_date=models.CharField(max_length=30,db_column='settlement_date',blank=True)    #结算日期

    def __str__(self):
        return self.people_name