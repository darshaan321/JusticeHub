from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),   # ⚠️ changed
    path('service/', views.service, name='service'),
    path('lawyer_registration/', views.lawyer_registration, name='lawyer_registration'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('lawyers/', views.lawyers, name='lawyers'),
    path('lawyer/<int:id>/', views.lawyer_detail, name='lawyer_detail')
    
   
]
