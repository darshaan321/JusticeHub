from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Lawyer


# Home
def index(request):
    return render(request, 'lawyers/index.html')


# About
def about(request):
    return render(request, 'lawyers/about.html')


# Login
def user_login(request):
    return render(request, 'lawyers/login.html')


# Services
def service(request):
    return render(request, 'lawyers/service.html')


def lawyer_registration(request):
    return render(request, 'lawyers/lawyer_registration.html')

# ✅ Lawyers List + Search
def lawyers(request):
    
    query = request.GET.get('q')

    if query:
        lawyers = Lawyer.objects.filter(name__icontains=query)
    else:
        lawyers = Lawyer.objects.all()

    return render(request, 'lawyers/lawyers.html', {'lawyers': lawyers})


# ✅ Lawyer Detail Page (IMPORTANT)
def lawyer_detail(request, id):
    lawyer = get_object_or_404(Lawyer, id=id)
    return render(request, 'lawyers/lawyer_detail.html', {'lawyer': lawyer})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Lawyer

from django.shortcuts import render, redirect
from .models import Lawyer

def lawyer_registration(request):
    if request.method == 'POST':
        Lawyer.objects.create(
            first_name=request.POST.get('first_Name'),
            last_name=request.POST.get('last_Name'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            contact_number=request.POST.get('contact_number'),
            degree=request.POST.get('degree'),
            address=request.POST.get('full_address'),
            city=request.POST.get('city'),
            experience=request.POST.get('practise_Length'),
            speciality=request.POST.get('speciality'),
            bar_id=request.POST.get('bar_id')
        )

        return redirect('lawyer_registration')

    return render(request, 'lawyers/lawyer_registration.html')

    #     # Password check
    #     if password != confirm_password:
    #         return render(request, 'lawyer_register.html', {'error': 'Passwords do not match'})

    #     # Create User
    #     user = User.objects.create_user(
    #         username=email,
    #         email=email,
    #         password=password
    #     )

    #     # Save Lawyer
    #     Lawyer.objects.create(
    #         user=user,
    #         first_name=first_name,
    #         last_name=last_name,
    #         contact=contact,
    #         degree=degree,
    #         address=address,
    #         city=city,
    #         experience=experience,
    #         speciality=speciality,
    #         bar_id=bar_id,
    #         case_handle=",".join(case_handle),
    #         profile_image=image
    #     )

    #     return redirect('login')

    # return render(request, 'lawyer_register.html')


# ✅ User Registration
def user_registration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_Name')
        last_name = request.POST.get('last_Name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        full_address = request.POST.get('full_address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        file = request.FILES.get('fileToUpload')

        Client.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact_number=contact_number,
            full_address=full_address,
            city=city,
            zip_code=zip_code,
            file=file
        )

        return redirect('user_registration')

    return render(request, 'lawyers/user_registration.html')