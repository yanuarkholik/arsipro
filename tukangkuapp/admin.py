from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from .models import Profile

from sellerapp.models import Request, Invoice, Images
# Custom Column


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):  
    list_display = ('user','buat', 'id')
    ordering = ('-buat',)
    search_fields = []

class ImagesAdminInline(admin.TabularInline):
    model = Images

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    inlines = [
        ImagesAdminInline,
    ]
    list_display = ('oleh', 'email', 'kontak', 'status', 'buat', 'id')
    ordering = ('-buat',)
    list_filter = (
        ('services'),
        ('status'),
    )

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('oleh', 'kepuasan',  'id')
    ordering = ('-buat',)
    list_filter = (
        ('kepuasan'),
    )