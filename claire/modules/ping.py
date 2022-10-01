from claire.functions.handler import cmd
from claire.functions.misc import eor
import time

@cmd(pattern="ping$")
async def ping(event):
    s = time.time()
    message = await eor(event, 'Pong!')
    d = time.time() - s
    await message.edit(f'Pong!  {d:.2f}s')
        