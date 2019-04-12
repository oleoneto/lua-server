def mark_as_published(modeladmin, request, queryset):
    queryset.update(status='P')


def mark_as_draft(modeladmin, request, queryset):
    queryset.update(status='D')


def mark_as_featured(modeladmin, request, queryset):
    queryset.update(featured=True)


def mark_as_unfeatured(modeladmin, request, queryset):
    queryset.update(destaque=False)
