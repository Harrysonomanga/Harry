from django.contrib import admin
from django.urls import path
from novapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('partners/', views.partners, name='partners'),
    path('clients/', views.clients, name='clients'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('upload/', views.document_upload, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
