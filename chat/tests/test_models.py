from chat.models import Chat, ChatRoom
from chat.tests.factories import ChatFactory, ChatRoomFactory
from django.test import TestCase
from users.factories import UserFactory


class ChatRoomTests(TestCase):
    def setUp(self):
        self.user_1 = UserFactory()
        self.user_2 = UserFactory()
        self.user_3 = UserFactory()

        self.chatroom_1 = ChatRoomFactory()
        self.chatroom_2 = ChatRoomFactory()

        self.chatroom_1.participants.add(self.user_1, self.user_2)
        self.chatroom_2.participants.add(self.user_2, self.user_3)

    def test_chatroom_model_creation(self):
        self.assertEqual(ChatRoom.objects.count(), 2)

    def test_participants_addition_to_chatroom_works(self):
        self.assertEqual(self.chatroom_1.participants.count(), 2)
        self.assertEqual(self.chatroom_2.participants.count(), 2)


class ChatTests(TestCase):
    def setUp(self):
        self.user_1 = UserFactory()
        self.user_2 = UserFactory()

        self.chatroom_1 = ChatRoomFactory()
        self.chatroom_2 = ChatRoomFactory()

        self.chatroom_1.participants.add(self.user_1, self.user_1)
        self.chatroom_2.participants.add(self.user_2, self.user_2)

        self.chat_1 = ChatFactory(author=self.user_1, room=self.chatroom_1)
        self.chat_1 = ChatFactory(author=self.user_2, room=self.chatroom_2)

    def test_chat_model_creation(self):
        self.assertEqual(Chat.objects.count(), 2)
