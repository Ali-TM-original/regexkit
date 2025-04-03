import re
from typing import List


class RegexKit:
    FLAGS = {
        "CASE_INSENSITIVE": re.IGNORECASE,
        "MULTILINE": re.MULTILINE,
        "DOTALL": re.DOTALL,
    }

    def __init__(self):
        self.parts: List[str] = []
        self.flags = 0

    def _add(self, part):
        self.parts.append(rf"{part}")
        return self

    def __or__(self, other):
        return self._add(f"(?:{self}|{other})")

    def __str__(self):
        return "".join(self.parts)

    def compile(self):
        return re.compile(str(self), self.flags)

    def digit(self):
        return self._add(r"\d")

    def word_char(self):
        return self._add(r"\w")

    def whitespace(self):
        return self._add(r"\s")

    def non_whitespace(self):
        return self._add(r"\S")

    def any_char(self):
        return self._add(".")

    def literal(self, text):
        return self._add(re.escape(text))

    def char_from(self, chars):
        return self._add(f"[{chars}]")

    def char_not_from(self, chars):
        return self._add(f"[^ {chars}]")

    def zero_or_more(self, lazy=False):
        return self._add("*?" if lazy else "*")

    def one_or_more(self, lazy=False):
        return self._add("+?" if lazy else "+")

    def optional(self, lazy=False):
        return self._add("??" if lazy else "?")

    def exactly(self, n, lazy=False):
        return self._add(f"{{{n}}}?" if lazy else f"{{{n}}}")

    def between(self, min_, max_, lazy=False):
        return self._add(f"{{{min_},{max_}}}?" if lazy else f"{{{min_},{max_}}}")

    def at_least(self, n, lazy=False):
        return self._add(f"{{{n},}}?" if lazy else f"{{{n},}}")

    def group(self, capturing=True, name=None):
        return self._add(f"(?P<{name}>" if name else ("(" if capturing else "(?:"))

    def end_group(self):
        return self._add(")")

    def start(self):
        return self._add("^")

    def end(self):
        return self._add("$")

    def word_boundary(self):
        return self._add(r"\b")

    def followed_by(self, pattern):
        return self._add(f"(?={pattern})")

    def not_followed_by(self, pattern):
        return self._add(f"(?!{pattern})")

    def preceded_by(self, pattern):
        return self._add(f"(?<={pattern})")

    def not_preceded_by(self, pattern):
        return self._add(f"(?<!{pattern})")

    def case_insensitive(self):
        self.flags |= self.FLAGS["CASE_INSENSITIVE"]
        return self

    def multiline(self):
        self.flags |= self.FLAGS["MULTILINE"]
        return self

    def dotall(self):
        self.flags |= self.FLAGS["DOTALL"]
        return self
