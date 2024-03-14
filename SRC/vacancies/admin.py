from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(vacancy)

# diliya
admin.site.register(Cvdetails)
admin.site.register(Skill)
admin.site.register(Media)
admin.site.register(Portfolio)

# sathma
admin.site.register(comregister)


# pasindu
admin.site.register(Student)
