# banking_app/forms.py
from django import forms


from .models import Customer, Branch, District


#
# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address',  'account_type', 'materials_provide']
#
#     district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select District")
#     branch = forms.ModelChoiceField(queryset=Branch.objects.none(), empty_label="Select Branch")
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['branch'].queryset = Branch.objects.none()

class DistrictChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class BranchChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name} - {obj.district}"

class CustomerForm(forms.ModelForm):
    district = DistrictChoiceField(queryset=District.objects.all(), empty_label="Select District")
    branch = BranchChoiceField(queryset=Branch.objects.all(), empty_label="Select Branch")

    class Meta:
        model = Customer
        fields = '__all__'
        # exclude = ['user']