from django.urls import path
from .views import chat_page, ChatBotView  # import your views

urlpatterns = [
    path('', chat_page, name='home'),         # Root URL (optional)
    path('chat/', chat_page, name='chat_page'),  # Now /chat/ works
    path('api/chat/', ChatBotView.as_view(), name='chat_api'),
]

        
  
