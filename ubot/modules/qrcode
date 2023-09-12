from ubot import *

__MODULE__ = "QrCode"
__HELP__ = """
Bantuan Untuk QrCode

• Perintah: <code>{0}qrGen</code> [text QRcode]
• Penjelasan: Untuk merubah QRcode text menjadi gambar.

• Perintah: <code>{0}qrRead</code> [reply to media]
• Penjelasan: Untuk merubah QRcode menjadi text.
"""




@PY.UBOT("qrgen")
async def _(client, message):
    await qr_gen_cmd(client, message)


@PY.UBOT("qrread")
async def _(client, message):
    await qr_read_cmd(client, message)
