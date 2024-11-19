nome = input('Qual o nome do personagem? ')
idade = int(input('Qual a idade do personagem? '))

def escolher_da_lista(classes):
    while True:
        print(f"Escolha uma das opções de tipo de personagem: {', '.join(classes)}")
        escolha = input("Digite sua escolha: ")
        if escolha in classes:
            print(f"Você escolheu: {escolha}")
            return escolha
        else:
            print("Entrada inválida. Tente novamente.")

classes = ['guerreiro', 'mago', 'monge', 'ninja']
escolha_usuario = escolher_da_lista(classes)

if escolha_usuario == 'guerreiro':
    print(f"O guerreiro atacou usando a espada")
elif escolha_usuario == 'mago':
    print(f"O mago atacou usando a magia")
elif escolha_usuario == 'monge':
    print(f"O monge atacou usando a artes marciais")
else:
    print(f"O ninja atacou usando a shuriken")
