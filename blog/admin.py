from django.contrib import admin

# Register your models here.
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
        list_display = ['id','title','count_text']
        list_display_links = ['title']

        def count_text(self,post):
            return '{}글자'.format(len(post.text))
        
        count_text.short_description = '내용글자수'
admin.site.register(Post,PostAdmin)
