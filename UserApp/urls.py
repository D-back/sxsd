from django.conf.urls import url

from UserApp import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^get_code',views.get_code),
    url(r'^ajax_username/',views.ajax_username,name='ajax_username'),
    url(r'^active/',views.active,name='active'),
    url(r'^logout/', views.logout, name='logout')

]
