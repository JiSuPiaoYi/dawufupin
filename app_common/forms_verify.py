from django import forms

class VerifyNav(forms.Form):
    name = forms.CharField(max_length=100, error_messages={'required': '名称不能为空'})
    sort = forms.IntegerField(error_messages={'required': '排序不能为空','invalid':'排序必须为数字'})