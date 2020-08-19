import asyncio
import aiohttp
import json


async def request_data(url):
    async with aiohttp.request('GET', url) as response:
        body = await response.json()
        return body

async def get_reddit_top(subreddit):
    url_pattern = f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'
    response = await request_data(url_pattern)
    if response:
        children_response = response.get('data').get('children')
        subred = children_response[0].get('data').get('subreddit')
        top = {subred: {}}
        for child in children_response:
            child_data = child.get('data')
            title = child_data.get('title')
            score = child_data.get('score')
            link = f"https://reddit.com{child_data.get('permalink')}"
            top_packing = {title: {'score': score, 'link': link}}
            top[subred].update(top_packing)
        result = json.dumps(top)
        return result


async def main():
    reddits = {"python", "compsci", "microbork"}
    result = await asyncio.gather(*(get_reddit_top(subreddit)
                                    for subreddit in reddits))
    print(result)
    return result

asyncio.run(main())
