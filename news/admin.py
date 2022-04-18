from django.contrib import admin

from news.models import *

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ('org', 'word', 'count','date')

class Bs4Admin(admin.ModelAdmin):
    list_display = ('org', 'word', 'count','date')

class CtvArchiveAdmin(admin.ModelAdmin):
    list_display = ('word', 'count','date')

class BoneBrothAdmin(admin.ModelAdmin):
    list_display = ('org', 'word', 'count', 'date')

class EntryBlacklist(admin.ModelAdmin):
    list_display = ('id', 'word')

class EntryWhitelist(admin.ModelAdmin):
    list_display = ('id', 'word')

admin.site.register(Entry, EntryAdmin)
admin.site.register(Bs4, Bs4Admin)
admin.site.register(CtvArchive, CtvArchiveAdmin)
admin.site.register(BoneBroth, BoneBrothAdmin)
admin.site.register(Whitelist, EntryWhitelist)
admin.site.register(Blacklist, EntryBlacklist)