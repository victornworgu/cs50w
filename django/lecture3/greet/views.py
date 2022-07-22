from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
def greet(request, name):
	return HttpResponse(f"Hello, {name.capitalize()}!")
"""
def greet(request, name):
	return render(request, "greet/index.html", {"name": name.capitalize()})
