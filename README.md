![alt text](./docs/cool.png)

### simplify the creation of regular expressions using a fluent interface


## Overview
RegexKit is a Python library that simplifies the creation of regular expressions using a fluent interface. It provides an intuitive way to construct complex regex patterns without manually writing raw regular expressions.

## Installation
``Note: for now the package has not been uploaded to pypi``
Ensure you have Python installed, then import the RegexKit module into your project.


#### Example Usage:

Pattern Example:
```python
from regexkit import Patterns

email_regex = Patterns.email()
print(bool(email_regex.match("test@example.com")))  # Output: True
```

RegexKit Example:
```python
from regexkit import RegexKit

pattern = RegexKit().literal("http").literal("s").optional().literal("://").compile()
print(bool(pattern.match("https://")))  # Output: True
print(bool(pattern.match("http://")))   # Output: True
```