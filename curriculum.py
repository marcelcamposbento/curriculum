def criar_curriculo():
    # Coleta de informações do usuário
    nome = input("Digite seu nome completo: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")
    endereco = input("Digite seu endereço: ")
    
    # Formação Acadêmica
    formacao = []
    while True:
        curso = input("Digite o nome do curso (ou pressione Enter para pular): ")
        if curso == "":
            break
        instituicao = input("Digite a instituição: ")
        ano_conclusao = input("Digite o ano de conclusão: ")
        formacao.append(f"{curso} - {instituicao} ({ano_conclusao})")
    
    # Experiência Profissional
    experiencia = []
    while True:
        cargo = input("Digite o cargo (ou pressione Enter para pular): ")
        if cargo == "":
            break
        empresa = input("Digite o nome da empresa: ")
        periodo = input("Digite o período trabalhado (ex: 2018-2020): ")
        descricao = input("Digite uma breve descrição das suas atividades: ")
        experiencia.append(f"{cargo} na {empresa} ({periodo}) - {descricao}")
    
    # Habilidades
    habilidades = input("Liste suas habilidades separadas por vírgula: ").split(",")
    
    # Montar o currículo
    curriculo = f"""
    Nome: {nome}
    E-mail: {email}
    Telefone: {telefone}
    Endereço: {endereco}
    
    Formação Acadêmica:
    {', '.join(formacao)}
    
    Experiência Profissional:
    {', '.join(experiencia)}
    
    Habilidades:
    {', '.join(habilidades)}
    """
    
    print("\nCurrículo Gerado:")
    print(curriculo)

# Executa a função
criar_curriculo()
