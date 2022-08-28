from django.shortcuts import render
from allauth.account.forms import SignupForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    form = SignupForm()
    context = {"form": form}
    return render(request, 'pages/home.html', context)

@login_required
def about(request):
    return render(request, 'pages/about.html')