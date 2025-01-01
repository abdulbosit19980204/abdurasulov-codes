from django.contrib import admin
from .models import Post, Notification, VisitorsAddressModel


class PostAdmin(admin.ModelAdmin):
    models = Post
    list_display = ('title', 'author', 'created', 'updated')
    list_filter = ('author',)


class AddressAdmin(admin.ModelAdmin):
    models = VisitorsAddressModel
    list_display = ('user', 'query', 'country', 'region', 'city', 'zip', 'lat', 'lon')
    list_display_links = ('user', 'query', 'country', 'region', 'city', 'zip', 'lat', 'lon')
    list_filter = ('country', 'user')


admin.site.register(Post, PostAdmin)
admin.site.register(Notification)
admin.site.register(VisitorsAddressModel, AddressAdmin)
