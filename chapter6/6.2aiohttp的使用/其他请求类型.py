import aiohttp
import asyncio

async def main():
    params = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get', params=params) as response:
            # session.post('http://httpbin.org/post', data=b'data')
            # session.put('http://httpbin.org/put', data=b'data')
            # session.delete('http://httpbin.org/delete')
            # session.head('http://httpbin.org/get')
            # session.options('http://httpbin.org/get')
            # session.patch('http://httpbin.org/patch', data=b'data')
            print(await response.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

