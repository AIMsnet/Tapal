from django import forms
from  .models import User, InwardRegistry
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput



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
        model = InwardRegistry
        
        fields = [
            'user_id',
            'ReferenceNumber',
            'ReferenceRecievedDate',
            'LatterDetails',
            'EmailId',
            'Address',
            'ReferenceType',
            'ReferenceDate',
            'RecievedFrom',
            'MobileNumber',
            'TypeOfReference',
            'Priority',            
        ]
        

class forwardForm(forms.ModelForm):
    model = InwardRegistry
    fields = [
            'user_id',   
    ]

# class reportForm(forms.Form):
   
   
        
        
            
# class BranchMasterForm(forms.Form):
#     branch_name =   forms.CharField(max_length=25, required=True)
#     branch_id   =   forms.CharField(max_length=16, required=True)
#     desk_name   =   forms.CharField(max_length=25, required=True)
#     desk_id     =   forms.CharField(max_length=10, required=True)
#     user_id     =   forms.CharField(max_length=16, required=True)


# class InwordDocForm(forms.Form):
#     inword_id   =   forms.CharField(max_length=16, required=True)
#     inword_date =   forms.DateField(required=True)
#     subject     =   forms.CharField(max_length=100, required=True)
#     sender_name =   forms.CharField(max_length=50, required=True)
#     sende_add   =   forms.CharField(max_length=60, required=True)
#     inword_type =   forms.CharField(max_length=16, required=True)   
#     courier_name=   forms.CharField(max_length=25, required=True)
#     courier_ref_no  =   forms.CharField(max_length=25, required=True)
#     letter_no   =   forms.CharField(max_length=25, required=True)
#     reply_ref_no=   forms.CharField(max_length=25, required=True)
#     reply_date  =   forms.DateField(required=True)

# class MonitorLatterForm(forms.Form):
#     inword_id   = forms.CharField(max_length=16, required=True)
#     received_date   =   forms.DateField(required=True)
#     desk_id     =   forms.CharField(max_length=16, required=True)
#     user_id     =   forms.CharField(max_length=16, required=True)
#     status      =   forms.CharField(max_length=20, required=True)
#     action      =   forms.CharField(max_length=75, required=True)
#     approved_by =   forms.CharField(max_length=16, required=True)
#     completion_date =   forms.DateField(required=True)
#     action_by_user_id   =   forms.CharField(max_length=16, required=True)
#     fowrd_date  =   forms.DateField(required=True)
#     forward_desk_id =   forms.CharField(max_length=16, required=True)
#     active_status   =   forms.BooleanField(required=True)
#     priority    =   forms.IntegerField(required=True)
#     inbox   =   forms.BooleanField(required=True)
#     owner   =   forms.CharField(max_length=16, required=True)

# class UserRegForms(forms.Form):
#     user_id     =   forms.CharField(max_length=8, required=True)
#     f_name      =   forms.CharField(max_length=30, required=True)
#     l_name      =   forms.CharField(max_length=30, required=True)
#     e_mailid    =   forms.CharField(max_length=40, required=True)
#     mobile_no   =   forms.CharField(max_length=10, required=True)
#     emp_id      =   forms.CharField(max_length=16, required=True)
#     role        =   forms.CharField(max_length=20, required=True)
#     designation =   forms.CharField(max_length=30, required=True)

    
