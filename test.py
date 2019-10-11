import discord ##discordでBOTを使うのにこれが必ずいる
import random ##運勢リストからランダムに出力するために必要

client = discord.Client()

@client.event #BOT起動時にcmdに表示される部分で無くてもよい
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#あいさつ反応「おはよう」
@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            ohayou = "おはよう、" + message.author.name + "。"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(ohayou)

    if message.content.startswith("依頼"):
        #レスポンスされる張り紙のリストを作成
        harigami = ["街中で出来そうなお使い系の依頼はどうだ？", "どこかの街に出かけて見るのはどうだ？", "ゴブリンの洞窟に関係する依頼がオススメだぞ。", "ちょいと難易度の高そうなダンジョンに挑んでみたらどうだ。", "危険な敵に関する仕事の受け手を求めている依頼があるようだぞ。", "店で買物でもして装備を整えるのも悪くはないんじゃないか？"]
        choice = message.author.name + "か。" + random.choice(harigami) #randomモジュール使用
        await message.channel.send(choice)


# token にDiscordのデベロッパサイトで取得したトークンを入れてください
client.run("NjMyMjgwNzg1NTY2ODI2NTIx.XaDHrg.QviZAevRxpBOtoSC2NqagCIUON4")
