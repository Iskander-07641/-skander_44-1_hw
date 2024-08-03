import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    print("BOT_TOKEN not found")
else:
    print(f"BOT_TOKEN is {TOKEN}")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

user_ids = set()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_ids.add(message.from_user.id)
    user_count = len(user_ids)
    await message.reply(f"Привет, {message.from_user.first_name}, наш бот обслуживает уже {user_count} пользователя(ей)")

@dp.message_handler(commands=['myinfo'])
async def myinfo_command(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.reply(f"Ваш id: {user_id}\nВаше имя: {first_name}\nВаш username: @{username}")

@dp.message_handler(commands=['random_recipe'])
async def random_recipe_command(message: types.Message):
    recipes = [
        "Салат Цезарь: курица, салат, пармезан, соус цезарь",
        "Паста Карбонара: паста, бекон, яйца, пармезан",
        "Борщ: свекла, капуста, картофель, мясо, сметана",
        "Плов: рис, мясо, морковь, лук, специи",
        "Оливье: картофель, морковь, колбаса, горошек, майонез"
    ]
    recipe = random.choice(recipes)
    await message.reply(recipe)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
