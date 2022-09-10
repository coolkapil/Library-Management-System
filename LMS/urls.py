"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/signup/", views.SignUpView.as_view(), name="signup"),
    path("staff/signup/", views.AdminSignUpView.as_view(), name="admin-signup"),
    path('user/', include('django.contrib.auth.urls')),

    path('', views.BookList.as_view(), name='book-list'),
    path('book/<int:pk>', views.BookDetail.as_view(), name='book-detail'),
    path('book/create', views.BookCreate.as_view(), name='book-create'),
    path('book/update/<int:pk>', views.BookUpdate.as_view(), name='book-update'),
    path('book/delete/<int:pk>', views.BookDelete.as_view(), name='book-delete'),

]
