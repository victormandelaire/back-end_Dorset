from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Tank
from .forms import TankForm


def tanks_app(request):
  template = loader.get_template('page.html') #Main page of the app
  return HttpResponse(template.render())

def tanks_desc(request):  #Page with all data
  mytanks = Tank.objects.all().values()
  template = loader.get_template('all_tanks.html')
  context = {
  'mytanks' : mytanks,
  }
  return HttpResponse(template.render(context, request))



def create(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = TankForm(request.POST or None)
    if form.is_valid():
      form.save()

    context['form'] = form
    return render(request, "create.html", context)

def update(request, id): #to go to the form to modify details of a tank
  mytank = Tank.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mytank': mytank,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id): #to update the information the user entered in the database and the page
  first = request.POST['first']
  second = request.POST['second']
  third = request.POST['third']
  last = request.POST['last']
  tank = Tank.objects.get(id=id)
  tank.tankname = first
  tank.nationality = second
  tank.crewmates_num = third
  tank.turret = last
  tank.save()
  context = { 'tank' : tank}
  template = loader.get_template('return_update.html')
  return HttpResponse(template.render(context, request))

def delete(request, id): #to delete a tank
  tank = Tank.objects.get(id=id)
  tank.delete()
  template = loader.get_template('return_delete.html')
  context = {}
  return HttpResponse(template.render(context, request))


