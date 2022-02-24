from django.test import TestCase

class UrlTests(TestCase):
    def test_load_page(self): # every test must begin a test_ or it will not run
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200, "Home page did not load.")

        # TODO:
            # get a home page to load
            # modify views.py, urls.py
            # create templates folder inside recipeFinder folder
            # create recipeFinder folder inside templates folder
            # create index.html inside nested recipeFinder folder
            # look at django documentation and tutorial