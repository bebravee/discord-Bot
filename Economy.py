import Emotions
import discord
import json
import random
from discord.ext import commands

coin = '<a:crowncoin:1084011890608439306>'


async def balance(ctx, who):
    await open_account(ctx.author)
    users = await get_bank_date()
    if who:
        who_wallet_amt = users[str(who.id)]['wallet']
        who_bank_amt = users[str(who.id)]['bank']
        em = discord.Embed(title='', colour=discord.Colour.blue())
        em.set_author(name=f'{who}', icon_url=who.avatar.url)
        em.add_field(name='В кармане', value=f'{coin} {who_wallet_amt}')
        em.add_field(name='В банке', value=f'{coin} {who_bank_amt}')
        em.add_field(name='Всего', value=f'{coin} {who_bank_amt + who_wallet_amt}')
        await ctx.response.send_message(embed=em)
        return
    else:
        user = ctx.author
        wallet_amt = users[str(user.id)]['wallet']
        bank_amt = users[str(user.id)]['bank']
        em = discord.Embed(title='', colour=discord.Colour.blue())
        em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
        em.add_field(name='В кармане', value=f'{coin} {wallet_amt}')
        em.add_field(name='В банке', value=f'{coin} {bank_amt}')
        em.add_field(name='Всего', value=f'{coin} {bank_amt + wallet_amt}')
        await ctx.response.send_message(embed=em)


async def work(ctx):
    await open_account(ctx.author)
    users = await get_bank_date()
    user = ctx.author
    earn = random.randrange(300, 1000)
    users[str(user.id)]['wallet'] += earn
    with open('money.json', 'w') as f:
        json.dump(users, f)
    em = discord.Embed(title='', colour=discord.Colour.green())
    em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
    em.add_field(name='', value=f'{await Emotions.randWork(ctx=ctx, earn=earn)}')
    await ctx.response.send_message(embed=em)


async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        if round(error.retry_after) > 3600:
            ti = round(error.retry_after)
            ti /= 60
            ti /= 60
            await ctx.response.send_message(f'команда в кд. Попробуйте через {round(ti)} часа.', ephemeral=True)
        elif round(error.retry_after) > 60:
            ti = round(error.retry_after)
            ti /= 60
            await ctx.response.send_message(f'команда в кд. Попробуйте через {round(ti)} минут.', ephemeral=True)
        else:
            await ctx.response.send_message(f'команда в кд. Попробуйте через {round(error.retry_after)} секунд.',
                                            ephemeral=True)


async def fifty(ctx, count):
    await open_account(ctx.author)
    users = await get_bank_date()
    user = ctx.author
    try:
        if count == 'all':
            all = users[str(user.id)]['wallet']
            if all == 0:
                await ctx.response.send_message(f'У вас в кармане 0 монет', ephemeral=True)
                return
            else:
                i = random.randint(0, 1)
                if i == 0:
                    em = discord.Embed(title='Победа',
                                       description=f'Теперь количество ваших {coin} в кармане равно {all * 2}',
                                       colour=discord.Colour.green())
                    em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
                    users[str(user.id)]['wallet'] += all
                    await ctx.response.send_message(embed=em)
                    with open('money.json', 'w') as f:
                        json.dump(users, f)
                if i == 1:
                    em = discord.Embed(title='Проигрышь',
                                       description=f'Теперь количество ваших {coin} в кармане равно нулю',
                                       colour=discord.Colour.red())
                    em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
                    users[str(user.id)]['wallet'] -= all
                    await ctx.response.send_message(embed=em)
                    with open('money.json', 'w') as f:
                        json.dump(users, f)
        elif int(count) <= 0:
            await ctx.response.send_message(f'Вы не можете играть с такой ставкой{coin}', ephemeral=True)
            return
        elif users[str(user.id)]['wallet'] <= int(count):
            all = users[str(user.id)]['wallet']
            if all == 0:
                await ctx.response.send_message(f'У Вас в кармане 0 {coin}', ephemeral=True)
                return
            else:
                i = random.randint(0, 1)
                if i == 0:
                    em = discord.Embed(title='Победа',
                                       description=f'Теперь количество ваших {coin} в кармане равно {all * 2}',
                                       colour=discord.Colour.green())
                    em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
                    users[str(user.id)]['wallet'] += all
                    await ctx.response.send_message(embed=em)
                    with open('money.json', 'w') as f:
                        json.dump(users, f)
                if i == 1:
                    em = discord.Embed(title='Проигрышь',
                                       description=f'Теперь количество ваших {coin} в кармане равно нулю',
                                       colour=discord.Colour.red())
                    em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
                    users[str(user.id)]['wallet'] -= all
                    await ctx.response.send_message(embed=em)
                    with open('money.json', 'w') as f:
                        json.dump(users, f)
        else:
            all = int(count)
            i = random.randint(0, 1)
            if i == 0:
                em = discord.Embed(title='Победа',
                                   description=f'Вы выйграли {all} {coin}',
                                   colour=discord.Colour.green())
                em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
                users[str(user.id)]['wallet'] += all
                await ctx.response.send_message(embed=em)
                with open('money.json', 'w') as f:
                    json.dump(users, f)
            if i == 1:
                em = discord.Embed(title='Проигрышь',
                                   description=f'Вы проиграли {all} {coin}',
                                   colour=discord.Colour.red())
                em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
                users[str(user.id)]['wallet'] -= all
                await ctx.response.send_message(embed=em)
                with open('money.json', 'w') as f:
                    json.dump(users, f)
    except:
        'discord.errors.ApplicationCommandInvokeError: Application Command raised an exception: ValueError: invalid ' \
        'literal for int() with base 10:'
        await ctx.response.send_message(f'Ставьте либо число, либо пишите "all"', ephemeral=True)
        return


