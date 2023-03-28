from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class AuthorAdmin(admin.ModelAdmin):
    pass

    # list_display = ('id',)
