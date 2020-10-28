from django.conf.urls.static import static

from . import settings
from django.contrib import admin
from django.urls import path, include
from admin_panel.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('client/', include('orders.urls')),
    path('admin_panel/', include('admin_panel.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)