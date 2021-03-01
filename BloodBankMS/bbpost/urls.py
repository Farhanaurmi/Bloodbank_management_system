"""BloodBankMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bbpost_home, name='bbpost_home'),
    path('cpost', views.cpost, name='cpost'),
    path('dpost/<int:d_id>/', views.dpost, name='dpost'),
    path('mypostd/<int:m_id>/', views.mypostd, name='mypostd'),
    path('mypost/', views.mypost, name='mypost'),
    path('mypostd/<int:m_id>/delete', views.mypostdelete, name='mypostdelete'),

]
