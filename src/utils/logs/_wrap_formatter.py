from logging import Formatter, LogRecord
from textwrap import wrap
from typing import Final

from src.utils.functions import tab

__all__ = ['WrapFormatter']


def _wrap(text: str, max_length: int) -> str:
    wrapped_text_list = []
    if not text.startswith('\n'):
        text = '\n' + text
    for line in text.split('\n'):
        wrapped_text_list.extend(wrap(line, max_length))
    if text.startswith('\n'):
        return '\n' + '\n'.join(wrapped_text_list)
    return '\n'.join(wrapped_text_list)


class WrapFormatter(Formatter):
    _DEFAULT_MAX_LENGTH: Final[int] = 120

    def __init__(self, *args, max_length: int = _DEFAULT_MAX_LENGTH, **kwargs):
        super().__init__(*args, **kwargs)
        self._max_length: Final[int] = max_length

    def formatException(self, ei):
        formatted_exception = super().formatException(ei)
        return tab(
            f'<<<\n{tab(formatted_exception)}' +
            ('' if formatted_exception.endswith('\n') else '\n') +
            '>>>'
        )

    def format(self, record: LogRecord):
        formatted = super().format(record)
        if '\n' in record.message or len(formatted) > self._max_length:
            old_message = record.message
            record.message = tab(_wrap(record.message, self._max_length))
            formatted = super().format(record)
            record.message = old_message
        return formatted
