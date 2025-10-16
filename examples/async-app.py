import asyncio
from threading import Thread

from inquirer_textual.InquirerApp import InquirerApp
from inquirer_textual.widgets.InquirerText import InquirerText

def start_app_loop(loop: asyncio.AbstractEventLoop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

if __name__ == '__main__':
    widget = InquirerText('What is your name?')
    app: InquirerApp[str] = InquirerApp(widget)

    loop = asyncio.new_event_loop()
    t = Thread(target=start_app_loop, args=(loop,), daemon=True)
    t.start()
    result = asyncio.run_coroutine_threadsafe(app.run_async(inline=True), loop).result()
    print(result)
    loop.stop()