from django.test import TestCase
from .forms import ActionForm, CategoryForm, PriorityForm

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
