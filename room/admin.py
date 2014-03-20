from django.contrib import admin
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import ModelForm
from room.models import Room, Floor, Building, Device

class DeviceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','device_code','status')


class DeviceInline(admin.TabularInline):
    model = Device
    extra = 1


class RoomAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','floor', 'status',)
    inlines = [DeviceInline,]


class FloorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','building')


class BuildingAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','status')



admin.site.register(Room, RoomAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Building, BuildingAdmin)
