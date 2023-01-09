from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client
from .models import Action, Category, Priority

# Create your tests here.
# User = get_user_model()


# class LoginTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

#     def testLogin(self):
#         self.client.login(username='john', password='johnpassword')
#         response = self.client.get('/login/')
#         self.assertEqual(response.status_code, 200)

    

class TestViews(TestCase):

    def setUp(self):
        User = get_user_model()
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    def testLogin(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)


    def test_get_action_list(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/actions/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/action_list.html')


    def test_get_filtered_action_list(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/filtered-actions/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/filtered_action_list.html')


    def test_get_priorities_list(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/priorities/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/priorities_list.html')


    def test_get_categories_list(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/categories/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/categories_list.html')
    

    def test_add_action(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/add-action/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/add_action.html')

    
    def test_add_action_item_redirect(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.post('/add-action/', {'title': 'Test Add Action'})
        self.assertRedirects(response, '/actions/')

    
    def test_update_action(self):
        self.client.login(username='john', password='johnpassword')
        action = Action.objects.create(title='TestAction')
        response = self.client.get(f'/update-action/{action.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/update_action.html')

    
    def test_add_category(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/add-category/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/add_category.html')
    

    def test_update_category(self):
        self.client.login(username='john', password='johnpassword')
        category = Category.objects.create(title='TestCategory')
        response = self.client.get(f'/update-category/{category.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/update_category.html')
    

    def test_add_category_item_redirect(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.post('/add-category/', {'title': 'Test Add Category', 'description': 'Test Cat Description'})
        self.assertRedirects(response, '/categories/')

    
    def test_add_priority(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/add-priority/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/add_priority.html')

    
    def test_update_priority(self):
        self.client.login(username='john', password='johnpassword')
        priority = Priority.objects.create(title='TestPriority')
        response = self.client.get(f'/update-priority/{priority.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/update_priority.html')

    
    def test_add_priority_item_redirect(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.post('/add-priority/', {'title': 'Test Add priority', 'description': 'Test Priority Description'})
        self.assertRedirects(response, '/priorities/')

    
    # def test_add_item_page(self):


    # def test_edit_item_page(self):

    
    # def test_can_add_item(self):

    
    # def test_can_delete_item(self):
    

    # def test_can_toggle_item(self):