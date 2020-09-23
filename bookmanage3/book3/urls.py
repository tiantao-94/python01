from django.urls import path
from book3.views import index

urlpatterns = [
    path('index/', index)
]