import factory
from chat.models import Chat, ChatRoom
from users.factories import UserFactory


class ChatRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChatRoom

    name = factory.Faker('word')


class ChatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Chat

    body = factory.Faker('sentence')
    author = factory.SubFactory(UserFactory)
    room = factory.SubFactory(ChatRoom)
