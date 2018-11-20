from django.contrib import admin

# from .models import IndustryLedgerForm,EducationLedgerForm,LifeMinimumLedgerForm,LifeOrphanLedgerForm,LifeGuaranteeLedgerForm,MedicalLedgerForm,HousingLedgerForm
# from .models import PasturageIndustryOutputForm,ForestryIndustryOutputForm,AgricultureIndustryOutputForm,AquacultureIndustryOutputForm,CommerceIndustryOutputForm,EntertainmentIndustryOutputForm,TrainIndustryOutputForm,OneIndustryOutputForm,TwoIndustryOutputForm,ThreeIndustryOutputForm,FourIndustryOutputForm,FiveIndustryOutputForm,SixIndustryOutputForm,HelpIndustryOutputForm
# from .models import ChengGuanMicroOutputForm,DaXinMicroOutputForm,DongXinMicroOutputForm,FangFanMicroOutputForm,FengDianMicroOutputForm,GaoDianMicroOutputForm,GaoTieMicroOutputForm,HeKouMicroOutputForm,HuangZhanMicroOutputForm,KaiFaMicroOutputForm,LiuJiMicroOutputForm,LvWangMicroOutputForm,PengDianMicroOutputForm,SanLiMicroOutputForm,SiGuMicroOutputForm,WuFengMicroOutputForm,XiaDianMicroOutputForm,XinChengMicroOutputForm,XuanHuaMicroOutputForm,YangPingMicroOutputForm
# from .models import ChengGuanEducationOutputForm,DaXinEducationOutputForm,DongXinEducationOutputForm,FangFanEducationOutputForm,FengDianEducationOutputForm,GaoDianEducationOutputForm,GaoTieEducationOutputForm,HeKouEducationOutputForm,HuangZhanEducationOutputForm,KaiFaEducationOutputForm,LiuJiEducationOutputForm,LvWangEducationOutputForm,PengDianEducationOutputForm,SanLiEducationOutputForm,SiGuEducationOutputForm,WuFengEducationOutputForm,XiaDianEducationOutputForm,XinChengEducationOutputForm,XuanHuaEducationOutputForm,YangPingEducationOutputForm
# from .models import CountyLifeOutputForm,ChengGuanLifeOutputForm,DaXinLifeOutputForm,DongXinLifeOutputForm,FangFanLifeOutputForm,FengDianLifeOutputForm,GaoDianLifeOutputForm,GaoTieLifeOutputForm,HeKouLifeOutputForm,HuangZhanLifeOutputForm,KaiFaLifeOutputForm,LiuJiLifeOutputForm,LvWangLifeOutputForm,PengDianLifeOutputForm,SanLiLifeOutputForm,SiGuLifeOutputForm,WuFengLifeOutputForm,XiaDianLifeOutputForm,XinChengLifeOutputForm,XuanHuaLifeOutputForm,YangPingLifeOutputForm
# from .models import ChengGuanMedicalOutputForm,DaXinMedicalOutputForm,DongXinMedicalOutputForm,FangFanMedicalOutputForm,FengDianMedicalOutputForm,GaoDianMedicalOutputForm,GaoTieMedicalOutputForm,HeKouMedicalOutputForm,HuangZhanMedicalOutputForm,KaiFaMedicalOutputForm,LiuJiMedicalOutputForm,LvWangMedicalOutputForm,PengDianMedicalOutputForm,SanLiMedicalOutputForm,SiGuMedicalOutputForm,WuFengMedicalOutputForm,XiaDianMedicalOutputForm,XinChengMedicalOutputForm,XuanHuaMedicalOutputForm,YangPingMedicalOutputForm
# from .models import CountyHousingOutputForm,ChengGuanHousingOutputForm,DaXinHousingOutputForm,DongXinHousingOutputForm,FangFanHousingOutputForm,FengDianHousingOutputForm,GaoDianHousingOutputForm,GaoTieHousingOutputForm,HeKouHousingOutputForm,HuangZhanHousingOutputForm,KaiFaHousingOutputForm,LiuJiHousingOutputForm,LvWangHousingOutputForm,PengDianHousingOutputForm,SanLiHousingOutputForm,SiGuHousingOutputForm,WuFengHousingOutputForm,XiaDianHousingOutputForm,XinChengHousingOutputForm,XuanHuaHousingOutputForm,YangPingHousingOutputForm
# from .models import FlexibleLedgerForm
from .models import AdministrativeVillageDataForm,AdministrativeVillageAdditionalForm
from .models import PoorHouseDataForm,PoorHouseAdditionalForm
from .models import PoorPeopleDataForm,PoorPeopleAdditionalForm
from .models import PolicyStaticForm
from .models import HelperDataForm

