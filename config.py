from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "15599295"))
API_HASH = getenv("API_HASH", "4ce42998f7df4a64934294dadca28ae0")
BOT_TOKEN = getenv("BOT_TOKEN", "5889054634:AAGu_lt5U8XmHwZTvVutBhQ75B_16N2q5cY")
BOT_NAME = getenv("BOT_NAME","𝐒𝐇𝐈𝐙𝐔𝐊𝐀 𓆩🇽𓆪 𝐑𝐎𝐁𝐎𝐓")
BOT_USERNAME = getenv("BOT_USERNAME", "itz_shizuka_robot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "its_star_boi")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Best_FriendsFor_Ever")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/252fc4a5c64895b0e539c.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/252fc4a5c64895b0e539c.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQAKSacRxSsSO_AihM_aBB6ZpapEH0Vo37Om4rIxbZDz7C093OaPeTFOAAj6MdK9I7RguFtRs_j88zUdrfXFDwx0dqYAQES5FowMeT9QLUyiFJfrHDVVUAPOkbozaljWa6xwFcaNFgGTpWpGHFasxqYJI1DcdHIs74wJPERivPbjoQW5zGgn_F2o9srP2JSM_lvm1ZOmlpFDQzDSaSRrIZVkOPRTMK9VHEKtuyuWcDZcsY6lVSDkgvXGYvNR-YwQRfHJp_3Y5EJp5ajQ12_wdgj9SIRIo4afkWWEHKiCtpVBzxwVqVRcAgqE6CZZb9tjGE05r8k3lMaV14Dk1m-m38AoAAAAAUx9yy8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5463205082").split()))
HEROKU_MODE = getenv("HEROKU_MODE", "ENABLE")
