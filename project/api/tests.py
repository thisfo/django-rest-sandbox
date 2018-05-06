from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from project.api.models import Project


class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.project_title = "Write world class code"
        self.project_owner = "It's a me"
        self.project = Project(title=self.project_title, owner=self.project_owner)

    def test_model_can_create_a_project(self):
        """Test the Project model can create a project."""
        old_count = Project.objects.count()
        self.project.save()
        new_count = Project.objects.count()
        self.assertNotEqual(old_count, new_count)
