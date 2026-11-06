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
5. Preparar a [apresentação de cinco minutos](docs/roteiro-apresentacao.md).

Os cenários foram preparados com assistência de IA a partir dos requisitos identificados.
A revisão pessoal, a validação das decisões de negócio e a apresentação ainda não são
declaradas realizadas. A atribuição de responsabilidade acadêmica não comprova execução.

O pacote não contém código do produto, arquivos privados de origem, dados reais de
usuários ou credenciais. A leitura dos cenários é autossuficiente para a avaliação.

## Revisão dos requisitos — 06/11/2026

Os dez cenários foram revisados contra a base `5f3072939bb7ce5f90b64bf0faa5483bbb0d3260`. Exportações agora referenciam as Features #35875 (inversores) e #35912 (fabricantes). Veja a [matriz com IDs](docs/matriz-rastreabilidade.md) e as [pendências por cenário](docs/pendencias.md). Etapas com regra pendente ficam bloqueadas para aceite; o conflito Excel/CSV não foi resolvido por suposição. Este pacote contém documentação, sem execução de testes ou entrega no Classroom.
