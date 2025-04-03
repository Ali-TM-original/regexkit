## Overview
RegexKit is a Python library that simplifies the creation of regular expressions using a fluent interface. It provides an intuitive way to construct complex regex patterns without manually writing raw regular expressions.

## Installation
Ensure you have Python installed, then import the RegexKit module into your project.

## Modules
### patterns.py
This module defines common regex patterns using RegexKit.

#### Methods:
- **email()**: Returns a compiled regex pattern for validating email addresses.
- **url()**: Returns a compiled regex pattern for validating URLs.
- **phone_international()**: Returns a compiled regex pattern for international phone numbers.
- **username()**: Returns a compiled regex pattern for usernames that may include _ and – having a length of 3 to 16 characters.
- **ipv4()**: Returns a compiled regex pattern for IPv4 addresses.
- **passport()**: Returns a compiled regex pattern for passport numbers.
- **duplicate_word()**: Returns a compiled regex pattern to find if there are duplicate words in a string.
- **html_tag()**: Returns a compiled regex pattern to find if there are html tags in a string
- **date()**: Returns a compiled regex pattern for dates in the following format DD.MMM.YYYY | DD-MMM-YYYY | DD/MMM/YYYY


#### Example Usage:

```python
from regexkit import Patterns

email_regex = Patterns.email()
print(bool(email_regex.match("test@example.com")))  # Output: True
```

### regexkit.py
This module defines the RegexKit class, which provides a fluent API for building regex patterns.

#### Class: RegexKit
##### Methods:
- **Character Matching**
  - digit(): Matches a digit (\d).
  - word_char(): Matches a word character (\w).
  - whitespace(): Matches whitespace (\s).
  - any_char(): Matches any character (.).
- **Quantifiers**
  - zero_or_more(): Matches zero or more occurrences (*).
  - one_or_more(): Matches one or more occurrences (+).
  - optional(): Matches zero or one occurrence (?).
  - exactly(n): Matches exactly n occurrences ({n}).
  - between(min, max): Matches between min and max occurrences ({min,max}).
  - at_least(n): Matches at least n occurrences ({n,}).
- **Grouping**
  - group(capturing=True, name=None): Creates a capturing or non-capturing group.
  - end_group(): Closes a previously opened group.
- **Anchors**
  - start(): Matches the beginning of a string (^).
  - end(): Matches the end of a string ($).
  - word_boundary(): Matches a word boundary (\b).
- **Lookaheads and Lookbehinds**
  - followed_by(pattern): Ensures a pattern follows the current position ((?=pattern)).
  - not_followed_by(pattern): Ensures a pattern does NOT follow ((?!pattern)).
  - preceded_by(pattern): Ensures a pattern precedes the current position ((?<=pattern)).
  - not_preceded_by(pattern): Ensures a pattern does NOT precede ((?<!pattern)).
- **Flags**
  - case_insensitive(): Enables case-insensitive matching.
  - multiline(): Enables multi-line matching (^ and $ match line starts and ends).
  - dotall(): Allows . to match newline characters (s flag).

#### Example Usage:

```python
from regexkit import RegexKit

pattern = RegexKit().start().digit().at_least(3).compile()
print(bool(pattern.match("123")))  # Output: True
```

### test_patterns.py
This module contains unit tests for validating regex patterns. It uses the pytest framework.

#### Example:
```python
import pytest
from regexkit import Patterns

def test_email():
    email_regex = Patterns.email()
    assert bool(email_regex.match("test@example.com")) == True
```

### main.py
This script demonstrates the usage of RegexKit and Patterns.

#### Example Execution:
```python
from regexkit import Patterns

if __name__ == "__main__":
    email_regex = Patterns.email()
    print("Email regex:", email_regex.pattern)
    print("Match test@example.com:", bool(email_regex.match("test@example.com")))
```

## Detailed Functionality
### 1. Creating Regular Expressions
RegexKit provides a method-chaining approach to construct regex patterns programmatically. This avoids the need to manually write raw regex strings and makes the code more readable.

Example:
```python
from regexkit import RegexKit

pattern = RegexKit().start().word_char().one_or_more().literal("@").word_char().one_or_more().compile()
print(bool(pattern.match("user@example")))  # Output: True
```


### 2. Using Predefined Patterns
Patterns provides commonly used regex patterns that can be reused.
Example:
```python
from regexkit import Patterns

email_regex = Patterns.email()
print(bool(email_regex.match("test@domain.com")))  # Output: True
```

### 3. Debugging and Testing
- The library supports unit testing with pytest.
- Patterns can be compiled and tested interactively using print() statements.

### 4. Handling Optional Elements
The .optional() method ensures that certain elements in a pattern are not mandatory.
Example:
```python
from regexkit import RegexKit

pattern = RegexKit().literal("http").literal("s").optional().literal("://").compile()
print(bool(pattern.match("https://")))  # Output: True
print(bool(pattern.match("http://")))   # Output: True
```


