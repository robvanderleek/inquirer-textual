from asyncio import sleep

from inquirer_textual import prompts
from inquirer_textual.common.PromptSettings import PromptSettings

if __name__ == '__main__':
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


    async def planets_func():
        await sleep(2)  # Simulate a delay in fetching the choices
        return ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


    result = prompts.select('Planet:', planets_func, settings=PromptSettings(mandatory=False)).value
    print(result)
