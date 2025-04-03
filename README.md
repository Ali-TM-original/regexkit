![alt text](./docs/cool.png)

### simplify the creation of regular expressions using a fluent interface


## Overview
RegexKit is a Python library that simplifies the creation of regular expressions using a fluent interface. It provides an intuitive way to construct complex regex patterns without manually writing raw regular expressions.

## Installation
``Note: for now the package has not been uploaded to pypi``
Ensure you have Python installed, then import the RegexKit module into your project.

## Purpose
The main purpose of this library is to make writing regex more fun and easier to understand. Regex in general is really hard to understand just by looking at it at least for me 😅 this just makes it easier to read and write regex 


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

# Docs
For further information regarding the lib head over to the [docs folder](/docs/RegexKit.md)
You will find a detailed analysis of the library and how to use it properly over there


# Contribution
Found an issue in the lib or do you just want to contribute head over to the issues and create and issue. Every small help is appreciated.  

  
  
  
  
Made with ♥️ by yours truly.
