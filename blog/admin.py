from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    list_display_links = ('date', )

# admin.site.register(Post, PostAdmin)

# Register your models here.
