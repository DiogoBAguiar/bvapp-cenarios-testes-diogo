'''
UCS001 - Manter inversores

Objetivo: Permitir que o usuário cadastre, consulte, altere e exclua inversores.

Requisitos:
- #24233 - Inclusão de inversores
- #24249 - Consulta de inversores
- #24253 - Atualização de inversores
- #24254 - Exclusão de inversores

Ator:
- Usuário autenticado com autorização de inclusão, consulta e edição
- Administrador ou Gerente (exclusão)
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de cadastro de inversores. Ele observa que
# existem os campos:
# - Número de série
# - Marca
# - Modelo (pertencente à marca selecionada)
# - Fornecedor
# - Usina
# - Operadora
# - Potência nominal
# - Data de instalação
# - Situação
# - Garantia de instalação
# - Opções
# -- Botão "Salvar"

# O ator preenche os campos com os dados do inversor: série
# 'INV-ESTUDO-001', marca 'Marca Estudo A', modelo 'Modelo Estudo A',
# fornecedor 'Fornecedor Estudo A', usina 'Usina Estudo A', operadora
# 'Operadora Estudo A', potência de 5 kW, instalação em 01/10/2026 e
# situação 'Ativo'. Todos os vínculos já estão cadastrados e ativos.

# Ao concluir o cadastro, ele seleciona a opção "Salvar". [A4]

# O sistema verifica que os dados estão corretos [RN1] e exibe a mensagem
# "Inversor cadastrado com sucesso e vinculado à Operadora e Localização
# selecionadas".

# O ator executa [A1].

# O ator verifica que o inversor cadastrado está na lista e que série,
# marca, modelo, potência, instalação e situação são iguais aos dados
# informados. [A2][A3]


# 🟠 [A1] - BUSCAR INVERSOR
# ---------------------------------------------------------------

# O ator acessa a página de consulta de inversores.

# O sistema exibe a lista de inversores cadastrados.

# O ator digita a série 'INV-ESTUDO-001' no campo de busca e seleciona
# 'Pesquisar'.

# O sistema exibe os inversores que correspondem ao termo digitado.


# 🟠 [A2] - EDITAR INVERSOR
# ---------------------------------------------------------------

# O ator executa [A1].

# O ator seleciona o inversor na lista e clica no botão para editar.

# O sistema exibe a página de edição com os campos preenchidos com os
# dados do inversor. O ator verifica que o número de série não pode
# ser alterado. [RN2]

# O ator altera a potência de 5 kW para 6 kW e seleciona "Salvar".

# O sistema salva os dados e exibe a mensagem "Dados do inversor
# atualizados com sucesso".

# O ator executa [A1] e verifica que o mesmo inversor exibe 6 kW e que
# os demais dados continuam iguais.


# 🟠 [A3] - EXCLUIR INVERSOR
# ---------------------------------------------------------------

# O ator executa [A1]. O inversor não tem painéis vinculados nem
# histórico de geração ou manutenção.

# O ator seleciona o inversor e a opção 'Excluir'. [A5][A6]

# O sistema pede a confirmação da exclusão, exibindo série e marca.

# O ator confirma a exclusão.

# O sistema remove o inversor definitivamente [RN3] e exibe a mensagem
# "Inversor removido/inativado com sucesso".

# O ator executa [A1] e verifica que o inversor não está na lista.
# A remoção definitiva é conferida pelo meio acordado com os
# stakeholders; a ausência na lista, sozinha, não a comprova.


# 🟠 [A4] - SÉRIE REPETIDA
# ---------------------------------------------------------------

# O ator tenta cadastrar um segundo inversor com a série
# 'INV-ESTUDO-001' e seleciona "Salvar".

# O sistema impede o cadastro, informa que a série já existe [RN1] e
# não cria outro inversor.


# 🟠 [A5] - EXCLUIR INVERSOR COM PAINEL VINCULADO
# ---------------------------------------------------------------

# O ator executa [A1] para um inversor que tem painel vinculado e
# seleciona 'Excluir'.

# O sistema recusa a exclusão, informa o impedimento [RN3] e o inversor
# continua cadastrado.


# 🟠 [A6] - EXCLUIR INVERSOR COM HISTÓRICO
# ---------------------------------------------------------------

# O ator executa [A1] para um inversor sem painel vinculado, mas com
# histórico de geração ou manutenção, seleciona 'Excluir' e confirma.

# O sistema inativa o inversor em vez de removê-lo e preserva o
# histórico. [RN3]


# 🟣 [RN1] VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------

# Os dados obrigatórios precisam ser informados e o número de série
# deve ser único entre os inversores (CA #24416). A unidade e a
# obrigatoriedade da garantia de instalação estão pendentes.

# 🟣 [RN2] SÉRIE NÃO EDITÁVEL
# ---------------------------------------------------------------

# Na edição, o número de série é somente leitura (CA-2.1.1.3.02).

# 🟣 [RN3] REGRAS DE EXCLUSÃO
# ---------------------------------------------------------------

# Somente Administrador ou Gerente pode excluir (CA #24473). Sem painéis
# e sem histórico, o inversor é removido definitivamente (CA-2.1.1.4.01).
# Com painel vinculado, a exclusão é recusada (CA-2.1.1.4.02, a validar).
# Com histórico, o inversor é inativado e o histórico é preservado
# (CA-2.1.1.4.03).


# Pendências de validação: docs/pendencias.md (UCS001).
# Especificação completa: docs/fluxos/UCS001_manter_inversores.md.
