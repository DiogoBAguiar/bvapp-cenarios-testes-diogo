"""
UCS005 — Exportar consulta filtrada de inversores em todos os formatos

Autoria / responsável acadêmico: Diogo Bruno Ferreira Martins de Aguiar
Preparação assistida por IA; revisão humana e apresentação pendentes.
Data: 05/11/2026. Revisão-base: 838d6ec05d26f6364e920e865d4abff59088dd34
Natureza: cenário documental; não é teste automatizado; não executado.

OBJETIVO
Conferir formatos obrigatórios, filtros, abrangência além da página e ordem do arquivo coletivo.
É um fluxo de relatório, sem operações CRUD divididas para aumentar a contagem.

REQUISITOS RELACIONADOS
Grupo: Gestão de Inversores.
Feature existente sem número: Exportação de inversores.
Critérios identificados pelos títulos originais: Formatos de exportação; Resultado completo da consulta; Filtros da exportação; Dados do arquivo; Entrega do arquivo; Ordenação.

ATOR
Usuário com as permissões da modalidade. Nas alternativas de autorização,
usuário com a permissão ausente, sem ampliar papéis ou poderes do cadastro.

PRÉ-CONDIÇÕES
Ambiente futuro isolado e massa sintética já preparada. Nenhuma criação de cadastro
ocorre neste cenário de exportação. Na execução futura, preservar os controles.
As definições pendentes são resolvidas antes de aprovar a etapa dependente.

DADOS DE TESTE
23 registros fictícios ESTUDO-INVERSORES-01 a 23 que correspondem ao filtro
e três CONTROLE-01 a 03 que não correspondem. Página de dez registros, se disponível.
O número 23 é massa que atravessa páginas, não limite de produto. Filtros previstos:
O conjunto exportado deve respeitar busca por série, modelo, fabricante, fornecedor, usina, operadora, situação e demais filtros definidos na consulta. Registros que não atendam aos filtros não devem ser acrescentados ao relatório.
Todos os dados são fictícios; não constituem limites ou regras novas.

[FP] FLUXO PRINCIPAL
1. Acessar a consulta e aplicar um filtro previsto que selecione os 23 alvos,
   excluindo os três controles. Conferir o total antes de exportar.
2. Escolher uma ordenação suportada e solicitar cada formato obrigatório, um por vez.
   Contrato de formatos: A exportação coletiva deve oferecer PDF e Excel; CSV é uma opção adicional e não substitui Excel. Cada arquivo entregue deve corresponder ao formato solicitado. A exportação de um registro individual é em PDF.
3. Verificar o início do download e a informação do resultado de obtenção.
4. Comparar identidades: os 23 alvos devem estar no arquivo, nenhum dos três controles.
   Repetir a solicitação em outra página: o conjunto continua completo.
5. Comparar a sequência com a ordenação da consulta, prevista para este grupo.
6. Se CSV estiver previsto/disponível, conferir as colunas definidas e respectivos
   valores: O arquivo CSV deve apresentar: Número de Série, Potência, Modelo, Fabricante, Fornecedor, Usina, Posse, Situação, Garantia de Compra e Garantia de Instalação. A verificação deve comparar os valores com os registros selecionados; campos ausentes na especificação original ou diferenças entre formatos permanecem nas pendências, sem presumir equivalência.
7. Não aprovar conteúdo completo de PDF/Excel sem a definição ainda pendente.
   Aprovação de conjunto/ordem não equivale à aprovação de todas as colunas.

[A] FLUXOS ALTERNATIVOS
1. Formato obrigatório ausente: registrar não atendimento; CSV não substitui Excel quando Excel é obrigatório.
2. Consulta vazia: comportamento pendente; não presumir arquivo vazio ou ausência de download.

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
