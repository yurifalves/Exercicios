import telebot
import pandas_datareader as web
import matplotlib.pyplot as plt
import os

bot = telebot.TeleBot(TOKEN)


'''@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    bot.reply_to(mensagem, 'respondendo a opcao1 :)')'''


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 asdfgasdfg
     /opcao2 asdfgasdfg
     /opcao3 asdfgasdfg
     Responder qualquer outra coisa não vai funcionar, clique em uma das opções.
    """
    ativo = mensagem.text  # O que o usuário enviou no telegram
    ativo_df = web.DataReader(ativo, data_source='yahoo', start='2022-03-01', end='2022-03-30')['Close']
    ativo_df.plot(color='red')
    plt.savefig(f'grafico-{ativo}.png')
    caminho_img = os.getcwd() + f'\grafico-{ativo}.png'
    photo = open(caminho_img, 'rb')
    bot.send_photo(mensagem.from_user.id, photo)
    bot.reply_to(mensagem, f'Cotação e Gráfico de "{ativo}" enviados com sucesso!')  # Responde marcando

bot.polling()  # Mantém o bot "funcionando/ligado"
