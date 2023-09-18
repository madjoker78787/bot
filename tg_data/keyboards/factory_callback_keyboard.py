from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.filters.callback_data import CallbackData


class NumbersCallbackFactory(CallbackData, prefix="city"):
    action: str
    value: Optional[int] = None



def factory_keyboard(buttons: dict):#prefix: str,
    builder = InlineKeyboardBuilder()
    for k, v, in buttons.items():
        if not k == "items":
            builder.button(
                text=k,
                callback_data=NumbersCallbackFactory(action='change', value=v)#, prefix=prefix
            )
    builder.adjust(*buttons['items'])
    return builder.as_markup()

def build_keyboard(buttons: dict):
    builder = InlineKeyboardBuilder()
    for k, v, in buttons.items():
        if not k == "items":
            builder.button(
                text=k,
                callback_data=v
            )
        builder.adjust(*buttons['items'])
    return builder.as_markup()



def assembly_keyboard(buttons: dict):
    builder = InlineKeyboardBuilder()
    for k, v, in buttons.items():
        if not k == "items":
            builder.add(types.InlineKeyboardButton(text=k, callback_data=v))
    builder.adjust(*buttons['items'])
    return builder.as_markup()
