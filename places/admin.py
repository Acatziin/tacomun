from django.contrib import admin
from .models import Profile, Place, EvalPlace, Category

# Register your models here.

class EvalPlaceInLine(admin.TabularInline):
    model = EvalPlace
    extra = 0

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'birthday')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'city', 'postal_code')
    inlines = (EvalPlaceInLine,)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
  

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Category, CategoryAdmin)
