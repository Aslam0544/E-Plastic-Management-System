"""
URL configuration for EPlasticManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from django.views.generic import TemplateView
from plasticmanagement.views import login, logout, adduser, adminviewusers, deleteuser, addwastageaction, viewwastages, \
    acceptorrejectwastage, \
    assignwastage, agentwastageupdate, deletewastage, getwastage

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='index.html'), name='login'),

    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('loginaction/', login, name='loginaction'),

    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),

    path('adduser/', TemplateView.as_view(template_name='adduser.html'), name='adduser'),
    path('adduseraction/',adduser, name='adduser'),
    path('viewusers/',adminviewusers, name='view users'),
    path('deleteuser/',deleteuser, name='delete user'),

    path('addwastage/', TemplateView.as_view(template_name='addwastage.html'), name='addwastage'),
    path('addwastageaction/',addwastageaction, name='addwastage'),
    path('viewwastages/', viewwastages, name='view wastages'),

    path('acceptorrejectwastage/',acceptorrejectwastage, name='accept or reject'),

    path('getwastage/', getwastage, name='getwastage'),
    path('assignwastageaction/', assignwastage, name='assign'),
    path('agentwastageupdateaction/', agentwastageupdate, name='agent update'),

    path('deletewastage/', deletewastage, name='delete wastage'),

    path('logout/', logout, name='logout'),
]
