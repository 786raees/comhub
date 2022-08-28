from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
# Create your views here.


@login_required
def home(request):
    initial = {'email':  '@gmail.com'}
    form = CustomerForm(request.POST or None, initial=initial)
    if form.is_valid():
        customer_object = form.save(commit=False)
        customer_object.user_type = 'Customer'
        customer_object.customer_of = request.user
        customer_object.save()
        form = CustomerForm(initial=initial)
    context = {"form": form}
    return render(request, 'pages/home.html', context)


User = get_user_model()


@login_required
def update_user(request, username):
    user = User.objects.filter(username=username, customer_of=request.user).first()
    form = CustomerForm(request.POST or None,instance=user)
    if form.is_valid():
        customer_object = form.save(commit=False)
        customer_object.user_type = 'Customer'
        customer_object.customer_of = request.user
        customer_object.save()
        return redirect("home")
    context = {"form": form}
    return render(request, 'pages/home.html', context)


@login_required
def about(request):
    return render(request, 'pages/about.html')
