from django.urls import path
from book2.views import index
urlpatterns = [
    path('index/', index)
]