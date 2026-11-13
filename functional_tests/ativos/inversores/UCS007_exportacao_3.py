'''
UCS007 - Tratar autorização e falha de exportação de inversores

Objetivo: Garantir que a exportação de inversores seja recusada para
quem não tem a autorização correspondente, mostre o andamento e informe
falhas sem entregar conteúdo de erro como relatório.

Requisitos:
- #35875 - Exportação de inversores
- #24249 - Consulta de inversores (CA #24439)
- US #24457

Ator:
- Perfil A: pode consultar a listagem e visualizar o registro
- Perfil B: não pode consultar a listagem
- Perfil C: pode consultar a listagem, mas não visualizar o registro
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Existe o inversor fictício 'ESTUDO-INVERSORES-01'. Os perfis A, B e C
# são sintéticos para este teste, não papéis novos do produto.

# Com o Perfil A, o ator acessa a consulta de inversores, aplica um filtro
# e seleciona a exportação coletiva. [A1][A3]

# Enquanto o arquivo é preparado, o sistema indica que a exportação está
# em andamento e impede um novo acionamento da mesma ação. [RN3]

# O sistema entrega o arquivo. O ator anota o endereço e a solicitação
# usados.

# O ator seleciona 'ESTUDO-INVERSORES-01' e a exportação da ficha
# individual. [A2][A4]

# O sistema entrega a ficha. O ator anota o endereço e a solicitação
# usados. [A5]


# 🟠 [A1] - EXPORTAÇÃO COLETIVA SEM AUTORIZAÇÃO DE CONSULTA
# ---------------------------------------------------------------

# Com o Perfil B, o ator abre diretamente o endereço anotado para a
# exportação coletiva, sem usar os controles da tela.

# O sistema recusa a exportação e não entrega nenhum relatório. [RN1][RN2]


# 🟠 [A2] - FICHA SEM AUTORIZAÇÃO DE VISUALIZAÇÃO
# ---------------------------------------------------------------

# Com o Perfil C, o ator abre diretamente o endereço anotado para a ficha
# de 'ESTUDO-INVERSORES-01'.

# O sistema recusa a exportação e não entrega nenhuma ficha. [RN1][RN2]


# 🟠 [A3] - FALHA NA EXPORTAÇÃO COLETIVA
# ---------------------------------------------------------------

# Com uma falha de obtenção preparada, o ator, com o Perfil A, solicita
# a exportação coletiva.

# O sistema informa a falha e não entrega o conteúdo do erro como
# relatório. [RN4]


# 🟠 [A4] - FALHA NA FICHA INDIVIDUAL
# ---------------------------------------------------------------

# Com a mesma falha preparada e o inversor existente, o ator solicita a
# ficha individual.

# O sistema informa a falha e não apresenta o erro como ficha. [RN4]


# 🟠 [A5] - OPÇÕES NA INTERFACE
# ---------------------------------------------------------------

# Com os Perfis B e C, o ator abre a consulta e registra se as opções de
# exportação aparecem. Esconder a opção não substitui a recusa
# verificada em [A1] e [A2].


# 🟣 [RN1] AUTORIZAÇÃO POR MODALIDADE
# ---------------------------------------------------------------

# A exportação coletiva exige autorização para consultar a listagem; a
# ficha individual exige autorização para visualizar o registro
# (CA #24439). Consultar a listagem não autoriza a ficha.

# 🟣 [RN2] RECUSA SEM ARQUIVO
# ---------------------------------------------------------------

# Uma solicitação sem a autorização correspondente é recusada e nenhum
# arquivo é entregue. Qualquer arquivo entregue em [A1] ou [A2] é defeito
# de controle de acesso.

# 🟣 [RN3] EXPORTAÇÃO EM ANDAMENTO
# ---------------------------------------------------------------

# Durante a preparação, o sistema indica o andamento e não aceita um
# novo acionamento (CA05 da Feature #35875, a validar).

# 🟣 [RN4] FALHA NA OBTENÇÃO
# ---------------------------------------------------------------

# Em caso de falha, o sistema informa o problema e não entrega o erro
# como relatório (CA06 da Feature #35875, a validar). Nova tentativa e
# retomada ainda não estão definidas.


# Pendências de validação: docs/pendencias.md (UCS007).
# Especificação completa: docs/fluxos/UCS007_exportacao_3.md.
