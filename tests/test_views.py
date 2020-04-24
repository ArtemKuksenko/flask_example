from unittest import TestCase
from unittest.mock import patch


class TestViews(TestCase):

    @patch('app.views.get_user')
    def test_get_user(self, mock_user):

        views = mock_user()
        views.get_user.return_value = [
            {
                'id_user': 1,
                'name_user': 'lean'
            }
        ]

        user = views.get_user('lean')
        self.assertIsNotNone(user)
        self.assertIsInstance(user[0], dict)





