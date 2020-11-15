from chat.views import ChatDetailView, HomePageView
from django.test import TestCase
from django.urls import resolve, reverse
from users.factories import UserFactory


class HomePageTests(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_home_page_resolves_homepageview(self):
        view = resolve(reverse('chat:home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    def test_home_page_works_for_logged_in_user(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('chat:home'))
        no_response = self.client.get('/homepage/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/home.html')
        self.assertContains(response, 'Contacts')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)

    def test_home_page_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('chat:home'))
        no_response = self.client.get('/homepage/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'chat/home.html')
        self.assertEqual(no_response.status_code, 404)


class ChatPageTests(TestCase):
    def setUp(self):
        self.user_1 = UserFactory()
        self.user_2 = UserFactory()

    def test_chat_page_resolves_chatdetailview(self):
        chat_url = reverse('chat:chatroom_detail', args=[str(self.user_1.id), str(self.user_2.id)])
        view = resolve(chat_url)
        self.assertEqual(view.func.__name__, ChatDetailView.as_view().__name__)

    def test_chat_page_works_for_logged_in_user(self):
        self.client.force_login(self.user_1)
        chat_url = reverse('chat:chatroom_detail', args=[str(self.user_1.id), str(self.user_2.id)])

        response = self.client.get(chat_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/chatroom_detail.html')
        self.assertContains(response, 'Chat')
        self.assertNotContains(response, 'Hi I should not be on this page!')

    def test_chat_page_redirects_for_anonymous_user(self):
        pass

    def test_valid_post_data_adds_chat_to_chatroom(self):
        pass
