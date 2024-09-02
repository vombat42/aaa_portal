from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found

import commune
from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('captcha/', include('captcha.urls')),
    path('', index, name='home'),
    path('', include('modules.system.urls', namespace='system')),
    path('game/', include('commune.urls', namespace='commune')),
]

from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
if DEBUG:
    # add debug toolbar only for DEBUG mode
    # urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))

    # for show media files in DEBUG mode
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

# handler404 = 'django_homehelper.views.page_not_found'
handler404 = page_not_found

# Настройка админ панели
admin.site.site_header = 'Панель администрирования сайта'
admin.site.index_title = 'Портал ААА'