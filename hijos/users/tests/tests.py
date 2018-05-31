from django.test import TestCase
from django.urls import reverse
from hijos.users import models


class UserTestCase(TestCase):
    """
    """
    fixtures = [
        'hijos/users/tests/fixtures/users.json'
    ]

    def setUp(self):
        self.user1 = models.User.objects.get(username='user1')
        self.user2 = models.User.objects.get(username='user2')
        self.url_login = reverse('account_login')

    def test_str(self):
        self.assertEqual(
            str(self.user1),
            "One, User (3)"
        )

    def test_create(self):
        url_create = reverse('users:user-create')
        data = {
            'username': 'test',
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@test.com',
            'degree': models.DEGREE_ENTEREDAPPRENTICE,
            'is_active': True
        }

        self.client.logout()
        response = self.client.post(url_create, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            self.url_login + '?next=' + url_create
        )

        self.client.force_login(user=self.user1)
        response = self.client.post(url_create, data, follow=True)
        self.assertEqual(response.status_code, 200)
        url_detail = reverse('users:user-detail', args=['test'])
        self.assertRedirects(response, url_detail)
        user = models.User.objects.get(username='test')
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_superuser)

    def test_read(self):
        url_list = reverse('users:user-list')
        url_detail = reverse('users:user-detail', args=['user1'])

        self.client.logout()
        response = self.client.get(url_list, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            self.url_login + '?next=' + url_list
        )
        response = self.client.get(url_detail, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            self.url_login + '?next=' + url_detail
        )

        self.client.force_login(user=self.user1)
        response = self.client.get(url_list, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'users/user_list.html'
        )
        response = self.client.get(url_detail, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'users/user_detail.html'
        )

        self.client.force_login(user=self.user2)
        response = self.client.get(url_list, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'users/user_list.html'
        )
        response = self.client.get(url_detail, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'users/user_detail.html'
        )


class AffiliationTestCase(TestCase):
    """
    """
    fixtures = [
        'hijos/users/tests/fixtures/users.json'
    ]

    def setUp(self):
        self.user1 = models.User.objects.get(username='user1')
        self.user2 = models.User.objects.get(username='user2')
        self.user4 = models.User.objects.get(username='user4')
        self.url_login = reverse('account_login')
        self.lodge = models.Lodge.objects.get(name='Example')
        self.affiliation = models.Affiliation.objects.get(
            lodge=self.lodge,
            user=self.user1
        )

    def test_str(self):
        self.assertEqual(
            str(self.affiliation),
            "One, User (3) @ Example"
        )

    def test_create(self):
        url_create = reverse('users:affiliation-create')
        data = {
            'lodge': 1,
            'user': 4,
            'category': 2
        }

        self.client.logout()
        response = self.client.post(url_create, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            self.url_login + '?next=' + url_create
        )

        self.client.force_login(user=self.user1)
        response = self.client.post(url_create, data, follow=True)
        self.assertEqual(response.status_code, 200)
        affiliation = models.Affiliation.objects.get(
            lodge=self.lodge,
            user=self.user4
        )
        url_detail = reverse(
            'users:affiliation-detail', args=[affiliation.pk]
        )
        self.assertRedirects(response, url_detail)

    def test_read(self):
        url_list = reverse('users:affiliation-list', args=[self.lodge.pk])
        url_detail = reverse(
            'users:affiliation-detail', args=[self.affiliation.pk]
        )

        self.client.logout()
        response = self.client.get(url_list, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            self.url_login + '?next=' + url_list
        )
        response = self.client.get(url_detail, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            self.url_login + '?next=' + url_detail
        )

        self.client.force_login(user=self.user1)
        response = self.client.get(url_list, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'users/affiliation_list.html'
        )
        response = self.client.get(url_detail, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'users/affiliation_detail.html'
        )

        self.client.force_login(user=self.user2)
        response = self.client.get(url_list, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'users/affiliation_list.html'
        )
        response = self.client.get(url_detail, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'users/affiliation_detail.html'
        )


class LodgeTestCase(TestCase):
    """
    """
    fixtures = [
        'hijos/users/tests/fixtures/users.json'
    ]

    def setUp(self):
        self.user1 = models.User.objects.get(username='user1')
        self.url_login = reverse('account_login')
        self.lodge = models.Lodge.objects.get(name='Example')

    def test_str(self):
        self.assertEqual(
            str(self.lodge),
            "Example"
        )

    def test_read(self):
        url_list = reverse('users:lodge-list')
        url_detail = reverse('users:lodge-detail', args=[self.lodge.pk])

        self.client.logout()
        response = self.client.get(url_list, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            self.url_login + '?next=' + url_list
        )
        response = self.client.get(url_detail, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            self.url_login + '?next=' + url_detail
        )

        self.client.force_login(user=self.user1)
        response = self.client.get(url_list, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'users/lodge_list.html'
        )
        response = self.client.get(url_detail, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'users/lodge_detail.html'
        )
