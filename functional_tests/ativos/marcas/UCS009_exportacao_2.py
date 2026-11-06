"""
UCS009 — Exportar ficha individual de fabricantes

Autoria / responsável acadêmico: Diogo Bruno Ferreira Martins de Aguiar
Preparação assistida por IA; revisão humana e apresentação pendentes.
Revisão documental: 06/11/2026. Criação: 05/11/2026. Revisão-base: 5f3072939bb7ce5f90b64bf0faa5483bbb0d3260
Natureza: cenário documental; não é teste automatizado; não executado.

OBJETIVO
Conferir a identidade da ficha individual e a resposta quando o alvo está indisponível.
É um fluxo de relatório, sem operações CRUD divididas para aumentar a contagem.

REQUISITOS RELACIONADOS
Grupo: Cadastro de Marcas (Fabricantes).
Feature #35912 — Exportação de fabricantes. Relacionadas: Consulta #24273 e US #25954.
Tópicos da consolidação local (mapeamento revisado em docs/matriz-rastreabilidade.md): Arquivo individual; Registro individual indisponível; Entrega do arquivo; Ativos da marca.

SITUAÇÃO DAS REGRAS E BLOQUEIOS
FP1 a FP5: PDF individual, identidade, indisponibilidade e ativos associados constam dos novos CA02/CA04/CA07/CA08 da Feature #35912; aguardam validação dos stakeholders. FP2: confirmar indicação de download, que não está definida nesses nove CAs. Confirmar campos completos do PDF e autorização da modalidade; não presumir que identidade correta valida todo o conteúdo.
Resultados de acréscimos a validar são expectativas propostas. Não aprovar essas etapas antes da decisão registrada dos stakeholders. IDs globais e rótulos locais são distinguidos em docs/matriz-rastreabilidade.md.

ATOR
Pessoa usuária cuja autorização para a modalidade deverá ser definida pelos stakeholders.
A matriz de perfis e permissões permanece pendente; não inferir autorização de exportação pelo acesso à consulta.

PRÉ-CONDIÇÕES
Ambiente futuro isolado e massa sintética já preparada. Nenhuma criação de cadastro
ocorre neste cenário de exportação. Na execução futura, preservar os controles.
As definições pendentes são resolvidas antes de aprovar a etapa dependente.

DADOS DE TESTE
Um registro fictício ESTUDO-MARCAS-01 e outro CONTROLE-01.
Para fabricantes, dois equipamentos não excluídos vinculados ao alvo, um excluído
e um de outra marca como controles; não se solicita manutenção desses equipamentos.
Todos os dados são fictícios; não constituem limites ou regras novas.

[FP] FLUXO PRINCIPAL
1. Selecionar ESTUDO-MARCAS-01 na consulta e solicitar sua ficha PDF.
2. Verificar início de download e informação do resultado.
3. Abrir o documento em futura execução e conferir a identidade do alvo, distinguindo-a
   de CONTROLE-01. Não aceitar PDF coletivo como substituto da ficha.
4. Conferir os equipamentos associados não excluídos por série, tipo e situação; o excluído e o de outra marca não devem integrar essa relação.
5. Na variante com alvo previamente indisponível, repetir a solicitação. Esperado:
   informar indisponibilidade; não entregar ficha de outro registro.

[A] FLUXOS ALTERNATIVOS
1. Alvo diferente no PDF: resultado divergente; conferir identificação, não apenas existência do arquivo.
2. Campos de PDF não definidos: marcar avaliação desses campos BLOQUEADA, mesmo com identidade correta.

REGRAS DE NEGÓCIO
Cada resultado proposto está sujeito à situação da regra indicada acima. Formato, conjunto, identidade e
entrega são verificações distintas. A implementação não define o resultado esperado.
Não definir mensagens literais, prazos, novas tentativas ou campos não especificados.

RESULTADOS ESPERADOS
Os resultados aparecem junto a cada ação para permitir comparação passo a passo.
Nenhum arquivo foi gerado ou cenário executado. Em futura execução registrar
versão, data, massa, esperado, observado e evidência, sem declarar sucesso antecipado.

PENDÊNCIAS
Consultar também SITUAÇÃO DAS REGRAS E BLOQUEIOS acima.
Campos completos de PDF coletivo e individual, unidades e apresentação de dados ausentes precisam de decisão. O conteúdo CSV descrito não autoriza presumir igualdade dos demais formatos. Definir consulta vazia, fotografia temporal do inventário e recuperação após perda de resposta.
"""
