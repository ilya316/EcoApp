from django.contrib import admin

from django.contrib import admin
from Company.models import Company, Comment


class CompanyAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Comment, CommentAdmin)

