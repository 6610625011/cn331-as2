from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Course, QuotaRequest

User = get_user_model()

class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        self.course = Course.objects.create(
            subject_id='CN101',
            subject_name='Introductory Computer Programming',
            subject_semester='1/2567',
            subject_amount=30,
            subject_amount_remaining=30,
            subject_credit=3
        )
    
    def test_index_view(self):
        c = Client()
        response = c.get(reverse('index'))
        self.assertRedirects(response, '/users/login/')

    def test_login_view_success(self):
        c = Client()
        response = c.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertRedirects(response, '/courses')
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_invalid(self):
        c = Client()
        response = c.post(reverse('login'), {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertContains(response, "Please enter a correct username and password. Note that both fields may be case-sensitive.")
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_courses_view(self):
        c = Client()
        c.login(username='testuser', password='password123')
        response = c.get(reverse('courses'))
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'courses.html') 

    def test_request_and_cancel_quota(self):
        c = Client()
        c.login(username='testuser', password='password123')
        
        # Request quota
        response = c.post(reverse('request_quota', args=[self.course.id]))
        self.assertRedirects(response, '/courses')
        self.assertEqual(QuotaRequest.objects.count(), 1)
        self.course.refresh_from_db()
        self.assertEqual(self.course.subject_amount_remaining, 29)
        
        # Cancel quota request
        response = c.post(reverse('cancel_quota_request', args=[self.course.id]))
        self.assertRedirects(response, '/mycourse')
        self.assertEqual(QuotaRequest.objects.count(), 0)
        self.course.refresh_from_db()
        self.assertEqual(self.course.subject_amount_remaining, 30)

    def test_mycourse_view(self):
        c = Client() 
        c.login(username='testuser', password='password123')
        QuotaRequest.objects.create(user=self.user, course=self.course)
        response = c.get(reverse('mycourse'))
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'mycourse.html')  
        self.assertContains(response, 'Introductory Computer Programming') 

    def test_logout_view(self):
        c = Client()
        c.login(username='testuser', password='password123')        
        response = c.post(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

