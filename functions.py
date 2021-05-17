import random
import requests


async def randomize(message: object, array: list):
    random_list = array
    random.shuffle(random_list)

    message_to_send = ''

    for index, item in enumerate(random_list):
        message_to_send += f'{index + 1} - {item}\n'

    await message.channel.send(message_to_send)


async def get_dog(message: object, *args):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    response_converted = response.json()
    await message.channel.send(response_converted['message'])


functions = {
    'randomize': randomize,
    'dog': get_dog,
}
