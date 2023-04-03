from django.contrib import admin
from .models import Post, Comment, Subscription, Profile
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content_header", "content_footer")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "approved")
    list_filter = ("created_on", "approved")
    search_fields = ["name", "email_address", "body"]
    actions = ["approved"]

    def approved(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Subscription)
class SubscribedUserAdmin(admin.ModelAdmin):
    list_display = ("email", "created_on")


admin.site.register(Profile)
