import sys
import time
import logging
from threading import Thread

from modules.console import console_log
from modules.discord import sendToDiscord


logging.basicConfig(level=logging.INFO, filename="log.txt",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


def main():
    threadDiscord = Thread(target=sendToDiscord)
    threadDiscord.daemon = True
    threadDiscord.start()
    threadConsole = Thread(target=console_log)
    threadConsole.daemon = True
    threadConsole.start()


if __name__ == "__main__":
    try:
        main()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nctrl + c detected!\nExit.")
        sys.exit()