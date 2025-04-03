from .regexkit import RegexKit


class Patterns:
    @staticmethod
    def email():
        """
        validates the email pattern
        """
        return (
            RegexKit()
            .start()
            .word_char()
            .one_or_more()
            .literal("@")
            .word_char()
            .one_or_more()
            .group(False)
            .literal(".")
            .word_char()
            .one_or_more()
            .end_group()
            .zero_or_more()
            .literal(".")
            .char_from("a-zA-Z")
            .at_least(2)
            .end()
            .case_insensitive()
            .compile()
        )

    @staticmethod
    def url():
        """
        validates url patterns
        """
        return (
            RegexKit()
            .start()
            .group(capturing=True)
            .literal("http")
            .optional()
            .literal("s")
            .optional()
            .literal("://")
            .char_from("a-zA-Z0-9")
            .one_or_more()
            .literal(".")
            .char_from("a-zA-Z")
            .one_or_more()
            .end_group()
            .group(capturing=False)
            .literal("/")
            .optional()
            .char_from("a-zA-Z0-9_/?.=&%-")
            .zero_or_more()
            .end_group()
            .end()
            .compile()
        )

    @staticmethod
    def phone_international():
        """
        validates patterns that may include + in the beginning having a number between length 1 - 3 a - then number of length 3 - 14
        """
        return (
            RegexKit()
            .start()
            .literal("+")
            .digit()
            .between(1, 3)
            .literal("-")
            .digit()
            .between(3, 14)
            .end()
            .compile()
        )

    @staticmethod
    def username():
        """
        validates patterns that may include _ and – having a length of 3 to 16 characters –
        """
        return (
            RegexKit().start().char_from("a-zA-Z0-9_-").between(3, 16).end().compile()
        )

    @staticmethod
    def ipv4():
        """Validates IPv4 addresses (e.g., '192.168.1.1')"""
        return (
            RegexKit()
            .start()
            .group(False)
            .digit()
            .between(1, 3)
            .literal(".")
            .digit()
            .between(1, 3)
            .literal(".")
            .digit()
            .between(1, 3)
            .literal(".")
            .digit()
            .between(1, 3)
            .end_group()
            .end()
            .compile()
        )

    @staticmethod
    def passport():
        """
        Validates Passport Numbers
        """
        return (
            RegexKit()
            .start()
            .char_from("A-PR-WY")
            .digit()
            .char_not_from("0")
            .digit()
            .whitespace()
            .optional()
            .digit()
            .exactly(4)
            .digit()
            .char_not_from("0")
            .end()
            .compile()
        )

    @staticmethod
    def duplicate_word():
        """
        Validates if there are duplicate words in a string
        """
        return (
            RegexKit()
            .group(capturing=True)
            .word_boundary()
            .word_char()
            .one_or_more()
            .word_boundary()
            .end_group()
            .followed_by(r".*\b\1\b")
            .compile()
        )

    @staticmethod
    def html_tag():
        """
        validates if html tags are in a string
        """
        return (
            RegexKit()
            .literal("<")
            .optional("/")
            .word_char()
            .one_or_more()
            .whitespace()
            .zero_or_more()
            .any_char()
            .zero_or_more(lazy=True)
            .literal(">")
            .compile()
        )

    @staticmethod
    def date():
        """
        validates if a date is in format DD.MMM.YYYY | DD-MMM-YYYY | DD/MMM/YYYY
        """
        return (
            RegexKit()
            .start()
            .digit()
            .exactly(2)
            .char_from("-/.")
            .char_from("a-zA-Z")
            .exactly(3)
            .char_from("-/.")
            .digit()
            .exactly(4)
            .end()
            .compile()
        )
