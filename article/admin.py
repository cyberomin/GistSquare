from django.contrib import admin
from .models import Article,UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model



class ArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article, ArticleAdmin)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(),UserProfileAdmin)