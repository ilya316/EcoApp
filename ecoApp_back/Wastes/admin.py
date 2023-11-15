from django.contrib import admin

from django.contrib import admin
from Wastes.models import WasteExample, WasteSite, WasteTypes


class WasteExampleAdmin(admin.ModelAdmin):
    pass


class WasteSiteAdmin(admin.ModelAdmin):
    pass


class WasteTypesAdmin(admin.ModelAdmin):
    pass


admin.site.register(WasteExample, WasteExampleAdmin)
admin.site.register(WasteSite, WasteSiteAdmin)
admin.site.register(WasteTypes, WasteTypesAdmin)
