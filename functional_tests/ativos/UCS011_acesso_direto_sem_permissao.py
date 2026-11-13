'''
UCS011 - Recusar edição e exclusão por acesso direto sem permissão

Objetivo: Garantir que um usuário sem a autorização correspondente não
consiga editar nem excluir inversores e marcas, mesmo solicitando a
operação diretamente, sem usar os botões da tela.

Requisitos:
- #24249 - Consulta de inversores (CA #24439)
- #24253 - Atualização de inversores (US #29059)
- #24254 - Exclusão de inversores (CA #24473)
- #24275 - Atualização de marcas (US #24594)
- #24278 - Exclusão de marcas (CA #24595)

Ator:
- Perfil L: pode consultar e visualizar ativos e marcas; não pode editar
  nem excluir; não é Administrador nem Gerente
- Perfil E: pode editar marcas; não é administrador
- Perfil A: Administrador, usado só para preparar e conferir os dados
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Existem o inversor 'INV-ESTUDO-ACESSO-001', com 5 kW, situação 'Ativo',
# sem painéis nem histórico, e a marca 'Marca Estudo Acesso', situação
# 'Ativo'. Os valores iniciais estão anotados.

# Com o Perfil A, o ator abre a edição e a exclusão de cada registro pela
# interface e anota o endereço e a solicitação usados, sem confirmar
# nenhuma alteração.

# Com o Perfil L, o ator abre a consulta e o detalhe dos dois registros.
# O sistema permite o acesso. [RN1] [A1]

# Com o Perfil L, o ator abre diretamente o endereço de edição do
# inversor e solicita gravar a potência de 6 kW, sem usar o botão da
# tela. [A2][A3]

# O sistema recusa a gravação e a potência continua 5 kW. [RN1]

# Com o Perfil L, o ator envia diretamente a solicitação de exclusão do
# inversor.

# O sistema recusa a exclusão, sem apresentá-la como concluída; o
# inversor continua 'Ativo'. [RN2]

# Com o Perfil L, o ator abre diretamente o endereço de edição da marca
# e solicita gravar o nome 'Marca Estudo Acesso Alterada'.

# O sistema recusa a gravação e o nome não muda. [RN1]

# Com o Perfil E, o ator envia diretamente a solicitação de exclusão da
# marca.

# O sistema recusa a exclusão e a marca continua 'Ativo'. [RN2]

# Com o Perfil A, o ator consulta os dois registros e verifica que
# continuam com os valores iniciais. [RN3]


# 🟠 [A1] - OPÇÕES NA INTERFACE
# ---------------------------------------------------------------

# Com o Perfil L, o ator abre a consulta e registra se as opções de
# editar e excluir aparecem. Esconder a opção não substitui a recusa
# verificada no fluxo principal.


# 🟠 [A2] - ALTERAR STATUS DO INVERSOR
# ---------------------------------------------------------------

# Com o Perfil L, o ator solicita diretamente a alteração do status do
# inversor.

# O sistema recusa e o status não muda (CA-2.1.1.3.01, US #29059).


# 🟠 [A3] - SEM AUTENTICAÇÃO
# ---------------------------------------------------------------

# Sem sessão iniciada, o ator abre diretamente o endereço de edição do
# inversor e solicita a gravação.

# O sistema recusa e o cadastro não muda (CA-2.1.1.3.01).


# 🟣 [RN1] CONSULTAR NÃO AUTORIZA EDITAR
# ---------------------------------------------------------------

# Autorização para listar ou visualizar não concede editar
# (CA-2.1.1.2.01, CA-2.1.1.3.01, CA-2.1.4.1.3.01).

# 🟣 [RN2] EXCLUSÃO RESTRITA
# ---------------------------------------------------------------

# Inversores só podem ser excluídos por Administrador ou Gerente
# (CA-2.1.1.4.01); marcas, só por administradores, e autorização de
# edição não substitui essa restrição (CA-2.1.4.1.4.01). A recusa não é
# apresentada como exclusão concluída (CA-2.1.1.4.06).

# 🟣 [RN3] O DADO É A PROVA
# ---------------------------------------------------------------

# A recusa é confirmada pelos dados inalterados, e não pela ausência de
# botão na tela. A forma da recusa (mensagem, código ou redirecionamento)
# não está definida e não é exigida.


# Pendências de validação: docs/pendencias.md (UCS011).
# Especificação completa: docs/fluxos/UCS011_acesso_direto_sem_permissao.md.
