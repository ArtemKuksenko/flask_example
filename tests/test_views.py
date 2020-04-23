from unittest import TestCase
from unittest.mock import patch, Mock

class TestViews(TestCase):

    def test_add_post(self):
        from app.views import add_post

        add_post_mock = Mock()
        add_post_mock.get_user.return_value = [
            {
                'id_user': 1,
                'name_user': 'lean'
            }
        ]





