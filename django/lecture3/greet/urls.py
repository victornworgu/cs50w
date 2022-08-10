from django.urls import path
from . import  views

app_name = "greet"
urlpatterns = [
	path("<str:name>", views.greet, name="greet")
]
