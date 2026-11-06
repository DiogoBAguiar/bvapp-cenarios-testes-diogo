# BVAPP — Cenários de teste de Diogo

Mini projeto individual da atividade **Elaboração de cenários de teste do BVapp**,
da disciplina Verificação, Validação e Teste de Software.

**Responsável acadêmico:** Diogo Bruno Ferreira Martins de Aguiar. **Data:** 05/11/2026.

São **10 cenários documentais**: quatro CRUD completos, com objetivos distintos,
e seis cenários de exportação. O recorte individual confirmado é **inversores e
fabricantes (marcas)**. Cada arquivo contém
identificador, objetivo, requisitos, ator, pré-condições, dados, fluxo principal,
alternativas, regras, resultados esperados e pendências.

**Não há implementação, interface, teste automatizado ou teste executado.** Os `.py`
guardam somente documentação, conforme o exemplo do professor. Não é necessário
instalar Python ou Django para ler. A árvore usa `config/` e `functional_tests/`
como inspiração de organização, com os grupos de Ativos em subpastas. Nenhum `manage.py`,
modelo, view ou template foi criado porque a entrega atual não os exige.

## Cenários

Veja os [fluxos em Markdown](docs/fluxos.md), com a descrição completa de cada cenário, ou os diagramas nesta página.

| Identificador | Arquivo | Natureza |
| --- | --- | --- |
| UCS001 | [Manter inversores](functional_tests/ativos/inversores/UCS001_manter_inversores.py) | CRUD completo |
| UCS002 | [Manter marcas](functional_tests/ativos/marcas/UCS002_manter_marcas.py) | CRUD completo |
| UCS003 | [Manter inversor com validação de unicidade e histórico](functional_tests/ativos/inversores/UCS003_crud_variacao.py) | CRUD completo |
| UCS004 | [Manter fabricante com validação de contato e cancelamento](functional_tests/ativos/marcas/UCS004_crud_variacao.py) | CRUD completo |
| UCS005 | [Exportar consulta filtrada de inversores em todos os formatos](functional_tests/ativos/inversores/UCS005_exportacao_1.py) | Exportação |
| UCS006 | [Exportar ficha individual de inversores](functional_tests/ativos/inversores/UCS006_exportacao_2.py) | Exportação |
| UCS007 | [Tratar autorização e falha de exportação de inversores](functional_tests/ativos/inversores/UCS007_exportacao_3.py) | Exportação |
| UCS008 | [Exportar consulta filtrada de fabricantes em todos os formatos](functional_tests/ativos/marcas/UCS008_exportacao_1.py) | Exportação |
| UCS009 | [Exportar ficha individual de fabricantes](functional_tests/ativos/marcas/UCS009_exportacao_2.py) | Exportação |
| UCS010 | [Tratar autorização e falha de exportação de fabricantes](functional_tests/ativos/marcas/UCS010_exportacao_3.py) | Exportação |

## Como revisar

1. Ler [escopo e fontes](docs/escopo-e-fontes.md).
2. Abrir um cenário pelo índice; seguir as quatro operações no mesmo arquivo quando CRUD.
3. Consultar a [matriz de rastreabilidade](docs/matriz-rastreabilidade.md).
4. Tratar as [pendências](docs/pendencias.md) antes de aprovar resultados dependentes.

Os cenários foram preparados com assistência de IA a partir dos requisitos identificados.
A revisão pessoal, a validação das decisões de negócio e a apresentação ainda não são
declaradas realizadas. A atribuição de responsabilidade acadêmica não comprova execução.

O pacote não contém código do produto, arquivos privados de origem, dados reais de
usuários ou credenciais. A leitura dos cenários é autossuficiente para a avaliação.

## Revisão dos requisitos — 06/11/2026

Os dez cenários foram revisados contra a base `5f3072939bb7ce5f90b64bf0faa5483bbb0d3260`. Exportações agora referenciam as Features #35875 (inversores) e #35912 (fabricantes). Veja a [matriz com IDs](docs/matriz-rastreabilidade.md) e as [pendências por cenário](docs/pendencias.md). Etapas com regra pendente ficam bloqueadas para aceite; o conflito Excel/CSV não foi resolvido por suposição. Este pacote contém documentação, sem execução de testes ou entrega no Classroom.

