from django.contrib import admin
from .models import signup, bookvehicle,proceed,summary,payment
from .models import trucks
from .models import driver

# Register your models here.

admin.site.register(signup),
admin.site.register(bookvehicle),
admin.site.register(proceed),
admin.site.register(trucks),
admin.site.register(driver),
admin.site.register(summary),
admin.site.register(payment),