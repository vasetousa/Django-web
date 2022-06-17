from django.contrib import admin

# Register your models here.

from user.user_pass.models import Employee, Manager, Department


class EmployeeInlineAdmin(admin.StackedInline):
    model = Manager


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = (EmployeeInlineAdmin,)
    list_display = ('first_name', 'last_name', 'employment_date', 'termination_date', 'department')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'employees', 'assigned_to_team')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

