from django.contrib import admin

from core.apps.companies.models import CompanyType


@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    search_fields = ("id", "title")
