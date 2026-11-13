'''
UCS004 - Manter fabricante com validação de contato e cancelamento

Objetivo: Garantir que o ciclo de cadastro, consulta, alteração e
exclusão de um fabricante não grave e-mail inválido nem alterações
canceladas, e preserve a identificação usada pelos equipamentos após a
inativação.

Requisitos:
- #24272 - Inclusão de marcas
- #24273 - Consulta de marcas
- #24275 - Atualização de marcas
- #24278 - Exclusão de marcas

Ator:
- Administrador
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O administrador acessa a página de cadastro de marcas e preenche nome
# 'Marca Estudo Cancelamento', identificação internacional, situação
# 'Ativo' e e-mail de suporte 'suporte@example.invalid'.

# Ele seleciona a opção "Salvar". [A2]

# O sistema verifica os dados [RN1] e confirma a inclusão do fabricante.

# O administrador executa [A1], abre o detalhe e confere identificação e
# contato.

# O administrador seleciona o fabricante e clica no botão para editar.

# O sistema exibe a página de edição com os campos preenchidos.

# O administrador troca o e-mail para 'sem-arroba' e seleciona "Salvar".

# O sistema recusa a atualização e não grava o contato inválido. [RN2]

# O administrador corrige o e-mail para 'novo@example.invalid' e
# seleciona 'Cancelar'.

# O sistema não grava a alteração. [RN3]

# O administrador abre a edição de novo, informa 'novo@example.invalid'
# e seleciona "Salvar".

# O sistema salva o novo contato no mesmo fabricante, exibe mensagem de
# sucesso e registra a alteração na auditoria. [RN5]

# O fabricante tem um modelo ou equipamento vinculado. O administrador
# executa [A1], seleciona o fabricante e a opção 'Excluir'.

# O sistema pede a confirmação. O administrador cancela e o fabricante
# continua disponível. [RN3]

# O administrador seleciona 'Excluir' de novo, confere o nome e
# confirma.

# O sistema inativa o fabricante e preserva as referências. [RN4]

# O administrador executa [A1] e verifica que o fabricante aparece como
# 'Inativo' e continua identificado nos cadastros vinculados.


# 🟠 [A1] - BUSCAR FABRICANTE
# ---------------------------------------------------------------

# O administrador acessa a página de consulta de marcas.

# O sistema exibe a lista de marcas cadastradas.

# O administrador digita 'Marca Estudo Cancelamento' no campo de busca e
# seleciona 'Pesquisar'.

# O sistema exibe as marcas que correspondem ao termo digitado.


# 🟠 [A2] - NOME JÁ USADO
# ---------------------------------------------------------------

# O administrador tenta cadastrar outra marca com um nome já cadastrado
# e seleciona "Salvar".

# O sistema impede o cadastro duplicado (CA #24556).


# 🟣 [RN1] VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------

# Nome, identificação internacional e situação são obrigatórios; site e
# telefone são opcionais. A situação aceita Ativo ou Inativo (CA
# #24553).

# 🟣 [RN2] E-MAIL DE SUPORTE
# ---------------------------------------------------------------

# O e-mail de suporte precisa ter formato válido (CA-2.1.4.1.3.05).

# 🟣 [RN3] CANCELAMENTO
# ---------------------------------------------------------------

# Cancelar a edição não grava a alteração digitada (CA-2.1.4.1.3.04).
# Cancelar a confirmação de exclusão mantém o fabricante disponível.

# 🟣 [RN4] EXCLUSÃO COM VÍNCULO
# ---------------------------------------------------------------

# Somente administradores podem excluir marcas (CA #24595). Com
# vínculos, o fabricante é inativado e as referências são preservadas; a
# exclusão não é definitiva (US #24600).

# 🟣 [RN5] AUDITORIA
# ---------------------------------------------------------------

# A alteração confirmada é registrada na auditoria (CA-2.1.4.1.3.11).


# Pendências de validação: docs/pendencias.md (UCS004).
# Especificação completa: docs/fluxos/UCS004_crud_variacao.md.