async def deposit(ctx, count):
    await open_account(ctx.author)
    users = await get_bank_date()
    user = ctx.author
    try:
        if count == 'all':
            all = users[str(user.id)]['wallet']
            users[str(user.id)]['wallet'] -= all
            users[str(user.id)]['bank'] += all
            em = discord.Embed(title='', colour=discord.Colour.green())
            em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
            em.add_field(name='', value=f'Вы перевели все {coin} в банк', inline=False)
            em.add_field(name='В кармане', value=f'{coin} ' + str(users[str(user.id)]['wallet']), inline=True)
            em.add_field(name='В банке', value=f'{coin} ' + str(users[str(user.id)]['bank']))
            await ctx.response.send_message(embed=em)
        elif int(count) <= 0:
            await ctx.response.send_message(f'Вы не можете перевести такое число {coin} в '
                                            f'банк', ephemeral=True)
            return
        elif users[str(user.id)]['wallet'] <= int(count):
            all = users[str(user.id)]['wallet']
            if all == 0:
                await ctx.response.send_message(f'У Вас в кармане 0 {coin}', ephemeral=True)
                return
            users[str(user.id)]['wallet'] -= all
            users[str(user.id)]['bank'] += all
            em = discord.Embed(title='', colour=discord.Colour.green())
            em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
            em.add_field(name='', value=f'Вы перевели все {coin} в банк', inline=False)
            em.add_field(name='В кармане',
                         value=f'{coin} ' + str(users[str(user.id)]['wallet']), inline=True)
            em.add_field(name='В банке', value=f'{coin} ' + str(users[str(user.id)]['bank']))
            await ctx.response.send_message(embed=em)
        else:
            users[str(user.id)]['wallet'] -= int(count)
            users[str(user.id)]['bank'] += int(count)
            em = discord.Embed(title='', colour=discord.Colour.green())
            em.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar.url)
            em.add_field(name='', value=f'Вы перевели {count} {coin} в банк', inline=False)
            em.add_field(name='В кармане',
                         value=f'{coin} ' + str(users[str(user.id)]['wallet']), inline=True)
            em.add_field(name='В банке', value=f'{coin} ' + str(users[str(user.id)]['bank']))
            await ctx.response.send_message(embed=em)
        with open('money.json', 'w') as f:
            json.dump(users, f)
    except:
        'discord.errors.ApplicationCommandInvokeError: Application Command raised an exception: ValueError: invalid ' \
        'literal for int() with base 10:'
        await ctx.response.send_message(f'Переводите либо числом, либо пишите "all"', ephemeral=True)
        return


async def open_account(user):
    with open('money.json', 'r') as f:
        users = json.load(f)
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 0
        users[str(user.id)]['bank'] = 0
    with open('money.json', 'w') as f:
        json.dump(users, f)
    return True


async def get_bank_date():
    with open('money.json', 'r') as f:
        users = json.load(f)
    return users
