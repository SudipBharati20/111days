"""
number_words.py
===============
Maps integer finger counts to their English spoken/display words.
Easily extensible to other languages by swapping the lookup table.
"""

from logger_setup import get_logger

logger = get_logger("finger_counter.words")

# ── Word tables ───────────────────────────────────────────────────────────────

_ENGLISH: dict[int, str] = {
    0:  "Zero",
    1:  "One",
    2:  "Two",
    3:  "Three",
    4:  "Four",
    5:  "Five",
    6:  "Six",
    7:  "Seven",
    8:  "Eight",
    9:  "Nine",
    10: "Ten",
}

_NEPALI: dict[int, str] = {
    0:  "Shunya",
    1:  "Ek",
    2:  "Dui",
    3:  "Teen",
    4:  "Char",
    5:  "Paanch",
    6:  "Chha",
    7:  "Saat",
    8:  "Aath",
    9:  "Nau",
    10: "Das",
}

LANGUAGES: dict[str, dict[int, str]] = {
    "english": _ENGLISH,
    "nepali":  _NEPALI,
}


class NumberWords:
    """
    Converts an integer (0-10) to its word representation.

    Parameters
    ----------
    language : str
        One of the keys in ``LANGUAGES`` (default: "english").
    """

    def __init__(self, language: str = "english"):
        language = language.lower()
        if language not in LANGUAGES:
            logger.warning(
                "Language %r not found, falling back to English.", language
            )
            language = "english"
        self._table = LANGUAGES[language]
        self._language = language
        logger.info("NumberWords initialised with language=%r.", language)

    def word(self, n: int) -> str:
        """Return the word for integer n. Clamps to [0, 10]."""
        n = max(0, min(n, 10))
        return self._table.get(n, str(n))

    def __getitem__(self, n: int) -> str:
        return self.word(n)

    @property
    def language(self) -> str:
        return self._language

    @staticmethod
    def available_languages() -> list[str]:
        return list(LANGUAGES.keys())
