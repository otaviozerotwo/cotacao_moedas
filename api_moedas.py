import requests

def main():
    print('#########################')
    print('###  TESTE API2 IFTM  ###')
    print('###  Consultar Moedas ###')
    print('#########################')
    print()

    opcaomoeda = int(input('Quer saber contação de qual moeda? \n1. Dolar\n2. Euro\n3. Bitcoin\n4. Todos\n'))

    if(opcaomoeda == 1):
        moeda = 'USD-BRL'
        nome = 'Dolar'
        sigla = 'USDBRL'
    elif(opcaomoeda == 2):
        moeda = 'EUR-BRL'
        nome = 'Euro'
        sigla = 'EURBRL'
    elif(opcaomoeda == 3):
        moeda = 'BTC-BRL'
        nome = 'Bitcoin'
        sigla = 'BTCBRL'
    elif(opcaomoeda == 4):
        moeda = 'USD-BRL,EUR-BRL,BTC-BRL,EUR-BRL'
        nome1 = 'Dolar'
        nome2 = 'Euro'
        nome3 = 'Bitcoin'
        sigla1 = 'USDBRL'
        sigla2 = 'EURBRL'
        sigla3 = 'BTCBRL'
    else:
        print('Opção incorreta!')
        exit()

    requisicao = requests.get('http://economia.awesomeapi.com.br/json/last/{}'.format(moeda))
    dados_json = requisicao.json()

    if(requisicao.status_code == 200):
        print('### COTAÇÃO DE HOJE ###')

        if(opcaomoeda != 4):
            print(nome, dados_json[sigla]['high'])
        else:
            print(nome1, dados_json[sigla1]['high'])
            print(nome2, dados_json[sigla2]['high'])
            print(nome3, dados_json[sigla3]['high'])
    else:
        print('{}: Erro no retorno da API.\n')

    print('-----------------------------------------')
    opcao = int(input('Deseja realizar uma nova consulta? \n1. Sim\n2. Sair\n'))

    if(opcao == 1):
        main()
    else:
        print('Indo embora .......')

if __name__ == '__main__':
    main()