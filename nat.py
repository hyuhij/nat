import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['mewtwo'])
def charizard(message):
  bot.reply_to(message, "Best Normal - Timid, modest \nFor Y  -  Timid, hasty \nFor X - Naive and jolly")
  
@bot.message_handler(commands=['mew'])
def charmander(message):
  bot.reply_to(message, "Best - Timid, modest")

@bot.message_handler(commands=['tyranitar'])
def charmander(message):
  bot.reply_to(message, "Best - Adamant, brave")

@bot.message_handler(commands=['sharpedo'])
def charmander(message):
  bot.reply_to(message, "Best - Jolly, adamant")

@bot.message_handler(commands=['start'])
def fp(message):
  bot.reply_to(message, "Hello there, \nThis is Nature Bot. \nThis bot contains Best natures of Important Legendary and Non-Legendary Pokemon. \nFor example Deoxys has 4 forms so use \n/deoxys - This will give data about all forms of deoxys. \nPlease note that all commands start with small letter. \nThis bot has only some pokemon \n always use the full evolved pokemon name")

@bot.message_handler(commands=['articuno'])
def charmeleon(message):
  bot.reply_to(message, "Best - Careful")

@bot.message_handler(commands=['tapu'])
def charmeleon(message):
  bot.reply_to(message, "Best Koko - Jolly, naive, adamant \nFor Bulu- Adamant, impish \nFor Lele- Timid, modest \nFor Fini- Modest, calm, bold")

@bot.message_handler(commands=['error'])
def charmeleon(message):
  bot.reply_to(message, "If u find any command broken or if there is any missed legendary or non legendary then pm @SIlVER_KING")

@bot.message_handler(commands=['hexagroup'])
def bulbasaur(message):
  bot.reply_to(message, "https://t.me/killers69 \nJoin to chat and enjoy")

@bot.message_handler(commands=['credits'])
def charmeleon(message):
  bot.reply_to(message, "This bot was built by @SILVER_KING \nSpecial credits for providing materials- @kaustubh_kurosaki")

@bot.message_handler(commands=['auction'])
def fp(message):
  bot.reply_to(message, "Join Auction group- \nhttps://t.me/+rS-WDKKNrCUyOWZl \nJoin auction channel- \nhttps://t.me/shinyhub_official \nDaily auction of shiny, legendary, non-legendary pokemon and tms")

@bot.message_handler(commands=['zapdos'])
def bulbasaur(message):
  bot.reply_to(message, "Best - Modest")

@bot.message_handler(commands=['moltres'])
def ivysaur(message):
  bot.reply_to(message, "Best - Modest")

@bot.message_handler(commands=['celebi'])
def venusaur(message):
  bot.reply_to(message, "Best - Modest, Quiet")

@bot.message_handler(commands=['hooh'])
def venusaur(message):
  bot.reply_to(message, "Best - Careful, adamant")

@bot.message_handler(commands=['lugia'])
def venusaur(message):
  bot.reply_to(message, "Best - Adamant")

@bot.message_handler(commands=['raikou'])
def venusaur(message):
  bot.reply_to(message, "Best - Timid")

@bot.message_handler(commands=['fp'])
def fp(message):
  bot.reply_to(message, "gay of all time")

