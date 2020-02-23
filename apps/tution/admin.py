from django.contrib import admin
from .models import *


class CategoryRelationInline(admin.StackedInline):
    model = CategoryRelation
    verbose_plural_name = "Category Relation"
    fk_name = "parent"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'tag_type', 'is_active')
    list_filter = ('tag_type', 'is_active')
    list_display_links = ('id', 'name')
    inlines = (CategoryRelationInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CategoryAdmin, self).get_inline_instances(request, obj)


class TutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'tutor', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tution, TutionAdmin)
