from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    #=====================================================================
    path("form1/", views.form1, name="form1"),
    path("form2/", views.form2, name="form2"),
    path("results/<favorite>/", views.results, name="results"),
    path("vote/", views.vote, name="vote"),
    #======================================================================
    path("form3/", views.form3, name="form3"),
    path("thanks/", views.thanks, name="thanks"),
    path("thanks_back/", views.thanks_back, name="thanks_back"),
    #======================================================================
    path("form4/", views.form4, name="form4"),
    path("modelform_to_model/", views.modelform_to_model, name="modelform_to_model"),
    #======================================================================
    path("simplepurchase/", views.simple_purchase, name="simplepurchase")
]