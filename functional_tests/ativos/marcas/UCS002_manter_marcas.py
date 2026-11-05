"""
UCS002 — Manter marcas

Autoria / responsável acadêmico: Diogo Bruno Ferreira Martins de Aguiar
Preparação: assistência de IA; revisão pessoal e apresentação pelo responsável pendentes.
Data: 05/11/2026
Natureza: especificação documental, não teste automatizado nem evidência de execução.
Revisão-base: 838d6ec05d26f6364e920e865d4abff59088dd34
Grupo de requisitos: Cadastro de Marcas (Fabricantes) (a numeração da fonte é preservada).

OBJETIVO
Descrever o ciclo completo de criar, consultar, atualizar e excluir marcas,
sem dividir as quatro operações em quatro cenários contados separadamente.

REQUISITOS RELACIONADOS
Features 2.1.4.1.1 Inclusão, 2.1.4.1.2 Consulta,
2.1.4.1.3 Atualização/Edição e 2.1.4.1.4 Exclusão, no grupo acima.
CAs exercitados: CA-2.1.4.1.1.01, CA-2.1.4.1.1.02, CA-2.1.4.1.1.03, CA-2.1.4.1.1.05, CA-2.1.4.1.1.06, CA-2.1.4.1.1.11, CA-2.1.4.1.2.01, CA-2.1.4.1.2.04, CA-2.1.4.1.2.09, CA-2.1.4.1.3.02, CA-2.1.4.1.3.03, CA-2.1.4.1.3.04, CA-2.1.4.1.3.05, CA-2.1.4.1.3.11, CA-2.1.4.1.4.01, CA-2.1.4.1.4.02, CA-2.1.4.1.4.03, CA-2.1.4.1.4.04, CA-2.1.4.1.4.07.

ATOR
Usuário com autorização para adicionar fabricantes, listar, visualizar e editar marcas; administrador para remover marcas.

PRÉ-CONDIÇÕES
- Ambiente futuro de estudo isolado, sem dados de produção ou ações reais nesta entrega.
- Massa sintética e vínculos preparados antes do fluxo; nenhum registro de controle é alterado.
- A autorização é verificada por operação, não inferida do acesso à listagem.
- Tratar as decisões em aberto abaixo antes de aprovar as etapas dependentes.

DADOS DE TESTE
Nome Marca Estudo A; tipo de identificação internacional; ID Internacional ID-ESTUDO-A (formato depende de definição da fonte); Situação Ativa, após confirmar domínio; e-mail suporte@example.invalid; site e telefone vazios. Nenhum CNPJ real é usado. Para exclusão com vínculos, preparar Modelo Estudo A associado à marca após a edição.
Os nomes e valores são fictícios e servem apenas de exemplo de entrada. Não constituem
novos limites, domínios, permissões ou regras de negócio.

[FP] FLUXO PRINCIPAL — CRUD COMPLETO
1. CRIAR. Preencher nome, documento e situação. O domínio de documento/situação deve ser confirmado antes de concluir a massa. Manter site e telefone opcionais em branco; salvar. Esperado: «Marca cadastrada com sucesso», cadastro disponível e auditoria de inclusão.
2. CONSULTAR. Buscar Marca Estudo A pelo nome; abrir o detalhe correto e conferir nome e e-mail. Contatos não informados devem aparecer como Não informado, sem transformar ausência em dado real.
3. ATUALIZAR. Editar a mesma marca e mudar seu nome para Marca Estudo A Revisada, mantendo o e-mail. Salvar. Esperado: identificação preservada, novo nome na consulta e «Marca atualizada com sucesso», com registro anterior/posterior na auditoria.
4. CONSULTAR APÓS ATUALIZAÇÃO. Reabrir a consulta e verificar a mesma identificação,
   os valores alterados e a preservação dos demais valores do cadastro.
5. EXCLUIR. Preparar modelo ou equipamento vinculado à marca. Como administrador, solicitar remoção, conferir o nome na confirmação e cancelar uma vez. Repetir e confirmar. Esperado: marca torna-se Inativa e continua identificável nos cadastros que a utilizam; os vínculos não são apagados. A operação de excluir desta variante é lógica, como exige a regra; não afirmar remoção definitiva.
6. CONSULTAR APÓS EXCLUSÃO. Conferir o resultado específico exigido no passo 5:
   remoção, inativação com vínculos preservados ou etapa bloqueada. Não usar ausência
   na listagem como prova suficiente de eliminação física.

[A] FLUXOS ALTERNATIVOS
1. Nome já usado. Tentar nova marca com nome já cadastrado. Esperado: não criar duplicidade, inclusive quando o registro anterior estiver excluído. Referência: CA-2.1.4.1.1.06.
2. E-mail inválido. Informar um e-mail de suporte sem formato válido na edição e salvar. Esperado: recusa da atualização. O texto exato da mensagem não é inventado. Referência: CA-2.1.4.1.3.05.
3. Cancelar edição. Alterar nome e cancelar. Esperado: a alteração digitada não é confirmada. Referência: CA-2.1.4.1.3.04.

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
Formato e validação de identificação internacional, domínio de situação, tratamento de marca sem vínculos na exclusão, recuperação após timeout e apresentação amigável de limites. Não omitir documento/situação só porque contatos são opcionais.
"""
