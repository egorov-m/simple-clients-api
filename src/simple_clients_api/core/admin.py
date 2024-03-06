from django.contrib import admin

from simple_clients_api.core import models


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Child)
class ChildAdmin(admin.ModelAdmin):
    ...


@admin.register(models.ClientWithSpouse)
class ClientWithSpouseAdmin(admin.ModelAdmin):
    ...


@admin.register(models.ChildClient)
class ChildClientAdmin(admin.ModelAdmin):
    ...


@admin.register(models.DocumentClient)
class DocumentClientAdmin(admin.ModelAdmin):
    ...


@admin.register(models.JobClient)
class JobClientAdmin(admin.ModelAdmin):
    ...


@admin.register(models.CommunicationClient)
class CommunicationClientAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Communication)
class CommunicationAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Passport)
class PassportAdmin(admin.ModelAdmin):
    ...
