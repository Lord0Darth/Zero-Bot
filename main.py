import discord
import random
import aiohttp
import websockets
import re
import os
import time
import io
from datetime import datetime
import secret
import music
import asyncio

client = discord.Client()
COR = 0X6B2986
COR = 0x9910C

token = secret.seu_token()
msg_id = None
msg_user = None

@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('--------ZERO-------')
    await client.change_presence(status=discord.Status("dnd"))

#######################################'Comandos De Diversão'##########################################

@client.event
async def on_message(message):
    if message.content.lower() == ".moeda":
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '😀')
        if choice == 2:
            await client.add_reaction(message, '👑')

    if message.content.lower() == "o zero está on??":
        await client.send_message(message.channel, "Se eu estou falando contigo '-' ")

    if message.content.lower() == "zero":
        embed = discord.Embed(color=0x0f7da)
        embed.set_image(
            url="https://images-ext-2.discordapp.net/external/UuIdfaTGI15OWrW9tZnlXD-rjkhVSzsuQXhUh7463Pg/https/i.imgur.com/T8auOavh.jpg?width=764&height=430")
        await client.send_message(message.channel, embed=embed, content='**Falou comigo??**')
        embed.set_footer(text="By: ◤LUCAS◥")

    if message.content.lower() == ".votar":
        await client.add_reaction(message, '✅')
        await client.add_reaction(message, '❌')


    elif message.content.lower() == ".ping":
        now = datetime.utcnow()
        p = now - message.timestamp
        return (await client.send_message(message.channel, '🏓Pong!  {}ms'.format(p.microseconds // 10000)))

    if message.content.lower() == ".suicidar":
        embed = discord.Embed(title='Adeus',
                              color=0x0f7da,
                              description='Um pombinho acabou de se suicidar ;-;', )
        embed.set_image(
            url="https://pa1.narvii.com/6767/c861294198bb35eb2442ade15e6f23c8ccabc678_hq.gif")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower() == "boa noite":
        await client.delete_message(message)
        await client.send_message(message.channel, "Boa noite :new_moon_with_face:")

    if message.content.lower() == "bom dia":
        await client.delete_message(message)
        await client.send_message(message.channel, "Bom dia :sun_with_face:")

    if message.content.lower() == ".frases":
        choice = random.randint(1, 8)
        if choice == 1:
            await client.send_message(message.channel, '"É patetico desisitir de algo sem nem mesmo ter tentado" ')
        if choice == 2:
            await client.send_message(message.channel,' "Nós não sabemos que tipo de pessoas realmente somos até um momento antes da nossa morte. Assim que a morte vier abraçá-lo você perceberá o que você é" ')
        if choice == 3:
            await client.send_message(message.channel, ' "Quem diz que não pode ser feito nunca deve interromper aquele que está fazendo." ')
        if choice == 4:
            await client.send_message(message.channel,' "Pesadelos não duram para sempre. Um dia você acorda e eles se foram." ')
        if choice == 5:
            await client.send_message(message.channel, ' "com grandes poderes vem grandes responsabilidades." ')
        if choice == 6:
            await client.send_message(message.channel,' "A vida é uma peça de teatro que não permite ensaios. Por isso, cante, chore, dance, ria e viva intensamente, antes que a cortina se feche e a peça termine sem aplausos." ')
        if choice == 7:
            await client.send_message(message.channel,' "Somente assasinos poderiam não demonstrar sentimentos sabendo que pessoas próximas dela estão mortas" ')
        if choice == 8:
            await client.send_message(message.channel, ' " Aquele que quebra as regras, é como o lixo. Mas é muito pior quem abandona os seus amigos"')

        if message.content.lower().startswith('.dog'):
            async with aiohttp.get('https://random.dog/woof.json') as r:
                if r.status == 200:
                    js = await r.json()
                    canal = message.channel
                    await client.delete_message(message)
                    await client.send_message(canal, js['url'])

        if message.content.lower() == ".suicidar":
            embed = discord.Embed(title='Adeus',
                                  color=0x0f7da,
                                  description='Um pombinho acabou de se suicidar ;-;', )
            embed.set_image(
                url="https://pa1.narvii.com/6767/c861294198bb35eb2442ade15e6f23c8ccabc678_hq.gif")
            await client.send_message(message.channel, embed=embed)

########################################'Comandos Utilitarios'############################################

    if message.content.lower() == ".test":
        await client.delete_message(message)
        await client.send_message(message.channel, "_Olá Mundo, estou vivo!_")

    if message.content.lower().startswith('.sobre'):
        embed = discord.Embed(
                                title=":information_source: Estas são minhas informações atuais ;D",
                                color=0x268dc2,
                                description="**Que sou eu?**\n"
                                            "Sou um simples bot pra discord em desenvolvimento criado pra sua diversão :v:\n"
                                            "Tenho comandos variados muitos deles são utilitarios e de diversão (_comandos de moderação e musica estão sendo desenvolvidos..._)\n"
                                            "Qualquer duvida use **.ajuda** pra ver os meus comandos em seus servidor\n"
                                            "Ou entre em contato com o meu criador __◤LUCAS◥#5146__", )
        await client.send_message(message.channel, embed=embed, content='')

    elif message.content.lower() == ".avatar":

        try:
            member = message.mentions[0]
            embed = discord.Embed(
                title="",
                color=0x268dc2,
                description='[Clique aqui](' + member.avatar_url + ') para acessar o link do avatar de {}! '.format(
                    member.name))

            embed.set_image(url=member.avatar_url)
            await client.send_message(message.channel, embed=embed)

        except:
            member = message.author
            embed = discord.Embed(
                title='Seu avatar'.format(member.name),
                color= 0x268dc2,
                description='[Clique aqui](' + member.avatar_url + ') para acessar o link do seu Avatar  '.format(
                    member.name))

            embed.set_image(url=member.avatar_url)
            await client.send_message(message.channel, embed=embed)

    elif message.content.lower() == ".userinfo":
        try:
            user = message.mentions[0]
            server = message.server
            embedinfo = discord.Embed(title='Informações do usuário', color= 0x268dc2, )
            embedinfo.set_thumbnail(url=user.avatar_url)
            embedinfo.add_field(name='Usuário:', value=user.name)
            embedinfo.add_field(name='Apelido', value=user.nick)
            embedinfo.add_field(name='ID:', value=user.id)
            embedinfo.add_field(name='Entrou em:', value=user.joined_at.strftime("%d %b %Y às %H:%M"))
            embedinfo.add_field(name='Server criado em:', value=server.created_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='Jogando:', value=user.game)
            embedinfo.add_field(name="Status:", value=user.status)
            embedinfo.add_field(name='Cargos:', value=([role.name for role in user.roles if role.name != "@everyone"]))
            await client.send_message(message.channel, embed=embedinfo)
        except ImportError:
            await client.send_message(message.channel, 'Buguei!')
        except:
            await client.send_message(message.channel, 'Mencione um usuário válido!')
        finally:
            pass

    elif message.content.lower().startswith('.serverinfo'):
        server = message.server
        embedserver = discord.Embed(
            title='Informações do Servidor',
            color=0x551A8B,
            descripition='Essas são as informações\n')
        embedserver = discord.Embed(name="{} Server ".format(message.server.name), color=0x268dc)
        embedserver.add_field(name="Nome:", value=message.server.name, inline=True)
        embedserver.add_field(name=":Dono:", value=message.server.owner.mention)
        embedserver.add_field(name="ID", value=message.server.id, inline=True)
        embedserver.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        embedserver.add_field(name=":Membros:", value=len(message.server.members), inline=True)
        embedserver.add_field(name=":Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        embedserver.add_field(name="Emojis:", value=f"{len(message.server.emojis)}/100")
        embedserver.add_field(name=":Região:", value=str(message.server.region).title())
        embedserver.set_thumbnail(url=message.server.icon_url)
        embedserver.set_footer(text="By: ◤LUCAS◥ ")
        await client.send_message(message.channel, embed=embedserver)

    if message.content.lower() == ".ajuda":
        embedhelp = discord.Embed(
            title="**Ajuda do Zero**",
            color=0x551A8B,
            description="Te mandei meus comandos no DM olhe suas mensagens diretas!\n"
                        ":sos: Servidor de Suporte\n"
                        "https://discord.me/zerohouse \n"
                        ":heart_decoration: Me convide para seu servidor\n"
                        "https://goo.gl/9nECqp", )
        embedhelp.set_thumbnail(
            url='https://st2.depositphotos.com/6367796/9368/v/950/depositphotos_93685540-stock-illustration-pop-art-comics-icon-help.jpg')
        embedhelp.set_footer(text="By: ◤LUCAS◥")
        msg =await client.send_message(message.channel, embed=embedhelp, content=message.author.mention)
        await client.add_reaction(msg, '🆘')
        embedhelp = discord.Embed(
            title=":bookmark: Comandos",
            color=0x551A8B,
            description="**Ainda estou em desenvolvimento mais tenho estes comandos abaixo que poderão te ajudar ;D**\n"
                        ".test   | Para saber se estou funcionado em seu servidor. \n"
                        ".moeda  | Escolherei aleatorimente entre cara ou coroa.\n"
                        ".ajuda  | Irei lhe enviar esta mensagem.\n"
                        ".sobre  | Irei dizer um pouco sobre mim e irei mostrar minhas informações atuais.\n"
                        ".userinfo  | Irei lhe mostrar as informações do usuario mencionado.\n "
                        ".serverinfo |  Irei lhe enviar as informações do servidor atual.\n" 
                        ".avatar  | Irei lhe mandar o avatar do usuario mencionado.\n"
                        ".votar (mensagem)| Irei enviar uma votação de :white_check_mark: ou :x: na sua mensagem\n"
                        ".ping  | Irei lhe responder com Pong! \n"
                        ".frases  | Irei lhe mandar frases aleatorias. \n"
                        " bom dia | Irei lhe dar um bom dia ensolarado.\n"
                        " boa noite | Irei lhe dar uma boa noite estrelada. \n"
                        ".convite | Irei te mandar o convite para me adicionar em seu servidor e junto o convite para entrar em meu servidor de suporte.\n"
                        ".suicidar | Livrara um pombinho de suas dores\n"
                        "Tenho outros comandos secretos que só podem ser usados em meu servidor de suporte :3",)
        embedhelp.set_footer(text="By: ◤LUCAS◥")
        await client.send_message(message.author, embed=embedhelp)

    elif message.content.lower() == ".convite":
        embedinvite = discord.Embed(
            title="Aqui estão os meus convites!!",
            color=0x551A8B,
            description="_Aqui está o convite para me adicionar em seu servidor e para entrar no meu servidor de suporte ;D_\n"
                        ":sos: Servidor de Suporte\n"
                        "https://discord.me/zerohouse \n"
                        ":heart_decoration: Me convide para seu servidor\n"
                        "https://goo.gl/9nECqp", )
        await client.send_message(message.channel, embed=embedinvite)

    elif message.content.lower() == ".sugestão":

        embedhelp = discord.Embed(
            title="Estas são minhas sugestões.",
            color=0x551A8B,
            description="Digite **1** para eu te recomendar um Anime.\n"
                        "Digite **2** para eu te recomendar um Serie.\n"
                        "Digite **3** para eu te recomendar um Filme. \n"
                        "Digite **4** para eu te recomendar um Livro.\n"
                        "Digite **5** para eu te recomendar um Mangá. \n"
                        "Digite **6** para eu te recomendar um Jogo. ", )
        embedhelp.set_footer(text="By: ◤LUCAS◥")
        await client.send_message(message.channel, embed=embedhelp)

###########################################'Comandos de Moderação###########################################################

    @client.event
    async def on_member_ban(user):
        channel = discord.utils.find(lambda c: c.name == 'chat', user.server.channels)
        embed = discord.Embed(title='Sinta o martelo!',
                              description='Algum moderador usou o martelo para banir o membro **@{0.name}** do servidor!\n\nO martelo deve ter doído <:martelodoban:414935434951524353>'.format(user),
                              color=0xbb0021)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_image(url='https://imgur.com/gallery/WOjy315')
        await client.send_message(channel, embed=embed)

########################################'Comandos de Adiministrador'#####################################

    if message.content.lower() == ".game":
        if not message.author.id == "302148993688010752":
         return await client.send_message(message.channel, 'ERR0R: Você não tem permisão para usar esse comando')
        game = message.content[5:]
        await client.delete_message(message)
        await client.change_presence(game=discord.Game(name=game, url='https://www.twitch.tv/universo_mangaka', type=1))
        await client.send_message(message.channel, "Meu status foi trocado para: " + game + "")

    if message.content.lower() == ".cargos":
        embed1 = discord.Embed(
            title="_Escolha seu Elo!_ ",
            color=0X6B2986,
            description="- Otaku = 🈸\n"
                        "- Zueiro  =  🎉 \n"
                        "- Geek = 💎\n"
                        "- Nerd = 👓\n"
                        "- Artista = 🎨\n"
                        "- Gamer  = 🎮", )

        botmsg = await client.send_message(message.channel, embed=embed1)

        await client.add_reaction(botmsg, "🈸")
        await client.add_reaction(botmsg, "🎉")
        await client.add_reaction(botmsg, "💎")
        await client.add_reaction(botmsg, "👓")
        await client.add_reaction(botmsg, "🎨")
        await client.add_reaction(botmsg, "🎮")

        global msg_id
        msg_id = botmsg.id

        global msg_user
        msg_user = message.author

    @client.event
    async def on_reaction_add(reaction, user):
        msg = reaction.message

        if reaction.emoji == "🈸" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Otaku", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

        if reaction.emoji == "🎉" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Zueiro", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

        if reaction.emoji == "💎" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Geek", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

        if reaction.emoji == "👓" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Nerd", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

        if reaction.emoji == "🎨" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Artista", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

        if reaction.emoji == "🎮" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Gamer", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

    @client.event
    async def on_reaction_remove(reaction, user):
        msg = reaction.message

        if reaction.emoji == "🈸" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Otaku", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

        if reaction.emoji == "🎉" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Zueiro", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

        if reaction.emoji == "💎" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Geek", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

        if reaction.emoji == "👓" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Nerd", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

        if reaction.emoji == "🎨" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Artista", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

        if reaction.emoji == "🎮" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Gamer", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove") \

client.run(token)

