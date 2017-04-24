from django import forms


class UserInfoForm(forms.Form):
    identify_number = forms.CharField(label='身份证', max_length=18, min_length=15)
    name = forms.CharField(label='姓名', max_length=4, min_length=2)


