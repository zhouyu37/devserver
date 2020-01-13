# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from api import models
# Create your views here.

def business_unit_list(request):
    queryset=models.BusinessUnit.objects.all()
    return render(request,"business_unit_list.html",{'queryset':queryset})


from django import forms
class BusinessUnitModelForm(forms.ModelForm):
    class Meta:
        model = models.BusinessUnit
        fields = '__all__'
        error_messages = {
            'name':{'required':'can not be None!'}
        }
    def __init__(self,*args,**kwargs):
        super(BusinessUnitModelForm,self).__init__(*args,**kwargs)
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

def business_unit_add(request):
    if request.method == 'GET':
        form = BusinessUnitModelForm()
        return render(request, 'business_unit_add.html', {'form': form})
    form = BusinessUnitModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/business/unit/list/')
    return render(request, 'business_unit_add.html', {'form': form})