## Fluxos visuais

Representações complementares dos cenários, no formato Mermaid usado no [repositório de referência](https://github.com/DiogoBAguiar/atividade-testes-software). Não acrescentam regras nem substituem as especificações. O ramo de validação é condicional: as pendências existentes continuam abertas e devem ser verificadas antes de cada etapa.

### UCS001 — Manter inversores

[Ver descrição completa, alternativas e pendências](docs/fluxos/UCS001_manter_inversores.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia e ler as pendências"]
    inicio --> decisao{"Regras necessárias à etapa estão validadas?"}
    decisao -->|Não| pendente["BLOQUEADO: registrar dúvida para stakeholders"]
    decisao -->|Sim| p1
    p1["Criar inversor com dados obrigatórios"]
    p2["Consultar o mesmo inversor"]
    p1 --> p2
    p3["Atualizar potência preservando a série"]
    p2 --> p3
    p4["Consultar os valores atualizados"]
    p3 --> p4
    p5["Solicitar e confirmar exclusão sem histórico ou vínculos impeditivos"]
    p4 --> p5
    p6["Conferir remoção pelo meio acordado"]
    p5 --> p6
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    class pendente,decisao pendencia
```

### UCS003 — Manter inversor com validação de unicidade e histórico

[Ver descrição completa, alternativas e pendências](docs/fluxos/UCS003_crud_variacao.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia e ler as pendências"]
    inicio --> decisao{"Regras necessárias à etapa estão validadas?"}
    decisao -->|Não| pendente["BLOQUEADO: registrar dúvida para stakeholders"]
    decisao -->|Sim| p1
    p1["Criar inversor com série inédita"]
    p2["Tentar série repetida: recusar duplicidade"]
    p1 --> p2
    p3["Consultar cadastro aceito"]
    p2 --> p3
    p4["Atualizar potência preservando a série"]
    p3 --> p4
    p5["Preparar histórico no mesmo inversor, sem painéis vinculados"]
    p4 --> p5
    p6["Solicitar e confirmar exclusão"]
    p5 --> p6
    p7["Conferir inativação e histórico preservado"]
    p6 --> p7
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    class pendente,decisao pendencia
```

### UCS005 — Exportar consulta filtrada de inversores em todos os formatos

[Ver descrição completa, alternativas e pendências](docs/fluxos/UCS005_exportacao_1.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia e ler as pendências"]
    inicio --> decisao{"Regras necessárias à etapa estão validadas?"}
    decisao -->|Não| pendente["BLOQUEADO: registrar dúvida para stakeholders"]
    decisao -->|Sim| p1
    p1["Filtrar 23 alvos e excluir 3 controles fictícios"]
    p2["Conciliar formatos: PDF e Excel versus PDF e CSV"]
    p1 --> p2
    p3["Solicitar formato e conferir entrega"]
    p2 --> p3
    p4["Conferir conjunto completo em páginas diferentes"]
    p3 --> p4
    p5["Comparar ordenação e colunas especificadas"]
    p4 --> p5
    p6["Manter avaliação de campos indefinidos bloqueada"]
    p5 --> p6
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    class pendente,decisao pendencia
```

### UCS006 — Exportar ficha individual de inversores

[Ver descrição completa, alternativas e pendências](docs/fluxos/UCS006_exportacao_2.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia e ler as pendências"]
    inicio --> decisao{"Regras necessárias à etapa estão validadas?"}
    decisao -->|Não| pendente["BLOQUEADO: registrar dúvida para stakeholders"]
    decisao -->|Sim| p1
    p1["Selecionar o inversor alvo"]
    p2["Solicitar ficha PDF individual"]
    p1 --> p2
    p3["Conferir entrega e identidade do alvo"]
    p2 --> p3
    p4["Na variante indisponível, conferir resposta prevista"]
    p3 --> p4
    p5["Manter campos e autorização pendentes bloqueados"]
    p4 --> p5
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    class pendente,decisao pendencia
```

### UCS007 — Tratar autorização e falha de exportação de inversores

[Ver descrição completa, alternativas e pendências](docs/fluxos/UCS007_exportacao_3.md)

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

### UCS002 — Manter marcas

[Ver descrição completa, alternativas e pendências](docs/fluxos/UCS002_manter_marcas.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia e ler as pendências"]
    inicio --> decisao{"Regras necessárias à etapa estão validadas?"}
    decisao -->|Não| pendente["BLOQUEADO: registrar dúvida para stakeholders"]
    decisao -->|Sim| p1
    p1["Criar fabricante com documento válido"]
    p2["Consultar fabricante e contatos"]
    p1 --> p2
    p3["Atualizar nome do mesmo fabricante"]
    p2 --> p3
    p4["Consultar os valores atualizados"]
    p3 --> p4
    p5["Preparar vínculo e cancelar uma exclusão"]
    p4 --> p5
    p6["Confirmar exclusão com vínculo"]
    p5 --> p6
    p7["Conferir inativação e vínculos preservados"]
    p6 --> p7
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    class pendente,decisao pendencia
```

### UCS004 — Manter fabricante com validação de contato e cancelamento

[Ver descrição completa, alternativas e pendências](docs/fluxos/UCS004_crud_variacao.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia e ler as pendências"]
    inicio --> decisao{"Regras necessárias à etapa estão validadas?"}
    decisao -->|Não| pendente["BLOQUEADO: registrar dúvida para stakeholders"]
    decisao -->|Sim| p1
    p1["Criar fabricante"]
    p2["Consultar identificação e contato"]
    p1 --> p2
    p3["Tentar e-mail inválido: expectativa de recusa a validar"]
    p2 --> p3
    p4["Corrigir e cancelar edição: expectativa a validar"]
    p3 --> p4
    p5["Reabrir e confirmar edição válida"]
    p4 --> p5
    p6["Cancelar exclusão e conferir preservação"]
    p5 --> p6
    p7["Confirmar exclusão com vínculo"]
    p6 --> p7
    p8["Conferir inativação e referências preservadas"]
    p7 --> p8
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    class pendente,decisao pendencia
```

### UCS008 — Exportar consulta filtrada de fabricantes em todos os formatos

[Ver descrição completa, alternativas e pendências](docs/fluxos/UCS008_exportacao_1.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia e ler as pendências"]
    inicio --> decisao{"Regras necessárias à etapa estão validadas?"}
    decisao -->|Não| pendente["BLOQUEADO: registrar dúvida para stakeholders"]
    decisao -->|Sim| p1
    p1["Filtrar 23 fabricantes e excluir 3 controles fictícios"]
    p2["Solicitar PDF e CSV previstos na revisão"]
    p1 --> p2
    p3["Conferir entrega proposta"]
    p2 --> p3
    p4["Conferir conjunto completo em páginas diferentes"]
    p3 --> p4
    p5["Comparar ordenação e colunas após validação"]
    p4 --> p5
    p6["Manter campos indefinidos bloqueados"]
    p5 --> p6
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    class pendente,decisao pendencia
```

### UCS009 — Exportar ficha individual de fabricantes

[Ver descrição completa, alternativas e pendências](docs/fluxos/UCS009_exportacao_2.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia e ler as pendências"]
    inicio --> decisao{"Regras necessárias à etapa estão validadas?"}
    decisao -->|Não| pendente["BLOQUEADO: registrar dúvida para stakeholders"]
    decisao -->|Sim| p1
    p1["Selecionar fabricante alvo"]
    p2["Solicitar PDF individual e conferir entrega proposta"]
    p1 --> p2
    p3["Conferir identidade do fabricante"]
    p2 --> p3
    p4["Conferir ativos associados não excluídos por série, tipo e situação"]
    p3 --> p4
    p5["Na variante indisponível, conferir resposta prevista"]
    p4 --> p5
    p6["Manter campos e autorização pendentes bloqueados"]
    p5 --> p6
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    class pendente,decisao pendencia
```

### UCS010 — Tratar autorização e falha de exportação de fabricantes

[Ver descrição completa, alternativas e pendências](docs/fluxos/UCS010_exportacao_3.md)

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
