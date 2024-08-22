from django.contrib import admin
from blog.models import Post, BlogComment
from tinymce.widgets import TinyMCE
from django.db import models

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment)