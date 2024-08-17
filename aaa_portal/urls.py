from django.contrib import admin
from django.urls import path, include

import commune

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('game/', include('commune.urls', namespace='commune')),
]
