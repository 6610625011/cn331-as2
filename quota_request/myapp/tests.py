from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Course, QuotaRequest
from myapp.admin import QuotaRequestAdmin
from unittest.mock import MagicMock
from django.contrib.admin.sites import site

# Create your tests here.
class CourseModelTests(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            subject_id='CN101',
            subject_name='Introductory Computer Programming',
            subject_semester='1/2567',
            subject_amount=30,
            subject_amount_remaining=30,
            subject_credit=3
        )

    def test_course_str(self):
        self.assertEqual(str(self.course), 'CN101')

    def test_course_initial_amount_remaining(self):
        self.assertEqual(self.course.subject_amount_remaining, self.course.subject_amount)

    def test_course_save_updates_remaining_amount(self):
        self.course.subject_amount = 40
        self.course.save()
        self.assertEqual(self.course.subject_amount_remaining, 40)

class QuotaRequestModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.course = Course.objects.create(
            subject_id='MA112',
            subject_name='Calculus 2',
            subject_semester='1/2568',
            subject_amount=25,
            subject_credit=3
        )
        self.quota_request = QuotaRequest.objects.create(
            user=self.user,
            course=self.course
        )

    def test_quota_request_str(self):
        self.assertEqual(str(self.quota_request), 'testuser - MA112')

    def test_quota_request_creation(self):
        self.assertEqual(self.quota_request.user.username, 'testuser')
        self.assertEqual(self.quota_request.course.subject_id, 'MA112')
        

class QuotaRequestAdminTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.course = Course.objects.create(
            subject_id='CN101',
            subject_name='Introductory Computer Programming',
            subject_semester='1/2567',
            subject_amount=30,
            subject_amount_remaining=30,
            subject_credit=3,
            quota_enabled=True
        )
        
        self.quota_request = QuotaRequest.objects.create(
            course=self.course,
            user=self.user,
            requested_at='2024-01-01 00:00:00'
        )

    def create_request(self):
        request = self.factory.post('/')
        return request

    def test_save_model_decrements_quota(self):
        admin = QuotaRequestAdmin(QuotaRequest, site)
        initial_amount_remaining = self.course.subject_amount_remaining
        
        new_quota_request = QuotaRequest(course=self.course, user=self.user)
        request = self.create_request()  
        admin.save_model(request, new_quota_request, None, False)

        self.course.refresh_from_db()
        self.assertEqual(self.course.subject_amount_remaining, initial_amount_remaining - 1)

    def test_save_model_fails_when_no_quota_remaining(self):
        self.course.subject_amount_remaining = 0
        self.course.save()

        admin = QuotaRequestAdmin(QuotaRequest, site)
        request = self.create_request()  
        
        new_quota_request = QuotaRequest(course=self.course, user=self.user)
        admin.save_model(request, new_quota_request, None, False)

        self.course.refresh_from_db()
        self.assertEqual(self.course.subject_amount_remaining, 0) 
        
    def test_delete_model_increments_quota(self):
        initial_amount_remaining = self.course.subject_amount_remaining
        
        admin_site = site
        quota_request_admin = QuotaRequestAdmin(QuotaRequest, admin_site)

        request = MagicMock()
        request.user = self.user

        quota_request_admin.delete_model(request, self.quota_request)

        self.course.refresh_from_db()
        
        self.assertEqual(self.course.subject_amount_remaining, initial_amount_remaining + 1)
        
    def test_delete_selected_requests_increments_quota(self):
        admin = QuotaRequestAdmin(QuotaRequest, site)
        initial_amount_remaining = self.course.subject_amount_remaining
        queryset = QuotaRequest.objects.filter(id=self.quota_request.id)
        request = self.create_request()
        admin.delete_selected_requests(request, queryset)
        self.course.refresh_from_db()
        self.assertEqual(self.course.subject_amount_remaining, initial_amount_remaining + 1)
        self.assertFalse(QuotaRequest.objects.filter(id=self.quota_request.id).exists())
