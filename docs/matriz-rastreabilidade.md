# Matriz de rastreabilidade

Cobertura selecionada, sem alegação de cobertura total ou execução. Base revisada: `5f3072939bb7ce5f90b64bf0faa5483bbb0d3260`.

## IDs do backlog e critérios revisados

`#` identifica item do OpenProject. CA01, CA02 etc. são rótulos dentro da Feature indicada, nunca IDs globais. Os rótulos de novos CAs abaixo provêm dos textos revisados; os IDs globais desses novos CAs não estão informados nesses textos. Não foram inventados nem confundidos com a numeração local.

| Cenários | Features | Critérios e histórias com ID original | Acréscimos relevantes e pendências |
| --- | --- | --- | --- |
| UCS001, UCS003 | #24233 Inclusão; #24249 Consulta; #24253 Atualização; #24254 Exclusão de inversores | Inclusão: #24401 campos, #24411 modelo da marca, #24412 potência, #24416 série única, #24418 sucesso; Consulta: #24439 autorização, #24441 campos; Atualização: #24460 formulário, #24461 série imutável, #24462 validações, #24463 sucesso, #24465 auditoria; Exclusão: #24473 perfis, #24474 confirmação, #24475 histórico, #24476 sem histórico/associações, #24477 sucesso, #24478 auditoria. US #24431 cadastro autorizado e #25893 detalhe. | #24233 CA11–CA13: extensões de unicidade, datas/garantias e vínculos; #24249 CA12: detalhe; #24254 CA07: painéis vinculados. Aprovação e conflitos pendentes. |
| UCS002, UCS004 | #24272 Inclusão; #24273 Consulta; #24275 Atualização; #24278 Exclusão de Fabricante | Inclusão: #24541 campos, #24542 opcionais, #24545 obrigatoriedade, #24553 Ativo/Inativo, #24556 unicidade, #24558 sucesso, #24560 auditoria; Consulta: #24584 autorização, #24585 campos; Atualização: #24590 formulário, #24591 validações, #24592 sucesso, #24593 auditoria; Exclusão: #24595 Administradores, #24596 confirmação, #24597 vínculos, #24598 mensagem da exclusão física, #24599 auditoria. US #24600 exclusão física/lógica; #25896 detalhe; #24571 e #24594 autorização de inclusão/edição. | #24272 CA09: unicidade incluindo excluídos; #24273 CA12: contatos no detalhe; #24275 CA05/CA06: cancelamento/e-mail. Acréscimos a validar. |
| UCS005 | #35875 Exportação de inversores; #24249 Consulta | CA #24449 exige PDF/Excel; #24445 ordenação, #24446 paginação, #24447 filtros; US #24457 | #35875 CA01–CA03/CA07: PDF/CSV, conjunto, colunas e entrega. Conflito Excel/CSV e aprovação dos acréscimos pendentes. |
| UCS006 | #35875 Exportação de inversores | US relacionada #24457 não substitui o ID da Feature | CA01/CA04/CA07: PDF individual, identidade/indisponibilidade, entrega. Validação e campos completos pendentes. |
| UCS007 | #35875 Exportação de inversores | US relacionada #24457 | CA05/CA06: andamento/falha. A matriz de autorização não consta desses CAs; FP1 bloqueado para definição. |
| UCS008 | #35912 Exportação de fabricantes; #24273 Consulta | #24586 paginação/ordem, #24587 filtros; US relacionada #25954 | #35912 CA04–CA06/CA09: formatos, conjunto, busca e ordem. Colunas CSV e aviso de download não constam desses nove CAs; confirmar a especificação. |
| UCS009 | #35912 Exportação de fabricantes | US relacionada #25954 | CA02/CA04/CA07/CA08: indisponibilidade, PDF, identidade e ativos associados. Validar acréscimos, campos e aviso de download. |
| UCS010 | #35912 Exportação de fabricantes | US relacionada #25954 | CA01/CA03: falha/andamento. Matriz de autorização não definida; FP1 bloqueado. |
| UCS011 | #24249 Consulta, #24253 Atualização e #24254 Exclusão de inversores; #24275 Atualização e #24278 Exclusão de Fabricante | Inversores: #24439 listar não autoriza editar/excluir, #24473 exclusão por Administrador/Gerente; US #29059 alteração de status. Fabricantes: US #24594 edição, #24595 exclusão por Administradores | Sem acréscimos: recusas vêm dos critérios originais. Forma da recusa e equivalência Administrador/Gerente pendentes. |

A existência de ID não equivale a aceite. As condições de bloqueio estão em cada cenário e em [pendências](pendencias.md).

## Referências locais preservadas

A tabela abaixo permite localizar as consolidações que deram origem aos cenários. `CA-2.1.x` não é ID do OpenProject e não substitui a tabela acima. Não há correspondência automática entre o sufixo local e o rótulo CA do backlog.

