from django.contrib import admin

from websites.models import Website, WebPage, WebsiteCategory

admin.site.register(Website)
admin.site.register(WebPage)
admin.site.register(WebsiteCategory)