from django.contrib import admin
from .models import Author, Post, Comment
from django.utils.html import format_html

# Inline Comments
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields =('date',)

# Customizing Author Admin view
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display= ('full_name', 'email_address')
    search_fields= ('full_name',)


# Customizing Post Admin view
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display = ('title', 'author', 'date')
    list_select_related = ('author',)
    search_fields = ('title', 'author')
    list_filter = ('author',)
    ordering = ('-date',) # Latest post first
    readonly_fields = ('date',)

    fieldsets = (
        ('Post Info', {
            'fields': ('title', 'author')
        }),
        ('MetaData',{
            'fields': ('slug', 'content'),
            'classes': ('collapse',)
        })
    )

    # Creating a preview of article
    def short_content(self, obj):
        return obj.content[:50]    
    short_content.short_description = 'Preview'
    list_display = ('title', 'short_content', 'author')

    # Inclusion of images
    def image_tag(self, obj):
        return format_html('<img src="{}" width="50"/>', obj.image.url)
    image_tag.short_description= "Image"
    list_display = ('title', 'short_content', 'image_tag', 'author')


