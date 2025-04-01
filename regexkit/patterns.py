from .regexkit import RegexKit

class Patterns:
    @staticmethod
    def email():
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