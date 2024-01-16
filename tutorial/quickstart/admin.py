from django.contrib import admin
from .serializers import User, Group

# Register your models here.
admin.site.register(User, Group)