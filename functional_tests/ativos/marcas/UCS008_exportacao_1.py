'''
UCS008 - Exportar consulta filtrada de fabricantes em todos os formatos

Objetivo: Permitir que o usuário exporte o resultado completo de uma
consulta filtrada de fabricantes, em PDF e CSV, na mesma ordem da
consulta.

Requisitos:
- #35912 - Exportação de fabricantes
- #24273 - Consulta de marcas
- US #25954

Ator:
- Usuário com autorização para consultar a listagem de marcas
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Existem 23 fabricantes fictícios 'ESTUDO-MARCAS-01' a '23' que atendem
# ao filtro e três 'CONTROLE-01' a '03' que não atendem. A página da
# consulta mostra dez registros.

# O ator acessa a página de consulta de marcas. Ele observa que existe a
# busca por fabricante.

# O ator aplica um filtro que seleciona os 23 fabricantes de estudo e
# confere que o total exibido é 23.

# O ator escolhe uma ordenação e seleciona a exportação em PDF. [A1]

# O sistema inicia o download e informa o resultado da obtenção do
# arquivo.

# O ator abre o arquivo e verifica que os 23 fabricantes de estudo estão
# nele, que nenhum dos três controles aparece [RN2] e que a ordem é a
# mesma da consulta. [RN3]

# O ator repete a exportação em CSV [RN1] e confere as colunas e os
# valores de cada fabricante exportado. [RN4]

# O ator vai para outra página da consulta e repete a exportação.
# O arquivo continua com os 23 fabricantes. [RN2] [A2]


# 🟠 [A1] - FORMATO AUSENTE
# ---------------------------------------------------------------

# O ator verifica que o sistema não oferece PDF ou CSV. Ele registra o
# requisito como não atendido, porque os dois formatos são
# obrigatórios. [RN1]


# 🟠 [A2] - CONSULTA VAZIA
# ---------------------------------------------------------------

# O ator aplica um filtro que não retorna nenhum fabricante e solicita a
# exportação. O comportamento esperado ainda não está definido; o ator
# registra o que observar, sem presumir arquivo vazio.


# 🟣 [RN1] FORMATOS OBRIGATÓRIOS
# ---------------------------------------------------------------

# A exportação coletiva oferece PDF e CSV. Cada arquivo entregue deve
# estar no formato solicitado. A ficha de um registro individual é em
# PDF.

# 🟣 [RN2] RESULTADO COMPLETO DA CONSULTA
# ---------------------------------------------------------------

# A exportação contém todos os registros que atendem aos filtros, e não
# apenas os da página exibida. Registros fora do filtro não entram.

# 🟣 [RN3] ORDENAÇÃO
# ---------------------------------------------------------------

# O arquivo segue a ordenação escolhida na consulta.

# 🟣 [RN4] COLUNAS DO CSV
# ---------------------------------------------------------------

# O CSV apresenta: Nome, Site Oficial, E-mail de Suporte e Telefone de
# Suporte. Essas colunas vêm do levantamento e ainda não constam dos
# CAs da Feature #35912; o conteúdo do PDF também não está definido.


# Pendências de validação: docs/pendencias.md (UCS008).
# Especificação completa: docs/fluxos/UCS008_exportacao_1.md.
