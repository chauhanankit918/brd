from django.contrib import admin

# Register your models here.

# from .models import Course  
from .models import  Student_detail ,Order,Student_Payment

# Register your models here.

admin.site.register(Student_detail),
admin.site.register(Order),
admin.site.register(Student_Payment),