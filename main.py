<p align="center">
  <img src="https://i.postimg.cc/D0qQ884r/FORWARD-BOT-PIC-17.png" alt="Forward Bot Banner" width="550"/>
</p>


<b> AK AUTO Forward Bot</b>

<b>Auto Restart All User Forwarding After Bot Restarted.</b>

![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=Welcome+To+AK+AUTO+Forward+Bot+!)

## How To Deploy [Video Tutorial](https://youtu.be/A-iIh_5WAlk)

## Features

- [x] Public Forward (Bot)
- [x] Private Forward (User Bot)
- [x] Custom Caption 
- [x] Custom Button
- [x] Skip Duplicate Messages
- [x] Skip Messages Based On Extensions & Keywords & Size
- [x] Filter Type Of Messages
- [x] Auto Restart Pending Task After Bot Restart 


<b>To Know About All Features, Join My <a href='https://t.me/AK_Botz_UPDATE'>Update Channel</a>.</b>

## Commands

```
start - check I'm alive 
forward - forward messages
unequify - delete duplicate media messages in chats
settings - configure your settings
stop - stop your ongoing tasks
reset - reset your settings
restart - restart server (owner only)
resetall - reset all users settings (owner only)
broadcast - broadcast a message to all your users (owner only)
```

## Variables

* `API_ID` API Id from my.telegram.org
* `API_HASH` API Hash from my.telegram.org
* `BOT_TOKEN` Bot token from @BotFather
* `BOT_OWNER` Telegram Account Id of Owner.
* `DATABASE_URI` Database uri from [MongoDB](https://mongodb.com) Watch [Video Tutorial](https://youtu.be/DAHRmFdw99o)

## Credits

* <b>[MR ABHAY](https://t.me/mr_abhay_k)</b>


import asyncio, logging
from config import Config
from pyrogram import Client as VJ, idle
from typing import Union, Optional, AsyncGenerator
from logging.handlers import RotatingFileHandler
from plugins.regix import restart_forwards

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

if __name__ == "__main__":
    VJBot = VJ(
        "VJ-Forward-Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=dict(root="plugins")
    )  
    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially.
        This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
        you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
        single call.
        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                
            limit (``int``):
                Identifier of the last message to be returned.
                
            offset (``int``, *optional*):
                Identifier of the first message to be returned.
                Defaults to 0.
        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
        Example:
            .. code-block:: python
                for message in app.iter_messages("pyrogram", 1, 15000):
                    print(message.text)
        """
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1
               
    async def main():
        await VJBot.start()
        bot_info  = await VJBot.get_me()
        await restart_forwards(VJBot)
        print("Bot Started.")
        await idle()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

