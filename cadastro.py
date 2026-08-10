#variáveis
admin = 'MasterAdmin'
senha_admin = '21071994'
dados_usuario = []
login = ''
senha = ''
usuario = login, senha
trocar_senha = ''
trocar_login = ''
opcao = ''

#loop principal
while True:

    print('-----------------------')
    print('- Cadastro de Usuário -')
    print('-----------------------')
    print('Digite uma das opções abaixo:')
    print('1. Cadastrar novo usuário')
    print('2. fazer login')
    print('3.Entrar como admin')
    print('4. Sair')
    opcao = input('Opção: ')

# Cadastro de usuário
    if opcao == '1':
        login = input('Digite o login do usuário: ')
        senha = input('Digite a senha do usuário: ')
        usuario = login, senha
        dados_usuario.append(usuario)
        print('Usuário cadastrado com sucesso!')

# Login de usuário
    if opcao == '2':
        login_input = input('Digite o login do usuário: ')
        senha_input = input('Digite a senha do usuário: ')
        if any(usuario["login"] == login for usuario in dados_usuario):
            print("Esse login já existe!")

        if (login_input, senha_input) in dados_usuario:
            print('Login realizado com sucesso!')

            if login_input == login and senha_input == senha:
                print('Deseja alterar o login ou a senha?')
                alterar = input('Digite "login" para alterar o login ou "senha" para alterar a senha: ')

                if alterar.lower() == 'login':
                    trocar_login = input('Digite o novo login: ')
                    dados_usuario.remove((login, senha))
                    login = trocar_login
                    usuario = login, senha
                    dados_usuario.append(usuario)
                    print('Login alterado com sucesso!')


                elif alterar.lower() == 'senha':
                    trocar_senha = input('Digite a nova senha: ')
                    dados_usuario.remove((login, senha))
                    senha = trocar_senha
                    usuario = login, senha
                    dados_usuario.append(usuario)
                    print('Senha alterada com sucesso!')
                else:
                    print('Opção inválida. Nenhuma alteração foi feita.')

        else:
            print('Login ou senha incorretos.')   

# Acesso ao modo admin
    if opcao == '3':

#loop para login do admin
        while True:

            login_admin = input('Digite o login do admin: ')
            senha_admin_input = input('Digite a senha do admin: ')


            if login_admin == admin and senha_admin_input == senha_admin:
                print('Acesso ao modo admin concedido.')
                print('Digite uma das opções abaixo:')
                
                print('escolha uma das opções abaixo:')
                print('1.Usuários cadastrados:')
                print('2.Alterar login ou senha de um usuário:')
                print('3.Excluir um usuário:')
                print('4.Sair do modo admin:')
                opcao_admin = input('Opção: ')

                if opcao_admin == '1':
                    if dados_usuario:
                        print('Usuários cadastrados:')
                        for usuario in dados_usuario:
                            print(f'Login: {usuario[0]}, Senha: {usuario[1]}')
                    else:
                        print('Nenhum usuário cadastrado.')
                        continue
                elif opcao_admin == '2':
                    login_alterar = input('Digite o login do usuário que deseja alterar: ')
                    for usuario in dados_usuario:
                        if usuario[0] == login_alterar:
                            print('Deseja alterar o login ou a senha?')
                            alterar_admin = input('Digite "login" para alterar o login ou "senha" para alterar a senha: ')

                            if alterar_admin.lower() == 'login':
                                novo_login = input('Digite o novo login: ')
                                dados_usuario.remove(usuario)
                                usuario = novo_login, usuario[1]
                                dados_usuario.append(usuario)
                                print('Login alterado com sucesso!')

                            elif alterar_admin.lower() == 'senha':
                                nova_senha = input('Digite a nova senha: ')
                                dados_usuario.remove(usuario)
                                usuario = usuario[0], nova_senha
                                dados_usuario.append(usuario)
                                print('Senha alterada com sucesso!')
                            else:
                                print('Opção inválida. Nenhuma alteração foi feita.')
                            break
                    else:
                        print('Usuário não encontrado.')
                        continue
                elif opcao_admin == '3':
                    login_excluir = input('Digite o login do usuário que deseja excluir: ')
                    for usuario in dados_usuario:
                        if usuario[0] == login_excluir:
                            dados_usuario.remove(usuario)
                            print('Usuário excluído com sucesso!')
                            break
                    else:
                        print('Usuário não encontrado.')
                        continue
                elif opcao_admin == '4':
                    print('Saindo do modo admin.')
                    break

            else:
                print('Login ou senha do admin incorretos.')
                continue

    if opcao == '4':
        print('Saindo do programa...')
        print('Programa encerrado.')
        break
