from django.conf.urls import url

from CartApp import views

urlpatterns = [
    url(r'^cart/',views.cart,name='cart'),
    url(r'^addToCart/',views.addToCart),
    url(r'^reduceFromCart/',views.reduceFromCart),
    url(r'^modifyGoodsNum/',views.modifyGoodsNum),
    url(r'^select/',views.select),
    url(r'^allselect/',views.allselect),

]