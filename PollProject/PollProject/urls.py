from django.contrib import admin
from django.urls import include, path

from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),           # URL для административной панели
    path('polls/', include('pollsapp.urls', namespace = 'polls')),# Подключение URL-ов из приложения pollsapp
    path('', RedirectView.as_view(url='/polls/', permanent=True)),
    path('api/', include('api.urls')),
]


