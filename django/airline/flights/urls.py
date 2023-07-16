from django.urls import path
from . import views

urlpatterns = [
	path("flights/", views.index, name="index")

]
