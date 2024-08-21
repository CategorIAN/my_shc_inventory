from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Department, AuthorForm, Author, SimplePurchaseForm, SimplePurchase
from .forms import ContactForm
from django.shortcuts import render


def index(request):
    template = loader.get_template("polls/index.html")
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

def form4(request):
    form = AuthorForm()
    return render(request, "polls/form4.html", {"form": form})

def simple_purchase(request):
    return render(request, "polls/simplepurchase.html", {"form": SimplePurchaseForm()})

def modelform_to_model(request):
    SimplePurchaseForm(request.POST).save()
    return HttpResponseRedirect("/polls/thanks")





