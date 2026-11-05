"""
UCS006 — Exportar ficha individual de inversores

Autoria / responsável acadêmico: Diogo Bruno Ferreira Martins de Aguiar
Preparação assistida por IA; revisão humana e apresentação pendentes.
Data: 05/11/2026. Revisão-base: 838d6ec05d26f6364e920e865d4abff59088dd34
Natureza: cenário documental; não é teste automatizado; não executado.

OBJETIVO
Conferir a identidade da ficha individual e a resposta quando o alvo está indisponível.
É um fluxo de relatório, sem operações CRUD divididas para aumentar a contagem.

REQUISITOS RELACIONADOS
Grupo: Gestão de Inversores.
Feature existente sem número: Exportação de inversores.
Critérios identificados pelos títulos originais: Arquivo individual; Registro individual indisponível; Entrega do arquivo.

ATOR
Usuário com as permissões da modalidade. Nas alternativas de autorização,
usuário com a permissão ausente, sem ampliar papéis ou poderes do cadastro.

PRÉ-CONDIÇÕES
Ambiente futuro isolado e massa sintética já preparada. Nenhuma criação de cadastro
ocorre neste cenário de exportação. Na execução futura, preservar os controles.
As definições pendentes são resolvidas antes de aprovar a etapa dependente.

DADOS DE TESTE
Um registro fictício ESTUDO-INVERSORES-01 e outro CONTROLE-01.
Para inversores, nenhuma suposição sobre campos completos do PDF é adicionada.
Todos os dados são fictícios; não constituem limites ou regras novas.

[FP] FLUXO PRINCIPAL
1. Selecionar ESTUDO-INVERSORES-01 na consulta e solicitar sua ficha PDF.
2. Verificar início de download e informação do resultado.
3. Abrir o documento em futura execução e conferir a identidade do alvo, distinguindo-a
   de CONTROLE-01. Não aceitar PDF coletivo como substituto da ficha.
4. Registrar como pendente o conjunto completo de campos da ficha; não derivar esse conjunto das colunas CSV.
5. Na variante com alvo previamente indisponível, repetir a solicitação. Esperado:
   informar indisponibilidade; não entregar ficha de outro registro.

[A] FLUXOS ALTERNATIVOS
1. Alvo diferente no PDF: resultado divergente; conferir identificação, não apenas existência do arquivo.
2. Campos de PDF não definidos: marcar avaliação desses campos BLOQUEADA, mesmo com identidade correta.

REGRAS DE NEGÓCIO
Cada resultado acima deriva do critério nomeado. Formato, conjunto, identidade e
entrega são verificações distintas. A implementação não define o resultado esperado.
Não definir mensagens literais, prazos, novas tentativas ou campos não especificados.

RESULTADOS ESPERADOS
Os resultados aparecem junto a cada ação para permitir comparação passo a passo.
Nenhum arquivo foi gerado ou cenário executado. Em futura execução registrar
versão, data, massa, esperado, observado e evidência, sem declarar sucesso antecipado.

PENDÊNCIAS
Campos completos de PDF coletivo e individual, unidades e apresentação de dados ausentes precisam de decisão. O conteúdo CSV descrito não autoriza presumir igualdade dos demais formatos. Definir consulta vazia, fotografia temporal do inventário e recuperação após perda de resposta.
"""
