from django.shortcuts import redirect
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
        return redirect(reverse("posts:feeds"))
    else:
        return redirect(reverse("users:login"))

