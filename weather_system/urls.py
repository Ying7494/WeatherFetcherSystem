"""weather_system URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url
from dashboard import views



# URL Mapping
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', views.dashboard),
    url(r'^login/', views.login),
    url(r'^api/login/', views.login_post),
    url(r'^api/logout/', views.logout_post),
    url(r'^api/weather/', views.weatherAPI),
    url(r'^api/getWeather/', views.getWeatherAPI),
    url(r'^cron/weather/', views.getWeather),
]
