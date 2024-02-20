from django.test import TestCase
from .forms import CommentForm

class TestCommentForm(TestCase):

    def test_form_is_vslid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())