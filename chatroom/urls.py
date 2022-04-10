from django.urls import path
from . import views
from .views import MessageListView

urlpatterns = [
    path('', views.get_message, name='chatroom-home'),
]