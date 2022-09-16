from django.test import TestCase
from students.models import *

class ModelsTest(TestCase):
    def test_user_and_user_optional_models_save_and_retrieve(self):
        user1 = User(
            username='test1',
            password='test1',
        )
        user1.save()

        user2 = User(
            username='test2',
            password='test2'
        )
        user2.save()

        user_optional1 = UserOptional(
            faculty='ИЭФ',
            specialty='ЭЭБ',
            group='173904',
            description='Forum creator',
            tg_link='https://t.me/esquiresword',
            user=user1
        )
        user_optional1.save()

        user_optional2 = UserOptional(
            faculty='ХХХ',
            specialty='ХХХ',
            group='010101',
            description='Test',
            tg_link='https://t.me',
            user=user2
        )
        user_optional2.save()

        all_users = User.objects.all()
        self.assertEqual(len(all_users), 2)
        self.assertEqual(all_users[0].username, user1.username)
        self.assertEqual(all_users[1].username, user2.username)

        all_users_optionals = UserOptional.objects.all()
        self.assertEqual(len(all_users_optionals), 2)
        self.assertEqual(all_users_optionals[0].description, user_optional1.description)
        self.assertEqual(all_users_optionals[1].description, user_optional2.description)
