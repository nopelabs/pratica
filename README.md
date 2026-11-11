# Prática diária no Hermes Agent

Uma skill para manter uma rotina curta de estudo no terminal. No começo de cada sessão, o Hermes pergunta se você quer fazer a prática do dia, por exemplo "Quer fazer os 10 min de Git agora?". Se você aceitar, ele monta uma leitura curta a partir de material local (um livro EPUB e os manuais do terminal) e um exercício pequeno para você digitar. Quando você disser que terminou, ele registra a lição e o tempo gasto.

Você pode ter várias trilhas ao mesmo tempo (Git, Python, Laravel...), cada uma com sua duração e prioridade. O Hermes oferece a trilha de prioridade 1 primeiro, entre as que ainda não foram feitas no dia. Para continuar de onde parou, a qualquer hora, peça "vamos continuar".

## Como funciona

- `pratica/SKILL.md`: o método, igual para qualquer tema.
- `pratica/references/<tema>.md`: o roteiro de cada tema, com as fontes. Hoje existe `git.md`.
- `pratica/templates/trilha.md`: o modelo de uma trilha.
- `pratica/scripts/secao-epub.py`: lê uma seção de um livro EPUB pelo título do sumário. Só lê; usa apenas o Python padrão.
- As suas trilhas ficam fora da skill, em `~/Developer/_trilhas/<tema>/trilha.md`:

      # Trilha

      tema: git
      minutos: 10
      prioridade: 1
      roteiro: git.md
      material: ~/dox/progit.epub

      ## Registro
      - 2026-11-11: lição 1, Repositório e primeiro commit (feita, 9 min)

  `minutos` é a duração de cada sessão; `prioridade` 1 vem primeiro, e 0 pausa a trilha; `material` é opcional.

## Instalação

Você precisa de macOS ou Linux, Python 3 e o Hermes Agent instalado.

1. Nesta página, clique em **Code → Download ZIP** e descompacte o arquivo. Dentro da pasta `pratica-main` há outra pasta chamada `pratica`. É essa pasta interna que você vai instalar.
2. Copie a pasta `pratica` para `~/.hermes/skills/` (ou para uma subpasta de categoria, como `~/.hermes/skills/productivity/`). Para um perfil com nome, use `~/.hermes/profiles/NOME-DO-PERFIL/skills/`.
3. Peça ao Hermes para guardar este gatilho na memória, com estas palavras:

   > Guarde na memória: "Usuário tem prática diária (skill pratica). No início de sessões no terminal, ofereça a trilha de maior prioridade ainda não feita hoje."

   O gatilho precisa ficar na memória porque uma skill só é lida quando o assunto aparece; a memória é lida em toda sessão. Não ponha duração nem tema no gatilho: eles ficam no `trilha.md`, para existir uma fonte só.
4. Para a trilha de Git, baixe o EPUB do Pro Git em português em https://git-scm.com/book/pt-br/v2 e guarde-o onde preferir.
5. Abra uma nova conversa e peça: "Crie uma trilha de Git de 10 minutos, prioridade 1, com o material em CAMINHO-DO-EPUB."

## Personalizar

- Outra pasta para as trilhas: mude a linha "Pasta das trilhas" em `pratica/SKILL.md`. O padrão `~/Developer/_trilhas/` segue a organização do autor, em que o `_` marca pastas de dados.
- Nova duração, prioridade ou material: edite a linha correspondente no `trilha.md` da trilha.
- Novo tema: peça ao Hermes uma trilha nova. Se não houver roteiro para o tema, ele propõe um com fontes oficiais antes de gravar.

## Sobre os arquivos

Tudo é texto, mais um script que só lê. A skill não acessa a internet: a leitura vem do livro local e dos manuais do terminal. Ela lê as suas trilhas e só acrescenta linhas de registro ao fim de cada sessão aceita; não faz commits.
