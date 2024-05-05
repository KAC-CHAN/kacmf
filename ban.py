
from pyrogram import Client, filters
import pyrogram

api_id = 26788480 # Your Telegram API ID 
api_hash = '858d65155253af8632221240c535c314'
bot_token = '6724157332:AAG27x7CwHkg8N52IpQxCobn0VQ_r9_mT2E'
owner_id = 6053757293
channel_id = -1001918883387 # ID of the channel 

app = pyrogram.Client("my_bot", api_id, api_hash, bot_token)

@app.on_message(filters.private & filters.command("removeall") & filters.user(owner_id))   
async def remove_all_subscribers(client, message):
    
    try:
        
        resp = await app.send(
            pyrogram.raw.functions.channels.EditParticipants(
                channel=pyrogram.raw.types.InputChannel(
                    channel_id=channel_id
                ),
                participants=[],
                invite_link=None
            )
        )
        
        await message.reply("All subscribers removed from channel.")
        
    except Exception as e:
        await message.reply(f"Error: {e}")

app.run()
