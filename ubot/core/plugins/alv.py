import random
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,
                            InputTextMessageContent)

from ubot import *


async def alive_cmd(client, message):
    msg = await message.reply("<b>Tunggu Sebentar...</b>", quote=True)
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"alive {message.id} {client.me.id}"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
        await msg.delete()
    except Exception as error:
        await msg.edit(error)


async def alive_query(client, inline_query):
    get_id = inline_query.query.split()
    for my in ubot._ubot:
        if int(get_id[2]) == my.me.id:
            try:
                peer = my._get_my_peer[my.me.id]
                users = len(peer["pm"])
                group = len(peer["gc"])
            except Exception:
                users = random.randrange(await my.get_dialogs_count())
                group = random.randrange(await my.get_dialogs_count())
            get_exp = await get_expired_date(my.me.id)
            exp = get_exp.strftime("%d-%m-%Y")
            if my.me.id == OWNER_ID:
                status = "<b>SuperVip</b> <code>[Bos]</code>"
            elif my.me.id in await get_seles():
                status = "<b>SuperPlus</b> <code>[karyawan]</code>"
            else:
                status = "<b>SuperPlus</b> <code>[pembeli]</code>"
            button = Button.alive(get_id)
            start = datetime.now()
            await my.invoke(Ping(ping_id=0))
            ping = (datetime.now() - start).microseconds / 1000
            uptime = await get_time((time() - start_time))
            msg = f"""
<b>❏ ʀᴇᴢᴀ-ᴜʙᴏᴛ</b>
<b>Hey, I am alive.</b>
┏━━━━━━━━━━━━━━━━━━━━━
┣ <b>peer_ubot:</b> <code>{len(ubot._ubot)}</code>
┣ <b>status:</b> {status} 
┣ <b>ping_dc:</b> <code>{str(ping).replace('.', ',')} ms</code>
┣ <b>reza_group:</b> <code>{group} group</code>
┣ <b>reza_users:</b> <code>{users} users</code>
┣ <b>reza_uptime:</b> <code>{uptime}</code>
┣ <b>reza_expires:</b> <code>{exp}</code>
┗━━━━━━━━━━━━━━━━━━━━━
"""

            await client.answer_inline_query(
                inline_query.id,
                cache_time=0,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="💬",
                            reply_markup=InlineKeyboardMarkup(button),
                            input_message_content=InputTextMessageContent(msg),
                        )
                    )
                ],
            )


async def alive_close(client, callback_query):
    get_id = callback_query.data.split()
    if not callback_query.from_user.id == int(get_id[2]):
        return await callback_query.answer(
            f"❌ Jangan Di Klik Mas {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for my in ubot._ubot:
        if callback_query.from_user.id == int(my.me.id):
            await my.delete_messages(
                unPacked.chat_id, [int(get_id[1]), unPacked.message_id]
            )
