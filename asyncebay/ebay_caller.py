import asyncio
import aiohttp


async def ebay_call(session, url):
    async with session.get(url) as resp:
        result = await resp.json(content_type=None)
        if result:
            return result


async def main(response_list, urls, headers):
    """
    creates tasks to make requests to a number of urls. The response from the requests are added to a provided list
    :param headers: request header for the urls
    :param response_list: responses are added to this list
    :param urls: list of urls to be requested
    :return:
    """
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.create_task(ebay_call(session, url)))
        results = await asyncio.gather(*tasks)

        # remove None values if any requests doesnt return valid responses
        results = list(filter(None, results))
        for result in results:
            response_list.append(result)


def start(response_list, urls, headers):
    asyncio.get_event_loop().run_until_complete(main(response_list, urls, headers))
