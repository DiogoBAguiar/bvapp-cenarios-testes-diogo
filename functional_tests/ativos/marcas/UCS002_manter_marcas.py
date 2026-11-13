'''
UCS002 - Manter marcas

Objetivo: Permitir que o usuário cadastre, consulte, altere e exclua
marcas (fabricantes).

Requisitos:
- #24272 - Inclusão de marcas
- #24273 - Consulta de marcas
- #24275 - Atualização de marcas
- #24278 - Exclusão de marcas

Ator:
- Usuário com autorização para adicionar, consultar e editar marcas
- Administrador (exclusão)
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a página de cadastro de marcas. Ele observa que existem
# os campos:
# - Nome
# - Tipo de identificação internacional
# - ID internacional
# - Situação (Ativo ou Inativo)
# - E-mail de suporte
# - Site oficial
# - Telefone de suporte
# - Opções
# -- Botão "Salvar"

# O ator preenche nome 'Marca Estudo A', o tipo e o ID internacional
# 'ID-ESTUDO-A', situação 'Ativo' e e-mail 'suporte@example.invalid'.
# Ele deixa site e telefone em branco, porque são opcionais.

# Ao concluir o cadastro, ele seleciona a opção "Salvar". [A4]

# O sistema verifica que os dados estão corretos [RN1][RN2], exibe a
# mensagem "Marca cadastrada com sucesso" e registra a inclusão na
# auditoria. [RN5]

# O ator executa [A1].

# O ator abre o detalhe da marca e confere nome e e-mail. Os contatos
# não informados aparecem como "Não informado" (a validar). [A2][A3]


# 🟠 [A1] - BUSCAR MARCA
# ---------------------------------------------------------------

# O ator acessa a página de consulta de marcas.

# O sistema exibe a lista de marcas cadastradas.

# O ator digita 'Marca Estudo A' no campo de busca e seleciona
# 'Pesquisar'.

# O sistema exibe as marcas que correspondem ao termo digitado.


# 🟠 [A2] - EDITAR MARCA
# ---------------------------------------------------------------

# O ator executa [A1].

# O ator seleciona a marca na lista e clica no botão para editar.

# O sistema exibe a página de edição com os campos preenchidos com os
# dados da marca.

# O ator altera o nome para 'Marca Estudo A Revisada', mantém o e-mail
# e seleciona "Salvar". [A5][A6]

# O sistema salva os dados, exibe a mensagem "Marca atualizada com
# sucesso" e registra os valores anterior e posterior na auditoria. [RN5]

# O ator executa [A1] e verifica que a mesma marca aparece com o novo
# nome e que os demais dados continuam iguais.


# 🟠 [A3] - EXCLUIR MARCA COM VÍNCULO
# ---------------------------------------------------------------

# A marca tem um modelo ou equipamento vinculado. O ator, como
# administrador, executa [A1], seleciona a marca e a opção 'Excluir'.

# O sistema pede a confirmação, exibindo o nome da marca.

# O ator cancela. O sistema mantém a marca sem alteração.

# O ator seleciona 'Excluir' de novo e confirma.

# O sistema torna a marca 'Inativa' e mantém os vínculos [RN4]; a marca
# continua identificável nos cadastros que a utilizam.

# O ator executa [A1] e verifica que a marca aparece como 'Inativa'.


# 🟠 [A4] - NOME JÁ USADO
# ---------------------------------------------------------------

# O ator tenta cadastrar uma nova marca com um nome já cadastrado e
# seleciona "Salvar".

# O sistema impede o cadastro duplicado. [RN2]


# 🟠 [A5] - E-MAIL INVÁLIDO
# ---------------------------------------------------------------

# Na edição, o ator informa um e-mail de suporte sem formato válido e
# seleciona "Salvar".

# O sistema recusa a atualização. [RN3]


# 🟠 [A6] - CANCELAR EDIÇÃO
# ---------------------------------------------------------------

# Na edição, o ator altera o nome e seleciona 'Cancelar'.

# O sistema não salva a alteração digitada (CA-2.1.4.1.3.04).


# 🟣 [RN1] VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------

# Nome, identificação internacional e situação são obrigatórios; site e
# telefone são opcionais. A situação aceita Ativo ou Inativo (CA #24553).
# O formato do ID internacional ainda não está definido.

# 🟣 [RN2] NOME ÚNICO
# ---------------------------------------------------------------

# Não pode haver duas marcas com o mesmo nome (CA #24556).

# 🟣 [RN3] E-MAIL DE SUPORTE
# ---------------------------------------------------------------

# O e-mail de suporte precisa ter formato válido (CA-2.1.4.1.3.05).

# 🟣 [RN4] REGRAS DE EXCLUSÃO
# ---------------------------------------------------------------

# Somente administradores podem excluir marcas (CA #24595). Com vínculos,
# a marca é inativada e os vínculos são preservados; sem vínculos, a
# exclusão é física (US #24600).

# 🟣 [RN5] AUDITORIA
# ---------------------------------------------------------------

# Inclusão, alteração e exclusão são registradas na auditoria.


# Pendências de validação: docs/pendencias.md (UCS002).
# Especificação completa: docs/fluxos/UCS002_manter_marcas.md.