# Register your models here.

# admin.site.register(IndustryLedgerForm)    #“产业扶起来”政策落实调查汇总表(台账表)
# admin.site.register(EducationLedgerForm)    #“教育扶起来”政策落实调查汇总表（台账表）
# admin.site.register(LifeMinimumLedgerForm)    #“生活保起来”政策落实情况统计表（低保台账表）
# admin.site.register(LifeOrphanLedgerForm)    #“生活保起来”政策落实情况统计表（孤儿台账表）
# admin.site.register(LifeGuaranteeLedgerForm)    #“生活保起来”政策落实情况统计表（五保台账表）
# admin.site.register(MedicalLedgerForm)    #“医疗保起来”政策落实情况统计表（台账表）
# admin.site.register(HousingLedgerForm)    #“住房保起来”政策落实情况统计表（台账表）
#
# admin.site.register(PasturageIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-产业-畜牧
# admin.site.register(ForestryIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-产业-林业
# admin.site.register(AgricultureIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-产业-农业
# admin.site.register(AquacultureIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-产业-水产
# admin.site.register(CommerceIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-农村电商
# admin.site.register(EntertainmentIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-农家乐
# admin.site.register(TrainIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-培训人次
# admin.site.register(OneIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-一大员
# admin.site.register(TwoIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-二大员
# admin.site.register(ThreeIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-三大员
# admin.site.register(FourIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-四大员
# admin.site.register(FiveIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-五大员
# admin.site.register(SixIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-六大员-六大员
# admin.site.register(HelpIndustryOutputForm)    #“产业扶起来”政策落实情况统计表（输出表）-带动贫困对象就业-其他方式帮助就业
#
#
# admin.site.register(ChengGuanMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-城关镇
# admin.site.register(DaXinMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-大新镇
# admin.site.register(DongXinMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-东新乡
# admin.site.register(FangFanMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-芳畈镇
# admin.site.register(FengDianMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-丰店镇
# admin.site.register(GaoDianMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-高店乡
# admin.site.register(GaoTieMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-高铁新区
# admin.site.register(HeKouMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-河口镇
# admin.site.register(HuangZhanMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-黄站镇
# admin.site.register(KaiFaMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-开发区
# admin.site.register(LiuJiMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-刘集镇
# admin.site.register(LvWangMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-吕王镇
# admin.site.register(PengDianMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-彭店乡
# admin.site.register(SanLiMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-三里城镇
# admin.site.register(SiGuMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-四姑镇
# admin.site.register(WuFengMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-悟峰山管委会
# admin.site.register(XiaDianMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-夏店镇
# admin.site.register(XinChengMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-新城镇
# admin.site.register(XuanHuaMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-宣化店镇
# admin.site.register(YangPingMicroOutputForm)    #扶贫小额信贷工作进展情况统计表（输出表）-阳平镇
#
# admin.site.register(ChengGuanEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-城关镇
# admin.site.register(DaXinEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-大新镇
# admin.site.register(DongXinEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-东新乡
# admin.site.register(FangFanEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-芳畈镇
# admin.site.register(FengDianEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-丰店镇
# admin.site.register(GaoDianEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-高店乡
# admin.site.register(GaoTieEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-高铁新区
# admin.site.register(HeKouEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-河口镇
# admin.site.register(HuangZhanEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-黄站镇
# admin.site.register(KaiFaEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-开发区
# admin.site.register(LiuJiEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-刘集镇
# admin.site.register(LvWangEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-吕王镇
# admin.site.register(PengDianEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-彭店乡
# admin.site.register(SanLiEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-三里城镇
# admin.site.register(SiGuEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-四姑镇
# admin.site.register(WuFengEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-悟峰山管委会
# admin.site.register(XiaDianEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-夏店镇
# admin.site.register(XinChengEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-新城镇
# admin.site.register(XuanHuaEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-宣化店镇
# admin.site.register(YangPingEducationOutputForm)    #“教育扶起来”政策落实情况统计表（输出表）-阳平镇
#
# admin.site.register(CountyLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-全县合计
# admin.site.register(ChengGuanLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-城关镇
# admin.site.register(DaXinLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-大新镇
# admin.site.register(DongXinLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-东新乡
# admin.site.register(FangFanLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-芳畈镇
# admin.site.register(FengDianLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-丰店镇
# admin.site.register(GaoDianLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-高店乡
# admin.site.register(GaoTieLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-高铁新区
# admin.site.register(HeKouLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-河口镇
# admin.site.register(HuangZhanLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-黄站镇
# admin.site.register(KaiFaLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-开发区
# admin.site.register(LiuJiLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-刘集镇
# admin.site.register(LvWangLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-吕王镇
# admin.site.register(PengDianLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-彭店乡
# admin.site.register(SanLiLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-三里城镇
# admin.site.register(SiGuLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-四姑镇
# admin.site.register(WuFengLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-悟峰山管委会
# admin.site.register(XiaDianLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-夏店镇
# admin.site.register(XinChengLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-新城镇
# admin.site.register(XuanHuaLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-宣化店镇
# admin.site.register(YangPingLifeOutputForm)    #“生活保起来”政策落实情况统计表（输出表）-阳平镇
#
# admin.site.register(ChengGuanMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-城关镇
# admin.site.register(DaXinMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-大新镇
# admin.site.register(DongXinMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-东新乡
# admin.site.register(FangFanMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-芳畈镇
# admin.site.register(FengDianMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-丰店镇
# admin.site.register(GaoDianMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-高店乡
# admin.site.register(GaoTieMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-高铁新区
# admin.site.register(HeKouMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-河口镇
# admin.site.register(HuangZhanMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-黄站镇
# admin.site.register(KaiFaMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-开发区
# admin.site.register(LiuJiMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-刘集镇
# admin.site.register(LvWangMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-吕王镇
# admin.site.register(PengDianMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-彭店乡
# admin.site.register(SanLiMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-三里城镇
# admin.site.register(SiGuMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-四姑镇
# admin.site.register(WuFengMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-悟峰山管委会
# admin.site.register(XiaDianMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-夏店镇
# admin.site.register(XinChengMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-新城镇
# admin.site.register(XuanHuaMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-宣化店镇
# admin.site.register(YangPingMedicalOutputForm)    #“医疗保起来”政策落实情况统计表（输出表）-阳平镇
#
# admin.site.register(CountyHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-全县合计
# admin.site.register(ChengGuanHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-城关镇
# admin.site.register(DaXinHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-大新镇
# admin.site.register(DongXinHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-东新乡
# admin.site.register(FangFanHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-芳畈镇
# admin.site.register(FengDianHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-丰店镇
# admin.site.register(GaoDianHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-高店乡
# admin.site.register(GaoTieHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-高铁新区
# admin.site.register(HeKouHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-河口镇
# admin.site.register(HuangZhanHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-黄站镇
# admin.site.register(KaiFaHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-开发区
# admin.site.register(LiuJiHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-刘集镇
# admin.site.register(LvWangHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-吕王镇
# admin.site.register(PengDianHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-彭店乡
# admin.site.register(SanLiHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-三里城镇
# admin.site.register(SiGuHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-四姑镇
# admin.site.register(WuFengHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-悟峰山管委会
# admin.site.register(XiaDianHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-夏店镇
# admin.site.register(XinChengHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-新城镇
# admin.site.register(XuanHuaHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-宣化店镇
# admin.site.register(YangPingHousingOutputForm)    #“住房保起来”政策落实情况统计表（输出表）-阳平镇
#
# admin.site.register(FlexibleLedgerForm)    #灵活台账表类型

