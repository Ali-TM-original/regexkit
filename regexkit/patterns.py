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
            .literal('https?://')
            .group(False)
            .literal('www.')
            .end_group().optional()
            .word_char().one_or_more()
            .literal('.')
            .group(capturing=False)
            .literal('com').__or__('org').__or__('net')
            .end_group()
            .group(False)
            .literal('/').word_char().one_or_more()
            .end_group().zero_or_more()
            .end()
            .case_insensitive()
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