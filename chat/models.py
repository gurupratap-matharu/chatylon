import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class ChatRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    participants = models.ManyToManyField(get_user_model(), related_name='chatrooms')

    class Meta:
        ordering = ('created_on', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chatroom_detail', args=[str(self.id)])


class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='chats')
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='chats')

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_on', )

    def __str__(self):
        return self.body

    def can_update(self, user):
        return user.is_superuser or self.author == user

    def can_delete(self, user):
        return user.is_superuser or self.author == user
