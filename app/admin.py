from django.contrib import admin

# Register your models here.
from .models import data
 
admin.site.register(data)

from .models import user_data
 
admin.site.register(user_data)

from .models import UserInput
 
admin.site.register(UserInput)


