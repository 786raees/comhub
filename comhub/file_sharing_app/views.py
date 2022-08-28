from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from file_sharing_app.models import File
from .forms import CustomerForm, FileForm
# Create your views here.
User = get_user_model()


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


@login_required
def update_user(request, username):
    user = User.objects.filter(username=username, customer_of=request.user).first()
    form = CustomerForm(request.POST or None, instance=user)
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


@login_required
def customer_file_page(request, username):
    customer = User.objects.filter(username=username, customer_of=request.user).first()
    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        file = form.save(commit=False)
        file.uploader = request.user
        file.assigned_to = customer
        file.save()
        form = FileForm()
    context = {
        "customer": customer,
        "form": form,
    }
    return render(request, 'pages/customer_file_page.html', context)


@login_required
def customer_file_upload_page(request, username, file_id):
    customer = User.objects.filter(username=username, customer_of=request.user).first()
    file = File.objects.filter(id=file_id).first()
    form = FileForm(request.POST or None, request.FILES or None, instance=file or None)
    if form.is_valid():
        file = form.save(commit=False)
        file.uploader = request.user
        file.assigned_to = customer
        file.save()
        return redirect("customer_file_page", username=(customer.username))
    context = {
        "customer": customer,
        "form": form,
    }
    return render(request, 'pages/customer_file_page.html', context)

@login_required
def delete_file(request, file_id):
    file = File.objects.filter(id=file_id).first()
    file.delete()
    return redirect("customer_file_page", username=(file.assigned_to.username))
