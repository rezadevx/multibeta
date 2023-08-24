
from ubot import *


__MODULE__ = "Crypto"
__HELP__ = """
 Bantuan Untuk Crypto

• Perintah : <code>{0}crypto</code> [currency]
• Penjelasan : Dapatkan nilai Real Time dari mata uang yang diberikan.
"""


@PY.UBOT("crypto")
async def _(client, message):
    await cryptoyesss(client, message)