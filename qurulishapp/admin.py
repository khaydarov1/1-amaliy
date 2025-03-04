from django.contrib import admin
from .models import Condition, Material, ConstructionType, MaterialPricing


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'condition')
    search_fields = ('name', 'condition__name')


@admin.register(ConstructionType)
class ConstructionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(MaterialPricing)
class MaterialPricingAdmin(admin.ModelAdmin):
    list_display = ('id', 'material', 'price_per_unit', 'currency')
    search_fields = ('material__name',)
