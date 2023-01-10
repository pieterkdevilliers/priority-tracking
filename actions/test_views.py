from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client
from .models import Action, Category, Priority

# Create your tests here.

# Test for loading pages / templates


class TestViews(TestCase):
    """
    Tests for Views
    """
    def setUp(self):
        """
        Sets up the user for the tests
        """
        User = get_user_model()
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')

    def test_login(self):
        """
        Tests user login
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_get_action_list_page(self):
        """
        Successfully loading the Action List page
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/actions/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/action_list.html')

    def test_get_filtered_action_list_page(self):
        """
        Successfully loading the Filtered Action List page
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/filtered-actions/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/filtered_action_list.html')

    def test_get_priorities_list_page(self):
        """
        Successfully loading the Priorities List page
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/priorities/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/priorities_list.html')

    def test_get_categories_list_page(self):
        """
        Successfully loading the Categories List page
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/categories/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/categories_list.html')

    def test_add_action_page(self):
        """
        Successfully loading the Add Action page
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/add-action/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/add_action.html')

    def test_add_action_redirect(self):
        """
        Successfully redirecting to the Action List after adding a new Action
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.post(
            '/add-action/', {'title': 'Test Add Action'})
        self.assertRedirects(response, '/actions/')

    def test_update_action_page(self):
        """
        Successfully loading the Action Update page
        """
        self.client.login(username='john', password='johnpassword')
        action = Action.objects.create(title='TestAction')
        response = self.client.get(f'/update-action/{action.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/update_action.html')

    def test_delete_action_page(self):
        """
        Successfully loading the Action Delete page
        """
        self.client.login(username='john', password='johnpassword')
        action = Action.objects.create(title='TestAction')
        response = self.client.get(f'/delete-action/{action.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/delete_action.html')

    def test_add_category_page(self):
        """
        Successfully loading the Add Category page
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/add-category/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/add_category.html')

    def test_update_category_page(self):
        """
        Successfully loading the Update Category page
        """
        self.client.login(username='john', password='johnpassword')
        category = Category.objects.create(title='TestCategory')
        response = self.client.get(
            f'/update-category/{category.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/update_category.html')

    def test_add_category_item_redirect(self):
        """
        Successfully redirecting to the Category
        List after adding a new Category
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.post(
            '/add-category/', {'title': 'Test Add Category',\
            'description': 'Test Cat Description'})
        self.assertRedirects(response, '/categories/')

    def test_delete_category_page(self):
        """
        Successfully loading the Category Delete page
        """
        self.client.login(username='john', password='johnpassword')
        category = Category.objects.create(title='TestCategory')
        response = self.client.get(
            f'/delete-category/{category.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/delete_category.html')

    def test_add_priority_page(self):
        """
        Successfully loading the Add Priority page
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/add-priority/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/add_priority.html')

    def test_update_priority_page(self):
        """
        Successfully loading the Update Priority page
        """
        self.client.login(username='john', password='johnpassword')
        priority = Priority.objects.create(title='TestPriority')
        response = self.client.get(
            f'/update-priority/{priority.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/update_priority.html')

    def test_add_priority_item_redirect(self):
        """
        Successfully redirecting to the Priorities List
        after adding a new Priority
        """
        self.client.login(username='john', password='johnpassword')
        response = self.client.post(
            '/add-priority/', {'title': 'Test Add priority',\
            'description': 'Test Priority Description'})
        self.assertRedirects(response, '/priorities/')

    def test_delete_priority_page(self):
        """
        Successfully loading the Category Delete page
        """
        self.client.login(username='john', password='johnpassword')
        priority = Priority.objects.create(title='Testpriority')
        response = self.client.get(
            f'/delete-priority/{priority.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actions/delete_priority.html')

    def test_complete_action(self):
        """
        Successfully marking an action as complete
        """
        self.client.login(username='john', password='johnpassword')
        action = Action.objects.create(title='TestAction', done_status=False)
        response = self.client.get(
            f'/complete-action/{action.id}', follow=True)
        self.assertRedirects(
            response, '/actions/', status_code=301, target_status_code=200)
        updated_action = Action.objects.get(id=action.id)
        self.assertTrue(updated_action.done_status)

