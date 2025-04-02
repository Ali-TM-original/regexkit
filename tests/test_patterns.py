import pytest
from regexkit import Patterns

class TestPatterns:

    def setup_method(self, method):
        self.pattern = Patterns()

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_email1(self):
        email = self.pattern.email()
        assert bool(email.match("test@example.com")) == True

    def test_email2(self):
        email = self.pattern.email()
        assert bool(email.match("another@another.com")) == True

    def test_url_1(self):
        url = self.pattern.url()
        assert  bool(url.match("https://www.elte.hu/")) == True

    def test_url_2(self):
        url = self.pattern.url()
        assert  bool(url.match("https://www.youtube.com/")) == True

    def test_international_number1(self):
        number = self.pattern.phone_international()
        assert bool(number.match("+36-123123123")) == True

    def test_international_number2(self):
        number = self.pattern.phone_international()
        assert bool(number.match("+37-123123123")) == True

    def test_username1(self):
        uname = self.pattern.username()
        assert bool(uname.match("hello-123")) == True

    def test_username2(self):
        uname = self.pattern.username()
        assert bool(uname.match("Al1_1s_C00L")) == True

    def test_ipv4_1(self):
        ipv4 = self.pattern.ipv4()
        assert bool(ipv4.match("192.168.0.1")) == True

    def test_ipv4_2(self):
        ipv4 = self.pattern.ipv4()
        assert bool(ipv4.match("10.10.10.10")) == True
