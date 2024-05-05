from pyrogram import Client, filters
from pyrogram.types import ChatPermissions

api_id = 26788480 # Your Telegram API ID 
api_hash = '858d65155253af8632221240c535c314'
bot_token = '6724157332:AAG27x7CwHkg8N52IpQxCobn0VQ_r9_mT2E'
owner_id = 6053757293
channel_id = -1001918883387 # ID of the channel 

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to remove all subscribers from the specified channel
async def remove_all_subscribers(client, message):
    if message.from_user.id == int(owner_id):
        try:
            # Initialize offset and batch size
            offset = 0
            batch_size = 100
            
            while True:
                # Get chat members
                chat_members = await client.get_chat_members(channel_id, offset=offset, limit=batch_size)
                
                # If no more members, break the loop
                if not chat_members:
                    break
                
                for member in chat_members:
                    # Restrict the member's permissions
                    await client.restrict_chat_member(
                        chat_id=channel_id,
                        user_id=member.user.id,
                        permissions=ChatPermissions(),
                    )
                
                # Update offset
                offset += batch_size

            await message.reply("All subscribers removed from the channel.")
        except Exception as e:
            await message.reply(f"An error occurred: {str(e)}")

# Command handler for the /removeall command
@app.on_message(filters.command("removeall") & filters.private)
async def remove_all_command(client, message):
    await remove_all_subscribers(client, message)

# Start the bot
app.run()
