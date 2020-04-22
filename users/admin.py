from django.contrib import admin

from users.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image','blog']


    def blog(self,value):
        return value.user.post_set.all()

admin.site.register(Profile,ProfileAdmin)

