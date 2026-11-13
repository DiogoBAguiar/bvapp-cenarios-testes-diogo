'''
UCS003 - Manter inversor com validação de unicidade e histórico

Objetivo: Garantir que o ciclo de cadastro, consulta, alteração e
exclusão de um inversor proteja a série única e preserve o histórico,
inativando o inversor em vez de removê-lo.

Requisitos:
- #24233 - Inclusão de inversores
- #24249 - Consulta de inversores
- #24253 - Atualização de inversores
- #24254 - Exclusão de inversores

Ator:
- Administrador
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O administrador acessa a página de cadastro de inversores e preenche
# os dados obrigatórios do inversor 'INV-ESTUDO-HIST-001': marca 'Marca
# Estudo A', modelo 'Modelo Estudo A', fornecedor, usina e operadora de
# estudo, potência de 5 kW, instalação em 01/10/2026 e situação 'Ativo'.

# Ele seleciona a opção "Salvar".

# O sistema verifica os dados [RN1] e cria o inversor.

# O administrador volta à página de cadastro, informa de novo a série
# 'INV-ESTUDO-HIST-001' e seleciona "Salvar".

# O sistema recusa o cadastro e informa que a série já existe. [RN1]

# O administrador executa [A1] e verifica que existe apenas um inversor
# com essa série, com marca, modelo e potência informados.

# O administrador seleciona o inversor e clica no botão para editar.

# O sistema exibe a página de edição. O administrador verifica que a
# série não pode ser alterada [RN2], muda a potência para 6 kW e
# seleciona "Salvar".

# O sistema salva os dados. O administrador executa [A1] e verifica que
# a mesma série exibe 6 kW.

# O administrador prepara um histórico de geração ou manutenção para o
# mesmo inversor, pelo meio acordado para a massa de estudo, e confere
# que esse histórico aparece na consulta. O inversor continua sem
# painéis vinculados. [A3]

# O administrador executa [A1], seleciona o inversor e a opção
# 'Excluir'. [A2]

# O sistema pede a confirmação. O administrador confere os dados e
# confirma.

# O sistema inativa o inversor e preserva o cadastro e o histórico.
# [RN3]

# O administrador localiza o inversor inativo e verifica que a
# identificação e o histórico continuam disponíveis.


# 🟠 [A1] - BUSCAR INVERSOR
# ---------------------------------------------------------------

# O administrador acessa a página de consulta de inversores.

# O sistema exibe a lista de inversores cadastrados.

# O administrador digita a série 'INV-ESTUDO-HIST-001' no campo de busca
# e seleciona 'Pesquisar'.

# O sistema exibe os inversores que correspondem ao termo digitado.


# 🟠 [A2] - EXCLUIR INVERSOR COM PAINEL VINCULADO
# ---------------------------------------------------------------

# O inversor tem painel vinculado. O administrador seleciona 'Excluir'.

# O sistema recusa a exclusão, informa o impedimento e o inversor
# continua cadastrado. [RN4]


# 🟠 [A3] - HISTÓRICO NÃO PREPARADO
# ---------------------------------------------------------------

# Se não houver meio definido para preparar ou consultar o histórico, o
# administrador marca a exclusão como BLOQUEADA e não segue o fluxo.


# 🟣 [RN1] SÉRIE ÚNICA
# ---------------------------------------------------------------

# O número de série deve ser único entre os inversores (CA #24416,
# CA-2.1.1.1.04). Uma segunda inclusão com a mesma série é recusada.

# 🟣 [RN2] SÉRIE NÃO EDITÁVEL
# ---------------------------------------------------------------

# Na edição, o número de série é somente leitura (CA-2.1.1.3.02).

# 🟣 [RN3] EXCLUSÃO COM HISTÓRICO
# ---------------------------------------------------------------

# Inversor com histórico de geração ou manutenção é inativado, e não
# removido; o histórico é preservado (CA #24475, CA-2.1.1.4.03).

# 🟣 [RN4] EXCLUSÃO COM PAINEL VINCULADO
# ---------------------------------------------------------------

# Inversor com painel vinculado não pode ser excluído (CA-2.1.1.4.02, a
# validar, inclusive a precedência quando também há histórico).


# Pendências de validação: docs/pendencias.md (UCS003).
# Especificação completa: docs/fluxos/UCS003_crud_variacao.md.
