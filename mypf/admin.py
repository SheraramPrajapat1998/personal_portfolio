from django.contrib import admin

from .models import Project, Images

class AdminImages(admin.TabularInline):
    model = Images
    extra = 2

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'created', 'github_link', 'description' ]
    list_display_links = ('github_link',)
    list_filter = ('type','created', 'updated' )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'description', 'github_link']
    date_hierarchy = 'created'
    radio_fields = {'type':admin.HORIZONTAL}
    inlines = [AdminImages]
    ordering = ['publish']
    list_display_links = ['title', 'github_link']

