from django.contrib import admin
from aboutus.models import Aboutus


class AboutusAdmin(admin.ModelAdmin):
    list_display =('aboutus_img','aboutus_title','aboutus_dec')

admin.site.register(Aboutus,AboutusAdmin)


# Register your models here.
