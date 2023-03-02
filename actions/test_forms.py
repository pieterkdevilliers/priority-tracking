from django.contrib.auth import get_user_model
from django.test import TestCase
from .forms import ActionForm, CategoryForm, PriorityForm, CreateUserForm, UpdateActionForm
User = get_user_model()

# Create your tests here.


class TestActionForm(TestCase):
    """
    Tests for Action Forms
    """

    def test_action_title_is_required(self):
        """
        Tests for Action Title is Required
        """
        form = ActionForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_priority_and_category_fields_are_not_required(self):
        """
        Tests for Priority Field NOT Required
        """
        form = ActionForm({'title': 'Test Action'})
        self.assertTrue(form.is_valid())

    def test_actionform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Action Fields Explicit
        """
        form = ActionForm()
        self.assertEqual(form.Meta.fields, ['title', 'priority', 'category'])


class TestUpdateActionForm(TestCase):
    """
    Tests for Update Action Forms
    """

    def test_action_title_is_required(self):
        """
        Tests for Action Title is Required
        """
        form = UpdateActionForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_priority_and_category_fields_are_not_required(self):
        """
        Tests for Priority and Category Fields NOT Required
        """
        form = UpdateActionForm({'title': 'Test Action'})
        self.assertTrue(form.is_valid())

    def test_actionform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Action Fields Explicit
        """
        form = UpdateActionForm()
        self.assertEqual(form.Meta.fields, ['title', 'priority', 'category'])


class TestCategoryForm(TestCase):
    """
    Tests for Category Form
    """

    def test_category_title_is_required(self):
        """
        Tests for Category Title is Required
        """
        form = CategoryForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_category_description_field_is_required(self):
        """
        Tests for Action Description is Required
        """
        form = CategoryForm({'title': 'Test Action', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_categoryform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Category Fields Explicit
        """
        form = CategoryForm()
        self.assertEqual(form.Meta.fields, ['title', 'description'])


class TestPriorityForm(TestCase):
    """
    Tests for Priority Form
    """

    def test_priority_title_is_required(self):
        """
        Tests for Priority Title is Required
        """
        form = PriorityForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_priority_description_field_is_required(self):
        """
        Tests for Priority Description is Required
        """
        form = PriorityForm({'title': 'Test Action', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_priorityform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Priority Fields Explicit
        """
        form = CategoryForm()
        self.assertEqual(form.Meta.fields, ['title', 'description'])


class TestCreateUserForm(TestCase):
    """
    Tests for Create User Form
    """

    def test_create_user_username_field_is_required(self):
        """
        Tests for Create User - Username is Required
        """
        form = CreateUserForm({'username': '', 'email': 'test@test.com',
                               'password1': 'testPassword1',
                               'password2': 'testPassword1'})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_create_user_email_field_is_required(self):
        """
        Tests for Create User - Email is Required
        """
        form = CreateUserForm({'username': 'testuser', 'email': '',
                               'password1': 'testPassword1',
                               'password2': 'testPassword1'})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_create_user_password1_field_is_required(self):
        """
        Tests for Create User - Password is Required
        """
        form = CreateUserForm({'username': 'testuser', 'email': 'test@test.com',
                               'password1': '',
                               'password2': 'testPassword1'})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(form.errors['password1']
                         [0], 'This field is required.')

    def test_create_user_password2_field_is_required(self):
        """
        Tests for Create User - Password2 is Required
        """
        form = CreateUserForm({'username': 'testuser',
                               'email': 'test@test.com',
                               'password1': 'testPassword1',
                               'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(
            form.errors['password2'][0], 'This field is required.')

    def test_createuserform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests for Create User Fields Explicit
        """
        form = CreateUserForm()
        self.assertEqual(form.Meta.fields, ['username', 'email', 'password1',
                                            'password2'])
