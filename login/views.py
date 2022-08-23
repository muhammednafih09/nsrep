from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static


def login(request):
    return render(request,"dashboard/index.html")