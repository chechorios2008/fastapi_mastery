import asyncio
import time


def sync_function(test_param: str) -> str:
    print("This is a sinchronous function")

    time.sleep(0.1)

    return f"Sync resulta: {test_param}"


# Also know as a coroutine function
async def async_function(test_param: str) -> str:
    print("This is a asynchronos coroutine function")

    await asyncio.sleep(0.1)

    return f"Async Result: {test_param}"


async def main():
    # sync_result = sync_function("Test")
    # print(sync_result)
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    print(f"Empty Future: {future}")

    future.set_result("Future Result: Test")
    future_result = await future
    print(future_result)

    coroutine_obj = sync_function("Test")
    print(coroutine_obj)

    coroutine_result = await coroutine_obj
    print(coroutine_result)

    task = asyncio.create_task(async_function("Test"))
    print(task)

    task_result = await task
    print(task_result)


if __name__ == "__main__":
    asyncio.run(main())