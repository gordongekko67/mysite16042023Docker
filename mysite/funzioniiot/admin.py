from django.contrib import admin
# Register your models here.
from .models import Titoli2
# Register your models here.

@admin.register(Titoli2)
class TitoliAdmin(admin.ModelAdmin):
    list_display = ('codtit2', 'codslugtit2', 'codisintit2', 'codbodytit2', 'codmintit2', 'codmaxtit2')
