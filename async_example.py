import asyncio

async def hello():
    print('Hello ...')
    #time.sleep(1)
    await asyncio.sleep(1)
    print('... World!')

async def main():
    await asyncio.gather(hello(),hello())

# print(print(print))
if __name__ == '__main__':
    asyncio.run(main())