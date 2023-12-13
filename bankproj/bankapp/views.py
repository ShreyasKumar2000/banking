# banking_app/views.py
from dal import autocomplete
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse

from .forms import CustomerForm

from django.contrib.auth import authenticate, login,logout

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import District, Branch


def home(request):
    return render(request, 'home.html')

#
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        c_password = request.POST.get('password2')

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('/register')
            else:
                cred = User.objects.create_user(username=username, password=password)
                cred.save()
        else:
            messages.info(request, "Passwords do not match")
            return redirect('/register')

        return redirect('/login')

    return render(request, "register_user.html")


def new_page(request):
    return render(request, 'new_page.html')

#
# def form_page(request):
#
#     if request.method == 'POST':
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             message = "Application accepted"
#             return render(request, 'form_page.html', {'message': message})
#     else:
#         form = CustomerForm()
#     return render(request, 'form_page.html', {'form': form})
# def get_branches(request, district_id):
#     branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
#     return JsonResponse({'branches': list(branches)})
#
#
# def load_branches(request):
#     district_id = request.GET.get('district_id')
#     branches = Branch.objects.filter(district_id=district_id)
#     data = [{'id': branch.id, 'name': branch.name} for branch in branches]
#
#     return JsonResponse(data, safe=False)

    # return render(request,"branches.html",{"branches":branches})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
#
def form_page(request):
    districts = District.objects.all()
    selected_district = None
    branches = None

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            print("Form saved successfully!")
        return render(request, 'application_accepted.html')



    else:
        form = CustomerForm()

    if 'district' in request.GET:
        selected_district_id = request.GET['district']
        selected_district = District.objects.get(id=selected_district_id)
        branches = Branch.objects.filter(district=selected_district)

    return render(request, 'form_page.html', {'form': form, 'districts': districts, 'selected_district': selected_district, 'branches': branches})

def get_branches(request):
    selected_district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=selected_district_id)

    branch_options = [{'id': branch.id, 'name': branch.name} for branch in branches]

    return JsonResponse(branch_options, safe=False)

