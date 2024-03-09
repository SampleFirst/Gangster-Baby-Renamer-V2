import logging
from pyrogram import Client
import asyncio
import os
from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6483924561:AAGgvHt6ocAShXHah-FQV6IXJ7cxps9WDrA")
API_ID = int(os.environ.get("API_ID", "10956858"))
API_HASH = os.environ.get("API_HASH", "cceefd3382b44d4d85be2d83201102b7")
STRING = os.environ.get("STRING", "BQCnMDoATgm6EV5D0XezMULX5ROFq3EMWEf50Sf3AXg8Dhp1s7VoLwDwqNQYIXgj3xtZUmEw7CNh5VFY0h_vBbPuZsMtIuIkLtPIWiGwdvHOJTwhJY-QrEq2297_yz1WvA6HiTvkgwvJtgfqnYBMwf5-rAMjLp6rfG8czJENj0HjRp1wCMpIRrVMyRWw5HElSGzolRUj-LAm3KO38zKa2_xxbovIRaRX5UMSPOJ9HJHphXJ5WZHuWIbfEH1Zufb29-bj0FNwo_2cOSAJWfkhMOJKElujJmXepFsRYBK01JEKKUV-aFWqBwEv-H_pyRpWlS8Mjm897KZhZoE5T5FuATHQ6GoSYwAAAAGCeNZRAQ")

logging.getLogger().setLevel(logging.INFO)


class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=10,
        )
        
    

    async def start(self):
         await super().start()
         me = await self.get_me()
         self.username = me.username
         logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
       

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot Restarting.......")


app = Bot()
app.run()