@admin.register(AdministrativeVillageDataForm)    #行政村基本信息表
class AdministrativeVillageDataForm(admin.ModelAdmin):
    list_display=('town_name','past_administrative_village','now_administrative_village',
                  'past_village_identifier','now_village_identifier','past_is_poor',
                  'now_is_poor','is_merge','is_rename','past_home_number','now_home_number',
                  'past_poor_home','now_poor_home','past_people_number','now_people_number',
                  'past_poor_people','now_poor_people','past_responsible_person',
                  'now_responsible_person','past_telephone_number','now_telephone_number',
                  'past_development_direction','now_development_direction','past_village_officer',
                  'now_village_officer','past_party_member','now_party_member',
                  'past_terrain_physiognomy','now_terrain_physiognomy','past_dimension',
                  'now_dimension','past_longitude','now_longitude','past_minimum_home',
                  'now_minimum_home','past_minimum_people','now_minimum_people','past_five_home',
                  'now_five_home','past_five_people','now_five_people','past_nation_people',
                  'now_nation_people','past_woman_people','now_woman_people',
                  'past_handicapped_people','now_handicapped_people','past_labor_people',
                  'now_labor_people','past_egression_people','now_egression_people',
                  'year_date','past_help_people','now_help_people','past_help_unit',
                  'now_help_unit','past_help_way','now_help_way','past_help_phone',
                  'now_help_phone')

