from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from lua_server.core.models.user import User
from lua_server.core.models.post import Comment, Lecture


class PostTestCase(APITestCase):

    # The client used to connect to the API
    client = APIClient()

    def setUp(self):
        """
        Preparing database and client.
        """

        alice = User.objects.create(first_name='Alice', last_name='Alfredo', username='alice',
                                    email='alice@example.com', password='I love all things bob')

        bob = User.objects.create(first_name='Bob', last_name='Bent', username='bob',
                                  email='bob@example.com', password='I love all things alice')

        _ = [Comment.objects.create(content=f"Alice says #{i}", author_id=alice.id) for i in range(3)]
        _ = [Lecture.objects.create(content=f"Alice lecture #{i}", slug=f"alice-lecture-{i}", author_id=alice.id) for i in range(2)]

        _ = [Comment.objects.create(content=f"Bob says #{i}", author_id=bob.id) for i in range(3)]
        _ = [Lecture.objects.create(content=f"Bob lecture #{i}", slug=f"bob-lecture-{i}", author_id=bob.id) for i in range(2)]

        # API endpoint
        self.namespace = '/api/v1/posts'

        # Forging authentication to API server
        # All requests will be authenticated.
        self.client.force_authenticate(user=User.objects.first())

    def test_must_auth(self):
        """
        Ensure resource CANNOT be viewed by user.
        """
        url = self.namespace
        self.client.credentials()
        self.client.logout()

        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_read(self):
        """
        Ensure resource CAN be viewed by authenticated user.
        """
        url = self.namespace

        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class CommentTestCase(PostTestCase):

    def test_can_delete_comment(self):
        resource_id = f"{self.namespace}/{Comment.objects.first().id}"

        res = self.client.delete(resource_id)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


class LectureTestCase(PostTestCase):

    def test_can_delete_lecture(self):
        # Authenticated as Alice
        user = User.objects.get(username='alice')
        self.client.force_authenticate(user=user)

        # Requesting to delete Alice's resource
        resource = Lecture.objects.get(slug='alice-lecture-1')
        resource_url = f"{self.namespace}/{resource.id}"

        print(f"Requester: {user.username}\nResource ID: {resource.id}\nOwner: {resource.author.username}\n")

        res = self.client.delete(resource_url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_cannot_delete_foreign_lecture(self):

        # Authenticated as Alice
        user = User.objects.get(username='alice')
        self.client.force_authenticate(user=user)

        # Requesting to delete Bob's resource
        resource = Lecture.objects.get(slug='bob-lecture-1')
        resource_url = f"{self.namespace}/{resource.id}"

        print(f"Requester: {user.username}\nResource ID: {resource.id}\nOwner: {resource.author.username}\n")

        res = self.client.delete(resource_url)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
