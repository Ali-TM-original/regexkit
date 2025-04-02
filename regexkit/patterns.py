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
            .word_char().one_or_more()
            .literal('@')
            .word_char().one_or_more()
            .group(False)
            .literal('.')
            .word_char().one_or_more()
            .end_group()
            .zero_or_more()
            .literal('.')
            .char_from('a-zA-Z').at_least(2)
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
            .literal("http").optional()
            .literal("s").optional()
            .literal("://")
            .char_from("a-zA-Z0-9").one_or_more()
            .literal(".")
            .char_from("a-zA-Z").one_or_more()
            .end_group()
            .group(capturing=False)
            .literal("/").optional()
            .char_from("a-zA-Z0-9_/?.=&%-").zero_or_more()
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
            .literal('+')
            .digit().between(1, 3)
            .literal('-')
            .digit().between(3, 14)
            .end()
            .compile()
        )

    @staticmethod
    def username():
        """
        validates patterns that may include _ and – having a length of 3 to 16 characters –
        """
        return(
            RegexKit()
            .start()
            .char_from("a-zA-Z0-9_-").between(3, 16)
            .end()
            .compile()
        )

    @staticmethod
    def ipv4():
        """Validates IPv4 addresses (e.g., '192.168.1.1')"""
        return (
            RegexKit()
            .start()
            .group(False)
            .digit().between(1, 3).literal(".")
            .digit().between(1, 3).literal(".")
            .digit().between(1, 3).literal(".")
            .digit().between(1, 3)
            .end_group()
            .end()
            .compile()
        )
