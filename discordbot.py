#!/usr/bin/env python3

# License MIT
# Copyright 2016-2023 Alex Winkler
# Version 4.0.3

from ftsbot.liquipediabot import liquipediabot
from ftsbot import secrets

bot = liquipediabot()

bot.run(secrets.token)
