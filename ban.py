
from pyrogram import Client, filters

# Replace the placeholders with your own values
api_id = 26788480
api_hash = '858d65155253af8632221240c535c314'
bot_token = '6724157332:AAG27x7CwHkg8N52IpQxCobn0VQ_r9_mT2E'
bot_owner_id = 6053757293

app = Client("bot_session", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.private & filters.command("removeall"))
def remove_all_subscribers(client, message):
    if message.from_user.id == bot_owner_id:
        # Replace the placeholder with the channel ID from which you want to remove subscribers
        channel_id = -1001918883387

        try:
            # Get a list of all channel members
            members = client.get_chat_members(channel_id)

            # Remove all subscribers from the channel
            for member in members:
                if member.user.is_bot:
                    continue  # Skip removing bots from the channel
                client.kick_chat_member(channel_id, member.user.id)
            
            # Send a confirmation message to the bot owner
            message.reply_text("All subscribers have been removed from the channel.")
        
        except Exception as e:
            message.reply_text("An error occurred while removing subscribers: " + str(e))
    
    else:
        message.reply_text("You are not authorized to use this command.")


app.run()
