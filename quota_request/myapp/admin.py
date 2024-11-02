from django.contrib import admin
from django.contrib import messages
from myapp.models import Course, QuotaRequest

class CourseAdmin(admin.ModelAdmin):
    list_display = ['subject_id', 'subject_name', 'subject_semester', 'subject_amount', 'quota_enabled']
    
    actions = ['toggle_quota_status']

    def toggle_quota_status(self, request, queryset):
        for course in queryset:
            course.quota_enabled = not course.quota_enabled
            course.save()
            # status = 'เปิด' if course.quota_enabled else 'ปิด'
            # messages.success(request, f'{status}ให้ขอโควต้าวิชา {course.subject_id} แล้ว')
        
    toggle_quota_status.short_description = "เปลี่ยนสถานะเปิด/ปิด ให้โควต้า"

class QuotaRequestAdmin(admin.ModelAdmin):
    list_display = ['course', 'user', 'requested_at']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        course = obj.course
        if course.subject_amount_remaining > 0:
            course.subject_amount_remaining -= 1
            course.save()
        #     messages.success(request, f"โควต้าคงเหลือของวิชา {course.subject_name} ลดลงเหลือ {course.subject_amount_remaining}.")
        # else:
        #     messages.error(request, f"โควต้าของวิชา {course.subject_name} เต็มแล้ว ไม่สามารถเพิ่มโควต้าได้.")

    def delete_model(self, request, obj):
        course = obj.course
        course.subject_amount_remaining += 1
        course.save()
        
        super().delete_model(request, obj)

        # messages.success(request, f"คำขอโควต้าสำหรับวิชา {course.subject_name} ถูกลบและจำนวนโควต้าคงเหลือเพิ่มขึ้นเป็น {course.subject_amount_remaining}.")


    def delete_selected_requests(self, request, queryset):
        for quota_request in queryset:
            course = quota_request.course
            course.subject_amount_remaining += 1 
            course.save()
            quota_request.delete() 
            # messages.success(request, f'Quota request for {course.subject_name} deleted and quota incremented.')

    delete_selected_requests.short_description = "Delete selected quota requests"

    def get_actions(self, request):
        actions = super().get_actions(request)
        actions.pop('delete_selected', None) 

        return actions

    actions = [delete_selected_requests]
        
# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(QuotaRequest, QuotaRequestAdmin)
