from discord.ui import View
import discord


class GenderView(View):
    @discord.ui.button(label='Парень', custom_id='male')
    async def male_button_callback(self, button, interaction):
        server = interaction.guild
        male_role = discord.utils.get(server.roles, name='♂️')
        female_role = discord.utils.get(server.roles, name='♀️')
        if female_role in interaction.user.roles:
            await interaction.response.send_message(f'Я выдал Вам роль {male_role.mention},'
                                                    f' но так как у Вас была роль {female_role.mention}, я её забрал',
                                                    ephemeral=True)
            await interaction.user.remove_roles(female_role)
            await interaction.user.add_roles(male_role)
        elif male_role in interaction.user.roles:
            await interaction.user.remove_roles(male_role)
            await interaction.response.send_message(f'Я забрал у Вас роль {male_role.mention},', ephemeral=True)
        else:
            await interaction.response.send_message(f'Я выдал Вам роль {male_role.mention}', ephemeral=True)
            await interaction.user.add_roles(male_role)

    @discord.ui.button(label='Девушка', custom_id='female')
    async def female_button_callback(self, button, interaction):
        server = interaction.guild
        male_role = discord.utils.get(server.roles, name='♂️')
        female_role = discord.utils.get(server.roles, name='♀️')
        if male_role in interaction.user.roles:
            await interaction.response.send_message(f'Я выдал Вам роль {female_role.mention},'
                                                    f' но так как у Вас была роль {male_role.mention}, я её забрал',
                                                    ephemeral=True)
            await interaction.user.remove_roles(male_role)
            await interaction.user.add_roles(female_role)
        elif female_role in interaction.user.roles:
            await interaction.user.remove_roles(female_role)
            await interaction.response.send_message(f'я забрал у вас роль {female_role.mention},', ephemeral=True)
        else:
            await interaction.response.send_message(f'Я выдал Вам роль {female_role.mention}', ephemeral=True)
            await interaction.user.add_roles(female_role)


class ServerRoleView(View):
    @discord.ui.select(min_values=0,
                       max_values=2,
                       placeholder='Выбрать роль',
                       options=[
                           discord.SelectOption(
                               label='Ценитель высокого искусства',
                               value='anime',
                               emoji='<:tohrusmug:1074794102467600435>',
                               description='Смотришь ли ты аниме'),
                           discord.SelectOption(
                               label='Геймер',
                               value='gamer',
                               emoji='<:anime_kmsfml:1074789245685874698>',
                               description='Играешь ли ты в игры'),
                       ])
    async def select_callback(self, select, interaction):
        server = interaction.guild
        Gamer_role = discord.utils.get(server.roles, name='Gamer')
        Anime_role = discord.utils.get(server.roles, name='Anime')
        role = None
        if Gamer_role in interaction.user.roles:
            await interaction.user.remove_roles(Gamer_role)
        if Anime_role in interaction.user.roles:
            await interaction.user.remove_roles(Anime_role)
        if 'gamer' in select.values:
            await interaction.user.add_roles(Gamer_role)
            role = f'{Gamer_role.mention}'
        if 'anime' in select.values:
            await interaction.user.add_roles(Anime_role)
            if Gamer_role in interaction.user.roles:
                role = f'{Gamer_role.mention}, {Anime_role.mention}'
            else:
                role = f'{Anime_role.mention}'
        if role is None:
            await interaction.response.send_message(f'Вы не выбрали ни одной роли, если у Вас до этого стояли '
                                                    f'какие-либо серверные роли, они были удалены', ephemeral=True)
        else:
            await interaction.response.send_message(f'Теперь у вас следующие серверные роли: {role}', ephemeral=True)


async def btn(ctx):
    em = discord.Embed(title='Гендерные роли', description='Выбор ролей не обязателен)')
    em.set_image(url='https://i.pinimg.com/originals/d1/19/f4/d119f46b16a114b1c889b4d5e4734cb7.gif')
    await ctx.send(embed=em, view=GenderView(timeout=None))
    await ctx.message.delete()


async def ro(ctx):
    em = discord.Embed(title='Серверные роли',
                       description='При выборе роли, Вас могут пинговать при поиске тиммейтов\n'
                                   'или для обсуждения какой-либо темы')
    em.set_image(url='https://i.pinimg.com/originals/5f/31/b8/5f31b8534e4f69f86adb69afe0b3f09e.gif')
    await ctx.response.send_message(embed=em, view=ServerRoleView(timeout=None))
