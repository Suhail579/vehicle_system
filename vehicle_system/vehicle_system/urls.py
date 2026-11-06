"""
URL configuration for vehicle_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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


from inventory import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path("vehiclelist" , views.Vehiclelist.as_view()),
    path("vehicledetails/<int:id>", views.Vehicledetails.as_view()),
    path("bookinglist", views.Bookinglist.as_view()),
    path("bookingdetails/<int:id>", views.Bookingdetails.as_view()),
]
