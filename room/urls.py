from django.urls import path
from .views import RoomListView,RoomDetailView


urlpatterns = [
    path('list/',RoomListView.as_view(),name='room_list'),
    path('<slug:slug>/detail/',RoomDetailView.as_view(),name='room_detail'),
]