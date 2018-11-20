from django import forms

class VerifyUser(forms.Form):
    name = forms.CharField(max_length=100, error_messages={'required': '姓名不能为空'})
    department_id = forms.IntegerField(error_messages={'required': '所属部门不能为空','invalid':'部门格式不正确'})
    mobile = forms.IntegerField(error_messages={'required': '手机号不能为空','invalid':'手机号格式不正确'})