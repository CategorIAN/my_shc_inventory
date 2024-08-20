from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Department
from .forms import NameForm, ContactForm
from django.shortcuts import render


def index(request):
    template = loader.get_template("polls/index.html")
    #department = Department.objects.get(cost_center=cost_center)
    #context = {"department": department}
    context = {}
    return HttpResponse(template.render(context, request))

def form1(request):
    template = loader.get_template("polls/form1.html")
    context = {}
    return HttpResponse(template.render(context, request))

def form2(request):
    template = loader.get_template("polls/form2.html")
    department = Department.objects.get(cost_center=11000)
    context = {"department": department}
    return HttpResponse(template.render(context, request))

def results(request, favorite):
    template = loader.get_template("polls/results.html")
    context = {"favorite": favorite}
    return HttpResponse(template.render(context, request))

def vote(request):
    favorite = request.POST["favorite"]
    admin_dept = Department.objects.get(cost_center=11000)
    admin_dept.favorite = favorite
    admin_dept.save()
    return HttpResponseRedirect("/polls/results/{}".format(favorite))

def form3(request):
    form = ContactForm()
    rendered_form = form.render("polls/form_snippet.html")
    return render(request, "polls/form3.html", {"form": rendered_form})

def thanks(request):
    template = loader.get_template("polls/thanks.html")
    context = {}
    return HttpResponse(template.render(context, request))

def thanks_back(request):
    return HttpResponseRedirect("/polls/thanks")




