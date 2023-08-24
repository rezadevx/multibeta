

from ubot  import *


async def cryptoyesss(client, message):
    if len(message.command) < 2:
        return await message.reply(f"{message.command} [currency]")
    currency = message.text.split(None, 1)[1].lower()
    m = await message.reply("`Processing...`")
    try:
        r = await get(
            "https://x.wazirx.com/wazirx-falcon/api/v2.0/crypto_rates",
            timeout=5,
        )
    except Exception as e:
        return await m.edit(f"Error : {e}")
    if currency not in r:
        return await m.edit(
            "Mata uang yang anda masukan salah.")
    body = {i.upper(): j for i, j in r.get(currency).items()}
    text = section(f"Tarif Kripto Saat Ini Untuk {currency.upper()}", body)
    await m.edit(text)