from django.contrib import admin
# from .models import HRCalendar, HireCard, EmployeeCard
#
# class HireCardAdmin(admin.ModelAdmin):
#     list_display = ('name','surname','middle_name','resume_link',)
#     list_filter = ('desired_position','interview_date','status')
#     ordering = ['surname','desired_position']
#
# class EmployeeCardAdmin(admin.ModelAdmin):
#     list_display = ('name', 'surname',
#                     'middle_name', 'employee_position', 'employee_department',)
#     list_filter = ('employee_department', 'employee_position',)
#     ordering = ['surname']
#
# class HRCalendarAdmin(admin.ModelAdmin):
#     list_display = ('event_type','title','description',)
#     list_filter = ('start_date','event_type',)
#     ordering = ['event_type']
#
#
# admin.site.register(HireCard, HireCardAdmin)
# admin.site.register(EmployeeCard, EmployeeCardAdmin)
# admin.site.register(HRCalendar, HRCalendarAdmin)