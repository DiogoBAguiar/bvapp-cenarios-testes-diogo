# UCS009 — Exportar ficha individual de fabricantes

[Índice de fluxos](../fluxos.md) · [README](../../README.md) · [Cenário no formato do professor (.py)](../../functional_tests/ativos/marcas/UCS009_exportacao_2.py)

Os losangos representam a avaliação da etapa no cenário, não novos controles da interface. **Falha esperada e corretamente tratada pode atender ao cenário negativo.** Uma falha inesperada interrompe apenas as etapas dependentes desta execução. Essa interrupção é uma orientação de teste, não uma regra do sistema. Não há repetição automática, rollback, preservação de campos ou retomada presumidos. Os acréscimos marcados **a validar** continuam sujeitos ao aceite dos stakeholders.

## Fluxo visual

```mermaid
flowchart TD
    inicio["Preparar massa fictícia; observar pendências de cada etapa"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; não declarar aceite de regras pendentes"]
    inicio --> p1
    p1["Selecionar fabricante alvo"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f1 --> parar
    q1 -->|Sim| p2
    p2["Solicitar PDF individual e conferir entrega proposta"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["Informar falha; não entregar erro como relatório - a validar"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Conferir identidade do fabricante"]
    p3 --> q3{"Etapa produziu o resultado esperado?"}
    q3 -->|Não ou não comprovado| f3["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f3 --> parar
    q3 -->|Sim| p4
    p4["Conferir ativos associados não excluídos por série, tipo e situação"]
    p4 --> q4{"Etapa produziu o resultado esperado?"}
    q4 -->|Não ou não comprovado| f4["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f4 --> parar
    q4 -->|Sim| p5
    p5["Na variante indisponível, conferir resposta prevista"]
    p5 --> q5{"Etapa produziu o resultado esperado?"}
    q5 -->|Não ou não comprovado| f5["Se não informar indisponibilidade ou entregar outro registro: divergência"]
    f5 --> parar
    q5 -->|Sim| p6
    p6["Manter campos pendentes bloqueados"]
    p6 --> q6{"Etapa produziu o resultado esperado?"}
    q6 -->|Não ou não comprovado| f6["PENDÊNCIA: não há decisão ou condição suficiente para esta etapa"]
    f6 --> parar
    q6 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5,f6 pendencia
```

## Falhas, recusas e pendências por etapa

As referências CAxx abaixo são rótulos dentro da Feature indicada, não IDs globais novos. Uma mensagem de falha não comprova que nenhuma gravação ocorreu; em perda de resposta, o estado final permanece a verificar.

| Etapa ou variante | Resposta prevista ou pendência | Base |
| --- | --- | --- |
| 1. Selecionar fabricante alvo | Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes. Não continuar etapas dependentes. | Resultados esperados do cenário; não há resposta automática definida para divergência constatada pelo avaliador |
| 2. Solicitar PDF individual e conferir entrega proposta | Informar falha; não entregar erro como relatório - a validar. Não continuar etapas dependentes. | #35912 CA01, acréscimo a validar |
| 3. Conferir identidade do fabricante | Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes. Não continuar etapas dependentes. | Resultados esperados do cenário; não há resposta automática definida para divergência constatada pelo avaliador |
| 4. Conferir ativos associados não excluídos por série, tipo e situação | Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes. Não continuar etapas dependentes. | Resultados esperados do cenário; não há resposta automática definida para divergência constatada pelo avaliador |
| 5. Na variante indisponível, conferir resposta prevista | Se não informar indisponibilidade ou entregar outro registro: divergência. Não continuar etapas dependentes. | #35912 CA02, a validar |
| 6. Manter campos pendentes bloqueados | PENDÊNCIA: não há decisão ou condição suficiente para esta etapa. Não continuar etapas dependentes. | Pendências do próprio cenário; não é falha comprovada do sistema |

## Especificação completa

Autoria / responsável acadêmico: Diogo Bruno Ferreira Martins de Aguiar
Preparação assistida por IA; revisão humana e apresentação pendentes.
Revisão documental: 06/11/2026. Criação: 05/11/2026. Revisão-base: 5f3072939bb7ce5f90b64bf0faa5483bbb0d3260
Natureza: cenário documental; não é teste automatizado; não executado.


### OBJETIVO

Conferir a identidade da ficha individual e a resposta quando o alvo está indisponível.
É um fluxo de relatório, sem operações CRUD divididas para aumentar a contagem.


### REQUISITOS RELACIONADOS

Grupo: Cadastro de Marcas (Fabricantes).
Feature #35912 — Exportação de fabricantes. Relacionadas: Consulta #24273 e US #25954.
Tópicos da consolidação local (mapeamento revisado em docs/matriz-rastreabilidade.md): Arquivo individual; Registro individual indisponível; Entrega do arquivo; Ativos da marca.


### SITUAÇÃO DAS REGRAS E BLOQUEIOS

FP1 a FP5: PDF individual, identidade, indisponibilidade e ativos associados constam dos novos CA02/CA04/CA07/CA08 da Feature #35912; aguardam validação dos stakeholders. FP2: confirmar indicação de download, que não está definida nesses nove CAs. Confirmar campos completos do PDF; não presumir que identidade correta valida todo o conteúdo.
Resultados de acréscimos a validar são expectativas propostas. Não aprovar essas etapas antes da decisão registrada dos stakeholders. IDs globais e rótulos locais são distinguidos em docs/matriz-rastreabilidade.md.


### ATOR

Administrador. O critério Autorização da Feature de exportação exige apenas autorização para visualizar o registro (exportação individual); o cenário usa o Administrador, que tem essa autorização.
A recusa sem essa autorização é verificada no UCS010.


### PRÉ-CONDIÇÕES

Ambiente futuro isolado e massa sintética já preparada. Nenhuma criação de cadastro
ocorre neste cenário de exportação. Na execução futura, preservar os controles.
As definições pendentes são resolvidas antes de aprovar a etapa dependente.


### DADOS DE TESTE

Um registro fictício ESTUDO-MARCAS-01 e outro CONTROLE-01.
Para fabricantes, dois equipamentos não excluídos vinculados ao alvo, um excluído
e um de outra marca como controles; não se solicita manutenção desses equipamentos.
Todos os dados são fictícios; não constituem limites ou regras novas.


### [FP] FLUXO PRINCIPAL

1. Selecionar ESTUDO-MARCAS-01 na consulta e solicitar sua ficha PDF.
2. Verificar início de download e informação do resultado.
3. Abrir o documento em futura execução e conferir a identidade do alvo, distinguindo-a
   de CONTROLE-01. Não aceitar PDF coletivo como substituto da ficha.
4. Conferir os equipamentos associados não excluídos por série, tipo e situação; o excluído e o de outra marca não devem integrar essa relação.
5. Na variante com alvo previamente indisponível, repetir a solicitação. Esperado:
   informar indisponibilidade; não entregar ficha de outro registro.


### [A] FLUXOS ALTERNATIVOS

1. Alvo diferente no PDF: resultado divergente; conferir identificação, não apenas existência do arquivo.
2. Campos de PDF não definidos: marcar avaliação desses campos BLOQUEADA, mesmo com identidade correta.


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