| Cenário | Grupo | Referências | Tipo |
| --- | --- | --- | --- |
| [UCS001](../functional_tests/ativos/inversores/UCS001_manter_inversores.py) | Gestão de Inversores | CA-2.1.1.1.01; CA-2.1.1.1.02; CA-2.1.1.1.03; CA-2.1.1.1.04; CA-2.1.1.1.07; CA-2.1.1.1.10; CA-2.1.1.1.12; CA-2.1.1.1.17; CA-2.1.1.2.01; CA-2.1.1.2.08; CA-2.1.1.3.02; CA-2.1.1.3.04; CA-2.1.1.3.14; CA-2.1.1.4.01; CA-2.1.1.4.02; CA-2.1.1.4.03; CA-2.1.1.4.04; CA-2.1.1.4.06; CA-2.1.1.4.07 | CRUD completo |
| [UCS002](../functional_tests/ativos/marcas/UCS002_manter_marcas.py) | Cadastro de Marcas (Fabricantes) | CA-2.1.4.1.1.01; CA-2.1.4.1.1.02; CA-2.1.4.1.1.03; CA-2.1.4.1.1.05; CA-2.1.4.1.1.06; CA-2.1.4.1.1.11; CA-2.1.4.1.2.01; CA-2.1.4.1.2.04; CA-2.1.4.1.2.09; CA-2.1.4.1.3.02; CA-2.1.4.1.3.03; CA-2.1.4.1.3.04; CA-2.1.4.1.3.05; CA-2.1.4.1.3.11; CA-2.1.4.1.4.01; CA-2.1.4.1.4.02; CA-2.1.4.1.4.03; CA-2.1.4.1.4.04; CA-2.1.4.1.4.07 | CRUD completo |
| [UCS003](../functional_tests/ativos/inversores/UCS003_crud_variacao.py) | Gestão de Inversores | CA-2.1.1.1.01; CA-2.1.1.1.02; CA-2.1.1.1.03; CA-2.1.1.1.04; CA-2.1.1.1.07; CA-2.1.1.1.10; CA-2.1.1.1.12; CA-2.1.1.1.17; CA-2.1.1.2.01; CA-2.1.1.2.08; CA-2.1.1.3.02; CA-2.1.1.3.04; CA-2.1.1.3.14; CA-2.1.1.4.01; CA-2.1.1.4.02; CA-2.1.1.4.03; CA-2.1.1.4.04; CA-2.1.1.4.06; CA-2.1.1.4.07 | CRUD completo |
| [UCS004](../functional_tests/ativos/marcas/UCS004_crud_variacao.py) | Cadastro de Marcas (Fabricantes) | CA-2.1.4.1.1.01; CA-2.1.4.1.1.02; CA-2.1.4.1.1.03; CA-2.1.4.1.1.05; CA-2.1.4.1.1.06; CA-2.1.4.1.1.11; CA-2.1.4.1.2.01; CA-2.1.4.1.2.04; CA-2.1.4.1.2.09; CA-2.1.4.1.3.02; CA-2.1.4.1.3.03; CA-2.1.4.1.3.04; CA-2.1.4.1.3.05; CA-2.1.4.1.3.11; CA-2.1.4.1.4.01; CA-2.1.4.1.4.02; CA-2.1.4.1.4.03; CA-2.1.4.1.4.04; CA-2.1.4.1.4.07 | CRUD completo |
| [UCS005](../functional_tests/ativos/inversores/UCS005_exportacao_1.py) | Gestão de Inversores | Formatos de exportação; Resultado completo da consulta; Filtros da exportação; Dados do arquivo; Entrega do arquivo; Ordenação | Exportação |
| [UCS006](../functional_tests/ativos/inversores/UCS006_exportacao_2.py) | Gestão de Inversores | Arquivo individual; Registro individual indisponível; Entrega do arquivo | Exportação |
| [UCS007](../functional_tests/ativos/inversores/UCS007_exportacao_3.py) | Gestão de Inversores | Autorização; Falha na obtenção do arquivo; Exportação em andamento | Exportação |
| [UCS008](../functional_tests/ativos/marcas/UCS008_exportacao_1.py) | Cadastro de Marcas (Fabricantes) | Formatos de exportação; Resultado completo da consulta; Filtros da exportação; Dados do arquivo; Entrega do arquivo; Ordenação | Exportação |
| [UCS009](../functional_tests/ativos/marcas/UCS009_exportacao_2.py) | Cadastro de Marcas (Fabricantes) | Arquivo individual; Registro individual indisponível; Entrega do arquivo; Ativos da marca | Exportação |
| [UCS010](../functional_tests/ativos/marcas/UCS010_exportacao_3.py) | Cadastro de Marcas (Fabricantes) | Autorização; Falha na obtenção do arquivo; Exportação em andamento | Exportação |
| [UCS011](../functional_tests/ativos/UCS011_acesso_direto_sem_permissao.py) | Gestão de Inversores e Cadastro de Marcas (Fabricantes) | CA-2.1.1.2.01; CA-2.1.1.3.01; CA-2.1.1.4.01; CA-2.1.1.4.06; CA-2.1.4.1.3.01; CA-2.1.4.1.4.01 | Controle de acesso |
