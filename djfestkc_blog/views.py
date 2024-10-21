from django.shortcuts import render, redirect

# Create your views here.

# Added to redirect from a usually valid home or index page to a valid url
def redirect_view(request):
    response = redirect('/admin')
    return response
