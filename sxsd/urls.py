"""sxsd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sxsdhome/',include('HomeApp.urls',namespace='sxsdhome')),
    url(r'^sxsdmarket/',include('MarketApp.urls',namespace='sxsdmarket')),
    url(r'^sxsdcart/',include('CartApp.urls',namespace='sxsdcart')),
    url(r'^sxsdmine/',include('MineApp.urls',namespace='sxsdmine')),
    url(r'^sxsduser/',include('UserApp.urls',namespace='sxsduser')),
    url(r'^sxsdorder/',include('OrderApp.urls',namespace='sxsdorder')),
]
