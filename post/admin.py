from django.contrib import admin

from post.models import Story, Comment

class StoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('keywords')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.keywords.all())

admin.site.register(Story, StoryAdmin)
admin.site.register(Comment)