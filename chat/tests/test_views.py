from chat.views import ChatDetailView, HomePageView
from django.test import TestCase
from django.urls import resolve, reverse


class HomePageTests(TestCase):
    def test_home_page_resolves_homepageview(self):
        pass

    def test_home_page_works_for_logged_in_user(self):
        pass

    def test_home_page_redirects_for_anonymous_user(self):
        pass


class ChatPageTests(TestCase):
    def test_chat_page_resolves_chatdetailview(self):
        pass

    def test_chat_page_works_for_logged_in_user(self):
        pass

    def test_chat_page_redirects_for_anonymous_user(self):
        pass
