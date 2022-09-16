from django.contrib import admin
from .models import Distribution, Client, Message


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
# Register your models here.
