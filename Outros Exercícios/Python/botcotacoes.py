import telebot
import pandas_datareader as web
import requests
import matplotlib.pyplot as plt
import os

bot = telebot.TeleBot(TOKEN)


moedas_dic = {'USD-BRL': 'Dólar Americano/Real Brasileiro', 'EUR-BRL': 'Euro/Real Brasileiro',
              'GBP-BRL': 'Libra Esterlina/Real Brasileiro',
              'AUD-BRL': 'Dólar Australiano/Real Brasileiro',
              'CAD-BRL': 'Dólar Canadense/Real Brasileiro', 'NZD-BRL': 'Dólar Neozelandês/Real Brasileiro',
              'HKD-BRL': 'Dólar de Hong Kong/Real Brasileiro', 'SGD-BRL': 'Dólar de Cingapura/Real Brasileiro',
              'TWD-BRL': 'Dólar Taiuanês/Real Brasileiro', 'ARS-BRL': 'Peso Argentino/Real Brasileiro',
              'BOB-BRL': 'Boliviano/Real Brasileiro',
              'AED-BRL': 'Dirham dos Emirados/Real Brasileiro',
              'BTC-BRL': 'Bitcoin/Real Brasileiro',
              'CHF-BRL': 'Franco Suíço/Real Brasileiro', 'CLP-BRL': 'Peso Chileno/Real Brasileiro',
              'CNY-BRL': 'Yuan Chinês/Real Brasileiro', 'COP-BRL': 'Peso Colombiano/Real Brasileiro',
              'DKK-BRL': 'Coroa Dinamarquesa/Real Brasileiro', 'DOGE-BRL': 'Dogecoin/Real Brasileiro',
              'ETH-BRL': 'Ethereum/Real Brasileiro',
              'ILS-BRL': 'Novo Shekel Israelense/Real Brasileiro',
              'INR-BRL': 'Rúpia Indiana/Real Brasileiro',
              'JPY-BRL': 'Iene Japonês/Real Brasileiro',
              'LTC-BRL': 'Litecoin/Real Brasileiro',
              'MXN-BRL': 'Peso Mexicano/Real Brasileiro',
              'NOK-BRL': 'Coroa Norueguesa/Real Brasileiro',
              'PEN-BRL': 'Sol do Peru/Real Brasileiro',
              'PLN-BRL': 'Zlóti Polonês/Real Brasileiro',
              'PYG-BRL': 'Guarani Paraguaio/Real Brasileiro',
              'RUB-BRL': 'Rublo Russo/Real Brasileiro',
              'SAR-BRL': 'Riyal Saudita/Real Brasileiro',
              'SEK-BRL': 'Coroa Sueca/Real Brasileiro',
              'THB-BRL': 'Baht Tailandês/Real Brasileiro',
              'TRY-BRL': 'Nova Lira Turca/Real Brasileiro',
              'UYU-BRL': 'Peso Uruguaio/Real Brasileiro',
              'XRP-BRL': 'XRP/Real Brasileiro',
              'ZAR-BRL': 'Rand Sul-Africano/Real Brasileiro'}


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


@bot.message_handler(commands=['moedasinst'])
def moedasinst(mensagem):
    texto = ''
    for moeda in moedas_dic:
        requisicao_dic = requests.get(f'https://economia.awesomeapi.com.br/last/{moeda}').json()[moeda.replace('-', '')]
        moeda_name = requisicao_dic["name"][:requisicao_dic["name"].find("/")]
        moeda_code = requisicao_dic["code"]
        preco_compra = round(float(requisicao_dic["bid"]), 2)
        texto += f'1 {moeda_code} ({moeda_name}) = {str(preco_compra).replace(".", ",")} {requisicao_dic["codein"]}\n{requisicao_dic["create_date"]}\n\n'
    bot.reply_to(mensagem, texto)


@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    texto_padrao = """
    Escolha uma opção para continuar (Clique no item):
     /acoes Compara o preço de diferentes ações
     /moedasinst Compara o preço de diferentes moedas
     Responder qualquer outra coisa não vai funcionar, clique em uma das opções.
    """
    bot.send_message(mensagem.chat.id, texto_padrao)


bot.polling()  # Mantém o bot "funcionando/ligado"
