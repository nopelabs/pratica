---
name: pratica
description: "Use when offering or running a daily practice session."
version: 1.0.0
author: Alexandre
license: MIT
platforms: [macos, linux]
metadata:
  hermes:
    tags: [prática, estudo, rotina, git, terminal]
---

# Prática diária

Sessões curtas de estudo no terminal, uma trilha por tema: leitura breve feita a partir de fontes oficiais e um exercício pequeno. O método é este arquivo; o conteúdo de cada tema fica em `references/<tema>.md`; as trilhas ativas do usuário ficam fora da skill, numa pasta dele.

## When to Use

- No início de uma sessão no terminal, quando a memória disser que o usuário tem prática diária.
- Quando o usuário pedir para praticar, criar, pausar ou ajustar uma trilha.
- Não use em sessões de mensageria (WhatsApp, Telegram etc.) nem no meio de outra tarefa.

## Onde ficam as trilhas

Pasta das trilhas: `~/Developer/_trilhas/`. Para usar outra pasta, mude só esta linha.

Cada trilha é uma pasta `<tema>/` com um `trilha.md` no formato de `templates/trilha.md`:

- `tema`: nome curto, igual ao da pasta.
- `minutos`: duração de cada sessão.
- `prioridade`: 1 é a mais alta; 0 pausa a trilha.
- `roteiro`: arquivo em `references/` desta skill.
- `## Registro`: uma linha por sessão, `- AAAA-MM-DD: lição N, título (feita|parcial)`.

O `trilha.md` é a única fonte de duração e prioridade. Não as repita na memória nem em outro arquivo: a cópia fica errada quando o usuário muda a trilha.

## 1. Oferecer

1. Confira a data local (`date +%F`).
2. Leia todos os `<pasta das trilhas>/*/trilha.md`. Ignore os de prioridade 0. Uma trilha foi feita hoje se o Registro tem uma linha com a data de hoje.
3. Escolha a de menor número de prioridade entre as não feitas hoje e pergunte em uma linha: `Quer fazer os <minutos> min de <Tema> agora?`. Se houver outras pendentes hoje, acrescente `(mais N trilhas hoje)`.
4. Se não houver trilha pendente, a pasta não existir ou estiver vazia, não ofereça nada.
5. Ofereça uma vez por sessão. Se o usuário recusar ou pedir outra coisa, atenda o pedido sem insistir.

## 2. Montar a sessão

1. Abra o roteiro indicado na trilha. A próxima lição é a primeira cujo número não aparece no Registro como `feita`; uma `parcial` é retomada.
2. Divida o tempo: cerca de 70% de leitura e 30% de exercício (10 min = 7 + 3; 20 = 14 + 6; 30 = 21 + 9). Se a lição couber em menos tempo, puxe a seguinte; se não couber, divida-a e registre `parcial`.
3. Leitura: escreva em português, em texto simples (o terminal não renderiza Markdown), a partir das fontes que o roteiro cita. Termine indicando o comando ou a seção para se aprofundar. Não mande o usuário para vídeos nem para fora do terminal.
4. Exercício: tarefas pequenas, numeradas, para o usuário digitar na pasta da trilha. É prática dele: não rode os comandos por ele. Quando ele disser que terminou, confira com comandos só de leitura e comente o resultado em poucas linhas.
5. Siga o ritmo do usuário: se ele fizer perguntas, responda; o tempo é referência, não cronômetro.

## 3. Registrar

1. Aceitar a sessão autoriza apenas acrescentar a linha de Registro ao `trilha.md`; qualquer outra mudança nos arquivos da trilha precisa de permissão.
2. Acrescente a linha ao fim do Registro, sem editar linhas anteriores.
3. Se o roteiro acabou, avise e proponha o próximo passo (outro roteiro, revisão ou pausar a trilha).

## Criar, ajustar ou pausar uma trilha

- Criar: confirme tema, minutos e prioridade; crie `<pasta das trilhas>/<tema>/trilha.md` a partir do template. Se não existir `references/<tema>.md`, monte o roteiro com fontes oficiais e verificáveis (documentação e manuais do próprio projeto, de preferência disponíveis no terminal), mostre-o e só grave com permissão.
- Ajustar ou pausar: mude a linha `minutos` ou `prioridade` (0 pausa) com permissão. Não renomeie pastas por causa de duração ou prioridade.
- Duas trilhas com a mesma prioridade: pergunte qual vem antes.

## Pitfalls

- Pôr duração ou tema no gatilho da memória cria uma segunda fonte que fica desatualizada. O gatilho só aponta para esta skill.
- Rodar o exercício pelo usuário tira dele a prática, que é o objetivo.
- Roteiros com material antigo podem ensinar comandos substituídos: prefira a forma atual e cite a antiga só como equivalência (ex.: `git switch` e `git restore` em vez de `git checkout` para essas funções).
- Trilha que pratica uma ferramenta de versionamento (ex.: Git) usa a própria pasta da trilha como área de treino. Não transforme a pasta das trilhas inteira num repositório: repositórios aninhados confundem os exercícios.
- Não use repositórios ou projetos reais do usuário como área de exercício; para observar um caso real, use só comandos de leitura.

## Verification

Depois de uma sessão, o `trilha.md` tem uma linha nova com a data de hoje e nenhuma outra mudança (`git diff` na pasta, quando ela for um repositório). Uma nova sessão no terminal, no mesmo dia, não oferece de novo essa trilha.
