from django.contrib import admin
from django.urls import path

from my_app import views

import os
from dotenv import load_dotenv
load_dotenv()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('addnew',views.addnew, name='addnew'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy, name='destroy'),
]
