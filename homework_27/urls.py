"""
URL configuration for homework_27 project.

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

from ads.views import DownloadAdsView, AdsView, AllAdsView
from categories.views import DownloadCategoriesView, CategoryView, AllCatergoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dads/', DownloadAdsView.as_view()),
    path('dcat/', DownloadCategoriesView.as_view()),
    path('ad/', AllAdsView.as_view()),
    path('cat/', AllCatergoryView.as_view()),
    path('ad/<int:pk>', AdsView.as_view(), name='ads'),
    path('cat/<int:pk>', CategoryView.as_view(), name='category'),
]
