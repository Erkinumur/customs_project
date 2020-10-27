from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('orders.urls')),
    path('admin_panel/', include('admin_panel.urls'))
]
