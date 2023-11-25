from aiogram import Router, types
from aiogram.filters import CommandStart
from databaza.db import Session, User

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    session = Session()
    user_list = session.query(User).filter(User.user_telegram_id == str(message.from_user.id)).first()
    if not user_list:

        user_telegram_id = message.from_user.id
        username = message.from_user.username
        created = message.date

        user = User(user_telegram_id=user_telegram_id, username=username, created=created)
        session = Session()
        session.add(user)
        session.commit()
        await message.reply("Sizning ma'lumotlaringizni saqlab qoldik")
    else:
        await message.answer('Siz malumotlar bazasida borsiz')
