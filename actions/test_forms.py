from django.test import TestCase
from .forms import ActionForm, CategoryForm, PriorityForm, CreateUserForm

# Create your tests here.

class TestActionForm(TestCase):

    def test_action_title_is_required(self):
        form = ActionForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_priority_and_category_fields_are_not_required(self):
        form = ActionForm({'title': 'Test Action'})
        self.assertTrue(form.is_valid())

    def test_actionform_fields_are_explicit_in_form_metaclass(self):
        form = ActionForm()
        self.assertEqual(form.Meta.fields, ['title', 'priority', 'category'])


class TestCategoryForm(TestCase):

    def test_category_title_is_required(self):
        form = CategoryForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_category_description_field_is_required(self):
        form = CategoryForm({'title': 'Test Action', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_categoryform_fields_are_explicit_in_form_metaclass(self):
        form = CategoryForm()
        self.assertEqual(form.Meta.fields, ['title', 'description'])

class TestPriorityForm(TestCase):

    def test_priority_title_is_required(self):
        form = PriorityForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_priority_description_field_is_required(self):
        form = PriorityForm({'title': 'Test Action', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_priorityform_fields_are_explicit_in_form_metaclass(self):
        form = CategoryForm()
        self.assertEqual(form.Meta.fields, ['title', 'description'])


class TestCreateUserForm(TestCase):

    def test_create_user_username_field_is_required(self):
        form = CreateUserForm({'username': '', 'email': 'test@test.com', 'password1': 'testPassword1', 'password2': 'testPassword1'})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    # def test_create_user_email_field_is_required(self):
    #     form = CreateUserForm({'username': 'testuser', 'email': '', 'password1': 'testPassword1', 'password2': 'testPassword1'})
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('email', form.errors.keys())
    #     self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_create_user_password1_field_is_required(self):
        form = CreateUserForm({'username': 'testuser', 'email': 'test@test.com', 'password1': '', 'password2': 'testPassword1'})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(form.errors['password1'][0], 'This field is required.')

    def test_create_user_password2_field_is_required(self):
        form = CreateUserForm({'username': 'testuser', 'email': 'test@test.com', 'password1': 'testPassword1', 'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2'][0], 'This field is required.')

    def test_createuserform_fields_are_explicit_in_form_metaclass(self):
        form = CreateUserForm()
        self.assertEqual(form.Meta.fields, ['username', 'email', 'password1', 'password2'])

