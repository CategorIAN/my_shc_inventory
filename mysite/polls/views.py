from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Department


def index(request):
    template = loader.get_template("polls/index2.html")
    #department = Department.objects.get(cost_center=cost_center)
    #context = {"department": department}
    context = {}
    return HttpResponse(template.render(context, request))

def results(request):
    return HttpResponse("Thankyou for your submission.")

def vote(request):
    return HttpResponseRedirect("/polls/results")
