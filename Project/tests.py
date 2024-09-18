from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from Project.models import Project, Task

class ProjectViewSetTest(APITestCase):
    def setUp(self):
        # Create an admin user for the project
        self.admin = get_user_model().objects.create_user(
            email='admin@example.com',
            password='adminpassword',
            first_name='Admin',
            last_name='User'
        )
        
        # Create a project for testing
        self.project = Project.objects.create(
            name='Test Project',
            code_invitation='INVITE123',
            admin=self.admin
        )
        # Add the admin as a member of the project
        self.project.members.add(self.admin)

        # Create another user to test project joining
        self.member = get_user_model().objects.create_user(
            email='member@example.com',
            password='memberpassword',
            first_name='Member',
            last_name='User'
        )

        # Obtain a JWT token for the member
        self.token_url = reverse('jwt-create')
        self.token_data = {
            'email': 'member@example.com',
            'password': 'memberpassword'
        }
        self.token = self.obtain_token()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def obtain_token(self):
        """Obtain a valid JWT token by authenticating"""
        response = self.client.post(self.token_url, self.token_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def obtain_admin_token(self):
        """Obtain a valid JWT token for the admin"""
        response = self.client.post(self.token_url, {
            'email': 'admin@example.com',
            'password': 'adminpassword'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def test_join_project(self):
        """Test joining a project via an invitation code"""
        url = reverse('projects-join')
        data = {"code_invitation": "INVITE123"}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.member, self.project.members.all())

    def test_create_task_for_project(self):
        """Test creating a new task in a project"""
        # Re-create an admin user for the project as the member does not have add permissions
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.obtain_admin_token())
        
        url = reverse('projects-tasks', args=[self.project.id])

        data = {
            'title': 'New Task',
            'description': 'This is a new task',
            'status': 'TODO',
            'priority': 'LOW',
            'start_date': '2025-01-01T10:00:00Z',
            'end_date': '2025-01-02T10:00:00Z'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get(id=response.data['id']).title, 'New Task')

    def test_admin_can_delete_project(self):
        """Test that the admin can delete a project"""
        # Re-create an admin user for the project as the member does not have delete permissions
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.obtain_admin_token())

        url = reverse('projects-detail', args=[self.project.id])
        response = self.client.delete(url)

        # Verify that the project was successfully deleted
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Project.objects.filter(id=self.project.id).exists())

    def test_member_cannot_delete_project(self):
        """Test that a member cannot delete a project"""

        # Re-create a member user for the project
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.obtain_token())

        url = reverse('projects-detail', args=[self.project.id])
        response = self.client.delete(url)

        # Verify that the member does not have permission to delete the project
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Project.objects.filter(id=self.project.id).exists())  # The project should still exist


class TaskViewSetTest(APITestCase):
    def setUp(self):
        # Create an admin user for the project
        self.admin = get_user_model().objects.create_user(
            email='admin@example.com',
            password='adminpassword',
            first_name='Admin',
            last_name='User'
        )
        
        # Create a project for testing
        self.project = Project.objects.create(
            name='Test Project',
            code_invitation='INVITE123',
            admin=self.admin
        )
        # Add the admin as a member of the project
        self.project.members.add(self.admin)

        # Create a task for testing
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            project=self.project,
            status='TODO',
            priority='LOW',
            start_date='2025-01-01T10:00:00Z',
            end_date='2025-01-02T10:00:00Z'
        )

        # Create another user to test comments
        self.member = get_user_model().objects.create_user(
            email='member@example.com',
            password='memberpassword',
            first_name='Member',
            last_name='User'
        )

        # Add the user as a member of the project
        self.project.members.add(self.member)

        # Obtain a JWT token for the member
        self.token_url = reverse('jwt-create')
        self.token_data = {
            'email': 'member@example.com',
            'password': 'memberpassword'
        }
        self.token = self.obtain_token()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def obtain_token(self):
        """Obtain a valid JWT token by authenticating"""
        response = self.client.post(self.token_url, self.token_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def test_get_comments_for_task(self):
        """Test fetching comments for a task"""
        url = reverse('tasks-comments', args=[self.task.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_comment_for_task(self):
        """Test creating a comment for a task"""
        url = reverse('tasks-comments', args=[self.task.id])
        data = {'message': 'This is a comment', 'sender': self.member.id}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'This is a comment')