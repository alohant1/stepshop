from django.urls import path

from mainapp.views import index, contacts, productone

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('productone/', productone, name='productone'),

]
