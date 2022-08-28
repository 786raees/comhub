from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
# Create your views here.

@login_required
def home(request):
    initial = {'email':'@gmail.com'}
    form = CustomerForm(request.POST or None, initial=initial)
    if form.is_valid():
        customer_object = form.save(commit=False)
        customer_object.user_type = 'Customer'
        customer_object.save()
        form = CustomerForm(initial=initial)
    context = {"form": form}
    return render(request, 'pages/home.html', context)

@login_required
def about(request):
    return render(request, 'pages/about.html')