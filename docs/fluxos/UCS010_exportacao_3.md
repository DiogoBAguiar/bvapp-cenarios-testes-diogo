# UCS010 — Tratar autorização e falha de exportação de fabricantes

[Índice de fluxos](../fluxos.md) · [README](../../README.md) · [Cenário original](../../functional_tests/ativos/marcas/UCS010_exportacao_3.py)

O diagrama resume o fluxo principal e as variantes indicadas. Antes de cada etapa, conferir seus bloqueios; o ramo “Sim” é condicional e não declara que já houve validação. Os fluxos alternativos e os resultados completos estão descritos abaixo.

## Fluxo visual

```mermaid
flowchart TD
    inicio["Preparar massa fictícia e ler as pendências"]
    inicio --> decisao{"Regras necessárias à etapa estão validadas?"}
    decisao -->|Não| pendente["BLOQUEADO: registrar dúvida para stakeholders"]
    decisao -->|Sim| p1
    p1["Definir matriz de autorização por modalidade"]
    p2["Após validação, solicitar exportação com perfil autorizado"]
    p1 --> p2
    p3["Conferir indicação de preparação proposta"]
    p2 --> p3
    p4["Avaliar falha controlada na exportação coletiva"]
    p3 --> p4
    p5["Avaliar falha controlada na ficha individual"]
    p4 --> p5
    p6["Registrar observações sem presumir política de retomada"]
    p5 --> p6
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    class pendente,decisao pendencia
```

## Especificação completa

Autoria / responsável acadêmico: Diogo Bruno Ferreira Martins de Aguiar
Preparação assistida por IA; revisão humana e apresentação pendentes.
Revisão documental: 06/11/2026. Criação: 05/11/2026. Revisão-base: 5f3072939bb7ce5f90b64bf0faa5483bbb0d3260
Natureza: cenário documental; não é teste automatizado; não executado.


### OBJETIVO

Conferir recusa por autorização, estado de andamento e resposta de falha sem entregar erro como relatório.
É um fluxo de relatório, sem operações CRUD divididas para aumentar a contagem.


### REQUISITOS RELACIONADOS

Grupo: Cadastro de Marcas (Fabricantes).
Feature #35912 — Exportação de fabricantes. Relacionadas: Consulta #24273 e US #25954.
Tópicos da consolidação local (mapeamento revisado em docs/matriz-rastreabilidade.md): Autorização; Falha na obtenção do arquivo; Exportação em andamento.


### SITUAÇÃO DAS REGRAS E BLOQUEIOS

FP1 e A1: BLOQUEADOS até aprovação da matriz de autorização por modalidade. FP2 a FP4: andamento e falha constam dos novos CA03/CA01 da Feature #35912; expectativas propostas, pendentes de validação. FP5: recuperação e tentativas continuam indefinidas.
Resultados de acréscimos a validar são expectativas propostas. Não aprovar essas etapas antes da decisão registrada dos stakeholders. IDs globais e rótulos locais são distinguidos em docs/matriz-rastreabilidade.md.


### ATOR

Pessoa usuária cuja autorização para a modalidade deverá ser definida pelos stakeholders.
A matriz de perfis e permissões permanece pendente; não inferir autorização de exportação pelo acesso à consulta.


### PRÉ-CONDIÇÕES

Ambiente futuro isolado e massa sintética já preparada. Nenhuma criação de cadastro
ocorre neste cenário de exportação. Na execução futura, preservar os controles.
As definições pendentes são resolvidas antes de aprovar a etapa dependente.


### DADOS DE TESTE

Perfis sintéticos propostos para discussão: A com consulta e visualização; B sem consulta; C sem visualização. Nenhum tem autorização de exportação presumida.
Alvo ESTUDO-MARCAS-01 existente e consulta filtrada com dados fictícios.
Os perfis representam permissões para esta análise, não novos papéis do produto.
Uma condição controlada de falha de obtenção deve ser preparada para futura execução.
Todos os dados são fictícios; não constituem limites ou regras novas.


### [FP] FLUXO PRINCIPAL

1. BLOQUEADO: submeter os perfis A, B e C à definição da matriz de exportação
   coletiva e individual. Registrar quem poderá exportar em cada modalidade e
   o resultado previsto para acesso não autorizado; não presumir recusa a B/C.
2. Após definir um perfil autorizado, solicitar exportação coletiva. Durante preparação, verificar
   indicação de andamento e controle da ação indisponível para novo acionamento.
3. Preparar a variante de falha controlada de obtenção e solicitar exportação.
   Esperado: falha informada; conteúdo de erro não é entregue como relatório.
4. Repetir a variante de falha para a ficha individual, mantendo alvo existente.
   Esperado: falha informada; nenhum relatório de erro apresentado como ficha.
5. Registrar o que foi possível observar; retorno do controle, número de tentativas
   e retomada após resposta desconhecida permanecem sem contrato aprovado.


### [A] FLUXOS ALTERNATIVOS

1. BLOQUEADO: confirmar se as modalidades têm autorizações independentes e sua relação com consulta/visualização. Somente depois definir os resultados das combinações.
2. Perda de resposta ou concorrência: resultado pendente; não presumir repetição automática nem reutilização do arquivo.


### REGRAS DE NEGÓCIO

Cada resultado proposto está sujeito à situação da regra indicada acima. Formato, conjunto, identidade e
entrega são verificações distintas. A implementação não define o resultado esperado.
Não definir mensagens literais, prazos, novas tentativas ou campos não especificados.


### RESULTADOS ESPERADOS

Os resultados aparecem junto a cada ação para permitir comparação passo a passo.
Nenhum arquivo foi gerado ou cenário executado. Em futura execução registrar
versão, data, massa, esperado, observado e evidência, sem declarar sucesso antecipado.


### PENDÊNCIAS

Consultar também SITUAÇÃO DAS REGRAS E BLOQUEIOS acima.
Campos completos de PDF coletivo e individual, unidades e apresentação de dados ausentes precisam de decisão. O conteúdo CSV descrito não autoriza presumir igualdade dos demais formatos. Definir consulta vazia, fotografia temporal do inventário e recuperação após perda de resposta.
