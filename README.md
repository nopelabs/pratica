# Prática diária no Hermes Agent

Uma skill para manter uma rotina curta de estudo no terminal. No começo de cada sessão, o Hermes pergunta se você quer fazer a prática do dia, por exemplo "Quer fazer os 10 min de Git agora?". Se você aceitar, ele monta uma leitura curta a partir de fontes oficiais e um exercício pequeno para você digitar.

Você pode ter várias trilhas ao mesmo tempo (Git, Python, Laravel...), cada uma com sua duração e prioridade. O Hermes oferece a de maior prioridade que ainda não foi feita no dia.

## Como funciona

- `pratica/SKILL.md`: o método, igual para qualquer tema.
- `pratica/references/<tema>.md`: o roteiro de cada tema, com as fontes. Hoje existe `git.md`.
- `pratica/templates/trilha.md`: o modelo de uma trilha.
- As suas trilhas ficam fora da skill, em `~/Developer/_trilhas/<tema>/trilha.md`. Cada uma diz a duração (`minutos`), a prioridade (1 é a mais alta; 0 pausa a trilha) e guarda o registro das sessões.

## Instalação

Você precisa de macOS ou Linux com o Hermes Agent instalado.

1. Nesta página, clique em **Code → Download ZIP** e descompacte o arquivo. Dentro da pasta `pratica-main` há outra pasta chamada `pratica`. É essa pasta interna que você vai instalar.
2. Copie a pasta `pratica` para `~/.hermes/skills/` (ou para uma subpasta de categoria, como `~/.hermes/skills/productivity/`). Para um perfil com nome, use `~/.hermes/profiles/NOME-DO-PERFIL/skills/`.
3. Peça ao Hermes para guardar este gatilho na memória, com estas palavras:

   > Guarde na memória: "Usuário tem prática diária (skill pratica). No início de sessões no terminal, ofereça a trilha de maior prioridade ainda não feita hoje."

   O gatilho precisa ficar na memória porque uma skill só é lida quando o assunto aparece; a memória é lida em toda sessão. Não ponha duração nem tema no gatilho: eles ficam no `trilha.md`, para existir uma fonte só.
4. Abra uma nova conversa e peça: "Crie uma trilha de Git de 10 minutos, prioridade 1."

## Personalizar

- Outra pasta para as trilhas: mude a linha "Pasta das trilhas" em `pratica/SKILL.md`. O padrão `~/Developer/_trilhas/` segue a organização do autor, em que o `_` marca pastas de dados.
- Nova duração ou prioridade: edite a linha correspondente no `trilha.md` da trilha.
- Novo tema: peça ao Hermes uma trilha nova. Se não houver roteiro para o tema, ele propõe um com fontes oficiais antes de gravar.

## Sobre os arquivos

Tudo é texto. A skill não roda scripts e não acessa a internet sozinha. Ela só lê as suas trilhas e acrescenta uma linha de registro ao fim de cada sessão aceita.
