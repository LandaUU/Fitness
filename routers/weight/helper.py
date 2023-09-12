import asyncio
import re
from typing import Coroutine

from routers.weight.exceptions import NegativeAnswer, NegativeWeight, UnexpectedAnswer

negative_answer_words = {'не взвешивался', 'не измерял', 'нет', 'неа', 'не', 'ноу', '-', 'no'}


async def delay(coro: Coroutine, seconds: int):
    await asyncio.sleep(seconds)
    await coro


async def search_weight_number_in_text(text: str):
    matches = re.findall(pattern=r'[-+]?(\d+([.,]\d*)?|[.,]\d+)([eE][-+]?\d+)?', string=text)

    for m in matches:
        for group in m:
            if float(group) < 0:
                raise NegativeWeight()
            return float(group)

    for word in negative_answer_words:
        if word.lower() in text.strip(' '):
            raise NegativeAnswer()

    raise UnexpectedAnswer()
