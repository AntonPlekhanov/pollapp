

from django.urls import path
from .views import PollListView, PollDetailView, VoteListView  # Исправлен импорт

urlpatterns = [
    path('polls/', PollListView.as_view(), name='poll_list'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    # path('choices/', ChoiceListView.as_view(), name='choice_list'),  # Удалена строка с ChoiceListView
    # path('choices/<int:pk>/', ChoiceDetailView.as_view(), name='choice_detail'), # Удалена строка с ChoiceDetailView
    path('votes/', VoteListView.as_view(), name='vote_list'),
    #path('votes/<int:pk>/', VoteDetailView.as_view(), name='vote_detail'),
]
