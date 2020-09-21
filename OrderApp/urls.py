from django.conf.urls import url

from OrderApp import views

urlpatterns = [
    url(r'^order/',views.order,name='order'),
    url(r'^orderDetail/',views.orderDetail,name='orderDetail'),
    url(r'^testPay/',views.testPay,name='testPay'),
]