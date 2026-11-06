# Pendências de validação

Revisão documental de 06/11/2026, base `5f3072939bb7ce5f90b64bf0faa5483bbb0d3260`. Nenhum cenário foi executado. Publicação no backlog não comprova aceite. Os números UCS identificam cenários, não requisitos.

## UCS001

Autorização: #24431 exige usuário logado e autorizado; #24439 restringe a consulta e #24473 exige Administrador/Gerente na exclusão. A matriz por operação e a separação entre listagem e detalhe permanecem pendentes. FP1: unidade/obrigatoriedade da garantia e condições dos vínculos precisam de validação. A1: bloqueio por painel vinculado é acréscimo levantado no sistema; sua aprovação e a precedência diante de histórico permanecem pendentes. #24416 define série única entre inversores; ampliar para outros tipos ou excluídos exige validação. FP2: campos adicionais do detalhe também dependem da validação dos acréscimos. Os demais resultados originais continuam rastreados, sem alegar homologação.

## UCS002

FP1: formato de ID internacional continua indefinido. O domínio Ativo/Inativo já consta do CA #24553; não é uma regra ausente. FP2: detalhes de contatos e texto “Não informado” são acréscimos a validar. FP3 e alternativas: validação de e-mail e cancelamento foram detalhados na revisão, sem evidência de aceite dos stakeholders. A1: #24556 proíbe nomes duplicados; estender a registros excluídos depende de validação. Autorizações: #24571 exige permissão de cadastro, #24584 restringe consulta, #24594 exige edição e #24595 reserva exclusão a Administradores; a matriz e a separação listagem/detalhe não estão definidas. Sem vínculos, a US #24600 já exige exclusão física; falta acordar como comprová-la, não decidir se a regra existe.

## UCS003

Aplicam-se as pendências de UCS001: garantias, elegibilidade dos vínculos e matriz de autorizações. A unicidade de série entre inversores tem origem no CA #24416; alcance a outros tipos e registros excluídos é acréscimo a validar. O fluxo com histórico usa #24475, mas depende da definição de quais registros caracterizam histórico e de sua preparação. A recusa por painéis vinculados é acréscimo a validar, inclusive a precedência quando também há histórico.

## UCS004

Aplicam-se as pendências de UCS002. FP2 e FP3: detalhe de contatos, validação de e-mail e cancelamento foram especificados na revisão, mas aguardam validação; as expectativas desses trechos são propostas, não um aceite presumido. #24553 já define Ativo/Inativo. #24600 já distingue exclusão física sem vínculos de inativação com vínculos; a prova da remoção física precisa ser acordada.

## UCS005

FP2 e A1: CONFLITO — CA #24449, em Consulta #24249, exige PDF e Excel; CA01 da nova Feature #35875 descreve PDF e CSV. Confirmar se Excel permanece exigido; CSV não é Excel e a nova descrição não comprova revogação do requisito original. FP3 a FP6: abrangência de todas as páginas, colunas CSV, entrega e ordenação constam dos acréscimos da exportação e aguardam validação. Filtros adicionais ao CA #24447 também precisam de validação. A autorização específica para exportar continua indefinida.

## UCS006

FP1 a FP5: PDF individual, identidade do registro, indisponibilidade e entrega constam dos acréscimos da Feature #35875, sem comprovação de validação dos stakeholders. Confirmar autorização da modalidade e campos completos do PDF. O conflito PDF/Excel versus PDF/CSV refere-se à exportação coletiva (UCS005); não resolve o contrato da ficha individual.

## UCS007

FP1 e A1: BLOQUEADOS até aprovação da matriz de autorização por modalidade. Ausência de consulta ou visualização não define sozinha a recusa da exportação. FP2 a FP4: andamento e falha constam dos novos CA05/CA06 da Feature #35875; expectativas propostas, pendentes de validação. FP5: retomada e tentativas continuam sem definição.

## UCS008

FP1 a FP6: PDF/CSV, abrangência, filtro e ordenação constam da nova Feature #35912 e aguardam validação dos acréscimos. As colunas CSV do levantamento não estão especificadas nos nove CAs dessa Feature: confirmar composição, sem inferir equivalência com a tabela ou com o PDF. Autorizações por modalidade, conjunto vazio e momento dos dados continuam pendentes.

## UCS009

FP1 a FP5: PDF individual, identidade, indisponibilidade e ativos associados constam dos novos CA02/CA04/CA07/CA08 da Feature #35912; aguardam validação dos stakeholders. FP2: confirmar indicação de download, que não está definida nesses nove CAs. Confirmar campos completos do PDF e autorização da modalidade; não presumir que identidade correta valida todo o conteúdo.

## UCS010

FP1 e A1: BLOQUEADOS até aprovação da matriz de autorização por modalidade. FP2 a FP4: andamento e falha constam dos novos CA03/CA01 da Feature #35912; expectativas propostas, pendentes de validação. FP5: recuperação e tentativas continuam indefinidas.

## Como encerrar uma pendência

Registrar a decisão, responsável pela validação, data e referência ao requisito atualizado. Até isso ocorrer, a etapa dependente permanece BLOQUEADA para aceite. Não escolher valores, mensagens, perfis ou política de recuperação. A autoria acadêmica permanece de Diogo; esta revisão não declara apresentação ou aprovação humana concluída.
