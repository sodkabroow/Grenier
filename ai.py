import json
import aiohttp
import logging

# настройки
fileLog = logging.FileHandler(
    filename="ai.py.log",
    mode="a",
    encoding="utf-8"
)
streamLog = logging.StreamHandler()

logging.basicConfig(
    #хендлеры для работы и в консоли и в файле
    handlers=(fileLog, streamLog),
    format="[%(asctime)s] <%(levelname)s> %(message)s",
    level=logging.INFO
)

with open("config/ai.json", "r", encoding="utf-8") as f:
    HFTOKEN = json.loads(f.read())["TOKEN"]

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {HFTOKEN}"}


async def genImage(request: str) -> bytes:
    if request is None:
        return b"0"
    
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(API_URL, data=json.dumps(request)) as response:
            logging.info(f"Получен ответ от {response.url}: {response.status}\nТип контента: {response.content_type}")
            if response.status == 200:
                bytesContent = await response.read()
            else:
                bytesContent = b"1"
            
    return bytesContent
