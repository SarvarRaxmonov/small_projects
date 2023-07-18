import logging
from aiogram import executor, types
from api import dp, bot
from scraper import WebScraperTool


wst = WebScraperTool()


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply(
        "Asaxiy bot ga xush kelibsiz \nIzlayotgan mahsulot nomini yozing :"
    )


@dp.message_handler()
async def product_item(message: types.Message):
    url = wst.search_keywords_to_url_format(message.text)
    get_item_url = wst.get_item_url(url)
    if get_item_url:
        product_data = wst.scrapping_web_page(get_item_url)
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=product_data[0],
            caption=f"{product_data[1][:1023]}",
        )
        if len(product_data[1]) > 1024:
            await bot.send_message(message.chat.id, product_data[1][1023:])
    else:
        await message.reply("Iltimos mahsulot nomini to'g'ri yozing !")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
