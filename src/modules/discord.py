import os
from time import sleep

from dotenv import load_dotenv # type: ignore
from discord_webhook import DiscordWebhook

from modules.info import getSystemInfo, getCpuInfo, getRamInfo, getDiskInfo


load_dotenv()
DISCORD_URL=os.getenv("DISCORD_URL")
DISCORD_DELAY=int(os.getenv("DISCORD_DELAY"))


def sendToDiscord():
    webhook = DiscordWebhook(url=DISCORD_URL, content=f":minidisc: :minidisc: :minidisc: \n\n{getSystemInfo()}\n\n :minidisc: :minidisc: :minidisc: ")
    webhook.execute()
    webhook = DiscordWebhook(url=DISCORD_URL, content=f":desktop: CPU usage: {getCpuInfo()}%\n\n:pencil: RAM usage: {getRamInfo()}%\n{getDiskInfo()}")
    webhook.execute()
    print("\n\n\n\nInformation successfully sent to discord!\n\n")
    while True:
        webhook.content=f":desktop: CPU usage: {getCpuInfo()}%\n\n:pencil: RAM usage: {getRamInfo()}%\n{getDiskInfo()}"
        webhook.edit()
        sleep(DISCORD_DELAY)