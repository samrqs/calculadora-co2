def emissao_anual(consumo_mwh):
    return consumo_mwh * 0.581

def emissao_mensal(emissao):
    return emissao / 12

def credito_reais(credito):
    return credito * 365

def valor_reais(qtd_arvores):
    return qtd_arvores * 34.90   
        
inicio = "1"

while inicio == "1":
    
    print("Cálculo de emissão e compensação de Co2 por consumo de energia elétrica para empresas:")

    escolha1 = input("Primeiro é necessário calcular a emissão de Co2. Você deseja calcular a emissão de Co2 por: 1)KWh 2)Valor da conta de energia ")
        
    if escolha1 == "1":
        
        consumo = float(input("Digite o valor do consumo de energia elétrica em KWh: "))
        
        consumo_mwh = consumo * 0.001 #Transformando KWh por MWh
        emissao = emissao_anual(consumo_mwh) #Calculo de emissão por ano pela função
      
        print('Emissão de Co2 por ano:', "%.2f" %(emissao),'tCo2.')
        print('Emissão de Co2 por mês:', "%.2f" %(emissao_mensal(emissao)),'tCo2.')
        
        escolha2 = input('Como deseja compensar as toneladas de carbono emitidas? 1)Gerando créditos de carbono 2) Plantio de mudas ')
        
        if escolha2 == "1": 
            
            credito = emissao
            credito_rs = credito_reais(credito)
            
            print('A quantidade de créditos para compensar',  "%.2f" %(emissao),'tCo2 é de:', "%.2f" %(credito), 'créditos que equivale a R$', "%.2f" %(credito_rs))
            print('Os créditos gerados podem ser investidos em projetos de Redução das Emissões por Desmatamento e Degradação (REDD) ou de Mecanismo de Desenvolvimento Limpo (MDL).')

            inicio = input("Digite 1 para voltar ao inicio ou qualquer tecla para sair do programa ")
            
        elif escolha2 == "2":
            
            qtd_arvores = emissao * 7  #Uma tonela de Co2 emitida equivale a 7 árvores
            
            print('A quantidade de árvores para compensar',  "%.2f" %(emissao),'tCo2 é de:', "%.2f" %(qtd_arvores), 'árvores.')
            print('O Projeto Plantar ajuda na platanção de árvores para compensar Co2. O valor total para o plantio é de: R$', "%.2f"%(valor_reais(qtd_arvores)),'.')
            
            inicio = input("Digite 1 para voltar ao inicio ou qualquer tecla para sair do programa ")
            
        else:
            inicio = input("Essa resposta não existe. Digite 1 para voltar ao inicio ou qualquer tecla para sair do programa.")

        
    elif escolha1 == "2":
        
        consumo_rs = float(input("Digite o valor do consumo de energia elétrica em R$: "))
        
        consumo_mwh = consumo_rs / 654.49 #Transformando R$ em MWh 
        emissao = emissao_anual(consumo_mwh) #Calculo de emissão por ano pela função
      
        print('Emissão de Co2 por ano:', "%.2f" %(emissao),'tCo2.')
        print('Emissão de Co2 por mês:', "%.2f" %(emissao_mensal(emissao)),'tCo2.')
        
        escolha2 = input('Como deseja compensar as toneladas de carbono emitidas? 1)Gerando créditos de carbono 2) Plantio de mudas ')
        
        if escolha2 == "1": 
            
            credito = emissao
            credito_rs = credito_reais(credito)
            
            print('A quantidade de créditos para compensar',  "%.2f" %(emissao),'tCo2 é de:', "%.2f" %(credito), 'créditos que equivale a R$', "%.2f" %(credito_rs))
            print('Os créditos gerados podem ser investidos em projetos de Redução das Emissões por Desmatamento e Degradação (REDD) ou de Mecanismo de Desenvolvimento Limpo (MDL).')

            inicio = input("Digite 1 para voltar ao inicio ou qualquer tecla para sair do programa ")
            
        elif escolha2 == "2":
            
            qtd_arvores = emissao * 7  #Uma tonela de Co2 emitida equivale a 7 árvores
            
            print('A quantidade de árvores para compensar',  "%.2f" %(emissao),'tCo2 é de:', "%.2f" %(qtd_arvores), 'árvores.')
            print('O Projeto Plantar ajuda na platanção de árvores para compensar Co2. O valor total para o plantio é de: R$', "%.2f"%(valor_reais(qtd_arvores)),'.')
            
            inicio = input("Digite 1 para voltar ao inicio ou qualquer tecla para sair do programa ")
            
        else:
            inicio = input("Essa resposta não existe. Digite 1 para voltar ao inicio ou qualquer tecla para sair do programa.")
   
    else: 

        inicio = input("Essa resposta não existe. Digite 1 para voltar ao inicio ou qualquer tecla para sair do programa.")

print("Programa finalizado.")