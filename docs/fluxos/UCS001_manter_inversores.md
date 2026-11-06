# UCS001 — Manter inversores

[Índice de fluxos](../fluxos.md) · [README](../../README.md) · [Cenário original](../../functional_tests/ativos/inversores/UCS001_manter_inversores.py)

Os losangos representam a avaliação da etapa no cenário, não novos controles da interface. **Falha esperada e corretamente tratada pode atender ao cenário negativo.** Uma falha inesperada interrompe apenas as etapas dependentes desta execução. Essa interrupção é uma orientação de teste, não uma regra do sistema. Não há repetição automática, rollback, preservação de campos ou retomada presumidos. Os acréscimos marcados **a validar** continuam sujeitos ao aceite dos stakeholders.

## Fluxo visual

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

## Falhas, recusas e pendências por etapa

As referências CAxx abaixo são rótulos dentro da Feature indicada, não IDs globais novos. Uma mensagem de falha não comprova que nenhuma gravação ocorreu; em perda de resposta, o estado final permanece a verificar.

| Etapa ou variante | Resposta prevista ou pendência | Base |
| --- | --- | --- |
| 1. Criar inversor com dados obrigatórios | Informar falha sem confirmar inclusão - a validar. Não continuar etapas dependentes. | #24233 CA15, acréscimo a validar |
| Inclusão recusada por entrada inválida | Não concluir inclusão; indicar campos obrigatórios faltantes ou alertar duplicidade. Recusa correta é resultado esperado da variante negativa. | #24403 e #24416 |
| 2. Consultar o mesmo inversor | PENDÊNCIA: resposta à falha de consulta e recuperação. Não continuar etapas dependentes. | Consolidação de Consulta: tratamento detalhado e recuperação pendentes |
| 3. Atualizar potência preservando a série | Apresentar motivo da falha sem confirmar edição - a validar. Não continuar etapas dependentes. | #24253 CA12, acréscimo a validar |
| Atualização recusada por validação | Não confirmar a gravação inválida; não inferir preservação dos campos digitados ou política de nova tentativa. | #24462: obrigatoriedade e potência positiva |
| 4. Consultar os valores atualizados | PENDÊNCIA: resposta à falha de consulta e recuperação. Não continuar etapas dependentes. | Consolidação de Consulta: tratamento detalhado e recuperação pendentes |
| 5. Solicitar e confirmar exclusão sem histórico ou vínculos impeditivos | Informar falha sem anunciar exclusão concluída - a validar. Não continuar etapas dependentes. | #24254 CA09, acréscimo a validar |
| 6. Conferir remoção pelo meio acordado | Registrar divergência ou impossibilidade de conferir; correção e retomada pendentes. Não continuar etapas dependentes. | Resultados esperados do cenário; não há resposta automática definida para divergência constatada pelo avaliador |

## Especificação completa

Autoria / responsável acadêmico: Diogo Bruno Ferreira Martins de Aguiar
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Revisão documental: 06/11/2026. Criação: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Revisão-base: 5f3072939bb7ce5f90b64bf0faa5483bbb0d3260
Grupo de requisitos: Gestão de Inversores (a numeração da fonte é preservada).


### OBJETIVO

Descrever o ciclo completo de criar, consultar, atualizar e excluir inversores,
sem dividir as quatro operações em quatro cenários contados separadamente.


### REQUISITOS RELACIONADOS

Features do OpenProject: #24233 (Inclusão), #24249 (Consulta), #24253 (Atualização) e #24254 (Exclusão).
Referências locais da consolidação (não são IDs do OpenProject): CA-2.1.1.1.01, CA-2.1.1.1.02, CA-2.1.1.1.03, CA-2.1.1.1.04, CA-2.1.1.1.07, CA-2.1.1.1.10, CA-2.1.1.1.12, CA-2.1.1.1.17, CA-2.1.1.2.01, CA-2.1.1.2.08, CA-2.1.1.3.02, CA-2.1.1.3.04, CA-2.1.1.3.14, CA-2.1.1.4.01, CA-2.1.1.4.02, CA-2.1.1.4.03, CA-2.1.1.4.04, CA-2.1.1.4.06, CA-2.1.1.4.07.


### SITUAÇÃO DAS REGRAS E BLOQUEIOS

Autorização: #24431 exige usuário logado e autorizado; #24439 restringe a consulta e #24473 exige Administrador/Gerente na exclusão. A matriz por operação e a separação entre listagem e detalhe permanecem pendentes. FP1: unidade/obrigatoriedade da garantia e condições dos vínculos precisam de validação. A1: bloqueio por painel vinculado é acréscimo levantado no sistema; sua aprovação e a precedência diante de histórico permanecem pendentes. #24416 define série única entre inversores; ampliar para outros tipos ou excluídos exige validação. FP2: campos adicionais do detalhe também dependem da validação dos acréscimos. Os demais resultados originais continuam rastreados, sem alegar homologação.
Resultados de acréscimos a validar são expectativas propostas. Não aprovar essas etapas antes da decisão registrada dos stakeholders. IDs globais e rótulos locais são distinguidos em docs/matriz-rastreabilidade.md.


### ATOR

Usuário autenticado com autorização de inclusão, listagem, visualização e edição; na exclusão, Administrador ou Gerente conforme a fonte. A equivalência dos perfis permanece pendente.


