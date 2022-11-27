import importlib
import os

from claire import LOGGER, bot


def import_modules(logger):
    path = "claire/modules/"
    for filename in os.listdir(path):
        if filename.endswith(".py"):
            importlib.import_module("claire.modules." + filename[:-3])
            logger.info("Imported module: " + filename)


import_modules(LOGGER)

print("Userbot Started Successfully ")


def main():
    try:
        bot.run_until_disconnected()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()