from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from users.models import CustomUser

CustomUser = get_user_model()


class HomePageView(ListView, LoginRequiredMixin):
    model = CustomUser
    context_object_name = 'user_list'
    template_name = 'chat/home.html'
