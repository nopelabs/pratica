# Roteiro: Git

Do zero ao uso diário, uma lição por sessão de 10 minutos. Pratique na pasta da trilha (ex.: `~/Developer/_trilhas/git/`); a lição 1 a transforma em repositório.

## Fontes

- `git help tutorial` e `git help tutorial-2`: tutorial oficial para iniciantes, no terminal.
- `git help everyday`: o conjunto mínimo de comandos do dia a dia.
- `git help glossary`: glossário oficial dos termos.
- `git help <comando>`: manual de cada comando.
- Pro Git, 2ª edição, em português: https://git-scm.com/book/pt-br/v2 (livre, licença CC BY-NC-SA 3.0). É de 2014: se o texto usar `git checkout` ou `git reset HEAD` para trocar de branch ou desfazer, ensine `git switch` e `git restore`.

## Lições

1. Repositório e primeiro commit: `git init`, `git status`, `git add`, `git commit`. Fontes: Pro Git 2.1; `git help tutorial`, IMPORTING A NEW PROJECT. Exercício: iniciar o repositório na pasta da trilha e commitar o `trilha.md`.
2. Os três estados (diretório de trabalho, stage, repositório). Fontes: Pro Git 1.3; `git help glossary` (index, working tree). Exercício: editar um arquivo e acompanhar cada estado com `git status`.
3. Ver o histórico: `git log`, `git log --oneline`, `git show`. Fontes: Pro Git 2.3; `git help tutorial`, VIEWING PROJECT HISTORY. Exercício: três commits pequenos e ler o log.
4. Ver diferenças: `git diff` e `git diff --staged`. Fonte: Pro Git 2.2. Exercício: alterar, comparar, colocar no stage, comparar de novo.
5. Ignorar arquivos: `.gitignore`. Fonte: Pro Git 2.2. Exercício: criar um arquivo de rascunho e fazer o Git ignorá-lo.
6. Remover e mover: `git rm`, `git mv`. Fonte: Pro Git 2.2. Exercício: renomear um arquivo e conferir que o histórico continua.
7. Desfazer antes do commit: `git restore` e `git restore --staged`. Fontes: Pro Git 2.4; `git help restore`. Exercício: estragar um arquivo e recuperá-lo.
8. Corrigir o último commit: `git commit --amend`. Fonte: Pro Git 2.4. Exercício: corrigir a mensagem de um commit.
9. Branches: `git branch`, `git switch`, `git switch -c`. Fontes: Pro Git 3.1; `git help tutorial`, MANAGING BRANCHES. Exercício: criar um branch, commitar nele e voltar ao main.
10. Mesclar: `git merge`. Fonte: Pro Git 3.2. Exercício: trazer o branch da lição 9 para o main.
11. Conflitos de merge. Fonte: Pro Git 3.2. Exercício: provocar um conflito de propósito e resolvê-lo.
12. Apelidos: `git config --global alias.*`. Fonte: Pro Git 2.7. Exercício: criar um apelido para `log --oneline`, com permissão, porque altera a configuração global.
13. Tags: `git tag`, `git tag -a`. Fonte: Pro Git 2.6. Exercício: marcar uma versão `v1.0` no repositório da trilha.
14. Guardar trabalho pela metade: `git stash`. Fonte: Pro Git 7.3. Exercício: guardar uma alteração, trocar de branch e recuperá-la.
15. Remotos, só leitura: `git remote -v`, `git fetch`, `git status` com upstream. Fontes: Pro Git 2.5; `git help tutorial`, USING GIT FOR COLLABORATION. Exercício: observar um repositório real do usuário que já tenha remoto, sem alterá-lo.
16. Revisão: `git help everyday`, seção INDIVIDUAL DEVELOPER (STANDALONE). Exercício: reproduzir de memória o ciclo editar, conferir, commitar e ver o log.
