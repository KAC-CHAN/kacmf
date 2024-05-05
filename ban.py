from pyrogram import Client, filters

# Replace with your API credentials
api_id = 26788480
api_hash = '858d65155253af8632221240c535c314'
bot_token = '6724157332:AAG27x7CwHkg8N52IpQxCobn0VQ_r9_mT2E'

from pyrogram import Client, filters

# Replace with your own values
api_id = 26788480
api_hash = '858d65155253af8632221240c535c314'
bot_token = '6724157332:AAG27x7CwHkg8N52IpQxCobn0VQ_r9_mT2E'
owner_id = 6053757293
channel_id = -1001918883387

# Create the Pyrogram client
app = Client("my_bot", api_id, api_hash, bot_token=bot_token)


# Command handler for /banall
@app.on_message(filters.private & filters.user(owner_id) & filters.command("banall"))
def ban_all_members(client, message):
    # Check if the bot is added to the specific channel
    if client.get_chat_member(channel_id, client.get_me().id).status == "administrator":
        # Get all members in the channel
        members = client.get_chat_members(channel_id)
        
        # Ban all members from the channel
        for member in members:
            if member.user.id != client.get_me().id:
                client.kick_chat_member(channel_id, member.user.id)
        
        message.reply_text("All members have been banned from the channel.")
    else:
        message.reply_text("Please add the bot to the specific channel with full rights before using this command.")


# Start the bot
app.run()
