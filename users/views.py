from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, UpdateView
from rest_framework import generics

from users.models import Profile
from users.permissions import IsAuthorOrReadOnly, IsProfileAuthorOrReadOnly
from users.serializers import ProfileSerializer, UserSerializer


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


class UserListAPIView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsAuthorOrReadOnly,)


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsAuthorOrReadOnly,)


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsProfileAuthorOrReadOnly,)


class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsProfileAuthorOrReadOnly,)
