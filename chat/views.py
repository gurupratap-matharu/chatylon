from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from chat.models import ChatRoom

CustomUser = get_user_model()


class HomePageView(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = 'user_list'
    template_name = 'chat/home.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(email=self.request.user.email)


class ChatDetailView(LoginRequiredMixin, DetailView):
    model = ChatRoom
    context_object_name = 'chatroom'
    template_name = 'chat/chat_detail.html'
