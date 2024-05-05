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
            # Get the total number of members in the channel
            chat_info = await client.get_chat(channel_id)
            total_members = chat_info.members_count

            # Remove subscribers in batches of 100
            for offset in range(0, total_members, 100):
                chat_members = await client.get_chat_members(channel_id, offset=offset)
                for member in chat_members:
                    # Restrict the member's permissions
                    await client.restrict_chat_member(
                        chat_id=channel_id,
                        user_id=member.user.id,
                        permissions=ChatPermissions(),
                    )
            await message.reply("All subscribers removed from the channel.")
        except Exception as e:
            await message.reply(f"An error occurred: {str(e)}")

# Command handler for the /removeall command
@app.on_message(filters.command("removeall") & filters.private)
async def remove_all_command(client, message):
    await remove_all_subscribers(client, message)

# Start the bot
app.run()
