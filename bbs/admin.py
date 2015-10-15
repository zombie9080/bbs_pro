from django.contrib import admin
import models

class BBS_userAdmin(admin.ModelAdmin):
    list_display = ('user','signature','photo')
    list_filter  = ('photo',)
    search_fields = ('user__username','signature','photo')


# Register your models here.
admin.site.register(models.BBS)
admin.site.register(models.BBS_user,BBS_userAdmin)
admin.site.register(models.Category)

