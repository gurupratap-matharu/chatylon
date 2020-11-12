from django.urls import path

from chat.views import ChatDetailView, HomePageView

app_name = 'chat'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:user_1>/<int:user_2>/chat/', ChatDetailView.as_view(), name='chatroom_detail'),
]
