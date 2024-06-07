def adicionar_evento(agenda, nome, data, local):
    evento = {"nome": nome, "data": data, "local": local}
    agenda.append(evento)
    print("Evento adicionado com sucesso!")

def listar_eventos(agenda):
    print("\nLISTA DE EVENTOS\n")
    for i, evento in enumerate(agenda, start=1):
        print(f"{i}. {evento['nome']} - {evento['data']} - {evento['local']}")

def remover_evento(agenda, posicao):
    if 1 <= posicao <= len(agenda):
        del agenda[posicao - 1]
        print("Evento removido com sucesso!")
    else:
        print("Posição inválido.")

def menu():
    print("\nAGENDA\n")
    print("1. Adicionar Evento")
    print("2. Listar Eventos")
    print("3. Remover Evento")
    print("4. Sair")

def main():
    agenda = []

    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do evento: ")
            data = input("Data do evento (dd/mm/aaaa): ")
            local = input("Local do evento: ")
            adicionar_evento(agenda, nome, data, local)
        elif opcao == '2':
            listar_eventos(agenda)
        elif opcao == '3':
            posicao = int(input("Digite a posição do evento a ser removido: "))
            remover_evento(agenda, posicao)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
