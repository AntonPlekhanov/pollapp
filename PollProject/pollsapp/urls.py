from django.urls import path, include
from . import views

app_name = 'pollsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('<int:poll_id>/results/', views.results, name='results'),
    path('polls/create/', views.create_poll_and_choices, name='create_poll_and_choices'),
    path('api/', include('api.urls')),
]




