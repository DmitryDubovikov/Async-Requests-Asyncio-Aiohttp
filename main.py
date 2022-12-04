import asyncio
import time

import aiohttp

async def get_pokemon(session, url):
    async with session.get(url) as res:
        pokemon_data = await res.json()
        return pokemon_data


async def example():

    starting_time = time.time()

    actions = []
    pokemon_data = []

    async with aiohttp.ClientSession() as session:
        for num in range(1, 101):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            actions.append(asyncio.ensure_future(get_pokemon(session, url)))

        pokemon_res = await asyncio.gather(*actions)
        for data in pokemon_res:
            pokemon_data.append(data)

    count = len(pokemon_data)
    total_time = time.time() - starting_time

    print({"data": len(pokemon_data), "count": count, "time": total_time})


if __name__ == "__main__":
    asyncio.run(example())