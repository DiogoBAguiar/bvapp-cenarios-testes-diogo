'''
UCS005 - Exportar consulta filtrada de inversores em todos os formatos

Objetivo: Permitir que o administrador exporte o resultado completo de
uma consulta filtrada de inversores, em cada formato obrigatório, na
mesma ordem da consulta.

Requisitos:
- #35875 - Exportação de inversores
- #24249 - Consulta de inversores
- US #24457

Ator:
- Administrador
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Existem 23 inversores fictícios 'ESTUDO-INVERSORES-01' a '23' que
# atendem ao filtro e três 'CONTROLE-01' a '03' que não atendem. A
# página da consulta mostra dez registros.

# O administrador acessa a página de consulta de inversores. Ele observa
# que existem filtros por série, modelo, fabricante, fornecedor, usina,
# operadora e situação.

# O administrador aplica um filtro que seleciona os 23 inversores de
# estudo e confere que o total exibido é 23.

# O administrador escolhe uma ordenação e seleciona a exportação em PDF.
# [A1]

# O sistema inicia o download e informa o resultado da obtenção do
# arquivo.

# O administrador abre o arquivo e verifica que os 23 inversores de
# estudo estão nele, que nenhum dos três controles aparece [RN2] e que a
# ordem é a mesma da consulta. [RN3]

# O administrador repete a exportação nos demais formatos obrigatórios.
# [RN1]

# No arquivo CSV, o administrador confere as colunas e os valores de
# cada inversor exportado. [RN4]

# O administrador vai para outra página da consulta e repete a
# exportação. O arquivo continua com os 23 inversores. [RN2] [A2]


# 🟠 [A1] - FORMATOS DIVERGENTES ENTRE AS FONTES
# ---------------------------------------------------------------

# O administrador verifica que o sistema oferece formatos diferentes dos
# exigidos por uma das fontes. Ele registra o conflito e marca a
# avaliação dos formatos como BLOQUEADA até a decisão dos stakeholders.
# CSV não substitui Excel. [RN1]


# 🟠 [A2] - CONSULTA VAZIA
# ---------------------------------------------------------------

# O administrador aplica um filtro que não retorna nenhum inversor e
# solicita a exportação. O comportamento esperado ainda não está
# definido; o administrador registra o que observar, sem presumir
# arquivo vazio.


# 🟣 [RN1] FORMATOS OBRIGATÓRIOS
# ---------------------------------------------------------------

# CONFLITO PENDENTE: o CA #24449 exige PDF e Excel; o CA01 da Feature
# #35875 descreve PDF e CSV. Cada arquivo entregue deve estar no formato
# solicitado. A ficha de um registro individual é em PDF.

# 🟣 [RN2] RESULTADO COMPLETO DA CONSULTA
# ---------------------------------------------------------------

# A exportação contém todos os registros que atendem aos filtros, e não
# apenas os da página exibida. Registros fora do filtro não entram.

# 🟣 [RN3] ORDENAÇÃO
# ---------------------------------------------------------------

# O arquivo segue a ordenação escolhida na consulta.

# 🟣 [RN4] COLUNAS DO CSV
# ---------------------------------------------------------------

# O CSV apresenta: Número de Série, Potência, Modelo, Fabricante,
# Fornecedor, Usina, Posse, Situação, Garantia de Compra e Garantia de
# Instalação. As colunas de PDF e Excel ainda não estão definidas.


# Pendências de validação: docs/pendencias.md (UCS005).
# Especificação completa: docs/fluxos/UCS005_exportacao_1.md.
