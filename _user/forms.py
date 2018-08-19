from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from . import models

class SignupForm(UserCreationForm):
    
    name = forms.CharField()
    age = forms.IntegerField()
    phone_number = forms.CharField()
    
    class Meta(UserCreationForm.Meta):
        
        fields = UserCreationForm.Meta.fields + (
            'email',
            'last_name',
            'first_name'
        )
    
    def save(self):
        
        user = super().save()
        
        profile = Profile.objects.create(
            user = user,
            name = self.cleaned_data['name'],
            age = self.cleaned_data['age'],
            phone_number = self.cleaned_data['phone_number']
        )

        return user.save()

class LoginForm(AuthenticationForm):

    answer = forms.IntegerField(label='3+3=?')
    
    def clean_answer(self): # clean_'필드명' : 유효성 검사

        if self.cleaned_data.get('answer', None) != 6:
            raise form.ValidationError('다시 입력해주세요')

