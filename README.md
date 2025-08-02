🔁 VK ↔ Telegram Message Bridge

Двусторонний мост между групповым чатом ВКонтакте и каналом/чатом в Telegram. Позволяет пересылать сообщения в обе стороны с сохранением авторов, на базе telethon и vk_api.
📌 Возможности

    📥 Получение сообщений из Telegram и пересылка в ВКонтакте.

    📤 Отправка сообщений из ВКонтакте в Telegram.

    🧠 Простейшее сопоставление авторов VK.

    📡 Работа с Telegram API через StringSession.

    🔄 Постоянная синхронизация через Telegram Client и VK LongPoll.

⚙️ Установка

    Установи зависимости:

pip install telethon vk_api

    Получи Telegram API ID и Hash:
    → https://my.telegram.org → API Development Tools.

    Сгенерируй SESSION_STRING для Telegram:

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())

    Получи GROUP_TOKEN для VK:
    → https://vk.com/dev → Создать токен сообщества с правами messages.

🏗 Структура проекта

project/
├── teleg_in.py     # Отправка сообщений из VK в Telegram
├── to_vk.py        # Отправка сообщений из Telegram в VK
├── vk_listener.py  # VK LongPoll слушатель
├── telegram_listener.py  # Telegram слушатель
└── README.md

🚀 Как запустить
1. Telegram → VK

Файл: telegram_listener.py
Перехватывает сообщения из Telegram и вызывает write_msg() для отправки в ВКонтакте.

@client.on(events.NewMessage(chat))
async def normal_handler(event):
    write_msg(event.message.message)

2. VK → Telegram

Файл: vk_listener.py
Использует LongPoll, чтобы принимать сообщения и пересылать их в Telegram через prinyalotvk():

if event.message.peer_id == int(peer_id):
    # Формирование имени отправителя
    ...
    teleg_in.prinyalotvk(message)

3. Отправка в VK

Файл: to_vk.py
Функция write_msg() отправляет сообщение от Telegram в беседу VK:

vk_session.method('messages.send', {...})

4. Отправка в Telegram

Файл: teleg_in.py
Функция prinyalotvk() принимает сообщение и отправляет его в Telegram-канал:

client.send_message(chat, message)

🛠 Настройки

В каждом файле нужно указать свои данные:

    API_ID, API_HASH, SESSION_STRING — для Telegram.

    GROUP_ID, GROUP_TOKEN, peer_id — для ВКонтакте.

    Telegram-канал/чат: @Kecsik (можно заменить).

    ⚠️ Никогда не публикуй токены и сессионные строки в открытом доступе!

👤 Распознавание пользователей VK

Автор сообщения определяется по from_id:

if event.message.from_id == 134127477:
    name = "LanS: "
elif event.message.from_id == 287082324:
    name = "AlSimakoff: "
else:
    name = "No name: "

Ты можешь расширить эту логику или загрузить имена из словаря.
📌 Примечания

    Поддержка вложений в VK пока отсутствует.

    Сообщения с вложениями в Telegram не обрабатываются (только текст).

    Скрипты можно запустить как фоновые процессы или объединить в один файл.

📄 Лицензия

MIT License
