from django.urls import path

from mainapp.views import index, contacts, productone, products, about

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('productone/', productone, name='productone'),
    path('products/', products, name='products'),
    path('about/', about, name='about'),

]
