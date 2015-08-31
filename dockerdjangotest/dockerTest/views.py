from django.shortcuts import render, redirect
from dockerTest.models import Person
from dockerTest.forms import modelForm
import pdb
# Create your views here.
def home(request):
	persons = Person.objects.all()
	mf = modelForm()
	return render(request, 'home.html', {'persons':persons, 'form':mf} )

def saveData(request):
	per = Person(name=request.POST.get('name'), number=request.POST.get('phone'))
	per.save()
	return redirect('home')