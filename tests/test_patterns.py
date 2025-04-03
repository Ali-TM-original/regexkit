import pytest
from regexkit import Patterns


class TestPatterns:

    def setup_method(self, method):
        self.pattern = Patterns()

    def test_email1(self):
        email = self.pattern.email()
        assert bool(email.match("test@example.com")) == True

    def test_email2(self):
        email = self.pattern.email()
        assert bool(email.match("another@another.com")) == True

    def test_url_1(self):
        url = self.pattern.url()
        assert bool(url.match("https://www.elte.hu/")) == True

    def test_url_2(self):
        url = self.pattern.url()
        assert bool(url.match("https://www.youtube.com/")) == True

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

    def test_duplicate1(self):
        dup = self.pattern.duplicate_word()
        assert bool(dup.match("world world world world world")) == True

    def test_duplicate2(self):
        dup = self.pattern.duplicate_word()
        assert bool(dup.match("world hello")) == False

    def test_html1(self):
        html = self.pattern.html_tag()
        assert bool(html.match("<h1>hello world</h1<")) == True

    def test_html2(self):
        html = self.pattern.html_tag()
        assert bool(html.match("hello world")) == False

    def test_date1(self):
        d = self.pattern.date()
        assert bool(d.match("12-Jan-2025")) == True

    def test_date2(self):
        d = self.pattern.date()
        assert bool(d.match("03/Feb/1999")) == True

    def test_date3(self):
        d = self.pattern.date()
        assert bool(d.match("25.Mar.2020")) == True

    def test_date4(self):
        d = self.pattern.date()
        assert bool(d.match("5-Apr-2023")) == False

    def test_date5(self):
        d = self.pattern.date()
        assert bool(d.match("12-APRIL-2025")) == False
