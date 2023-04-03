import random
import discord
import gifHub
from discord import Option
from googletrans import Translator

translator = Translator()
coin = '<a:crowncoin:1084011890608439306>'


async def randWork(ctx, earn):
    works = [f'Работая на заводе, Вы заработали {earn} {coin}',
             f'Идя по улице, Вы случайно нашли {earn} {coin}',
             f'Работая дворником, Вы заработали {earn} {coin}',
             f'Работая программистом на фрилансе, Вы заработали {earn} {coin}',
             f'Работая программистом в гугл, Вы заработали {earn} {coin}']
    i = random.randint(0, len(works) - 1)
    work = works[i]
    return work


async def tr(ctx, message, *, lang):
    try:
        translated = translator.translate(message, dest=lang)
        await ctx.respond(f'{translated.text}')
    except:
        'invalid destination language'
        await ctx.respond(f'there is no language: {lang}')


async def help(ctx):
    em = discord.Embed(title='Commands')
    em.set_image(url='https://media.tenor.com/IV5d_iissCEAAAAM/roronoa-zoro.gif')
    em.add_field(name=f'/rage   -   разозлиться\n'
                      f'/smile   -   улыбнуться\n'
                      f'/punch   -   ударить\n'
                      f'/cry   -   заплакать\n'
                      f'/hug   -   обнять\n'
                      f'/hello   -   поприветствовать\n'
                      f'/dance   -   затанцевать\n'
                      f'/shy   -   засмущаться', value='')
    await ctx.send(embed=em)
    await ctx.delete()


async def emCreator(gif_hub, ctx, text, user: discord.Member = None):
    i = random.randint(0, len(gif_hub) - 1)
    gif = gif_hub[i]
    em = discord.Embed()
    em.set_image(url=gif)
    if user:
        em.add_field(name=f'', value=f'{ctx.author.mention} {text} {user.mention}')
    elif not user:
        em.add_field(name=f'', value=f'{ctx.author.mention} {text}')
    return em


async def punch(ctx, user: Option(discord.Member, description='выбери любого участника', required=True)):
    em = await emCreator(gif_hub=gifHub.punch_gif, ctx=ctx, text='бьёт', user=user)
    await ctx.send(embed=em)
    await ctx.delete()


async def rage(ctx):
    em = await emCreator(gif_hub=gifHub.rage_gif, ctx=ctx, text='злится')
    await ctx.send(embed=em)
    await ctx.delete()


async def smile(ctx):
    em = await emCreator(gif_hub=gifHub.smile_gif, ctx=ctx, text='улыбается')
    await ctx.send(embed=em)
    await ctx.delete()


async def hello(ctx, user: Option(discord.Member, description='выбери любого участника', required=False)):
    if user:
        em = await emCreator(gif_hub=gifHub.hello_gif, ctx=ctx, text='приветствует', user=user)
        await ctx.send(embed=em)
        await ctx.delete()
    else:
        em = await emCreator(gif_hub=gifHub.hello_gif, ctx=ctx, text='Машет ручкой')
        await ctx.send(embed=em)
        await ctx.delete()


async def cry(ctx):
    em = await emCreator(gif_hub=gifHub.cry_gif, ctx=ctx, text='плачет(')
    await ctx.send(embed=em)
    await ctx.delete()


async def dance(ctx):
    em = await emCreator(gif_hub=gifHub.dence_gif, ctx=ctx, text='танцует')
    await ctx.send(embed=em)
    await ctx.delete()


async def shy(ctx):
    em = await emCreator(gif_hub=gifHub.shy_gif, ctx=ctx, text='покраснел...')
    await ctx.send(embed=em)
    await ctx.delete()


async def hug(ctx, user: Option(discord.Member, description='выбери любого участника', required=True)):
    em = await emCreator(gif_hub=gifHub.hug_gif, ctx=ctx, text='обнимает', user=user)
    await ctx.send(embed=em)
    await ctx.delete()
