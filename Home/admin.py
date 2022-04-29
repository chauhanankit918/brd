from django.contrib import admin

# Register your models here.

# Register your models here.

from .models import query_form , slider , q_form   ,email_data

# Register your models here.

admin.site.register(query_form),
admin.site.register(slider),
admin.site.register(q_form),
admin.site.register(email_data),