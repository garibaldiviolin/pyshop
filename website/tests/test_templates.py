from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual('Lista de Produtos', self.selenium.title)


'''class IndexTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(IndexTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(IndexTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/accounts/register/')
        # find the form element
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_name('register')

        # Fill the form with data
        first_name.send_keys('Yusuf')
        last_name.send_keys('Unary')
        username.send_keys('unary')
        email.send_keys('yusuf@qawba.com')
        password1.send_keys('123456')
        password2.send_keys('123456')

        # submitting the form
        submit.send_keys(Keys.RETURN)

        # check the returned result
        assert 'Check your email' in selenium.page_source
'''
