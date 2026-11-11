#!/usr/bin/env python3
"""Imprime o texto de uma seção de um livro EPUB, procurada pelo título no sumário.

Uso:
  secao-epub.py LIVRO.epub --lista            lista os títulos do sumário
  secao-epub.py LIVRO.epub "Título da seção"  imprime a seção em texto simples

Só lê o arquivo; não grava nada. Usa apenas a biblioteca padrão do Python.
"""
import html
import posixpath
import re
import sys
import zipfile
from typing import NoReturn


def falha(msg) -> NoReturn:
    print(f"erro: {msg}", file=sys.stderr)
    sys.exit(1)


def sumario(z):
    nav = [n for n in z.namelist() if n.lower().endswith("nav.xhtml")]
    if not nav:
        falha("o EPUB não tem nav.xhtml (sumário EPUB 3)")
    base = posixpath.dirname(nav[0])
    texto = z.read(nav[0]).decode("utf-8", "ignore")
    itens = []
    for href, rotulo in re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', texto, re.S):
        rotulo = html.unescape(re.sub(r"<[^>]+>", "", rotulo)).strip()
        arquivo, _, ancora = href.partition("#")
        itens.append((rotulo, posixpath.normpath(posixpath.join(base, arquivo)), ancora))
    return itens


def texto_simples(trecho):
    trecho = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", trecho, flags=re.S)
    trecho = re.sub(r"<br\s*/?>|</(p|div|h\d|li|pre|tr)>", "\n", trecho)
    trecho = html.unescape(re.sub(r"<[^>]+>", "", trecho))
    linhas = [l.rstrip() for l in trecho.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip()


def main():
    if len(sys.argv) != 3:
        falha((__doc__ or "uso: secao-epub.py LIVRO.epub TÍTULO").strip())
    livro, pedido = sys.argv[1], sys.argv[2]
    try:
        z = zipfile.ZipFile(livro)
    except (OSError, zipfile.BadZipFile) as e:
        falha(f"não consegui abrir {livro}: {e}")
    itens = sumario(z)
    if pedido == "--lista":
        print("\n".join(r for r, _, _ in itens))
        return
    achados = [i for i, (r, _, _) in enumerate(itens) if r.casefold() == pedido.casefold()]
    if not achados:
        falha(f'seção "{pedido}" não encontrada; use --lista para ver os títulos')
    if len(achados) > 1:
        print(f'aviso: {len(achados)} seções com esse título; mostrando a primeira', file=sys.stderr)
    i = achados[0]
    _, arquivo, ancora = itens[i]
    conteudo = z.read(arquivo).decode("utf-8", "ignore")
    inicio = 0
    if ancora:
        m = re.search(r'id="%s"' % re.escape(ancora), conteudo)
        inicio = conteudo.rfind("<", 0, m.start()) if m else 0
    fim = len(conteudo)
    if i + 1 < len(itens):
        _, prox_arquivo, prox_ancora = itens[i + 1]
        if prox_arquivo == arquivo and prox_ancora:
            m = re.search(r'id="%s"' % re.escape(prox_ancora), conteudo)
            if m and m.start() > inicio:
                fim = conteudo.rfind("<", 0, m.start())
    print(texto_simples(conteudo[inicio:fim]))


if __name__ == "__main__":
    main()
