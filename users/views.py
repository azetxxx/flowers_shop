from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from common.views import CommonContextMixin
from django.core.mail import send_mail

from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import User, EmailVerification


class UserLoginView(CommonContextMixin, LoginView):
    template_name = 'users/login.html'
    title = 'Login 🌼 Fun Flowers'
    form_class = UserLoginForm


class UserRegistrationView(CommonContextMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    title = 'Sign Up 🌼 Fun Flowers'
    success_url = reverse_lazy('users:login')
    success_message = 'Fantastic! Check your email and hit that activation link to start your floral adventure 🌼 Fun Flowers'


class UserProfileView(CommonContextMixin, TemplateView):
    template_name = 'users/profile.html'
    title = 'Profile 🌼 Fun Flowers'


class OrderListView(CommonContextMixin, TemplateView):
    template_name = 'users/order-list.html'
    title = 'History 🌼 Fun Flowers'


class UserLoginSettingsView(CommonContextMixin, UpdateView):
    model = User
    template_name = 'users/login-settings.html'
    title = 'Login Settings 🌼 Fun Flowers'
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:login-settings', args=(self.object.id,))


class EmailVerificationView(CommonContextMixin, TemplateView):
    template_name = 'users/email-verification.html'
    title = 'Verified 🌼 Fun Flowers'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))




@login_required
def wishlist(request):
    context = {
        'title': 'Wishlist 🌼 Fun Flowers',
    }
    return render(request, 'users/wishlist.html', context)
