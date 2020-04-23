from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


class PasswordResetModifiedView(PasswordResetView):
    def form_valid(self, form):
        if self.request.method == "POST":
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                return super().form_valid(form)
            form.errors['email'] = ' '
            error = 'The email address provided does not exist in our database'
            return render(self.request, 'users/password_reset.html', {'form': form, 'error': error})
