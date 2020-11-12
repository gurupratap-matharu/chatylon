from django.urls import path

from chat.views import HomePageView

app_name = 'chat'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
