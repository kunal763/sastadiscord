from django.contrib import admin
from .models import Topic,Message,Room
# Register your models here.
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Room)
