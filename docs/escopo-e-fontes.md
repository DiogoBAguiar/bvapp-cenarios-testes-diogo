# Escopo e fontes

## Autoridade e limites

O enunciado pede pelo menos dez cenários por estudante e reúne criar, consultar,
atualizar e excluir no mesmo cenário quando houver CRUD. Este pacote contém 10.
Os IDs UCS001 a UCS010 identificam somente cenários deste mini projeto: não são
novas Features, EPICs ou renumeração do BVAPP.

O recorte individual confirmado é Gestão de Inversores e Cadastro de Marcas
(Fabricantes). Os quatro cenários CRUD reúnem inclusão, consulta, atualização e
exclusão, variando os objetivos de manutenção normal, unicidade/histórico e
validação/cancelamento. Os seis cenários de relatório distinguem conjunto coletivo,
ficha individual e autorização/falha em cada grupo.

A preparação usou a revisão dos requisitos identificada por `838d6ec05d26f6364e920e865d4abff59088dd34`.
O hash fixa a versão consultada; os resumos funcionais e resultados necessários estão
nos próprios cenários, sem exigir acesso a repositório privado. Não se publicam aqui
os documentos de origem nem o código de implementação.

Os requisitos estavam organizados, mas continham decisões em aberto. Onde a regra
não permite determinar o resultado, o cenário registra BLOQUEADO e a dúvida; não
escolhe uma regra para fazer o fluxo parecer completo. A organização do cenário não
equivale a validação dos requisitos pelos stakeholders.

## Referências didáticas públicas

- [Aula 06 — Introdução ao TDD](https://maxwellamaral.github.io/aula-eng-testes/docs/06-introducao-tdd/).
- [Exemplo UCS001 — Manter produtos](https://raw.githubusercontent.com/maxwellamaral/maxwellamaral.github.io/refs/heads/main/specs/tests/products/UCS001-manter-produtos.py).
- [Estrutura de pastas da aula](https://maxwellamaral.github.io/aula-eng-testes/assets/images/06-introducao-tdd/estrutura-pastas.png).

A estrutura foi adaptada ao caráter documental desta entrega. Nenhum teste de TDD,
red/green, execução de software ou aprovação funcional é alegado.
