'''
UCS006 - Exportar ficha individual de inversores

Objetivo: Permitir que o administrador exporte em PDF a ficha de um
inversor específico e receba aviso quando o inversor não estiver
disponível.

Requisitos:
- #35875 - Exportação de inversores
- #24249 - Consulta de inversores
- US #24457

Ator:
- Administrador
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Existem os inversores fictícios 'ESTUDO-INVERSORES-01' e
# 'CONTROLE-01'.

# O administrador acessa a página de consulta de inversores e seleciona
# 'ESTUDO-INVERSORES-01'.

# O administrador seleciona a opção de exportar a ficha em PDF. [A1]

# O sistema inicia o download e informa o resultado da obtenção do
# arquivo.

# O administrador abre o PDF e verifica que ele identifica
# 'ESTUDO-INVERSORES-01', e não 'CONTROLE-01'. [RN1] [A2]

# O administrador registra como pendente a conferência dos demais campos
# da ficha. [RN2]


# 🟠 [A1] - INVERSOR INDISPONÍVEL
# ---------------------------------------------------------------

# O inversor selecionado deixou de estar disponível antes da
# solicitação. O administrador seleciona a exportação da ficha.

# O sistema informa que o inversor está indisponível e não entrega a
# ficha de outro registro.


# 🟠 [A2] - INVERSOR DIFERENTE NO PDF
# ---------------------------------------------------------------

# O administrador verifica que o PDF entregue identifica outro inversor.
# Ele registra o resultado como divergente, mesmo que o arquivo exista.


# 🟣 [RN1] FICHA DO REGISTRO SELECIONADO
# ---------------------------------------------------------------

# A ficha individual é um PDF do inversor selecionado. Um PDF coletivo
# não substitui a ficha.

# 🟣 [RN2] CAMPOS DA FICHA
# ---------------------------------------------------------------

# Os campos completos da ficha ainda não estão definidos e não são
# derivados das colunas do CSV. Até a definição, a avaliação desses
# campos fica BLOQUEADA, mesmo com a identidade correta.


# Pendências de validação: docs/pendencias.md (UCS006).
# Especificação completa: docs/fluxos/UCS006_exportacao_2.md.
