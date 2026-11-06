# BVAPP — Cenários de teste de Diogo

Mini projeto individual da atividade **Elaboração de cenários de teste do BVapp**,
da disciplina Verificação, Validação e Teste de Software.

**Responsável acadêmico:** Diogo Bruno Ferreira Martins de Aguiar. **Data:** 05/11/2026.

São **11 cenários documentais**: quatro CRUD completos, com objetivos distintos,
seis cenários de exportação e um cenário negativo de controle de acesso. O recorte individual confirmado é **inversores e
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
| UCS011 | [Recusar edição e exclusão por acesso direto sem permissão](functional_tests/ativos/UCS011_acesso_direto_sem_permissao.py) | Controle de acesso |

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

O UCS011 foi acrescentado na mesma data e base. Ele verifica, para inversores e fabricantes, que perfis sem a autorização correspondente são recusados ao solicitar edição ou exclusão diretamente, sem usar os controles da tela. As recusas esperadas vêm dos critérios de autorização já existentes (CA-2.1.1.2.01, CA-2.1.1.3.01, CA-2.1.1.4.01, CA-2.1.4.1.3.01 e CA-2.1.4.1.4.01); nenhuma regra nova foi criada.

## Fluxos visuais

Os losangos representam a avaliação da etapa no cenário, não novos controles da interface. **Falha esperada e corretamente tratada pode atender ao cenário negativo.** Uma falha inesperada interrompe apenas as etapas dependentes desta execução. Essa interrupção é uma orientação de teste, não uma regra do sistema. Não há repetição automática, rollback, preservação de campos ou retomada presumidos. Os acréscimos marcados **a validar** continuam sujeitos ao aceite dos stakeholders.

As respostas documentadas estão detalhadas nas tabelas de cada [fluxo](docs/fluxos.md). Cada operação e conferência tem uma saída para resultado inesperado ou não comprovado.

