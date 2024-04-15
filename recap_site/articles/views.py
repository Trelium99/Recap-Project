from django.shortcuts import render
from .forms import CreateUserForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from functools import wraps
# Create your views here.

all_things_to_read = [
    {"title": "Space Ships",
     "description": "Not all ships are the same lets take a look!",
     "author": "Jason",
     "date": "2024/04/11",
     "content": "aihjbssib piAUFHSipfuhgAS FJhbdFPKSbgj ajsdFHspiodfuhas dopfjahdgjahg asfpdgjhasdipfgh ",
     "slug": "post1"},

     {"title": "Im different",
     "description": "Not all ships are the same lets take a look!",
     "author": "Jason",
     "date": "2024/04/11",
     "content": "aihjbssib piAUFHSipfuhgAS FJhbdFPKSbgj ajsdFHspiodfuhas dopfjahdgjahg asfpdgjhasdipfgh ",
     "slug": "post2"},

     {"title": "Something else",
     "description": "Not all ships are the same lets take a look!",
     "author": "Jason",
     "date": "2024/04/11",
     "content": "aihjbssib piAUFHSipfuhgAS FJhbdFPKSbgj ajsdFHspiodfuhas dopfjahdgjahg asfpdgjhasdipfgh ",
     "slug": "post3"},
]

def logged_in_already(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if args[0].user.is_authenticated:
            return HttpResponseRedirect(reverse("all_reads"))
        return function(*args, **kwargs)
    return decorated_function


@logged_in_already
def home(request):
    return render(request, "articles/index.html")


@logged_in_already
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            form_username = request.POST.get('username')
            form_password = request.POST.get('password')
            
            user = authenticate(request, username=form_username, password=form_password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("all_reads"))
    return render(request, "articles/login.html", {
        "form":form,
    })

@logged_in_already
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login-page"))
    return render(request, "articles/register.html", {
        "form":form,
    })

@login_required(login_url="login-page")
def all_reads(request):
    return render(request, "articles/all-reads.html", {
        "articles": all_things_to_read,
    })

@login_required(login_url="login-page")
def posts(request, posts_slug):
    for item in all_things_to_read:
        if item["slug"] == posts_slug:
            found_post = item
    return render(request, "articles/indiv-posts.html", {
        "item": found_post,
    })

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("home-page"))