from operator import imod
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("felipe",views.felipe,name="felipe"),
    path("david",views.david,name="david")

]