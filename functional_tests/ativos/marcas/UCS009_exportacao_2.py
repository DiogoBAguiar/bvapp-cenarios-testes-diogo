'''
UCS009 - Exportar ficha individual de fabricantes

Objetivo: Permitir que o usuário exporte em PDF a ficha de um fabricante
específico, com seus equipamentos associados, e receba aviso quando o
fabricante não estiver disponível.

Requisitos:
- #35912 - Exportação de fabricantes
- #24273 - Consulta de marcas
- US #25954

Ator:
- Usuário com autorização para visualizar o registro do fabricante
'''

# 🟢 [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# Existem os fabricantes fictícios 'ESTUDO-MARCAS-01' e 'CONTROLE-01'.
# 'ESTUDO-MARCAS-01' tem dois equipamentos ativos vinculados e um
# equipamento excluído; há ainda um equipamento de outra marca.

# O ator acessa a página de consulta de marcas e seleciona
# 'ESTUDO-MARCAS-01'.

# O ator seleciona a opção de exportar a ficha em PDF. [A1]

# O sistema inicia o download e informa o resultado da obtenção do
# arquivo.

# O ator abre o PDF e verifica que ele identifica 'ESTUDO-MARCAS-01', e
# não 'CONTROLE-01'. [RN1] [A2]

# O ator confere que a ficha lista os dois equipamentos ativos
# vinculados, com série, tipo e situação, e que o equipamento excluído e
# o de outra marca não aparecem. [RN2]

# O ator registra como pendente a conferência dos demais campos da
# ficha. [RN3]


# 🟠 [A1] - FABRICANTE INDISPONÍVEL
# ---------------------------------------------------------------

# O fabricante selecionado deixou de estar disponível antes da
# solicitação. O ator seleciona a exportação da ficha.

# O sistema informa que o fabricante está indisponível e não entrega a
# ficha de outro registro.


# 🟠 [A2] - FABRICANTE DIFERENTE NO PDF
# ---------------------------------------------------------------

# O ator verifica que o PDF entregue identifica outro fabricante. Ele
# registra o resultado como divergente, mesmo que o arquivo exista.


# 🟣 [RN1] FICHA DO REGISTRO SELECIONADO
# ---------------------------------------------------------------

# A ficha individual é um PDF do fabricante selecionado. Um PDF coletivo
# não substitui a ficha.

# 🟣 [RN2] EQUIPAMENTOS ASSOCIADOS
# ---------------------------------------------------------------

# A ficha lista os equipamentos não excluídos vinculados ao fabricante
# (CAs da Feature #35912, a validar).

# 🟣 [RN3] CAMPOS DA FICHA
# ---------------------------------------------------------------

# Os campos completos da ficha ainda não estão definidos. Até a
# definição, a avaliação desses campos fica BLOQUEADA, mesmo com a
# identidade correta.


# Pendências de validação: docs/pendencias.md (UCS009).
# Especificação completa: docs/fluxos/UCS009_exportacao_2.md.
