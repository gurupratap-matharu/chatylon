from django.urls import path

from users.views import ProfileCreate, ProfileDetailView, ProfileUpdate

urlpatterns = [
    path('create/', ProfileCreate.as_view(), name='profile_create'),
    path('<uuid:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('<uuid:pk>/update', ProfileUpdate.as_view(), name='profile_update'),
]
