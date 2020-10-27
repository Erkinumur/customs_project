from django.contrib import admin

from admin_panel.models import *

admin.site.register(Client)
admin.site.register(Driver)
admin.site.register(Order)
admin.site.register(Worker)