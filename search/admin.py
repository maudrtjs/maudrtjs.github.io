from django.contrib import admin
from .models import Sheet
from django.utils.html import format_html


class SheetAdmin(admin.ModelAdmin):
    list_display = ('compositor', 'title', 'composition_date', 'show_pdf_link')
    list_filter = ('instrumentation', 'style', 'compositor_period', 'nb_instruments')
    # date_hierarchy = 'composition_date'
    ordering = ('compositor', 'title')
    search_fields = ('title', 'compositor', 'instrumentation', 'style', 'compositor_period')
    fieldsets = (
        ('General',
         {'classes': ['collaspse,'],
          'fields': ('title', 'compositor', 'pdf_link')
          }),
        ('Additional information:',
         {'description': 'Can you help us to improve our database?',
          'fields': (
          'subtitle', 'instrumentation','nb_instruments', 'composition_date', 'first_interpretation_date',
          'release_date', 'duration', 'compositor_period', 'style', 'key','editor',  'source',
          'difficulty', 'popularity', 'comments', 'dedication', 'sections', 'num_opus')
          }),
    )

    def show_pdf_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.pdf_link)

    show_pdf_link.short_description = "score URL"


# Register your models here.
admin.site.register(Sheet, SheetAdmin)
