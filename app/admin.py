from django.contrib import admin

from app.models import AutoModel, Brand, Maintenance, Service, Vehicle


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'name', )
    list_display_links = ('name', )
    list_editable = ('is_active', )
    list_filter = ('name', )
    list_per_page = 10
    search_fields = ('name', )


@admin.register(AutoModel)
class AutoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'name', 'brand', )
    list_display_links = ('name', )
    list_editable = ('is_active', )
    list_filter = ('name', 'brand', )
    list_per_page = 10
    search_fields = ('name', 'brand', )


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'vehicle', 'license_plate', )
    list_display_links = ('vehicle', )
    list_editable = ('is_active', )
    list_filter = ('owner', 'model', 'brand', )
    list_per_page = 10
    search_fields = ('vehicle', 'licence_plate', )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'name', 'value')
    list_display_links = ('name', )
    list_editable = ('is_active', )
    list_filter = ('name', )
    list_per_page = 10
    search_fields = ('name', 'value')


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_finished', 'owner',
                    'vehicle', 'service', 'new_maintenance'
                    )
    list_display_links = ('owner', )
    list_editable = ('is_finished', )
    list_filter = ('owner', )
    list_per_page = 10
    search_fields = ('owner', )
