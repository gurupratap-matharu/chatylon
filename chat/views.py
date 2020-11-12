import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from chat.models import ChatRoom

CustomUser = get_user_model()

logger = logging.getLogger(__name__)


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
    template_name = 'chat/chatroom_detail.html'

    def get_object(self):
        user_1, user_2 = self.kwargs['user_1'], self.kwargs['user_2']
        logger.info('user_1: %s', user_1)
        logger.info('user_2: %s', user_2)

        chatroom = ChatRoom.objects.filter(participants=user_1).filter(participants=user_2)
        logger.info('chatroom: %s', chatroom)
        if not chatroom:
            logger.info('creating new chatroom. hold on...')
            chatroom = ChatRoom.objects.create()
            chatroom.participants.add(user_1)
            chatroom.participants.add(user_2)
            logger.info('chatroom created and participants added!')
            logger.info(chatroom.participants.all())
            return chatroom
        return chatroom[0]
