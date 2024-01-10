from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "4ed1b0d3f9394927baac66bcae1a4d53")
      API_ID = int(getenv("API_ID", "29219263"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6281601464:AAGG46HfGlBUAJTeojKFg3QIXB0XBm65y5I")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001310101942:-1001511985432").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
