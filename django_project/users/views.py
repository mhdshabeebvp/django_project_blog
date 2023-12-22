from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile  # Assuming you have a Profile model


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create or get a profile for the newly registered user
            profile, created = Profile.objects.get_or_create(user=user)

            messages.success(
                request, f"Your Account has been created! You are now able to login"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    # Retrieve or create the profile for the current user
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, "users/profile.html", {"profile": profile})
