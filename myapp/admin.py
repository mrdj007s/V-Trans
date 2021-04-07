from django.contrib import admin
from .models import signup
from .models import bookvehicle
from .models import proceed 
from .models import summary
from .models import payment
from .models import trucks
from .models import driver
from .models import contactus, Transaction

# Register your models here.

admin.site.register(signup),
admin.site.register(bookvehicle),
admin.site.register(proceed),
admin.site.register(trucks),
admin.site.register(driver),
admin.site.register(summary),
admin.site.register(payment),
admin.site.register(contactus),
admin.site.register(Transaction)