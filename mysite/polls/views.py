from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
'''
from .models import (SimplePurchaseForm, PurchaseForm, Employee, Department, Item_Purchase, Purchase,
                     Item_Purchase_Form, RIPF)
'''
from django.shortcuts import render
from django.forms import modelformset_factory

def index(request):
    return render(request, "polls/index.html", {})

def thanks(request):
    return render(request, "polls/thanks.html", {})

def do_nothing(request):
    return HttpResponseRedirect("/polls/thanks")
'''
def simple_purchase(request):
    return render(request, "polls/simplepurchase.html", {"form": SimplePurchaseForm()})

def modelform_to_model(request):
    SimplePurchaseForm(request.POST).save()
    return HttpResponseRedirect("/polls/thanks")

def purchase_initial(request):
    return render(request, "polls/purchase_initial.html", {"form": PurchaseForm()})

def enter_initial(request):
    initial = PurchaseForm(request.POST)
    employee, dept = initial.data['employee'], initial.data['dept']
    return HttpResponseRedirect("/polls/purchase_items/{}/{}".format(employee, dept))

def purchase_items(request, employee, dept):
    employee = Employee.objects.get(id=employee)
    dept = Department.objects.get(cost_center=dept)
    purchase = Purchase(employee=employee, dept=dept)
    print("----------------------------------------------------------------")
    f = RIPF()
    print(f)
    print("=========================")
    RIPFormSet = modelformset_factory(Item_Purchase, form=RIPF, min_num=3)
    print("~~~~~~~~~~~~")
    formset = RIPFormSet(queryset=Item_Purchase.objects.none())
    context = {"employee": employee, "dept": dept, "formset": formset}
    return render(request, "polls/purchase_items.html", context)

def submit_purchase(request, employee, dept):
    purchase = Purchase(employee_id=employee, dept_id=dept)
    RIPFormSet = modelformset_factory(Item_Purchase, form=RIPF)
    formset = RIPFormSet(request.POST)
    formset.save()

    return HttpResponseRedirect("/polls/thanks")
'''




