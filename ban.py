from pyrogram import Client, filters

# Replace with your API credentials
api_id = 26788480
api_hash = '858d65155253af8632221240c535c314'
bot_token = '6724157332:AAG27x7CwHkg8N52IpQxCobn0VQ_r9_mT2E'

# Create the Pyrogram client
app = Client('my_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to ban all members from a specific channel
def ban_all_members(channel_id):
    # Get all members in the channel
    members = app.get_chat_members(channel_id)

    # Ban each member from the channel
    for member in members:
        user_id = member.user.id
        app.kick_chat_member(channel_id, user_id)

# Filter private messages from the bot owner
@Client.on_message(filters.private)
def handle_private_message(client, message):
    if message.text == '/banall':
        # Replace with the specific channel ID and owner ID
        channel_id = '-1001918883387'
        owner_id = '6053757293'

        # Verify that the message is from the bot owner
        if message.from_user.id == owner_id:
            ban_all_members(channel_id)
            message.reply_text('All members have been banned from the channel.')
        else:
            message.reply_text('You are not authorized to use this command.')

# Start the bot
app.run()
