from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data()
        context["title"] = "Login 🌼 Fun Flowers"
        return context


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        context["title"] = "Sign Up 🌼 Fun Flowers"
        return context


class UserProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context["title"] = "Profile 🌼 Fun Flowers"
        return context


class OrderListView(TemplateView):
    template_name = 'users/order-list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data()
        context["title"] = "History 🌼 Fun Flowers"
        return context


class UserLoginSettingsView(UpdateView):
    model = User
    template_name = 'users/login-settings.html'
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:login-settings', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserLoginSettingsView, self).get_context_data()
        context["title"] = "Login Settings 🌼 Fun Flowers"
        return context


@login_required
def wishlist(request):
    context = {
        'title': 'Wishlist 🌼 Fun Flowers',
    }
    return render(request, 'users/wishlist.html', context)


# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Success! Your signup was successful!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm

#     context = {
#         'title': 'Sign Up 🌼 Fun Flowers',
#         'form': form
#     }
#     return render(request, 'users/registration.html', context)


# @login_required
# def account(request):
#     context = {
#         'title': 'My Account 🌼 Fun Flowers',
#     }
#     return render(request, 'users/account.html', context)


# def login_settings(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:login-settings'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)

#     context = {
#         'form': form,
#         'title': 'Login Settings 🌼 Fun Flowers',
#     }
#     return render(request, 'users/login-settings.html', context)
