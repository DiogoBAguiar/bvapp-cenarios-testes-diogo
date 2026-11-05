"""
UCS001 — Manter inversores

Autoria / responsável acadêmico: Diogo Bruno Ferreira Martins de Aguiar
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Data: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Revisão-base: 838d6ec05d26f6364e920e865d4abff59088dd34
Grupo de requisitos: Gestão de Inversores (a numeração da fonte é preservada).

OBJETIVO
Descrever o ciclo completo de criar, consultar, atualizar e excluir inversores,
sem dividir as quatro operações em quatro cenários contados separadamente.

REQUISITOS RELACIONADOS
Features 2.1.1.1 Inclusão, 2.1.1.2 Consulta,
2.1.1.3 Atualização/Edição e 2.1.1.4 Exclusão, no grupo acima.
CAs exercitados: CA-2.1.1.1.01, CA-2.1.1.1.02, CA-2.1.1.1.03, CA-2.1.1.1.04, CA-2.1.1.1.07, CA-2.1.1.1.10, CA-2.1.1.1.12, CA-2.1.1.1.17, CA-2.1.1.2.01, CA-2.1.1.2.08, CA-2.1.1.3.02, CA-2.1.1.3.04, CA-2.1.1.3.14, CA-2.1.1.4.01, CA-2.1.1.4.02, CA-2.1.1.4.03, CA-2.1.1.4.04, CA-2.1.1.4.06, CA-2.1.1.4.07.

ATOR
Usuário autenticado com autorização de inclusão, listagem, visualização e edição; na exclusão, Administrador ou Gerente conforme a fonte. A equivalência dos perfis permanece pendente.

PRÉ-CONDIÇÕES
- Ambiente futuro de estudo isolado, sem dados de produção ou ações reais nesta entrega.
- Massa sintética e vínculos preparados antes do fluxo; nenhum registro de controle é alterado.
- A autorização é verificada por operação, não inferida do acesso à listagem.
- Tratar as decisões em aberto abaixo antes de aprovar as etapas dependentes.

DADOS DE TESTE
Número de Série INV-ESTUDO-001; Marca Marca Estudo A; Modelo Modelo Estudo A pertencente à Marca; Fornecedor Fornecedor Estudo A; Usina Usina Estudo A; Operadora Operadora Estudo A; Potência Nominal 5 kW; Instalação 01/10/2026; Situação Ativo. Todos os vínculos são referências sintéticas previamente cadastradas e ativas. Garantia de instalação: valor e unidade dependem da pendência indicada abaixo; não usar um número arbitrário como regra aprovada.
Os nomes e valores são fictícios e servem apenas de exemplo de entrada. Não constituem
novos limites, domínios, permissões ou regras de negócio.

[FP] FLUXO PRINCIPAL — CRUD COMPLETO
1. CRIAR. Preencher os dados obrigatórios, selecionar o Modelo da Marca e a Usina/Operadora existentes. Resolver a garantia de instalação antes de concluir a configuração da massa. Salvar uma vez. Esperado: o inversor é criado e aparece a mensagem «Inversor cadastrado com sucesso e vinculado à Operadora e Localização selecionadas».
2. CONSULTAR. Buscar INV-ESTUDO-001 na consulta, abrir a linha correspondente e confrontar série, marca, modelo, potência, instalação e situação com os dados cadastrados.
3. ATUALIZAR. Abrir a edição do mesmo inversor, conferir que a série não pode ser alterada e mudar a potência de 5 para 6 kW. Salvar e reabrir a consulta. Esperado: a mesma identificação exibe 6 kW e a mensagem «Dados do inversor atualizados com sucesso».
4. CONSULTAR APÓS ATUALIZAÇÃO. Reabrir a consulta e verificar a mesma identificação,
   os valores alterados e a preservação dos demais valores do cadastro.
5. EXCLUIR. Usar a variante sem painéis vinculados, sem histórico de geração/manutenção e sem associações impeditivas. Solicitar exclusão; conferir série e marca na confirmação; confirmar. Esperado: remoção definitiva do registro, não apenas troca de situação, e mensagem «Inversor removido/inativado com sucesso». A demonstração de remoção definitiva precisa de meio observável acordado; ausência na lista isoladamente não a prova.
6. CONSULTAR APÓS EXCLUSÃO. Conferir o resultado específico exigido no passo 5:
   remoção, inativação com vínculos preservados ou etapa bloqueada. Não usar ausência
   na listagem como prova suficiente de eliminação física.

[A] FLUXOS ALTERNATIVOS
1. Painel vinculado. Preparar variante com painel associado e solicitar exclusão. Esperado: recusa, informação do impedimento e inversor preservado. Referência: CA-2.1.1.4.02.
2. Histórico existente. Sem painel associado, mas com histórico de geração/manutenção: a operação de exclusão deve inativar e preservar o histórico, em vez de remover definitivamente. Referência: CA-2.1.1.4.03.
3. Série repetida. Tentar cadastrar uma segunda referência com INV-ESTUDO-001. Esperado: impedir duplicidade e informar o problema; não criar outro inversor. Referência: CA-2.1.1.1.04.

[A-COM] CONCORRÊNCIA E INTERRUPÇÃO
Se outra pessoa alterar o cadastro durante o fluxo, ou ocorrer perda de resposta,
registrar o ponto interrompido e a dúvida. Não escolher prevalência, prazo, repetição
automática ou recuperação que não esteja definida. Os resultados dessas variantes
permanecem pendentes de especificação; não são cenários aprovados.

REGRAS DE NEGÓCIO E ORÁCULO
- Os resultados dos passos vêm dos CAs relacionados, não da resposta atual do sistema.
- O cadastro em uma operação não concede autorização para as operações seguintes.
- Cancelamento e bloqueio não devem ser descritos como conclusão bem-sucedida.
- O comportamento específico de exclusão do grupo não é generalizado a outro grupo.

RESULTADOS ESPERADOS E REGISTRO FUTURO
- Comparar entrada, consulta inicial, consulta após edição e resultado da exclusão.
- Em futura execução, anotar versão, data, massa, passo, esperado, observado e evidência.
- Nesta entrega: nenhum resultado observado; nenhum teste executado; sem homologação.
- Se uma pendência impedir decidir entre aceitar e recusar, marcar BLOQUEADO,
  identificar a decisão necessária e não converter o caso em sucesso.

PENDÊNCIAS PARA STAKEHOLDERS
Unidade da garantia e conciliação da garantia de instalação obrigatória; equivalência dos perfis Administrador/Gerente; identificação de histórico; forma de comprovar remoção definitiva; concorrência e perda de resposta. O fluxo CRUD está descrito por completo, mas as etapas que dependem dessas definições não recebem aprovação presumida.
"""
