import asyncio
import re
from typing import Coroutine

negative_answer_words = {'не взвешивался', 'не измерял', 'не следил', 'нет', 'неа', 'не', 'ноу', '-', 'no'}


class NegativeAnswer(Exception):
    pass


class UnexpectedAnswer(Exception):
    pass


class NegativeNumber(Exception):
    pass


async def delay(coro: Coroutine, seconds: int):
    await asyncio.sleep(seconds)
    await coro


async def search_steps_number_in_text(text: str):

    matches = re.findall(pattern=r'[-+]?(\d+([.,]\d*)?|[.,]\d+)([eE][-+]?\d+)?', string=text)

    for m in matches:
        for group in m:
            if float(group) < 0:
                raise NegativeNumber()
            return float(group)

    for word in negative_answer_words:
        if word.lower() in text.strip(' '):
            raise NegativeAnswer()

    raise UnexpectedAnswer()
