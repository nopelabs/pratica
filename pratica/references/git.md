# Roteiro: Git

Do zero ao uso diário, uma lição por sessão de 10 minutos. Pratique na pasta da trilha (ex.: `~/Developer/_trilhas/git/`); a lição 1 a transforma em repositório.

## Fontes

- Pro Git, 2ª edição, em português: livro oficial, livre (licença CC BY-NC-SA 3.0). Baixe o EPUB em https://git-scm.com/book/pt-br/v2 e aponte a linha `material:` da trilha para ele. As lições citam os títulos exatos do sumário do EPUB, para usar com `scripts/secao-epub.py`.
- `git help tutorial` e `git help tutorial-2`: tutorial oficial para iniciantes, no terminal.
- `git help everyday`: o conjunto mínimo de comandos do dia a dia.
- `git help glossary`: glossário oficial dos termos.
- `git help <comando>`: manual de cada comando.

O livro mostra comandos antigos ao lado dos novos (ex.: `git checkout` e `git reset HEAD` ao lado de `git switch` e `git restore`). Ensine a forma nova e cite a antiga só como equivalência.

## Lições

1. Repositório e primeiro commit: `git init -b main`, `git status`, `git add`, `git commit`. Seções: "Inicializando um repositório em um diretório existente", "Fazendo o Commit de suas Alterações"; `git help tutorial`, IMPORTING A NEW PROJECT. Exercício: na pasta da trilha, rodar `git rev-parse --show-toplevel`, que deve dar erro por ainda não haver repositório (se não der, pare e avise); iniciar o repositório e fazer o primeiro commit do `trilha.md`. O `-b main` dá ao branch inicial o nome `main`; sem ele, o Git usa `master`, salvo se `init.defaultBranch` estiver configurado.
2. Os três estados (diretório de trabalho, área de preparação, repositório). Seções: "Os Três Estados", "Verificando o status dos seus arquivos"; `git help glossary` (index, working tree). Exercício: editar um arquivo e acompanhar cada estado com `git status`.
3. Ver o histórico: `git log`, `git log --oneline`, `git show`. Seção: "Visualizando o Histórico de Commits"; `git help tutorial`, VIEWING PROJECT HISTORY. Exercício: três commits pequenos e ler o log.
4. Ver diferenças: `git diff` e `git diff --staged`. Seção: "Visualizando suas Alterações Preparadas e Não Preparadas". Exercício: alterar, comparar, preparar com `git add`, comparar de novo.
5. Ignorar arquivos: `.gitignore`. Seção: "Ignorando Arquivos". Exercício: criar um arquivo de rascunho e fazer o Git ignorá-lo.
6. Remover e mover: `git rm`, `git mv`. Seções: "Removendo Arquivos", "Movendo Arquivos". Exercício: renomear um arquivo e conferir que o histórico continua.
7. Desfazer antes do commit: `git restore` e `git restore --staged`. Seção: "Desfazendo coisas com git restore"; `git help restore`. Exercício: estragar um arquivo e recuperá-lo.
8. Corrigir o último commit: `git commit --amend`. Seção: "Desfazendo Coisas". Exercício: corrigir a mensagem de um commit.
9. Branches: `git branch`, `git switch`, `git switch -c`. Seções: "Criando um Novo Branch", "Mudando de Branches"; `git help tutorial`, MANAGING BRANCHES. Exercício: criar um branch, commitar nele e voltar ao `main`.
10. Mesclar: `git merge`. Seção: "Mesclagem (Merging) Básica". Exercício: trazer o branch da lição 9 para o `main`.
11. Conflitos de merge. Seção: "Conflitos Básicos de Mesclagem (Merge Conflicts)". Exercício: provocar um conflito de propósito e resolvê-lo.
12. Apelidos: `git config --global alias.*`. Seção: "Aliases (Apelidos) no Git". Exercício: criar um apelido para `log --oneline`, com permissão, porque altera a configuração global.
13. Tags: `git tag`, `git tag -a`. Seções: "Listando Suas Tags", "Tags Anotadas (Annotated Tags)". Exercício: marcar uma versão `v1.0` no repositório da trilha.
14. Guardar trabalho pela metade: `git stash`. Seção: "Fazendo Stash do Seu Trabalho". Exercício: guardar uma alteração, trocar de branch e recuperá-la.
15. Remotos, só leitura: `git remote -v`, `git fetch`, `git status` com upstream. Seções: "Mostrando seus Remotos", "Buscando (fetching) e Extraindo (pulling) de Seus Remotos"; `git help tutorial`, USING GIT FOR COLLABORATION. Exercício: observar um repositório real do usuário que já tenha remoto, sem alterá-lo.
16. Revisão: `git help everyday`, seção INDIVIDUAL DEVELOPER (STANDALONE). Exercício: reproduzir de memória o ciclo editar, conferir, commitar e ver o log.
