from django.contrib import admin
import models

class BBS_userAdmin(admin.ModelAdmin):
    list_display = ('user','signature','photo')
    list_filter  = ('photo',)
    search_fields = ('user__username','signature','photo')
class BBSAdmin(admin.ModelAdmin):
	list_display = ('title','summary','author','view_count','create_date')
	list_filter = ('create_date',)
	search_fields = ('title','author')


# Register your models here.
admin.site.register(models.BBS,BBSAdmin)
admin.site.register(models.BBS_user,BBS_userAdmin)
admin.site.register(models.Category)

