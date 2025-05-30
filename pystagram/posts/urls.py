from django.urls import path
from users.views import feeds

urlpatterns = [
    path('feeds/', feeds),
]