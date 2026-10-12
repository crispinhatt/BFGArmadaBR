#!/usr/bin/env python3
"""Gera o langEN.xml traduzido a partir do langEN.xml original e do bfga_ptbr.json.

Uso:
    python GERAR_XML.py <langEN.xml original> <bfga_ptbr.json> <saida langEN.xml>

- Lê o original em UTF-16 (com BOM) e preserva toda a estrutura (cabeçalho, ordem, CRLF).
- Troca apenas o texto de cada entrada pela "traducao" do JSON.
- Chaves repetidas no original aparecem no JSON como "Chave", "Chave#2"...
- Confere {0}..{9} e \\n antes de gravar e avisa se algo diferir do original.
"""
import re, sys, json, collections

def main(src, js, dst):
    raw = open(src, encoding='utf-16', newline='').read()
    data = json.load(open(js, encoding='utf-8'))
    pat = re.compile(r'<([^\s<>/!?]+)>(.*?)</\1>', flags=re.S)
    seen, out, pos, avisos, n = collections.Counter(), [], 0, [], 0
    for m in pat.finditer(raw):
        k = m.group(1)
        if k == 'root':
            continue
        seen[k] += 1
        key = k if seen[k] == 1 else f'{k}#{seen[k]}'
        item = data.get(key)
        if item is None:
            continue
        orig, new = m.group(2), item['traducao']
        mk = lambda s: collections.Counter(re.findall(r'\{\d+\}|\\n', s))
        if mk(orig) != mk(new):
            avisos.append(key)
        if re.search(r'[&<>]', new):
            sys.exit(f'ERRO: caractere proibido (& < >) em {key}')
        out.append(raw[pos:m.start(2)]); out.append(new); pos = m.end(2); n += 1
    out.append(raw[pos:])
    open(dst, 'wb').write(b'\xff\xfe' + ''.join(out).encode('utf-16-le'))
    print(f'{n} entradas gravadas em {dst}')
    if avisos:
        print('Entradas em que {n} ou \\n diferem do original (conferir):')
        for a in avisos:
            print('  -', a)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
