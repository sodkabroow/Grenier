# Grenier
Бот для генерации изображений в дискорде

## Установка
Если у вас установлен [git](https://git-scm.com/), то перейдите в папку в которой должен находиться бот и введите
```bash
git clone https://github.com/sodkahakann/Grenier.git
```
Дальше переходите к настройке, иначе нажмите на Code -> Download ZIP, распакуйте и переходите к настройке

## Настройка
Для начала в папке с ботом создайте ещё одну папку называемой config, в ней создайте 2 файла

1. ai.json
```json
{
    "TOKEN": "https://huggingface.co/docs/hub/security-tokens"
}
```

2. discord.json
```json
{
    "TOKEN": "https://discordpy.readthedocs.io/en/stable/discord.html#creating-a-bot-account"
}
```

## Зависимости
Для начала скачайте [python для linux](https://docs.python-guide.org/starting/install3/linux/) или [python для windows](https://www.python.org/downloads/)(обязательно [добавьте python в path](https://youtu.be/lhtK6ftsTBo)), откройте консоль и пропишите
```text
pip install -r requirements.txt
```

## Запуск
[Пригласите бота](https://discordpy.readthedocs.io/en/stable/discord.html#inviting-your-bot), для linux систем [создайте и перейдите в venv](https://docs.python.org/3/library/venv.html)(если требуется) и пропишите
```bash
python bot.py
```
Для windows откройте файл start.bat

## Внимание
Написан на коленке, да и думать над его будущим не охота

### Благодарность
Спасибо [huggingface](https://huggingface.co/) за предоставление api, а [stablityai](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) за хороший ии
