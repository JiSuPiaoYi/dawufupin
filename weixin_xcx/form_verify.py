from django import forms


#用户登录表单验证
class VerifyAccountBind(forms.Form):
    mobile = forms.CharField(max_length=11, error_messages={'required': '请输入手机号','max_length':'手机号不合法'})
    passwd = forms.CharField(error_messages={'required': '请输入密码'})
    openid = forms.CharField(error_messages={'required': '用户微信信息缺失'})

#用户登录表单验证
class VerifyPassword(forms.Form):
    old_password = forms.CharField(error_messages={'required': '请输入原密码'})
    new_password = forms.CharField(min_length=6,error_messages={'required': '请输入新密码', 'min_length': '密码最小长度6位'})
    qr_new_password = forms.CharField(min_length=6, error_messages={'required': '请确认新密码', 'min_length': '密码最小长度6位'})
    token = forms.CharField(error_messages={'required': 'token错误'})