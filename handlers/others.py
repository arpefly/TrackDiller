from aiogram.types import Message


async def other_text(message: Message):
    print(f'new message from {message.from_user.username} : {message.from_user.first_name} {message.from_user.last_name}\n'
          f'message text: {message.text}\n')
