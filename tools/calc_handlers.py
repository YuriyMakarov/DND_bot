from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State

from tools.calculators import JumpCalculator
from keyboards import make_reply_keyboard, calc_keyboard


class JumpStates(StatesGroup):
    strength_jump = State()


router = Router()


@router.message(Command(commands=["tools"]))
@router.message(F.text == "Инструменты")
async def tool(message: Message):
    await message.answer(
        text="Инструменты:"
             "Расчет прыжков(/calc_jump)\n"
             "Расчет переносимого веса(/calc_weight) - В разработке\n"
             "Конвертер монет(/convert_coins)",
        reply_markup=make_reply_keyboard(calc_keyboard, 1, 1, 1)
    )


@router.message(StateFilter(None), Command(commands=["calc_jump"]))
@router.message(StateFilter(None), F.text == "Расчет прыжков")
async def tool_jump(message: Message, state: FSMContext):
    await message.answer(text="Введите значение характеристики силы вашего персонажа")
    await state.set_state(JumpStates.strength_jump)


@router.message(JumpStates.strength_jump)
async def super_jump(message: Message, state: FSMContext):
    await message.answer(text="Делаем расчет")
    if not(message.text.isdigit()):
        await message.answer(text="Введите положительное число, а не строку.")
    elif int(message.text) < 1:
        await message.answer(text="Принимаются только положительные числа")
    else:
        har_strength = int(message.text)
        jumping = JumpCalculator(har_strength)
        await message.answer(
            text=f"Прыжок в высоту\n"
                 f"При разбеге в 10 футов: {jumping.calc_jump_height(True)}\n"
                 f"Без разбега: {jumping.calc_jump_height(False)}\n"
                 f"_____________________________________\n"
                 f"Прыжок в длину\n"
                 f"При разбеге в 10 футов: {jumping.calc_jump_length(True)}\n"
                 f"Без разбега: {jumping.calc_jump_length(False)}\n"
        )
    await state.clear()


@router.message(Command(commands=["calc_weight"]))
@router.message(F.text == "Расчет веса")
async def tool_weight(message: Message):
    await message.answer(text="В разработке")


@router.message(Command(commands=["converter_coins"]))
@router.message(F.text == "Конвертер монет")
async def tool_convert_coins(message: Message):
    await message.answer(text="п")