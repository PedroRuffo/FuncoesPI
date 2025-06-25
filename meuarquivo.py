# Apresentação das Funções do PI
# Integrantes:
# • Enzo Meneghin Lustosa - RA: 1051392511052
# • Guilherme Escobar Cassiano - RA: 1051392511001
# • Marina Luiza de Araujo Paiva - RA: 1051392511040
# • Pedro Henrique R. Ruffo de Souza - RA: 1051392511030

# Função 1: Filtro
def filtrar_area():
    cursos_por_area = {
        "front-end": ["HTML", "CSS", "JavaScript", "React"],
        "back-end": ["Python", "Java", "Node.js", "PHP"],
        "mobile": ["Flutter", "React Native", "Kotlin", "Swift"],
        "banco de dados": ["Modelagem de Dados", "MySQL", "SQL", "Oracle Database"],
        "nuvem": ["AWS", "Azure", "Google Cloud", "DevOps com Cloud"]
    }

    while True:
        print("\nEscolha uma área:")
        print("1 - Front-end")
        print("2 - Back-end")
        print("3 - Mobile")
        print("4 - Banco de Dados")
        print("5 - Nuvem")
        area_digitada = input("\nÁrea escolhida: ").strip().lower()

        match area_digitada:
            case "front-end" | "frontend":
                area = "front-end"
                break
            case "back-end" | "backend":
                area = "back-end"
                break
            case "mobile":
                area = "mobile"
                break
            case "banco de dados" | "bd":
                area = "banco de dados"
                break
            case "nuvem" | "cloud":
                area = "nuvem"
                break
            case _:
                print("\nÁrea inválida! Por favor, digite uma das áreas disponíveis.")

    print("\nCursos disponíveis nessa área:")
    for curso in cursos_por_area[area]:
        print(f"- {curso}")

filtrar_area()


# Função 2: Barra de Pesquisa
def pesquisar_curso(cursos, nome_pesquisado):

    encontrados = []

    for nome_curso in cursos.keys():
        if nome_pesquisado.lower() in nome_curso.lower():
            encontrados.append(nome_curso)

    return encontrados


cursos_disponiveis = {
    "HTML": None,
    "CSS": None,
    "React": None,
    "Javascript ": None,
    "Node.js": None,
    "PHP": None,
    "MySQL": None,
    "SQL": None,
    "Azure": None,
    "AWS": None,
}

nome = input("Digite o nome ou parte do nome do curso que deseja pesquisar: ")

resultados = pesquisar_curso(cursos_disponiveis, nome)

if resultados:
    print("\nCursos encontrados:")
    for curso in resultados:
        print(f"- {curso}")
else:
    print("\nNenhum curso encontrado com esse nome.")


# Função 3: Cadastro e Login
usuarios = {}

def cadastrar():
    print("=== Cadastro de Novo Usuário ===")
    usuario = input("Escolha um nome de usuário: ")

    if usuario in usuarios:
        print("Usuário já existe! Tente outro nome.")
        return False

    senha = input("Escolha uma senha: ")
    usuarios[usuario] = senha
    print("Usuário cadastrado com sucesso!")
    return True

def login():
    print("=== Login ===")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False

def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ").lower()

        if opcao == "cadastrar":
            cadastrar()
        elif opcao == "login":
            login()
        elif opcao == "sair":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
