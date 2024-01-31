import os
import aiohttp
import asyncio

async def fetch_json(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    async with aiohttp.ClientSession() as session:
        data = await fetch_json(session, url)
        output_folder = "json_files_async"
        os.makedirs(output_folder, exist_ok=True)

        for i, item in enumerate(data):
            with open(os.path.join(output_folder, f"file_{i}.json"), "w") as file:
                file.write(str(item))

if name == "main":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())