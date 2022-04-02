import telebot
import pandas_datareader as web
import requests
import matplotlib.pyplot as plt
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

bot = telebot.TeleBot('5280082287:AAF9zyPYm49sqF2NfwcqGmc01QYWBQqgxDY')


moedas_dic = {'USD-BRL': 'Dólar Americano/Real Brasileiro', 'EUR-BRL': 'Euro/Real Brasileiro',
              'GBP-BRL': 'Libra Esterlina/Real Brasileiro', 'AUD-BRL': 'Dólar Australiano/Real Brasileiro',
              'CAD-BRL': 'Dólar Canadense/Real Brasileiro', 'NZD-BRL': 'Dólar Neozelandês/Real Brasileiro',
              'HKD-BRL': 'Dólar de Hong Kong/Real Brasileiro', 'SGD-BRL': 'Dólar de Cingapura/Real Brasileiro',
              'TWD-BRL': 'Dólar Taiuanês/Real Brasileiro', 'ARS-BRL': 'Peso Argentino/Real Brasileiro',
              'BOB-BRL': 'Boliviano/Real Brasileiro', 'AED-BRL': 'Dirham dos Emirados/Real Brasileiro',
              'BTC-BRL': 'Bitcoin/Real Brasileiro', 'CHF-BRL': 'Franco Suíço/Real Brasileiro', 'CLP-BRL': 'Peso Chileno/Real Brasileiro',
              'CNY-BRL': 'Yuan Chinês/Real Brasileiro', 'COP-BRL': 'Peso Colombiano/Real Brasileiro',
              'DKK-BRL': 'Coroa Dinamarquesa/Real Brasileiro', 'DOGE-BRL': 'Dogecoin/Real Brasileiro',
              'ETH-BRL': 'Ethereum/Real Brasileiro', 'ILS-BRL': 'Novo Shekel Israelense/Real Brasileiro',
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
    texto = '''Envie agora a Data inicial e Data final no formato *datainicial* *datafinal*.
    Ex: *30/03/2016 07/04/2022*.
    (*30 de Março de 2016* até *07 de Abril de 2022*)
    '''
    msg_enviada = bot.send_message(mensagem.chat.id, texto, parse_mode='Markdown')
    bot.register_next_step_handler(msg_enviada, acoes3, ativo)


def acoes3(mensagem, ativo):
    datas = mensagem.text
    dia1, mes1, ano1 = datas.split()[0].split(sep='/')
    dia2, mes2, ano2 = datas.split()[1].split(sep='/')
    ativo_df = web.DataReader(ativo, data_source='yahoo', start=f'{ano1}-{mes1}-{dia1}-', end=f'{ano2}-{mes2}-{dia2}')['Close']
    ativo_df.plot(color='crimson')
    plt.title(ativo, fontsize=20)
    plt.legend([ativo], loc='upper left')
    plt.xlabel('Data', fontsize=13)
    plt.ylabel('R$', fontsize=9)
    plt.savefig(f'{ativo}.png')
    caminho_img = os.listdir(os.getcwd())[os.listdir(os.getcwd()).index(rf'{ativo}.png')]
    photo = open(caminho_img, 'rb')
    bot.send_photo(mensagem.chat.id, photo)
    photo.close()
    os.remove(caminho_img)
    bot.send_message(mensagem.chat.id, f'Cotação de "{ativo}" ({dia1}/{mes1}/{ano1}-{dia2}/{mes2}/{ano2}) enviada com sucesso!')  # Responde
    texto_final = """
    Para voltar ao menu inicial clique em:
     /inicio Retorna ao menu do bot
    """
    bot.send_message(mensagem.chat.id, texto_final)


@bot.message_handler(commands=['moedasinst'])
def moedasinst(mensagem):
    texto_inicio = """
        Selecione algum método para consulta
        /google
        /awesomeapi
        """
    bot.send_message(mensagem.chat.id, texto_inicio)


@bot.message_handler(commands=['google'])
def google1(mensagem):
    texto = '''Envie o nome da moeda a ser consultada.\nEx: Dólar\n\n
/moedasgoogle Moedas Suportadas'''
    msg_enviada = bot.send_message(mensagem.chat.id, texto)
    bot.register_next_step_handler(msg_enviada, google2)


def google2(mensagem):
    texto_inicio = """
            Para saber quantas as moedas suportadas:
            /moedasgoogle
            """
    ativo = None
    if mensagem.text != '/moedasgoogle':
        ativo = mensagem.text
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.google.com')
        barra_pesquisa = driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        barra_pesquisa.send_keys(ativo)
        barra_pesquisa.submit()
        valor_ativo = driver.find_element(By.XPATH,
                                          '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
        horario = driver.find_element(By.XPATH,
                                      '//*[@id="knowledge-currency__updatable-data-column"]/div[2]/span').text[:-2]
        bot.send_message(mensagem.chat.id, f'*1 {mensagem.text} = R$ {valor_ativo}* ({horario})', parse_mode='Markdown')
        time.sleep(1)
        texto_final = """
        Para voltar ao menu inicial clique em:
         /inicio Retorna ao menu do bot.
        """
        bot.send_message(mensagem.chat.id, texto_final)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.google.com')
        barra_pesquisa = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        barra_pesquisa.send_keys('dolar')
        barra_pesquisa.submit()
        horario = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[2]/span').text[:-2]
        moedas = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr[3]/td[3]/div/select').text
        qtd_moedas = len(moedas.splitlines())
        texto = f'''
            *{qtd_moedas}* Moedas no total ({horario})\n
{moedas}
        '''
        bot.send_message(mensagem.chat.id, texto, parse_mode='Markdown')
        texto_final = """
            Seleciona alguma opção:
             /google Voltar ao menu de consultas (google)
             /inicio Retorna ao menu do bot.
            """
        bot.send_message(mensagem.chat.id, texto_final)


@bot.message_handler(commands=['awesomeapi'])
def awesomeapi(mensagem):
    texto_inicio = """
        Para saber todas as moedas suportadas:
        /moedas-awesomeapi
        """
    texto = ''
    for moeda in moedas_dic:
        requisicao_dic = requests.get('https://economia.awesomeapi.com.br/last/{moeda}').json()[moeda.replace('-', '')]
        moeda_name = requisicao_dic["name"][:requisicao_dic["name"].find("/")]
        moeda_code = requisicao_dic["code"]
        preco_compra = round(float(requisicao_dic["bid"]), 2)
        texto += f'*1 {moeda_code} ({moeda_name}) = {str(preco_compra).replace(".", ",")} {requisicao_dic["codein"]}*\n{requisicao_dic["create_date"]}\n\n'
    bot.send_message(mensagem.chat.id, texto, parse_mode='Markdown')
    texto_final = """
    Para voltar ao menu inicial:
     /inicio Retorna ao menu do bot
    """
    bot.send_message(mensagem.chat.id, texto_final)


@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem):
    texto_padrao = """
    Escolha uma opção para continuar:
     /acoes Compara o preço de diferentes ações
     /moedasinst Compara o preço de diferentes moedas
    """
    bot.send_message(mensagem.chat.id, texto_padrao)


bot.polling()  # Mantém o bot "funcionando/ligado"
