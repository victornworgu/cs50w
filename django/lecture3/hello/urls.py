from django.urls import path
from . import  views

urlpatterns = [
	path("", views.index, name="index"),
	path ("victor", views.victor),
	path ("multiply", views.multiply)
]
