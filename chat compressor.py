import re

# Função para processar as respostas e armazenar nas variáveis
def process_input(user_input, context):
    user_input = user_input.lower()

    if context['step'] == 0:  # Identificar o tipo de compressor
        if 'pistão' in user_input or 'pistao' in user_input:
            context['compressor_type'] = 'pistão'
            context['step'] = 1
            return "Você escolheu compressor a pistão. Qual foi a última vez que você trocou o óleo do compressor? (em dias)"

        elif 'parafuso' in user_input:
            context['compressor_type'] = 'parafuso'
            return "Por enquanto, este chatbot só tem suporte para compressores a pistão. Vamos trabalhar em atualizações futuras para incluir esse tipo."

    elif context['step'] == 1:  # resposta oleo + Pergunta sobre troca filtro de ar
        try:
            days = int(user_input)
            context['oil_change_days'] = days
            context['step'] = 2
            return "Faz quantos dias que o filtro de ar foi trocado? (em dias)"
        except ValueError:
            return "Por favor, informe a quantidade de dias em um formato numérico."

    elif context['step'] == 2:  # resposta filtro de ar + Pergunta esgotamento de agua compressor
        try:
            days = int(user_input)
            context['air_change_days'] = days
            context['step'] = 3
            return "faz quantos dias que esgotou a agua do compressor?"
        except ValueError:
            return "Por favor, informe a quantidade de dias em um formato numérico."

    elif context['step'] == 3:  # resposta esgotamento de agua compresso + Pergunta tmp op diária
        try:
            days = int(user_input)
            context['scape_water_days'] = days
            context['step'] = 4
            return "Qual é o tempo de operação diário do compressor?"
        except ValueError:
            return "Por favor, informe a quantidade de horas em um formato numérico."      

    elif context['step'] == 4:  # resposta tmp op diária + Pergunta vazamento oleo
        try:
            days = int(user_input)
            context['daily_op'] = days
            context['step'] = 5
            return "Há algum vazamento de óleo no compressor?"
        except ValueError:
            return "Por favor, responda com 'sim' ou 'nao'."  

    elif context['step'] == 5:  #  resposta vazamento oleo + Pergunta ruido
        try:
            days = str(user_input)
            context['oil_spill'] = str
            context['step'] = 6
            return "Você percebeu algum aumento no nível de ruído do compressor?"
        except ValueError:
            return "Por favor, responda com 'sim' ou 'nao'" 

    elif context['step'] == 6:  #  resposta ruido
        try:
            days = str(user_input)
            context['weird_noises'] = str
            return generate_diagnosis(context)
        except ValueError:
            return "Por favor, responda com 'sim' ou 'nao'" 

# Função para gerar o diagnóstico baseado nas respostas
def generate_diagnosis(context):
    diagnosis = "Relatório do Compressor a Pistão:\n"

    # Análise da troca de óleo
    if context['oil_change_days'] >= 30:
        diagnosis += "- O compressor precisa de troca de óleo imediatamente.\n"
    else:
        diagnosis += "- O óleo do compressor está dentro do período recomendado.\n"

    # Análise do filtro de ar
    if context['air_change_days'] >= 90:
        diagnosis += "- O filtro de ar pode precisar ser trocado.\n"
    else:
        diagnosis += "- O filtro de ar está em dia.\n"

    # Análise esgotamento água
    if context['scape_water_days'] >= 7:
        diagnosis += "- Voce precisa esgotar a agua do seu compressor.\n"
    else:
        diagnosis += "- agua do compressor está ok!!.\n"

    # Análise tempo de operação diário do compressor
    if context['daily_op'] >= 8:
        diagnosis += "- Voce precisa fazre uma manutenção preventiva.\n"
    else:
        diagnosis += "- Tempo de operação do compressor está ok!!.\n"

    # Análise Vazamento óleo
    if context['oil_spill'] == 'sim':
        diagnosis += "- Voce precisa fazer uma manutenção no compressor não é normal ocorrer vazamento de óleo.\n"
    else:
        diagnosis += "- Ok!!.\n"

    # Análise ruído
    if context['weird_noises'] == 'sim':
        diagnosis += "- Voce precisa fazer uma manutenção no compressor não é normal fazer barulhos incomuns.\n"
    else:
        diagnosis += "- Ok!!.\n"

    diagnosis += "\nPara agendar a sua manutenção, fale com um atendente ou chame no número 46 99*******.\n"
    return diagnosis

# Loop principal do chatbot
def chatbot():
    print("Bem-vindo ao Chatbot de Manutenção de Compressores!")
    print("Seu compressor é a pistão ou parafuso?")

    context = {'step': 0, 'compressor_type': None, 'oil_change_days': None, 'air_change_days': None}

    while True:
        user_input = input("Você: ")
        if user_input.lower() in ['tchau', 'sair', 'adeus']:
            print("Chatbot: Tchau! Espero ter ajudado.")
            break

        response = process_input(user_input, context)
        print("Chatbot:", response)

# Executando o chatbot
chatbot()
