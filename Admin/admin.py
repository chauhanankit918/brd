from django.contrib import admin

# Register your models here.

from .models import Course  ,UserProfile
from .Leacturemodels import Lecture  

# Register your models here.

admin.site.register(Course),
admin.site.register(Lecture),
admin.site.register(UserProfile),