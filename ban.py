
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

    channel_id = -1001918883387

    try:
      is_admin = client.get_chat_member(channel_id, message.from_user.id).status == "administrator"  

      if not is_admin:
        message.reply("I don't have admin rights in this channel")
        return

      members = client.get_chat_members(channel_id)

      for member in members:
        if member.user.is_bot:  
          continue   
        client.ban_chat_member(channel_id, member.user.id)

      message.reply("All subscribers removed")

    except Exception as e:
      message.reply(f"Error: {e}")

  else:
    message.reply("Not authorized")


app.run()