### PRÉ-CONDIÇÕES

- Ambiente futuro de estudo isolado, sem dados de produção ou ações reais nesta entrega.
- Massa sintética e vínculos preparados antes do fluxo; nenhum registro de controle é alterado.
- A autorização é verificada por operação, não inferida do acesso à listagem.
- Tratar as decisões em aberto abaixo antes de aprovar as etapas dependentes.


### DADOS DE TESTE

Número de Série INV-ESTUDO-001; Marca Marca Estudo A; Modelo Modelo Estudo A pertencente à Marca; Fornecedor Fornecedor Estudo A; Usina Usina Estudo A; Operadora Operadora Estudo A; Potência Nominal 5 kW; Instalação 01/10/2026; Situação Ativo. Todos os vínculos são referências sintéticas previamente cadastradas e ativas. Garantia de instalação: valor e unidade dependem da pendência indicada abaixo; não usar um número arbitrário como regra aprovada.
Os nomes e valores são fictícios e servem apenas de exemplo de entrada. Não constituem
novos limites, domínios, permissões ou regras de negócio.


### [FP] FLUXO PRINCIPAL — CRUD COMPLETO

1. CRIAR. Preencher os dados obrigatórios, selecionar o Modelo da Marca e a Usina/Operadora existentes. Resolver a garantia de instalação antes de concluir a configuração da massa. Salvar uma vez. Esperado: o inversor é criado e aparece a mensagem «Inversor cadastrado com sucesso e vinculado à Operadora e Localização selecionadas».
2. CONSULTAR. Buscar INV-ESTUDO-001 na consulta, abrir a linha correspondente e confrontar série, marca, modelo, potência, instalação e situação com os dados cadastrados.
3. ATUALIZAR. Abrir a edição do mesmo inversor, conferir que a série não pode ser alterada e mudar a potência de 5 para 6 kW. Salvar e reabrir a consulta. Esperado: a mesma identificação exibe 6 kW e a mensagem «Dados do inversor atualizados com sucesso».
4. CONSULTAR APÓS ATUALIZAÇÃO. Reabrir a consulta e verificar a mesma identificação,
   os valores alterados e a preservação dos demais valores do cadastro.
5. EXCLUIR. Usar a variante sem painéis vinculados, sem histórico de geração/manutenção e sem associações impeditivas. Solicitar exclusão; conferir série e marca na confirmação; confirmar. Esperado: remoção definitiva do registro, não apenas troca de situação, e mensagem «Inversor removido/inativado com sucesso». A demonstração de remoção definitiva precisa de meio observável acordado; ausência na lista isoladamente não a prova.
6. CONSULTAR APÓS EXCLUSÃO. Conferir o resultado específico exigido no passo 5:
   remoção, inativação com vínculos preservados ou etapa bloqueada. Não usar ausência
   na listagem como prova suficiente de eliminação física.


### [A] FLUXOS ALTERNATIVOS

1. Painel vinculado. Preparar variante com painel associado e solicitar exclusão. Esperado: recusa, informação do impedimento e inversor preservado. Referência: CA-2.1.1.4.02.
2. Histórico existente. Sem painel associado, mas com histórico de geração/manutenção: a operação de exclusão deve inativar e preservar o histórico, em vez de remover definitivamente. Referência: CA-2.1.1.4.03.
3. Série repetida. Tentar cadastrar uma segunda referência com INV-ESTUDO-001. Esperado: impedir duplicidade e informar o problema; não criar outro inversor. Referência: CA-2.1.1.1.04.


### [A-COM] CONCORRÊNCIA E INTERRUPÇÃO

Se outra pessoa alterar o cadastro durante o fluxo, ou ocorrer perda de resposta,
registrar o ponto interrompido e a dúvida. Não escolher prevalência, prazo, repetição
automática ou recuperação que não esteja definida. Os resultados dessas variantes
permanecem pendentes de especificação; não são cenários aprovados.


### REGRAS DE NEGÓCIO E ORÁCULO

- Os resultados originais vêm dos CAs relacionados; os acréscimos estão explicitamente sujeitos à validação indicada acima.
- O cadastro em uma operação não concede autorização para as operações seguintes.
- Cancelamento e bloqueio não devem ser descritos como conclusão bem-sucedida.
- O comportamento específico de exclusão do grupo não é generalizado a outro grupo.


### RESULTADOS ESPERADOS E REGISTRO FUTURO

- Comparar entrada, consulta inicial, consulta após edição e resultado da exclusão.
- Em futura execução, anotar versão, data, massa, passo, esperado, observado e evidência.
- Nesta entrega: nenhum resultado observado; nenhum teste executado; sem homologação.
- Se uma pendência impedir decidir entre aceitar e recusar, marcar BLOQUEADO,
  identificar a decisão necessária e não converter o caso em sucesso.


### PENDÊNCIAS PARA STAKEHOLDERS

Unidade da garantia e conciliação da garantia de instalação obrigatória; equivalência dos perfis Administrador/Gerente; identificação de histórico; forma de comprovar remoção definitiva; concorrência e perda de resposta. O fluxo CRUD está descrito por completo, mas as etapas que dependem dessas definições não recebem aprovação presumida.
