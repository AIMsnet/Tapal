from django import forms
from  .models import InwardRegistry

# BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
# FAVORITE_COLORS_CHOICES = [
# ('blue', 'Blue'),
# ('green', 'Green'),
# ('black', 'Black'),
# ]


class InwardRegistryForm(forms.ModelForm):
    class Meta:
        model = InwardRegistry
        # fields = "__all__"
        fields = [
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
            'AttachedDocuments',
        ]
            
class BranchMasterForm(forms.Form):
    branch_name =   forms.CharField(max_length=25, required=True)
    branch_id   =   forms.CharField(max_length=16, required=True)
    desk_name   =   forms.CharField(max_length=25, required=True)
    desk_id     =   forms.CharField(max_length=10, required=True)
    user_id     =   forms.CharField(max_length=16, required=True)


class InwordDocForm(forms.Form):
    inword_id   =   forms.CharField(max_length=16, required=True)
    inword_date =   forms.DateField(required=True)
    subject     =   forms.CharField(max_length=100, required=True)
    sender_name =   forms.CharField(max_length=50, required=True)
    sende_add   =   forms.CharField(max_length=60, required=True)
    inword_type =   forms.CharField(max_length=16, required=True)   
    courier_name=   forms.CharField(max_length=25, required=True)
    courier_ref_no  =   forms.CharField(max_length=25, required=True)
    letter_no   =   forms.CharField(max_length=25, required=True)
    reply_ref_no=   forms.CharField(max_length=25, required=True)
    reply_date  =   forms.DateField(required=True)

class MonitorLatterForm(forms.Form):
    inword_id   = forms.CharField(max_length=16, required=True)
    received_date   =   forms.DateField(required=True)
    desk_id     =   forms.CharField(max_length=16, required=True)
    user_id     =   forms.CharField(max_length=16, required=True)
    status      =   forms.CharField(max_length=20, required=True)
    action      =   forms.CharField(max_length=75, required=True)
    approved_by =   forms.CharField(max_length=16, required=True)
    completion_date =   forms.DateField(required=True)
    action_by_user_id   =   forms.CharField(max_length=16, required=True)
    fowrd_date  =   forms.DateField(required=True)
    forward_desk_id =   forms.CharField(max_length=16, required=True)
    active_status   =   forms.BooleanField(required=True)
    priority    =   forms.IntegerField(required=True)
    inbox   =   forms.BooleanField(required=True)
    owner   =   forms.CharField(max_length=16, required=True)

class UserRegForms(forms.Form):
    user_id     =   forms.CharField(max_length=8, required=True)
    f_name      =   forms.CharField(max_length=30, required=True)
    l_name      =   forms.CharField(max_length=30, required=True)
    e_mailid    =   forms.CharField(max_length=40, required=True)
    mobile_no   =   forms.CharField(max_length=10, required=True)
    emp_id      =   forms.CharField(max_length=16, required=True)
    role        =   forms.CharField(max_length=20, required=True)
    designation =   forms.CharField(max_length=30, required=True)

    
