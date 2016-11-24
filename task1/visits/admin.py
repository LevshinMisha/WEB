from django.contrib import admin
from .models import Visit


class VisitAdmin(admin.ModelAdmin):
    readonly_fields = ['get_urls']
    fieldsets = (
        (None, {'fields': ('ip', 'browser')}),
        ('Hits', {
            'fields': (
                'hit_count', 'last_hit'
            )}),
        ('Urls', {'fields': ('urls',)}),
    )

admin.site.register(Visit, VisitAdmin)