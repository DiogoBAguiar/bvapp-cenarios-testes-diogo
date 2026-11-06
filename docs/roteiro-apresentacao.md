# Roteiro de apresentação — cinco minutos

Este é um roteiro para ensaio, não declaração de apresentação já realizada.

| Tempo | Conteúdo e ação |
| --- | --- |
| 0:00–0:40 | Apresentar o objetivo do mini projeto e os 10 cenários; esclarecer que a entrega é documental. |
| 0:40–1:10 | Mostrar `functional_tests/ativos/`, o agrupamento e a matriz de rastreabilidade. |
| 1:10–2:50 | Abrir UCS003 — Manter inversor com validação de unicidade e histórico. Explicar pré-condições, massa fictícia, inclusão, consulta, edição e exclusão no mesmo cenário. |
| 2:50–3:40 | Explicar o inversor com histórico: a exclusão resulta em inativação e preservação do histórico; o resultado vem do CA, não de uma implementação presumida. |
| 3:40–4:30 | Mostrar uma pendência: definição da unidade da garantia e do meio de consulta do histórico. Explicar por que uma etapa bloqueada não recebe aprovação. |
| 4:30–5:00 | Mostrar como os arquivos poderão ser reutilizados futuramente e encerrar reiterando que não houve execução de testes. |

Antes da apresentação, Diogo deve ler os arquivos, confirmar o recorte com o grupo,
verificar as referências e ensaiar com cronômetro. Não memorizar uma afirmação de
funcionamento que esta atividade não demonstrou.

## Pontos para a apresentação após a revisão

Explicar os IDs #35875 e #35912 e a diferença entre ID global e rótulo de CA. Mostrar uma etapa bloqueada por autorização ainda indefinida e o conflito de formatos #24449 versus CA01 de #35875. Destacar que #24600 já prevê exclusão física de fabricante sem vínculos. Não apresentar publicação no backlog como aceite dos stakeholders, nem documentação como teste executado.
