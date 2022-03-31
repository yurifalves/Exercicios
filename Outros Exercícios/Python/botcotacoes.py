import telebot
import pandas_datareader as web
import matplotlib.pyplot as plt
import os

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['acoes'])
def acoes1(mensagem):
    msg_enviada = bot.send_message(mensagem.chat.id, 'Envie o código da ação. Ex: PETR4.SA')
    bot.register_next_step_handler(msg_enviada, acoes2)


def acoes2(mensagem):
    ativo = mensagem.text  # O que o usuário enviou no telegram
    ativo_df = web.DataReader(ativo, data_source='yahoo', start='2021-03-01', end='2022-03-30')['Close']
    ativo_df.plot(color='crimson')
    plt.ylabel('R$', fontsize=15)
    plt.xlabel('Data', fontsize=15)
    plt.title(ativo, fontsize=20)
    plt.legend([ativo])
    plt.savefig(f'{ativo}.png')
    caminho_img = os.getcwd() + rf'\{ativo}.png'
    photo = open(caminho_img, 'rb')
    bot.send_photo(mensagem.chat.id, photo)
    bot.send_message(mensagem.chat.id, f'Cotação e Gráfico de "{ativo}" enviados com sucesso!')  # Responde
    photo.close()
    os.remove(caminho_img)


@bot.message_handler(commands=['moedas'])
def moedas(mensagem):
    bot.reply_to(mensagem, 'vc selecionou moedas')


@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    texto_padrao = """
    Escolha uma opção para continuar (Clique no item):
     /acoes Compara o preço de diferentes ações
     /moedas Compara o preço de diferentes moedas
     Responder qualquer outra coisa não vai funcionar, clique em uma das opções.
    """
    bot.send_message(mensagem.chat.id, texto_padrao)


bot.polling()  # Mantém o bot "funcionando/ligado"
