from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
from random import choice
from markdown2 import Markdown

class NewWikiForm(forms.Form):
	title = forms.CharField(label="Wiki Title", widget=forms.TextInput(attrs={'autofocus': '', 'placeholder':'Enter wiki title here'}))
	content = forms.CharField(label="Wiki Content", widget=forms.Textarea(attrs={'placeholder':'Enter wiki content here. Markdown format supported'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def view_entry(request, title):
	if title in util.list_entries():
		converter = Markdown()
		product = converter.convert(util.get_entry(title))
		return render(request, "encyclopedia/entry.html", {"entry": product, "title": title})
	else:
		return render(request, "encyclopedia/entry.html", {"error": "404: The requested page does not exist", "title": "404: Not Found"})

def edit(request, title):
	form = NewWikiForm()
	form.content = util.get_entry(title)
	if title in util.list_entries():
		return render(request, "encyclopedia/edit.html", {"entry": util.get_entry(title), "form": form, "title": title})

def search(request):
	query = request.POST.get("q")
	entries = util.list_entries()
	if query in entries:
		return render(request, "encyclopedia/entry.html", {"entry": util.get_entry(query), "title": query})
	else:
		if query and query.strip():
			filtered = [x for x in entries if query in x]
			"""filtered = []
			for x in entries:
				if query in x:
					filtered.append(x)"""
			return render(request, "encyclopedia/search.html", {"search_results": filtered, "query": query})
	return render(request, "encyclopedia/index.html", {"entries": entries})

def addnew(request):
	if request.method == "POST":
		form = NewWikiForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data.get('title')
			content = form.cleaned_data.get('content')
			if title in util.list_entries():
				return render(request, "encyclopedia/addnew.html", {"form": form, "error": 'A wiki entry with this title already exists'})
			else:
				util.save_entry(title, content)
				return redirect('viewentry', title=title)

	return render(request, "encyclopedia/addnew.html", {"form": NewWikiForm})

def random(request):
	random_entry = choice(util.list_entries())
	return redirect('viewentry', title=random_entry)
