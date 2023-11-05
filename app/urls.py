from django.urls import path
from .views import *

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('signup', SignUp.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('create', CreateAnimal.as_view(), name='create'),
]
