# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 9:38
# @Author  : 许志文
# @Site    :
# @File    : sms.py
# @Software: PyCharm

from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid, sys
from aliyunsdkcore.profile import region_provider

try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except:
    pass

"""
短信业务调用接口示例，版本号：v20170525

Created on 2017-06-12

"""


# 注意：不要更改
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

# ACCESS_KEY_ID/ACCESS_KEY_SECRET 根据实际申请的账号信息进行替换
ACCESS_KEY_ID = "LTAIVWyEAq6CAJTD"
ACCESS_KEY_SECRET = "SGuhG4l8rJNmlNild9S8AYbKDtQBjx"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME,REGION,DOMAIN)

def send_sms(phone_numbers, sign_name, template_code, template_param=None):
    business_id = uuid.uuid1()
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)

    # 短信模板变量参数
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)

    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(business_id)

    # 短信签名
    smsRequest.set_SignName(sign_name);

    # 短信发送的号码列表，必填。
    smsRequest.set_PhoneNumbers(phone_numbers)

    # 调用短信发送接口，返回json
    smsResponse = acs_client.do_action_with_exception(smsRequest)


    return smsResponse


def query_send_detail(biz_id, phone_number, page_size, current_page, send_date):
    queryRequest = QuerySendDetailsRequest.QuerySendDetailsRequest()
    # 查询的手机号码
    queryRequest.set_PhoneNumber(phone_number)
    # 可选 - 流水号
    queryRequest.set_BizId(biz_id)
    # 必填 - 发送日期 支持30天内记录查询，格式yyyyMMdd
    queryRequest.set_SendDate(send_date)
    # 必填-当前页码从1开始计数
    queryRequest.set_CurrentPage(current_page)
    # 必填-页大小
    queryRequest.set_PageSize(page_size)

    # 调用短信记录查询接口，返回json
    queryResponse = acs_client.do_action_with_exception(queryRequest)


    return queryResponse


__name__ = 'send'
if __name__ == 'send':
    '''
    自定义参数
    phone_numbers = sys.argv[1]
    sign_name = sys.argv[2]
    template_code = sys.argv[3]
    template_param = sys.argv[4]
    '''
    print send_sms(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == 'query':
    print query_send_detail("1234567^8901234", "13000000000", 10, 1, "20170612")
