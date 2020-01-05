from util import list_check
import asyncio
import functools


class AsyncWriter:
    def __init__(self, array=None):
        if not list_check(array) or len(array) == 0:
            print("Object is initialized with empty array.")
            self.array = []
        else:
            self.array = array
            print("Object is initialized with predefined array.")

    async def print_async(self, loop: asyncio.AbstractEventLoop, array: list = None):
        def wait_and_print(elem_):
            print(elem_)

        array_ = array if list_check(array) else self.array
        for idx, elem in enumerate(array_):
            loop.call_later(pow(2, idx), functools.partial(wait_and_print, elem))
        return await asyncio.sleep(pow(2, len(array_) - 1) + 1)