@bot.message_handler(commands=['entei'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, careful, jolly, impish")

@bot.message_handler(commands=['suicune'])
def fp(message):
  bot.reply_to(message, "Best- Careful")

@bot.message_handler(commands=['jirachi'])
def fp(message):
  bot.reply_to(message, "Best- Modest")

@bot.message_handler(commands=['kyogre'])
def fp(message):
  bot.reply_to(message, "Best- Modest, calm")

@bot.message_handler(commands=['groudon'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, impish")

@bot.message_handler(commands=['rayquaza'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, jolly")

@bot.message_handler(commands=['mamoswine'])
def fp(message):
  bot.reply_to(message, "Best- Adamant")

@bot.message_handler(commands=['melloetta'])
def fp(message):
  bot.reply_to(message, "Best Normal- Modest, calm \nFor Pirouette form - Jolly, hasty, naive, adamant")

@bot.message_handler(commands=['deoxys'])
def fp(message):
  bot.reply_to(message, "Best Normal - Timid, modest \nFor Attack - Naive, hasty, timid, jolly \nSpeed - Naive, hasty, timid, modest \nDefence - Relaxed, sassy")

@bot.message_handler(commands=['regirock'])
def fp(message):
  bot.reply_to(message, "Best- Relaxed")

@bot.message_handler(commands=['registeel'])
def fp(message):
  bot.reply_to(message, "Best- Sassy, relaxed")

@bot.message_handler(commands=['regice'])
def fp(message):
  bot.reply_to(message, "Best- Calm, careful")

@bot.message_handler(commands=['latias'])
def fp(message):
  bot.reply_to(message, "Best- Calm, modest, timid")

@bot.message_handler(commands=['latios'])
def fp(message):
  bot.reply_to(message, "Best- Modest, calm")

@bot.message_handler(commands=['arceus'])
def fp(message):
  bot.reply_to(message, "Best- Modest, timid")

@bot.message_handler(commands=['guzzlord'])
def fp(message):
  bot.reply_to(message, "Best- Adamant")

@bot.message_handler(commands=['buzzwole'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, impish")

@bot.message_handler(commands=['kommoo'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, impish, careful, jolly")

@bot.message_handler(commands=['dialga'])
def fp(message):
  bot.reply_to(message, "Best- Modest")

@bot.message_handler(commands=['giratina'])
def fp(message):
  bot.reply_to(message, "Best- Brave, adamant")

@bot.message_handler(commands=['palkia'])
def fp(message):
  bot.reply_to(message, "Best- Modest, timid")

@bot.message_handler(commands=['regigigas'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, adamant")

@bot.message_handler(commands=['darkrai'])
def fp(message):
  bot.reply_to(message, "Best- Modest, timid")

@bot.message_handler(commands=['reshiram'])
def fp(message):
  bot.reply_to(message, "Best- Modest")

@bot.message_handler(commands=['zekrom'])
def fp(message):
  bot.reply_to(message, "Best- Adamant")

@bot.message_handler(commands=['kyurem'])
def fp(message):
  bot.reply_to(message, "Best Normal - Adamant, modest \nWhite - Modest, timid \nBlack - Adamant, jolly")

@bot.message_handler(commands=['victini'])
def fp(message):
  bot.reply_to(message, "Best- Adamant")

@bot.message_handler(commands=['hoopa'])
def fp(message):
  bot.reply_to(message, "Best Confined - Modest, quite \nUnbound - Modest, quite ")

@bot.message_handler(commands=['diancie'])
def fp(message):
  bot.reply_to(message, "Best- Relaxed, sassy")

@bot.message_handler(commands=['volcanion'])
def fp(message):
  bot.reply_to(message, "Best- Modest")

@bot.message_handler(commands=['xerneas'])
def fp(message):
  bot.reply_to(message, "Best- Modest (if spa), adamant (if atk)")

@bot.message_handler(commands=['yveltal'])
def fp(message):
  bot.reply_to(message, "Best- Modest (if spa), adamant (if atk)")

@bot.message_handler(commands=['zygarde'])
def fp(message):
  bot.reply_to(message, "Best 10% - Jolly \n100% - Adamant, careful")

@bot.message_handler(commands=['necrozma'])
def fp(message):
  bot.reply_to(message, "Best Normal - Modest, quiet \nDusk - Adamant, brave \nDawn - Quiet, modest \nUltra - Modest, timid ")

@bot.message_handler(commands=['solgaleo'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, jolly")

@bot.message_handler(commands=['lunala'])
def fp(message):
  bot.reply_to(message, "Best- Modest, timid")

@bot.message_handler(commands=['zeraora'])
def fp(message):
  bot.reply_to(message, "Best- Jolly")

@bot.message_handler(commands=['marshadow'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, jolly")

@bot.message_handler(commands=['pheromosa'])
def fp(message):
  bot.reply_to(message, "Best- Hasty, naive, jolly")

@bot.message_handler(commands=['venusaur'])
def fp(message):
  bot.reply_to(message, "Best- Modest, calm, bold")

@bot.message_handler(commands=['blastoise'])
def fp(message):
  bot.reply_to(message, "Best- Modest, calm")

@bot.message_handler(commands=['charizard'])
def fp(message):
  bot.reply_to(message, "Best Normal- Modest, hasty, timid \nFor X- Jolly, naive \nFor Y- Modest, hasty, timid ")

@bot.message_handler(commands=['alakazam'])
def fp(message):
  bot.reply_to(message, "Best- Timid, hasty, naive")

@bot.message_handler(commands=['pinsir'])
def fp(message):
  bot.reply_to(message, "Best- jolly, adamant")

@bot.message_handler(commands=['heracross'])
def fp(message):
  bot.reply_to(message, "Best- Impish, careful, jolly")

@bot.message_handler(commands=['aerodactyl'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, naive, hasty")

@bot.message_handler(commands=['gyarados'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, careful, jolly")

@bot.message_handler(commands=['galvantula'])
def fp(message):
  bot.reply_to(message, "Best- Timid")

@bot.message_handler(commands=['arcanine'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, hasty, naive")

@bot.message_handler(commands=['snorlax'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave, careful, sassy")

@bot.message_handler(commands=['jolteon'])
def fp(message):
  bot.reply_to(message, "Best- Timid, naive, hasty")

@bot.message_handler(commands=['tentacruel'])
def fp(message):
  bot.reply_to(message, "Best- Timid")

@bot.message_handler(commands=['gengar'])
def fp(message):
  bot.reply_to(message, "Best- Timid, hasty")

@bot.message_handler(commands=['electrode'])
def fp(message):
  bot.reply_to(message, "Best- Timid, hasty, naive")

@bot.message_handler(commands=['dragonite'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, careful, jolly")

@bot.message_handler(commands=['ampharos'])
def fp(message):
  bot.reply_to(message, "Best- Calm, modest, sassy, bold")

@bot.message_handler(commands=['blaziken'])
def fp(message):
  bot.reply_to(message, "Best- Jolly")

@bot.message_handler(commands=['sceptile'])
def fp(message):
  bot.reply_to(message, "Best- Timid, hasty, naive")

@bot.message_handler(commands=['slaking'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, adamant")

@bot.message_handler(commands=['stoutland'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, adamant")

@bot.message_handler(commands=['darmanitan'])
def fp(message):
  bot.reply_to(message, "Best Zen - Modest, quiet, calm, bold")

@bot.message_handler(commands=['ninjask'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, naive, hasty")

@bot.message_handler(commands=['durant'])
def fp(message):
  bot.reply_to(message, "Best- Jolly")

@bot.message_handler(commands=['cinccino'])
def fp(message):
  bot.reply_to(message, "Best- Jolly")

@bot.message_handler(commands=['greninja'])
def fp(message):
  bot.reply_to(message, "Best ASH- Timid, naive, hasty")

@bot.message_handler(commands=['chesnaught'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave")

@bot.message_handler(commands=['delphox'])
def fp(message):
  bot.reply_to(message, "Best- Timid, hasty")

@bot.message_handler(commands=['crustle'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave, impish, careful")

@bot.message_handler(commands=['armaldo'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave, impish")

@bot.message_handler(commands=['golisopod'])
def fp(message):
  bot.reply_to(message, "Best- Impish, adamant, brave")

@bot.message_handler(commands=['scrafty'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave")

@bot.message_handler(commands=['florges'])
def fp(message):
  bot.reply_to(message, "Best- Modest, calm, bold")

@bot.message_handler(commands=['goodra'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, modest, careful")

@bot.message_handler(commands=['mienshao'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, hasty, naive")

@bot.message_handler(commands=['crabominable'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave")

@bot.message_handler(commands=['ferrothorn'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, impish, careful")

@bot.message_handler(commands=['dragalge'])
def fp(message):
  bot.reply_to(message, "Best- Modest, quiet, calm, sassy")

@bot.message_handler(commands=['krookodile'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, jolly")

@bot.message_handler(commands=['lucario'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, hasty, naive")

@bot.message_handler(commands=['dhelmise'])
def fp(message):
  bot.reply_to(message, "Best- Adamant")

@bot.message_handler(commands=['decidueye'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, careful")

@bot.message_handler(commands=['primarina'])
def fp(message):
  bot.reply_to(message, "Best- Modest, calm")

@bot.message_handler(commands=['metagross'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave, impish")

@bot.message_handler(commands=['garchomp'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, hasty, naive")

@bot.message_handler(commands=['incineroar'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave")

@bot.message_handler(commands=['sylveon'])
def fp(message):
  bot.reply_to(message, "Best- Modest, calm")

@bot.message_handler(commands=['manecite'])
def fp(message):
  bot.reply_to(message, "Best- Timid, naive, hasty")

@bot.message_handler(commands=['haxorus'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, naive, hasty, adamant")

@bot.message_handler(commands=['lopuuny'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, hasty, naive")

@bot.message_handler(commands=['braviary'])
def fp(message):
  bot.reply_to(message, "Best- Adamant")

@bot.message_handler(commands=['excadrill'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave")

@bot.message_handler(commands=['conkeldurr'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave")

@bot.message_handler(commands=['salamence'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, jolly")

@bot.message_handler(commands=['wishiwashi'])
def fp(message):
  bot.reply_to(message, "Best School- Adamant, impish, brave, relaxed, carefull, sassy")

@bot.message_handler(commands=['volcarona'])
def fp(message):
  bot.reply_to(message, "Best- Timid, naive, hasty")

@bot.message_handler(commands=['togekiss'])
def fp(message):
  bot.reply_to(message, "Best- Modest,calm")

@bot.message_handler(commands=['blissey'])
def fp(message):
  bot.reply_to(message, "Best- Modest, mild")

@bot.message_handler(commands=['noivern'])
def fp(message):
  bot.reply_to(message, "Best- Timid, hasty, naive")

@bot.message_handler(commands=['infernape'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, naive, hasty")

@bot.message_handler(commands=['chandelure'])
def fp(message):
  bot.reply_to(message, "Best- Modest, timid, calm, bold")

@bot.message_handler(commands=['espeon'])
def fp(message):
  bot.reply_to(message, "Best- Timid, hasty, naive")

@bot.message_handler(commands=['starmie'])
def fp(message):
  bot.reply_to(message, "Best- Timid")

@bot.message_handler(commands=['gallade'])
def fp(message):
  bot.reply_to(message, "Best- Jolly")

@bot.message_handler(commands=['ninetales'])
def fp(message):
  bot.reply_to(message, "Best Alolan- Timid")

@bot.message_handler(commands=['muk'])
def fp(message):
  bot.reply_to(message, "Best Alolan- Adamant, sassy, brave, careful")

@bot.message_handler(commands=['musdale'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave")

@bot.message_handler(commands=['hawlucha'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, naive, hasty")

@bot.message_handler(commands=['clawitzer'])
def fp(message):
  bot.reply_to(message, "Best- Modest")

@bot.message_handler(commands=['barbaracle'])
def fp(message):
  bot.reply_to(message, "Best- Adamant")

@bot.message_handler(commands=['leavanny'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, jolly")

@bot.message_handler(commands=['houndoom'])
def fp(message):
  bot.reply_to(message, "Best- timid")

@bot.message_handler(commands=['scizor'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave, impish, careful")

@bot.message_handler(commands=['accelgor'])
def fp(message):
  bot.reply_to(message, "Best- Timid, naive, hasty")

@bot.message_handler(commands=['escavalier'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, impish, relaxed")

@bot.message_handler(commands=['lycanroc'])
def fp(message):
  bot.reply_to(message, "Best- Jolly")

@bot.message_handler(commands=['druddigon'])
def fp(message):
  bot.reply_to(message, "Best- Adamant")

@bot.message_handler(commands=['tyrantrum'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, brave")

@bot.message_handler(commands=['staraptor'])
def fp(message):
  bot.reply_to(message, "Best- Jolly, hasty, naive")

@bot.message_handler(commands=['golurk'])
def fp(message):
  bot.reply_to(message, "Best- Adamant, impish")

@bot.message_handler(commands=['palossand'])
def fp(message):
  bot.reply_to(message, "Best- Modest, quiet")

@bot.message_handler(commands=['jellicent'])
def fp(message):
  bot.reply_to(message, "Best- Modest, calm, quiet, sassy")

@bot.message_handler(commands=['ribombee'])
def fp(message):
  bot.reply_to(message, "Best- Timid, hasty, naive")
  
bot.polling()