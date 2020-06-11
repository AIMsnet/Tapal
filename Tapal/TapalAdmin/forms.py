from django import forms
from  .models import User, InwardReg, InwardDocs
from django.contrib.auth.forms import UserCreationForm



class createUserForms(UserCreationForm):
    error_css_class = 'error'
    class Meta:
        model = User
        fields  =   [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'mobile_no',
            'employee_id',
            'role',
            'desk_id',
            'designation',
            'password1',
            'password2'
        ]



    def clean_email(self):
        print('inside email')
        email = self.cleaned_data['email']
        print(email)
        if User.objects.filter(email=email).exists():
            print('email already exist')
            raise forms.ValidationError("This email Id already exist.")
            
        if '@' not in email:
            print('INVALID email ')
            raise forms.ValidationError("This email Id is INVALID .")
        return email

    def clean_password2(self):
        print('inside password confirmation')
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        print(password2)
        if password1 != password2:
            print('Password does not match')
            raise forms.ValidationError("Password does not match.Please re-enter password")
        return password2


class InwardRegistryForm(forms.ModelForm):
    class Meta:
        model = InwardReg
        
        fields = [
            'user_id',
            'RecRefNumber',
            'LttrRecDate',
            'LatterDetails',
            'EmailId',
            'Address',
            'TypeOfReference',
            'RecDate',
            'RecFrom',
            'MobileNumber',
            'RecFromDept',
            'Priority',
            'Status'    
        ]
        

class forwardForm(forms.ModelForm):
    model = InwardReg
    fields = [
            'user_id',   
    ]

class InwardDocForm(forms.ModelForm):
    class Meta:
        model  =  InwardDocs
        fields = [
                'DocsAttch',   
        ]
    
