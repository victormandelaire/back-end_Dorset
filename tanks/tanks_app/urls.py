from django.urls import path
from . import views

urlpatterns = [
    path('tanks_app/', views.tanks_app, name='tanks_app'), #links the content of views.py to display it.
    path('tanks_app/tanks_desc/', views.tanks_desc, name='tanks_desc'),
    path('tanks_app/create/', views.create, name='create'),
    path('tanks_app/tanks_desc/update/<int:id>', views.update, name='update'),
    path('tanks_app/tanks_desc/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('tanks_app/tanks_desc/delete/<int:id>', views.delete, name='delete'),
]