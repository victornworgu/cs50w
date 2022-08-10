from django.urls import path
from . import  views

app_name = "hello"
urlpatterns = [
	path("", views.index, name="index"),
	path("victor", views.victor),
	path("multiply", views.multiply),
	path("x", views.x)
]
