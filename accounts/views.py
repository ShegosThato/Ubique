from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from . import forms

@login_required
def accounts(request, person_id):
    template = 'accounts.html'
    person = get_object_or_404(Person,pk=person_id)
    con = {
           'person': person,
           
        }
    return render(request, template, con)

def add(request):
    template = 'index.html'
    #post
    if request.method == 'POST':
        addform = forms.PersonForm(request.POST)
        #validate form
        if addform.is_valid():
            addform.cleaned_data['first_name']
            addform.cleaned_data['middle_name']
            addform.cleaned_data['last_name']
            addform.cleaned_data['id_num']
            addform.cleaned_data['house_num']
            addform.cleaned_data['street_name']
            addform.cleaned_data['town']
            addform.cleaned_data['city']
            addform.cleaned_data['province']
            addform.cleaned_data['zip_code']
            addform.cleaned_data['id_pic']
            addform.save()
    #get
    addform = forms.PersonForm()
    con = {
        'addform': addform,
    }
    return redirect('ubi:index')

def search_by_id(request, id_num):
    template = 'index.html'
    result = Person.objects.get(pk=id_num)
    addform = forms.PersonForm()
    ctxt = {'peeps': result, 'addform': addform}
    return render(request, template, ctxt)

def index(request):
    template = 'index.html'
    addform = forms.PersonForm()
    peeps = Person.objects.all()
    ctxt = {'peeps': peeps,
            'addform': addform,
        }
    return render(request, template, ctxt)

def delete_acc(request, person_id):
    person = Person.objects.filter(pk=person_id).delete()
    return redirect('ubi:index')