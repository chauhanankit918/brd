from xml.dom.minidom import Attr
from django import forms
from Student.models import Student_detail
from django.forms import ModelForm, Select, Textarea, TextInput, NumberInput, DateField


class Student_detailForm(forms.ModelForm):
    class Meta:
        cls_sty = 'form-control  '
        model = Student_detail
        fields = ['Name', 'Email',  'Number', 'DOB', 'Aadhaar', 'Gender', 'Education', 'doc_10', 'doc_12', 'doc_ug',
                  'doc_pg', 'Course_name',   'State', 'City', 'House', 'Post_office', 'Block', 'District', 'Pincode']

        # fields = '__all__'
        label = {
            'Gender': 'Gender',
            'Date': 'Date'
        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': cls_sty, 'placeholder': 'Name'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'}),
            'Number': forms.TextInput(attrs={'class': cls_sty, 'type': 'phone', 'placeholder': 'Number'}),
            #  'Number2' : forms.TextInput(attrs={'class': cls_sty ,'type':'phone' ,'placeholder':'Alternate No.'}),
            'Gender': Select(attrs={'class': 'form-select', 'type': 'choice'}),
            'DOB': forms.TextInput(attrs={'class': cls_sty,
                                          'type': 'date'
                                          }),
            'Education': Select(attrs={'class': 'form-select ', 'type': 'choice'}),

            'Aadhaar': forms.TextInput(attrs={'class': cls_sty, 'placeholder': 'Aadhaar No.'}),
            'Course_name': Select(attrs={'class': 'form-select', 'type': 'choice'}),
            'State': forms.TextInput(attrs={'class': cls_sty, }),
            'doc_10': forms.FileInput(attrs={'class': cls_sty, 'type': 'file'}),
            'doc_12': forms.FileInput(attrs={'class': cls_sty, 'type': 'file'}),
            'doc_ug': forms.FileInput(attrs={'class': cls_sty, 'type': 'file'}),
            'doc_pg': forms.FileInput(attrs={'class': cls_sty, 'type': 'file'}),
            'City': forms.TextInput(attrs={'class': cls_sty}),
            'House': forms.TextInput(attrs={'class': cls_sty}),
            'Post_office': forms.TextInput(attrs={'class': cls_sty}),
            'Block': forms.TextInput(attrs={'class': cls_sty}),
            'District': forms.TextInput(attrs={'class': cls_sty}),
            'Pincode': forms.TextInput(attrs={'class': cls_sty}),
        }
        
