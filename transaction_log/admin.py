from django.contrib import admin
from models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('username','timestamp',)

admin.site.register(Transaction,TransactionAdmin)
