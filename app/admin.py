from datetime import date

from django.contrib import admin
from django.http import Http404
from django.shortcuts import redirect

from app.models import AutoModel, Brand, Maintenance, Service, Vehicle


@admin.action(description='Maintenace today')
def send_email_action(modeladmin, request, queryset):
    for data in queryset:
        today = date.today()
        if data.next_date == today:
            return redirect(f'/send-email/{data.id}/')
        else:
            raise Http404()


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'name', )
    list_display_links = ('name', )
    list_editable = ('is_active', )
    list_filter = ('name', )
    list_per_page = 10
    search_fields = ('name', )
    ordering = ['name', ]


@admin.register(AutoModel)
class AutoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'name', 'brand', )
    list_display_links = ('name', )
    list_editable = ('is_active', )
    list_filter = ('name', 'brand', )
    list_per_page = 10
    search_fields = ('name', 'brand', )
    ordering = ['name', ]
    autocomplete_fields = ('brand', )


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'vehicle', 'license_plate', )
    list_display_links = ('vehicle', )
    list_editable = ('is_active', )
    list_filter = ('owner', 'model', 'brand', )
    list_per_page = 10
    search_fields = ('vehicle', 'licence_plate', )
    ordering = ['owner', ]
    autocomplete_fields = ('owner', 'brand', 'model', )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'name', 'value')
    list_display_links = ('name', )
    list_editable = ('is_active', )
    list_filter = ('name', )
    list_per_page = 10
    search_fields = ('name', 'value')
    ordering = ['name', ]


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_started', 'is_finished', 'owner', 'vehicle', 'next_date')
    list_display_links = ('owner', )
    list_editable = ('is_started', 'is_finished', )
    list_filter = ('owner', )
    list_per_page = 10
    search_fields = ('owner', )
    ordering = ['owner', ]
    autocomplete_fields = ('owner', 'vehicle', 'service')
    actions = [send_email_action]

    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f'/send-email/{obj.id}/')

    def response_change(self, request, obj):
        return redirect(f'/send-email/{obj.id}/')
