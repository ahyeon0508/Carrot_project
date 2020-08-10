"""Carrot_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from management import views

# router = routers.DefaultRouter()
# router.register(r'carrot', views.Carrot_status_list)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Carrot_status_list.as_view(), name='carrots'),
    path('carrots/', views.Carrot_status_list.as_view(), name='carrots-status-list'),
    path('carrots/write/', views.Carrot_status_write.as_view(), name='carrots-status-write'),
    path('carrots/<int:pk>/', views.Carrot_status_retrieve.as_view(), name='carrots-status-retrieve'),
    path('carrots/<int:pk>/update/', views.Carrot_status_update.as_view(), name='carrots-status-update'),
    path('carrots/<int:pk>/delete/', views.Carrot_status_delete.as_view(), name='carrots-status-delete'),

    path('carrots/current-status/', views.CurrentCarrotStatus.as_view(), name='current-carrots-status'),
    path('carrots/current-carrot-img/', views.CarrotCarrotImage.as_view(), name='currnet-carrot-img'),
    path('carrots/get-action/', views.Carrot_Action.as_view(), name='get-action'),

]

