from django.contrib import admin

# Register your models here.

from .models import Site, Manpower, Attendance, Expense, Tool, total_amount_per_laborer

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass

@admin.register(Manpower)
class ManpowerAdmin(admin.ModelAdmin):
    pass

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    pass

@admin.register(total_amount_per_laborer)
class total_amount_per_laborerAdmin(admin.ModelAdmin):
    pass



