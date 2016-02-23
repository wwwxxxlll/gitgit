from django.contrib import admin

# Register your models here.

from blog.models import *

admin.site.register(lanmu)
admin.site.register(wenzhang,Adisplay)
admin.site.register(pinglun)
admin.site.register(AdminM)
admin.site.register(Group)

