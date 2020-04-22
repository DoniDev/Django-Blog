from django.contrib import admin

from blog.models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ['title','date_posted','author','id']

    ordering = ['date_posted']

    list_display_links = ['title']

    search_fields = ['title','date_posted']

    list_filter = ['author']

admin.site.register(Post,PostAdmin)
