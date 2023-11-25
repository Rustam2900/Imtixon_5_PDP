from aiogram import types
from aiogram import Router
from databaza.db import Session, Message_mes,User
from aiogram.filters import Command
router = Router()


@router.message(Command('info'))
async def user_list(message: types.Message):
    session = Session()
    user_list = session.query(User).filter(User.user_telegram_id == str(message.from_user.id)).first()
    if user_list:
        res = f"{user_list.username} {user_list.user_telegram_id} {user_list.created}\n"
    else:
        res = "Users not found"
    await message.answer(res)


@router.message()
async def user_chat_handler(message: types.Message) -> None:
    user_id = str(message.from_user.id)
    text = message.text
    created = message.date
    mes = Message_mes(user_id=user_id, text=text, created=created)
    session = Session()
    session.add(mes)
    session.commit()
    await message.answer(f"{message.from_user.username} saqlash kerak bolgan qanday habaringiz bor")