### UCS001 — Manter inversores

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS001_manter_inversores.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia; observar pendências de cada etapa"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; não declarar aceite de regras pendentes"]
    inicio --> p1
    p1["Criar inversor com dados obrigatórios"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["Informar falha sem confirmar inclusão - a validar"]
    f1 --> parar
    q1 -->|Sim| p2
    p1 -->|Obrigatório ausente| obrig["Recusar inclusão e indicar campos faltantes"]
    p1 -->|Série duplicado| dup["Recusar duplicidade e emitir alerta"]
    obrig --> negativo["AVALIAÇÃO: conferir recusa; encerrar variante negativa sem avançar com cadastro inexistente"]
    dup --> negativo
    p2["Consultar o mesmo inversor"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["PENDÊNCIA: resposta à falha de consulta e recuperação"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Atualizar potência preservando a série"]
    p3 --> q3{"Etapa produziu o resultado esperado?"}
    q3 -->|Não ou não comprovado| f3["Apresentar motivo da falha sem confirmar edição - a validar"]
    f3 --> parar
    q3 -->|Sim| p4
    p3 -->|Entrada viola validação| validacao["Impedir atualização inválida; conferir recusa e encerrar variante"]
    p4["Consultar os valores atualizados"]
    p4 --> q4{"Etapa produziu o resultado esperado?"}
    q4 -->|Não ou não comprovado| f4["PENDÊNCIA: resposta à falha de consulta e recuperação"]
    f4 --> parar
    q4 -->|Sim| p5
    p5["Solicitar e confirmar exclusão sem histórico ou vínculos impeditivos"]
    p5 --> q5{"Etapa produziu o resultado esperado?"}
    q5 -->|Não ou não comprovado| f5["Informar falha sem anunciar exclusão concluída - a validar"]
    f5 --> parar
    q5 -->|Sim| p6
    p6["Conferir remoção pelo meio acordado"]
    p6 --> q6{"Etapa produziu o resultado esperado?"}
    q6 -->|Não ou não comprovado| f6["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f6 --> parar
    q6 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5,f6 pendencia
```

### UCS002 — Manter marcas

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS002_manter_marcas.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia; observar pendências de cada etapa"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; não declarar aceite de regras pendentes"]
    inicio --> p1
    p1["Criar fabricante com documento válido"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["PENDÊNCIA: resposta à falha técnica de inclusão não definida"]
    f1 --> parar
    q1 -->|Sim| p2
    p1 -->|Obrigatório ausente| obrig["Recusar inclusão e indicar campos faltantes"]
    p1 -->|Nome duplicado| dup["Recusar duplicidade e emitir alerta"]
    obrig --> negativo["AVALIAÇÃO: conferir recusa; encerrar variante negativa sem avançar com cadastro inexistente"]
    dup --> negativo
    p2["Consultar fabricante e contatos"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["Distinguir falha de consulta vazia - a validar; recuperação pendente"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Atualizar nome do mesmo fabricante"]
    p3 --> q3{"Etapa produziu o resultado esperado?"}
    q3 -->|Não ou não comprovado| f3["PENDÊNCIA: resposta à falha técnica de edição não definida"]
    f3 --> parar
    q3 -->|Sim| p4
    p3 -->|Entrada viola validação| validacao["Impedir atualização inválida; conferir recusa e encerrar variante"]
    p4["Consultar os valores atualizados"]
    p4 --> q4{"Etapa produziu o resultado esperado?"}
    q4 -->|Não ou não comprovado| f4["Distinguir falha de consulta vazia - a validar; recuperação pendente"]
    f4 --> parar
    q4 -->|Sim| p5
    p5["Preparar vínculo e cancelar uma exclusão"]
    p5 --> q5{"Etapa produziu o resultado esperado?"}
    q5 -->|Não ou não comprovado| f5["Se alteração ocorrer apesar do cancelamento: divergência; recuperação pendente"]
    f5 --> parar
    q5 -->|Sim| p6
    p6["Confirmar exclusão com vínculo"]
    p6 --> q6{"Etapa produziu o resultado esperado?"}
    q6 -->|Não ou não comprovado| f6["Informar falha sem anunciar exclusão concluída - a validar"]
    f6 --> parar
    q6 -->|Sim| p7
    p7["Conferir inativação e vínculos preservados"]
    p7 --> q7{"Etapa produziu o resultado esperado?"}
    q7 -->|Não ou não comprovado| f7["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f7 --> parar
    q7 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5,f6,f7 pendencia
```

### UCS003 — Manter inversor com validação de unicidade e histórico

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS003_crud_variacao.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia; observar pendências de cada etapa"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; não declarar aceite de regras pendentes"]
    inicio --> p1
    p1["Criar inversor com série inédita"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["Informar falha sem confirmar inclusão - a validar"]
    f1 --> parar
    q1 -->|Sim| p2
    p1 -->|Obrigatório ausente| obrig["Recusar inclusão e indicar campos faltantes"]
    p1 -->|Série duplicado| dup["Recusar duplicidade e emitir alerta"]
    obrig --> negativo["AVALIAÇÃO: conferir recusa; encerrar variante negativa sem avançar com cadastro inexistente"]
    dup --> negativo
    p2["Tentar série repetida: recusar duplicidade"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Consultar cadastro aceito"]
    p3 --> q3{"Etapa produziu o resultado esperado?"}
    q3 -->|Não ou não comprovado| f3["PENDÊNCIA: resposta à falha de consulta e recuperação"]
    f3 --> parar
    q3 -->|Sim| p4
    p4["Atualizar potência preservando a série"]
    p4 --> q4{"Etapa produziu o resultado esperado?"}
    q4 -->|Não ou não comprovado| f4["Apresentar motivo da falha sem confirmar edição - a validar"]
    f4 --> parar
    q4 -->|Sim| p5
    p4 -->|Entrada viola validação| validacao["Impedir atualização inválida; conferir recusa e encerrar variante"]
    p5["Preparar histórico no mesmo inversor, sem painéis vinculados"]
    p5 --> q5{"Etapa produziu o resultado esperado?"}
    q5 -->|Não ou não comprovado| f5["PENDÊNCIA: não há decisão ou condição suficiente para esta etapa"]
    f5 --> parar
    q5 -->|Sim| p6
    p6["Solicitar e confirmar exclusão"]
    p6 --> q6{"Etapa produziu o resultado esperado?"}
    q6 -->|Não ou não comprovado| f6["Informar falha sem anunciar exclusão concluída - a validar"]
    f6 --> parar
    q6 -->|Sim| p7
    p7["Conferir inativação e histórico preservado"]
    p7 --> q7{"Etapa produziu o resultado esperado?"}
    q7 -->|Não ou não comprovado| f7["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f7 --> parar
    q7 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5,f6,f7 pendencia
```

### UCS004 — Manter fabricante com validação de contato e cancelamento

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS004_crud_variacao.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia; observar pendências de cada etapa"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; não declarar aceite de regras pendentes"]
    inicio --> p1
    p1["Criar fabricante"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["PENDÊNCIA: resposta à falha técnica de inclusão não definida"]
    f1 --> parar
    q1 -->|Sim| p2
    p1 -->|Obrigatório ausente| obrig["Recusar inclusão e indicar campos faltantes"]
    p1 -->|Nome duplicado| dup["Recusar duplicidade e emitir alerta"]
    obrig --> negativo["AVALIAÇÃO: conferir recusa; encerrar variante negativa sem avançar com cadastro inexistente"]
    dup --> negativo
    p2["Consultar identificação e contato"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["Distinguir falha de consulta vazia - a validar; recuperação pendente"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Tentar e-mail inválido: expectativa de recusa a validar"]
    p3 --> q3{"Etapa produziu o resultado esperado?"}
    q3 -->|Não ou não comprovado| f3["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f3 --> parar
    q3 -->|Sim| p4
    p4["Corrigir e cancelar edição: expectativa a validar"]
    p4 --> q4{"Etapa produziu o resultado esperado?"}
    q4 -->|Não ou não comprovado| f4["Se alteração ocorrer apesar do cancelamento: divergência; recuperação pendente"]
    f4 --> parar
    q4 -->|Sim| p5
    p5["Reabrir e confirmar edição válida"]
    p5 --> q5{"Etapa produziu o resultado esperado?"}
    q5 -->|Não ou não comprovado| f5["PENDÊNCIA: resposta à falha técnica de edição não definida"]
    f5 --> parar
    q5 -->|Sim| p6
    p6["Cancelar exclusão e conferir preservação"]
    p6 --> q6{"Etapa produziu o resultado esperado?"}
    q6 -->|Não ou não comprovado| f6["Se alteração ocorrer apesar do cancelamento: divergência; recuperação pendente"]
    f6 --> parar
    q6 -->|Sim| p7
    p7["Confirmar exclusão com vínculo"]
    p7 --> q7{"Etapa produziu o resultado esperado?"}
    q7 -->|Não ou não comprovado| f7["Informar falha sem anunciar exclusão concluída - a validar"]
    f7 --> parar
    q7 -->|Sim| p8
    p8["Conferir inativação e referências preservadas"]
    p8 --> q8{"Etapa produziu o resultado esperado?"}
    q8 -->|Não ou não comprovado| f8["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f8 --> parar
    q8 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5,f6,f7,f8 pendencia
```

### UCS005 — Exportar consulta filtrada de inversores em todos os formatos

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS005_exportacao_1.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia; observar pendências de cada etapa"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; não declarar aceite de regras pendentes"]
    inicio --> p1
    p1["Filtrar 23 alvos e excluir 3 controles fictícios"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["PENDÊNCIA: resposta à falha de consulta e recuperação"]
    f1 --> parar
    q1 -->|Sim| p2
    p2["Conciliar formatos: PDF e Excel versus PDF e CSV"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["PENDÊNCIA: não há decisão ou condição suficiente para esta etapa"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Solicitar formato e conferir entrega"]
    p3 --> q3{"Etapa produziu o resultado esperado?"}
    q3 -->|Não ou não comprovado| f3["Informar falha; não entregar erro como relatório - a validar"]
    f3 --> parar
    q3 -->|Sim| p4
    p4["Conferir conjunto completo em páginas diferentes"]
    p4 --> q4{"Etapa produziu o resultado esperado?"}
    q4 -->|Não ou não comprovado| f4["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f4 --> parar
    q4 -->|Sim| p5
    p5["Comparar ordenação e colunas especificadas"]
    p5 --> q5{"Etapa produziu o resultado esperado?"}
    q5 -->|Não ou não comprovado| f5["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f5 --> parar
    q5 -->|Sim| p6
    p6["Manter avaliação de campos indefinidos bloqueada"]
    p6 --> q6{"Etapa produziu o resultado esperado?"}
    q6 -->|Não ou não comprovado| f6["PENDÊNCIA: não há decisão ou condição suficiente para esta etapa"]
    f6 --> parar
    q6 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5,f6 pendencia
```

### UCS006 — Exportar ficha individual de inversores

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS006_exportacao_2.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia; observar pendências de cada etapa"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; não declarar aceite de regras pendentes"]
    inicio --> p1
    p1["Selecionar o inversor alvo"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f1 --> parar
    q1 -->|Sim| p2
    p2["Solicitar ficha PDF individual"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["Informar falha; não entregar erro como relatório - a validar"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Conferir entrega e identidade do alvo"]
    p3 --> q3{"Etapa produziu o resultado esperado?"}
    q3 -->|Não ou não comprovado| f3["Informar falha; não entregar erro como relatório - a validar"]
    f3 --> parar
    q3 -->|Sim| p4
    p4["Na variante indisponível, conferir resposta prevista"]
    p4 --> q4{"Etapa produziu o resultado esperado?"}
    q4 -->|Não ou não comprovado| f4["Se não informar indisponibilidade ou entregar outro registro: divergência"]
    f4 --> parar
    q4 -->|Sim| p5
    p5["Manter campos e autorização pendentes bloqueados"]
    p5 --> q5{"Etapa produziu o resultado esperado?"}
    q5 -->|Não ou não comprovado| f5["PENDÊNCIA: não há decisão ou condição suficiente para esta etapa"]
    f5 --> parar
    q5 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5 pendencia
```

### UCS007 — Tratar autorização e falha de exportação de inversores

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS007_exportacao_3.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia; observar pendências de cada etapa"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; não declarar aceite de regras pendentes"]
    inicio --> p1
    p1["Definir matriz de autorização por modalidade"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["PENDÊNCIA: não há decisão ou condição suficiente para esta etapa"]
    f1 --> parar
    q1 -->|Sim| p2
    p2["Após validação, solicitar exportação com perfil autorizado"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["Informar falha; não entregar erro como relatório - a validar"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Conferir indicação de preparação proposta"]
    p3 --> q3{"Etapa produziu o resultado esperado?"}
    q3 -->|Não ou não comprovado| f3["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f3 --> parar
    q3 -->|Sim| p4
    p4["Avaliar falha controlada na exportação coletiva"]
    p4 --> q4{"Etapa produziu o resultado esperado?"}
    q4 -->|Não ou não comprovado| f4["Falha não informada ou erro entregue como relatório: divergência da proposta"]
    f4 --> parar
    q4 -->|Sim| p5
    p5["Avaliar falha controlada na ficha individual"]
    p5 --> q5{"Etapa produziu o resultado esperado?"}
    q5 -->|Não ou não comprovado| f5["Falha não informada ou erro entregue como relatório: divergência da proposta"]
    f5 --> parar
    q5 -->|Sim| p6
    p6["Registrar observações sem presumir política de retomada"]
    p6 --> q6{"Etapa produziu o resultado esperado?"}
    q6 -->|Não ou não comprovado| f6["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f6 --> parar
    q6 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5,f6 pendencia
```

### UCS008 — Exportar consulta filtrada de fabricantes em todos os formatos

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS008_exportacao_1.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia; observar pendências de cada etapa"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; não declarar aceite de regras pendentes"]
    inicio --> p1
    p1["Filtrar 23 fabricantes e excluir 3 controles fictícios"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["Distinguir falha de consulta vazia - a validar; recuperação pendente"]
    f1 --> parar
    q1 -->|Sim| p2
    p2["Solicitar PDF e CSV previstos na revisão"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["Informar falha; não entregar erro como relatório - a validar"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Conferir entrega proposta"]
    p3 --> q3{"Etapa produziu o resultado esperado?"}
    q3 -->|Não ou não comprovado| f3["Informar falha; não entregar erro como relatório - a validar"]
    f3 --> parar
    q3 -->|Sim| p4
    p4["Conferir conjunto completo em páginas diferentes"]
    p4 --> q4{"Etapa produziu o resultado esperado?"}
    q4 -->|Não ou não comprovado| f4["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f4 --> parar
    q4 -->|Sim| p5
    p5["Comparar ordenação e colunas após validação"]
    p5 --> q5{"Etapa produziu o resultado esperado?"}
    q5 -->|Não ou não comprovado| f5["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f5 --> parar
    q5 -->|Sim| p6
    p6["Manter campos indefinidos bloqueados"]
    p6 --> q6{"Etapa produziu o resultado esperado?"}
    q6 -->|Não ou não comprovado| f6["PENDÊNCIA: não há decisão ou condição suficiente para esta etapa"]
    f6 --> parar
    q6 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5,f6 pendencia
```

### UCS009 — Exportar ficha individual de fabricantes

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS009_exportacao_2.md)

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
    p6["Manter campos e autorização pendentes bloqueados"]
    p6 --> q6{"Etapa produziu o resultado esperado?"}
    q6 -->|Não ou não comprovado| f6["PENDÊNCIA: não há decisão ou condição suficiente para esta etapa"]
    f6 --> parar
    q6 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5,f6 pendencia
```

### UCS010 — Tratar autorização e falha de exportação de fabricantes

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS010_exportacao_3.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia; observar pendências de cada etapa"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; não declarar aceite de regras pendentes"]
    inicio --> p1
    p1["Definir matriz de autorização por modalidade"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["PENDÊNCIA: não há decisão ou condição suficiente para esta etapa"]
    f1 --> parar
    q1 -->|Sim| p2
    p2["Após validação, solicitar exportação com perfil autorizado"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["Informar falha; não entregar erro como relatório - a validar"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Conferir indicação de preparação proposta"]
    p3 --> q3{"Etapa produziu o resultado esperado?"}
    q3 -->|Não ou não comprovado| f3["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f3 --> parar
    q3 -->|Sim| p4
    p4["Avaliar falha controlada na exportação coletiva"]
    p4 --> q4{"Etapa produziu o resultado esperado?"}
    q4 -->|Não ou não comprovado| f4["Falha não informada ou erro entregue como relatório: divergência da proposta"]
    f4 --> parar
    q4 -->|Sim| p5
    p5["Avaliar falha controlada na ficha individual"]
    p5 --> q5{"Etapa produziu o resultado esperado?"}
    q5 -->|Não ou não comprovado| f5["Falha não informada ou erro entregue como relatório: divergência da proposta"]
    f5 --> parar
    q5 -->|Sim| p6
    p6["Registrar observações sem presumir política de retomada"]
    p6 --> q6{"Etapa produziu o resultado esperado?"}
    q6 -->|Não ou não comprovado| f6["Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes"]
    f6 --> parar
    q6 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2,f3,f4,f5,f6 pendencia
```

### UCS011 — Recusar edição e exclusão por acesso direto sem permissão

[Ver descrição completa, respostas às falhas e pendências](docs/fluxos/UCS011_acesso_direto_sem_permissao.md)

```mermaid
flowchart TD
    inicio["Preparar massa fictícia com o Perfil A e registrar valores iniciais"]
    parar["AVALIAÇÃO: registrar resultado e interromper etapas dependentes desta execução"]
    concluir["Registrar resultado do percurso; recusas conferidas pelo dado inalterado"]
    inicio --> p1
    p1["Anotar endereço e solicitação de edição e exclusão usados pela interface"]
    p1 --> q1{"Etapa produziu o resultado esperado?"}
    q1 -->|Não ou não comprovado| f1["Sem meio de reproduzir a solicitação: etapas 3 a 6 bloqueadas nesta execução"]
    f1 --> parar
    q1 -->|Sim| p2
    p2["Perfil L abre consulta e detalhe dos dois registros"]
    p2 --> q2{"Etapa produziu o resultado esperado?"}
    q2 -->|Não ou não comprovado| f2["Perfil L sem consulta: rever preparação dos perfis antes de avaliar recusas"]
    f2 --> parar
    q2 -->|Sim| p3
    p3["Perfil L grava edição do inversor por acesso direto"]
    p3 --> q3{"Recusada e potência inalterada?"}
    q3 -->|Não| d3["DEFEITO: gravação aceita sem autorização de edição"]
    d3 --> parar
    q3 -->|Sim| p4
    p4["Perfil L envia exclusão do inversor por acesso direto"]
    p4 --> q4{"Recusada e inversor preservado?"}
    q4 -->|Não| d4["DEFEITO: exclusão aceita ou anunciada fora do perfil Administrador/Gerente"]
    d4 --> parar
    q4 -->|Sim| p5
    p5["Perfil L grava edição da marca por acesso direto"]
    p5 --> q5{"Recusada e nome inalterado?"}
    q5 -->|Não| d5["DEFEITO: gravação aceita sem autorização de edição"]
    d5 --> parar
    q5 -->|Sim| p6
    p6["Perfil E envia exclusão da marca por acesso direto"]
    p6 --> q6{"Recusada e marca Ativa?"}
    q6 -->|Não| d6["DEFEITO: permissão de edição tratada como permissão de exclusão"]
    d6 --> parar
    q6 -->|Sim| p7
    p7["Perfil A confere os dois registros contra os valores iniciais"]
    p7 --> q7{"Valores iguais aos iniciais?"}
    q7 -->|Não| d7["DEFEITO: alteração gravada apesar da recusa; registrar evidência"]
    d7 --> parar
    q7 -->|Sim| concluir
    classDef pendencia fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef defeito fill:#ffebe9,stroke:#cf222e,color:#24292f
    classDef avaliacao fill:#e7f1ff,stroke:#0969da,color:#24292f
    class parar,concluir avaliacao
    class f1,f2 pendencia
    class d3,d4,d5,d6,d7 defeito
```
