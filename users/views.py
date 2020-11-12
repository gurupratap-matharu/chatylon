from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, UpdateView

from users.models import Profile


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'users/profile_detail.html'


class ProfileCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Profile
    fields = ['bio', 'location', 'country', 'birth_date']
    template_name = 'users/profile_form.html'
    success_message = 'Profile created successfully!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ['bio', 'location', 'country', 'birth_date']
    template_name = 'users/profile_update_form.html'
    success_message = 'Profile updated successfully!'
