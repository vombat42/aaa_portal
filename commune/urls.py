from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.defaults import page_not_found

from aaa_portal import settings
from commune import views

app_name = 'commune'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Проект \"Коммуна\""