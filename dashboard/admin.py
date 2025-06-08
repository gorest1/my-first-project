
from django.contrib import admin
from .models import OrderQueue, KPIRecord

@admin.register(OrderQueue)
class OrderQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('client',)

@admin.register(KPIRecord)
class KPIRecordAdmin(admin.ModelAdmin):
    list_display = ('metric', 'value', 'timestamp')
    list_filter = ('metric',)
    date_hierarchy = 'timestamp'

from .models import ShiftSchedule, AlertLog, Report

@admin.register(ShiftSchedule)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('date','shift','planned','completed')
    list_filter = ('shift',)

@admin.register(AlertLog)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('timestamp','level','message')
    list_filter = ('level',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title','generated_at')