@admin.register(AdministrativeVillageAdditionalForm)    #行政村附加表
class AdministrativeVillageAdditionalForm(admin.ModelAdmin):
    list_display=('past_village_identifier','now_village_identifier','bank_name',
                  'bank_number','card_people','people_id','policy_number',
                  'policy_multiplier','plan_money','fact_money','date_year',
                  'date_month','remarks')

@admin.register(PoorHouseDataForm)    #贫困户基本信息表
class PoorHouseDataForm(admin.ModelAdmin):
    list_display=('past_village_identifier','now_village_identifier','house_identifier',
                  'house_group','householder_identifier','householder_name','householder_id',
                  'family_number','people_nation','education_degree','school_situation',
                  'health_situation','labor_ability','work_situation','work_time','join_medical',
                  'offpoor_attribute','offpoor_year','poor_attribute','poor_reason','danger_house',
                  'water_safe','water_hard','is_minimum','average_income','telephone','address',
                  'year_date','first_identify','help_people','help_unit','help_way','help_phone')

@admin.register(PoorHouseAdditionalForm)    #贫困户附加表
class PoorHouseAdditionalForm(admin.ModelAdmin):
    list_display=('past_village_identifier','now_village_identifier','house_identifier',
                  'bank_name','bank_number','card_people','people_id',
                  'householder_id','policy_number','policy_multiplier','plan_money',
                  'fact_money','date_year','date_month','remarks')

@admin.register(PoorPeopleDataForm)    #贫困人口基本信息表
class PoorPeopleDataForm(admin.ModelAdmin):
    list_display=('house_identifier','people_identifier','people_name',
                  'people_id','poor_attribute','family_number','people_relationship',
                  'people_nation','education_degree','school_situation','health_situation',
                  'labor_ability','work_time','join_medical','offpoor_attribute',
                  'poor_reason','telephone','address','birth_date','is_five','year_date',
                  'first_identify','help_people','help_unit','help_way','help_phone',
                  'special_people')

@admin.register(PoorPeopleAdditionalForm)    #贫困人口附加表
class PoorPeopleAdditionalForm(admin.ModelAdmin):
    list_display=('house_identifier','people_identifier','people_id',
                  'bank_name','bank_number','card_people','card_id',
                  'policy_number','policy_multiplier','plan_money','fact_money',
                  'date_year','date_month','remarks')

@admin.register(PolicyStaticForm)    #政策静态表
class PolicyStaticFormAdmin(admin.ModelAdmin):
    list_display=('policy_number','policy_first_layer','policy_second_layer',
                  'policy_third_layer','subsidy_one','subsidy_two','subsidy_three',
                  'subsidy_limit','limit_condition','policy_object','implement_department')

@admin.register(HelperDataForm)    #帮扶人基本信息表
class HelperDataForm(admin.ModelAdmin):
    list_display=('unit_name','helper_name','helper_sex','helper_post',
                  'helper_type','poor_town','past_administrative_village',
                  'now_administrative_village','past_village_identifier',
                  'now_village_identifier','poor_home','poor_name','poor_group',
                  'household_identifier','office_phone','mobile_phone','year_date')