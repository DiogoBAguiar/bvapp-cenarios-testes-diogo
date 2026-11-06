# UCS002 — Manter marcas

[Índice de fluxos](../fluxos.md) · [README](../../README.md) · [Cenário original](../../functional_tests/ativos/marcas/UCS002_manter_marcas.py)

O diagrama resume o fluxo principal e as variantes indicadas. Antes de cada etapa, conferir seus bloqueios; o ramo “Sim” é condicional e não declara que já houve validação. Os fluxos alternativos e os resultados completos estão descritos abaixo.

## Fluxo visual

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

## Especificação completa

Autoria / responsável acadêmico: Diogo Bruno Ferreira Martins de Aguiar
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Revisão documental: 06/11/2026. Criação: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Revisão-base: 5f3072939bb7ce5f90b64bf0faa5483bbb0d3260
Grupo de requisitos: Cadastro de Marcas (Fabricantes) (a numeração da fonte é preservada).


### OBJETIVO

Descrever o ciclo completo de criar, consultar, atualizar e excluir marcas,
sem dividir as quatro operações em quatro cenários contados separadamente.


### REQUISITOS RELACIONADOS

Features do OpenProject: #24272 (Inclusão), #24273 (Consulta), #24275 (Atualização) e #24278 (Exclusão).
Referências locais da consolidação (não são IDs do OpenProject): CA-2.1.4.1.1.01, CA-2.1.4.1.1.02, CA-2.1.4.1.1.03, CA-2.1.4.1.1.05, CA-2.1.4.1.1.06, CA-2.1.4.1.1.11, CA-2.1.4.1.2.01, CA-2.1.4.1.2.04, CA-2.1.4.1.2.09, CA-2.1.4.1.3.02, CA-2.1.4.1.3.03, CA-2.1.4.1.3.04, CA-2.1.4.1.3.05, CA-2.1.4.1.3.11, CA-2.1.4.1.4.01, CA-2.1.4.1.4.02, CA-2.1.4.1.4.03, CA-2.1.4.1.4.04, CA-2.1.4.1.4.07.


### SITUAÇÃO DAS REGRAS E BLOQUEIOS

FP1: formato de ID internacional continua indefinido. O domínio Ativo/Inativo já consta do CA #24553; não é uma regra ausente. FP2: detalhes de contatos e texto “Não informado” são acréscimos a validar. FP3 e alternativas: validação de e-mail e cancelamento foram detalhados na revisão, sem evidência de aceite dos stakeholders. A1: #24556 proíbe nomes duplicados; estender a registros excluídos depende de validação. Autorizações: #24571 exige permissão de cadastro, #24584 restringe consulta, #24594 exige edição e #24595 reserva exclusão a Administradores; a matriz e a separação listagem/detalhe não estão definidas. Sem vínculos, a US #24600 já exige exclusão física; falta acordar como comprová-la, não decidir se a regra existe.
Resultados de acréscimos a validar são expectativas propostas. Não aprovar essas etapas antes da decisão registrada dos stakeholders. IDs globais e rótulos locais são distinguidos em docs/matriz-rastreabilidade.md.


### ATOR

Usuário com autorização para adicionar fabricantes, listar, visualizar e editar marcas; administrador para remover marcas.


### PRÉ-CONDIÇÕES

- Ambiente futuro de estudo isolado, sem dados de produção ou ações reais nesta entrega.
- Massa sintética e vínculos preparados antes do fluxo; nenhum registro de controle é alterado.
- A autorização é verificada por operação, não inferida do acesso à listagem.
- Tratar as decisões em aberto abaixo antes de aprovar as etapas dependentes.


### DADOS DE TESTE

Nome Marca Estudo A; tipo de identificação internacional; ID Internacional ID-ESTUDO-A (formato depende de definição da fonte); Situação Ativo (CA #24553); e-mail suporte@example.invalid; site e telefone vazios. Nenhum CNPJ real é usado. Para exclusão com vínculos, preparar Modelo Estudo A associado à marca após a edição.
Os nomes e valores são fictícios e servem apenas de exemplo de entrada. Não constituem
novos limites, domínios, permissões ou regras de negócio.


### [FP] FLUXO PRINCIPAL — CRUD COMPLETO

1. CRIAR. Preencher nome, documento e situação. O formato do documento internacional deve ser confirmado antes de concluir a massa; Ativo/Inativo constam do CA #24553. Manter site e telefone opcionais em branco; salvar. Esperado: «Marca cadastrada com sucesso», cadastro disponível e auditoria de inclusão.
2. CONSULTAR. Buscar Marca Estudo A pelo nome; abrir o detalhe correto e conferir nome e e-mail. Proposta pendente de validação: contatos não informados aparecem como Não informado, sem transformar ausência em dado real.
3. ATUALIZAR. Editar a mesma marca e mudar seu nome para Marca Estudo A Revisada, mantendo o e-mail. Salvar. Esperado: identificação preservada, novo nome na consulta e «Marca atualizada com sucesso», com registro anterior/posterior na auditoria.
4. CONSULTAR APÓS ATUALIZAÇÃO. Reabrir a consulta e verificar a mesma identificação,
   os valores alterados e a preservação dos demais valores do cadastro.
5. EXCLUIR. Preparar modelo ou equipamento vinculado à marca. Como administrador, solicitar remoção, conferir o nome na confirmação e cancelar uma vez. Repetir e confirmar. Esperado: marca torna-se Inativa e continua identificável nos cadastros que a utilizam; os vínculos não são apagados. A operação de excluir desta variante é lógica, como exige a regra; não afirmar remoção definitiva.
6. CONSULTAR APÓS EXCLUSÃO. Conferir o resultado específico exigido no passo 5:
   remoção, inativação com vínculos preservados ou etapa bloqueada. Não usar ausência
   na listagem como prova suficiente de eliminação física.


### [A] FLUXOS ALTERNATIVOS

1. Nome já usado. Tentar nova marca com nome já cadastrado. Esperado: não criar duplicidade. A variante com cadastro anterior excluído fica BLOQUEADA até validação da extensão dessa regra. Referência: CA-2.1.4.1.1.06.
2. E-mail inválido. Informar um e-mail de suporte sem formato válido na edição e salvar. Esperado: recusa da atualização. O texto exato da mensagem não é inventado. Referência: CA-2.1.4.1.3.05.
3. Cancelar edição. Alterar nome e cancelar. Esperado: a alteração digitada não é confirmada. Referência: CA-2.1.4.1.3.04.


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

Formato e validação de identificação internacional, meio de comprovar a exclusão física sem vínculos exigida pela US #24600, recuperação após timeout e apresentação amigável de limites. Não omitir documento/situação só porque contatos são opcionais.
