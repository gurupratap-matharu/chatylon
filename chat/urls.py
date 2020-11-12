from django.urls import path

from chat.views import ChatDetailView, HomePageView

app_name = 'chat'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<uuid:pk>/', ChatDetailView.as_view(), name='chat_detail'),
]
