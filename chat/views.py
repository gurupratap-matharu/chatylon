import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.forms import Form
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin

from chat.forms import ChatForm
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


class ChatDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = ChatRoom
    context_object_name = 'chatroom'
    template_name = 'chat/chatroom_detail.html'
    form_class = ChatForm
    success_message = 'Message sent successfully!'

    def get_success_url(self):
        return reverse_lazy('chat:chatroom_detail',
                            args=[self.kwargs['user_1'], self.kwargs['user_2']])

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

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            logger.info('valid form recieved...')
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.room = self.get_object()
        form.instance.author = self.request.user
        form.save()
        messages.success(self.request, self.success_message)
        logger.info('saved chat with form...%s', form)
        return super().form_valid(form)
