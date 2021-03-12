from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Proff)
admin.site.register(Module)
admin.site.register(Level)
admin.site.register(Course)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Program)
