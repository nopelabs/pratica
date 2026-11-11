---
name: pratica
description: "Use when offering or running a daily practice session."
version: 1.1.0
author: Alexandre
license: MIT
platforms: [macos, linux]
metadata:
  hermes:
    tags: [prática, estudo, rotina, terminal]
---

# Prática diária

Sessões curtas de estudo no terminal, uma trilha por tema: leitura breve feita a partir de material local e um exercício pequeno. O método é este arquivo; o conteúdo de cada tema fica em `references/<tema>.md`; as trilhas ativas do usuário ficam fora da skill, numa pasta dele.

## When to Use

- No início de uma sessão no terminal, quando a memória disser que o usuário tem prática diária.
- Quando o usuário pedir para praticar, continuar de onde parou, criar, pausar ou ajustar uma trilha.
- Não use em sessões de mensageria (WhatsApp, Telegram etc.) nem no meio de outra tarefa.

## Onde ficam as trilhas

Pasta das trilhas: `~/Developer/_trilhas/`. Para usar outra pasta, mude só esta linha.

Cada trilha é uma pasta `<tema>/` com um `trilha.md` no formato de `templates/trilha.md`:

- `tema`: nome curto, igual ao da pasta.
- `minutos`: duração de cada sessão.
- `prioridade`: número inteiro; 1 vem primeiro, depois 2, 3...; 0 pausa a trilha.
- `roteiro`: arquivo em `references/` desta skill.
- `material`: opcional; caminho de um livro EPUB local que o roteiro cita (ex.: `~/dox/progit.epub`).
- `## Registro`: uma linha por lição, `- AAAA-MM-DD: lição N, título (feita, M min)` ou `(parcial, M min)`. Sem tempo medido, omita `, M min`.

O `trilha.md` é a única fonte de duração e prioridade. Não as repita na memória nem em outro arquivo: a cópia fica errada quando o usuário muda a trilha.

## 1. Oferecer

1. Confira a data local (`date +%F`).
2. Leia todos os `<pasta das trilhas>/*/trilha.md`. Ignore os de prioridade 0. Uma trilha conta como feita hoje se o Registro tem qualquer linha com a data de hoje, `feita` ou `parcial`.
3. Uma trilha sem `minutos` ou `prioridade` numéricos, ou cujo `roteiro` não existe em `references/`, não é oferecida: avise em uma linha qual arquivo está com problema.
4. Entre as não feitas hoje, escolha a de prioridade 1 primeiro (o menor número). Empate: ordem alfabética do tema. Pergunte em uma linha: `Quer fazer os <minutos> min de <Tema> agora?`. Se houver outras pendentes hoje, acrescente `(mais N trilhas hoje)`.
5. Se não houver trilha pendente, a pasta não existir ou estiver vazia, não ofereça nada.
6. Ofereça uma vez por sessão. Se o usuário recusar ou pedir outra coisa, atenda o pedido sem insistir.

O usuário pode pedir uma sessão a qualquer momento ("vamos continuar", "mais uma"), mesmo de uma trilha já feita hoje: monte a próxima lição normalmente. A regra de "feita hoje" vale só para a oferta automática.

## 2. Montar a sessão

1. Ao começar, anote a hora (`date +%H:%M`); ela serve para medir o tempo, sem perguntar nada ao usuário.
2. Abra o roteiro indicado na trilha. A próxima lição é a primeira sem linha `feita` no Registro; se a última linha for `parcial`, retome essa lição do ponto em que parou.
3. Divida o tempo: cerca de 70% de leitura e 30% de exercício (10 min = 7 + 3; 20 = 14 + 6; 30 = 21 + 9). Se a lição couber em menos tempo, puxe a seguinte; se não couber, divida-a e registre `parcial`.
4. Leitura: escreva em português, em texto simples (o terminal não renderiza Markdown), a partir de material lido nesta sessão:
   - Se a trilha tem `material` e o arquivo existe, leia as seções que a lição cita com `python3 <skill_dir>/scripts/secao-epub.py <material> "<título>"` (`--lista` mostra os títulos).
   - Leia também os manuais citados (`git help ...` ou equivalente do tema), com `| col -b` para tirar a formatação.
   - Sem material legível, use só os manuais. Nunca cite como fonte algo que não leu nesta sessão.
   Termine indicando onde se aprofundar (seção do livro ou comando). Não mande o usuário para vídeos nem para fora do terminal.
5. Termos e comandos: use os comandos exatamente como são; na primeira vez que um termo técnico aparecer, explique-o em português simples e dê o nome usado pelo livro (ex.: stage, que o Pro Git chama de área de preparação). Não invente traduções.
6. Exercício: tarefas pequenas, numeradas, para o usuário digitar na pasta da trilha. É prática dele: não rode os comandos por ele. Quando ele disser que terminou, confira com comandos só de leitura e comente o resultado em poucas linhas.
7. Siga o ritmo do usuário: se ele fizer perguntas, responda; o tempo é referência, não cronômetro.

## 3. Registrar

1. Quando o usuário disser que terminou (ou encerrar no meio), anote a hora de novo e calcule os minutos desde o início.
2. Aceitar a sessão autoriza apenas acrescentar linhas de Registro ao `trilha.md`; qualquer outra mudança nos arquivos da trilha precisa de permissão.
3. Acrescente uma linha por lição trabalhada, ao fim do Registro, sem editar linhas anteriores. Duas lições na mesma sessão: duas linhas, cada uma com o seu tempo (a segunda começa quando a primeira termina).
4. Não faça commit do registro. Se a pasta da trilha for um repositório, o `trilha.md` modificado fica para o usuário commitar, o que também é prática.
5. Se o roteiro acabou, avise e proponha o próximo passo (outro roteiro, revisão ou pausar a trilha).

## Criar, ajustar ou pausar uma trilha

- Criar: confirme tema, minutos e prioridade (e o material, se houver); crie `<pasta das trilhas>/<tema>/trilha.md` a partir do template. Se não existir `references/<tema>.md`, monte o roteiro com fontes oficiais e verificáveis (documentação e manuais do próprio projeto, de preferência disponíveis no terminal), mostre-o e só grave com permissão.
- Ajustar ou pausar: mude a linha `minutos`, `prioridade` (0 pausa) ou `material` com permissão. Não renomeie pastas por causa de duração ou prioridade.

## Pitfalls

- Pôr duração ou tema no gatilho da memória cria uma segunda fonte que fica desatualizada. O gatilho só aponta para esta skill.
- Rodar o exercício pelo usuário tira dele a prática, que é o objetivo.
- Material antigo ensina comandos substituídos: prefira a forma atual e cite a antiga só como equivalência (ex.: `git switch` e `git restore` em vez de `git checkout` para essas funções).
- Trilha que pratica uma ferramenta de versionamento (ex.: Git) usa a própria pasta da trilha como área de treino. Não transforme a pasta das trilhas inteira num repositório: repositórios aninhados confundem os exercícios.
- Não use repositórios ou projetos reais do usuário como área de exercício; para observar um caso real, use só comandos de leitura.
- O livro do `material` é do usuário: só leia, nunca mova nem copie para dentro da skill (a licença e o tamanho não cabem num repositório público).

## Verification

Depois de uma sessão, `git diff -- trilha.md` (ou a comparação com o conteúdo anterior, se a pasta não for repositório) mostra só linhas novas de Registro com a data de hoje e o tempo. Uma nova sessão no terminal, no mesmo dia, não oferece de novo essa trilha.
