import discord
import Classes
import Emotions
import Economy
from discord import Option
from discord.ext import commands

client = commands.Bot(command_prefix='.', intents=discord.Intents.all(), auto_help=True)
client.remove_command('help')

intents = discord.Intents.default()


@client.slash_command(autoComplete=True, description='translator')
async def tr(ctx, message, *, lang):
    await Emotions.tr(ctx=ctx, message=message, lang=lang)


@client.slash_command(autocomplete=True, description='команды бота')
async def help(ctx):
    await Emotions.help(ctx=ctx)


@client.slash_command(autocomplete=True, description='Ваш баланс')
async def balance(ctx, user: Option(discord.Member, description='выбери любого участника', required=False)):
    await Economy.balance(ctx=ctx, who=user)


@client.slash_command(autocomplete=True, description='50 на 50')
async def fifty(ctx, count):
    await Economy.fifty(ctx=ctx, count=count)


@client.slash_command(autocomplete=True, description='Вперёд на работу')
@commands.cooldown(1, 10800, commands.BucketType.user)
async def work(ctx):
    await Economy.work(ctx=ctx)


@work.error
async def work_error(ctx, error):
    await Economy.work_error(ctx=ctx, error=error)


@client.slash_command(autocomplete=True, description='Перевести монеты в банк')
async def deposit(ctx, count):
    await Economy.deposit(ctx=ctx, count=count)


@client.slash_command(autocomplete=True, description='Ударить')
async def punch(ctx, user: Option(discord.Member, description='выбери любого участника', required=True)):
    await Emotions.punch(ctx=ctx, user=user)


@client.slash_command(autocomplete=True, description='Разозлиться')
async def rage(ctx):
    await Emotions.rage(ctx=ctx)


@client.slash_command(autocomplete=True, description='Улыбнуться')
async def smile(ctx):
    await Emotions.smile(ctx=ctx)


@client.slash_command(autocomplete=True, description='Поздороваться')
async def hello(ctx, user: Option(discord.Member, description='выбери любого участника', required=False)):
    await Emotions.hello(ctx=ctx, user=user)


@client.slash_command(autocomplete=True, description='Заплакать')
async def cry(ctx):
    await Emotions.cry(ctx=ctx)


@client.slash_command(autocomplete=True, description='Затанцевать')
async def dance(ctx):
    await Emotions.dance(ctx=ctx)


@client.slash_command(autocomplete=True, description='Покраснеть')
async def shy(ctx):
    await Emotions.shy(ctx=ctx)


@client.slash_command(autocomplete=True, description='Обнять')
async def hug(ctx, user: Option(discord.Member, description='выбери любого участника', required=True)):
    await Emotions.hug(ctx=ctx, user=user)


@client.command()
async def btn(ctx):
    await Classes.btn(ctx=ctx)


@client.command()
async def ro(ctx):
    await Classes.ro(ctx=ctx)


@client.event
async def on_member_join(member):
    await client.get_channel(1073273093688131584).send(str(member.mention) + ' добро пожаловать не сервер :wave:')
    await client.get_channel(1073273093688131584).send(
        'https://i.pinimg.com/originals/26/1f/db/261fdbdd9daff46c9771c09e8592d6e2.gif')


@client.event
async def on_member_remove(member):
    await client.get_channel(1073273093688131584).send(str(member.mention) + ' покинул сервер :crying_cat_face:')
    await client.get_channel(1073273093688131584).send('https://media.tenor.com/QMHFxt501O0AAAAM/one-piece-sanji.gif')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="фонк"))


client.run('TOKEN')
