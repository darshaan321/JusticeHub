

# class Lawyer(models.Model):
#     name = models.CharField(max_length=100)
#     specialization = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     experience = models.IntegerField()
#     contact = models.CharField(max_length=15)

#     def _str_(self):
#         return self.name
from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    full_address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    file = models.FileField(upload_to='clients/', null=True, blank=True)

    def __str__(self):
        return self.first_name
    

def user_registration(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_Name')
        
        print(first_name)
        
        messages.success(request, "Registration Successful!")
        return redirect('user_registration')

    else:
     return render(request, 'lawyers/user_registration.html')
 


from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Lawyer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    profile_image = models.ImageField(upload_to='lawyers/', null=True, blank=True)  # 🔥 IMPORTANT

    degree = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    speciality = models.CharField(max_length=100)
    bar_id = models.CharField(max_length=50)
    

    def __str__(self):
        return self.first_name