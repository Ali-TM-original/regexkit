from regexkit import RegexKit
from regexkit import Patterns

if __name__ == '__main__':
    email_regex = Patterns.email()
    print("Email regex:", email_regex.pattern)
    print("Match test@example.com:", bool(email_regex.match("test@example.com")))

    phone_regex = Patterns.phone_international()
    print("Phone regex:", phone_regex.pattern)
    print("Match +36-101111111:", bool(phone_regex.match("+36-101111111")))
