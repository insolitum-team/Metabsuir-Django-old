from django.test import TestCase
from app.models import *


class ModelsTest(TestCase):
    def test_section_model(self):
        section1 = Section(
            name='section1'
        )
        section1.save()

        section2 = Section(
            name='section2'
        )
        section2.save()

        all_sections = Section.objects.all()
        self.assertEqual(len(all_sections), 2)
        self.assertEqual(all_sections[0].name, section1.name)
        self.assertEqual(all_sections[1].name, section2.name)

    # todo test_theme_model
    # def test_theme_model(self):
    #     theme1 = Section(
    #         name='theme1'
    #         main_post=,
    #         author=,
    #         section=,
    #     )
    #     theme1.save()
    #
    #     theme2 = Section(
    #         name='theme1'
    #         main_post =,
    #         author =,
    #         section =,
    #     )
    #     theme2.save()
    #
    #     all_themes = Theme.objects.all()
    #     self.assertEqual(len(all_themes), 2)
    #     self.assertEqual(all_themes[0].name, theme1.name)
    #     self.assertEqual(all_themes[1].name, theme2.name)

    # todo test Message model
