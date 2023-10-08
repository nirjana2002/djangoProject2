from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from . import forms
from .models import Bank
# Create your views here.

def create_bank(request):
    if request.method == 'GET':
        form = forms.BankCreationForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse('created successfully')
    else:
        form = forms.BankCreationForm()
    return render(request, template_name='form.html', context={"form": form})

def update_bank(request, b_id):
    bank = Bank.objects.get(pk=b_id)
    if request.method == 'GET':
        form = forms.BankUpdatationForm(request.GET, instance=bank)
        print('form is updated')
        if form.is_valid():
            form.save()
            return HttpResponse('updated successfully')
    else:
        form = forms.BankCreationForm(instance=bank)
    return render(request, template_name='form.html', context={"form": form})


def delete_bank(request, b_id):
    Bank.objects.get(pk=b_id).delete()
    return redirect('/')
