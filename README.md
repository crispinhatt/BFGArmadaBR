# Battlefleet Gothic: Armada — Tradução PT-BR

> Tradução não-oficial completa do jogo (Classic, com as DLCs Tau Empire e Space Marines) para o Português do Brasil.

---

## 📋 Sobre o projeto

Este projeto, assim como sua documentação, foi feito com o uso da plataforma CLAUDE: a tradução foi escrita em blocos de conversa, seguindo um glossário do universo Warhammer 40.000, e cada bloco foi validado por script. O autor do repositório dirigiu o projeto, testou no jogo e definiu escolhas como manter o nome **Gothic** sem tradução.

Este projeto traduz **5.329 termos** do jogo Battlefleet Gothic: Armada para o Português do Brasil (o arquivo tem 6.139 entradas, e 810 são campos vazios do próprio jogo), cobrindo todos os textos visíveis:

- Diálogos, legendas de cinemáticas e narrativa da campanha
- Missões, briefings e objetivos
- Interface (menus, opções, teclas, HUD, tela de frota)
- Armas, habilidades, melhorias, traços, tripulações e favores
- Tutoriais e dicas de carregamento
- Conquistas e sistema de ranking
- DLCs **Tau Empire** e **Space Marines**

**Versão do jogo testada:** 2.0.26100 (mostrada no menu principal)  
**Plataforma:** PC (Steam)

---

## ✅ O que foi traduzido

| Categoria | Termos | Descrição |
| --- | --- | --- |
| Dialogue | 1.629 | Diálogos e legendas da campanha e das cinemáticas |
| Weaponry | 585 | Armas e atributos de armamento |
| Game | 425 | Nomes, patentes, tripulações e termos gerais |
| Menu | 406 | Menus, opções, teclas e tela de frota |
| Upgrade | 291 | Melhorias de naves |
| Skill | 273 | Habilidades ativas e tripulações |
| Favor | 179 | Favores das facções |
| Ship | 157 | Características das naves |
| Tooltips | 153 | Dicas de terreno e ordens |
| Content | 129 | Textos de interface e missões |
| Briefing | 120 | Briefings de missão |
| Traits | 113 | Traços de naves |
| TutoWindow + Tutobox | 205 | Tutoriais |
| Loading | 85 | Dicas das telas de carregamento |
| StellarMap | 83 | Mapa estelar da campanha |
| InGame | 80 | Textos durante a batalha |
| Objectif | 79 | Objetivos de missão |
| Achievement | 68 | Conquistas |
| + outros | ~269 | Ranking, Modo Elite, popups, placar de líderes etc. |

### Termos mantidos em inglês/latim (intencionalmente)

Nomes e termos canônicos do universo Warhammer 40K foram preservados: `Gothic` (nome do setor, também em "Guerra Gothic" e "Frota de Batalha Gothic"), `Warp`, `Imperium`, `Adeptus Astartes`, `Adeptus Mechanicus`, `Space Marines`, `Eldar`, `Tau`, `Orks` (e a gíria Orkish: `Kaptin`, `Kroozer`, `Kannon`, `Gunz`, `Boyz`, `teef`, `humie`, `Waaagh!`), `Port Maw`, `Exterminatus`, `Ranking`, nomes de Capítulos (`Dark Angels`, `Blood Angels`, `Ultramarines`, `Imperial Fists`, `Space Wolves`), termos Tau (`Tau'Va`, `Kor'Vattra`, `Mont'Ka`, `Kauyon`), classes e nomes de naves (`Dauntless`, `Cobra`, `Firestorm`, `Hellbringer`…), planetas, sistemas e personagens.

Consulte o [GLOSSARIO.md](GLOSSARIO.md) para a lista completa de termos adotados.

---

## Como foi traduzido?

Para saber de mais detalhes leia `COMO_FUNCIONA.md`.

Verificou-se que o jogo lê o texto de um arquivo solto, `langEN.xml`, em `BattleFleetGothic\Content\Localization` (o único `.pak` do jogo, aberto no FModel, não contém nenhum arquivo de localização). O arquivo é um XML em UTF-16 com 6.139 entradas, em que o nome da tag é a chave do texto.

A CLAUDE dividiu as entradas em 80 blocos, na ordem do arquivo, e traduziu um bloco por vez seguindo o glossário. Antes da tradução completa foi gerado um XML de teste apenas com textos de menu, para confirmar que a fonte do jogo exibe os acentos do português. Um script então montou o `langEN.xml` traduzido, conferindo a cada bloco se `{0}`, `{1}`…, `\n` e marcadores de tecla como `[SpaceBar]` continuavam idênticos ao original.

A tradução foi feita direto na conversa com a CLAUDE, sem uso de API.

---

## 🛠️ Como instalar

### Pré-requisitos

- Jogo instalado via Steam (as DLCs são opcionais; os textos delas estão no mesmo arquivo)
- Nenhuma ferramenta extra: basta substituir um arquivo

### Passo a passo

**1. Faça backup do arquivo original**

```
Copie o arquivo:
...\SteamLibrary\steamapps\common\Battlefleet Gothic Armada\BattleFleetGothic\Content\Localization\langEN.xml

Para uma pasta segura antes de continuar (por exemplo, langEN.original.xml na área de trabalho).
```

**2. Baixe o arquivo de tradução**

Baixe o arquivo `langEN.xml` da seção [Releases](https://github.com/crispinhatt/BFGArmadaBR/releases) deste repositório.

**3. Substitua o arquivo**

- Feche o jogo
- Cole o `langEN.xml` baixado na pasta `...\BattleFleetGothic\Content\Localization`, substituindo o original

**4. Jogue!**

- Abra o jogo normalmente pelo Steam em **inglês**
- Os textos aparecerão automaticamente em **Português do Brasil**

> Dica: o arquivo é UTF-16 com BOM. Se for abri-lo em um editor, use um que preserve essa codificação (VS Code, Notepad++), ou não edite.

---

## 🔄 Como desinstalar / restaurar

Para voltar ao inglês original, basta restaurar o backup:

1. Feche o jogo
2. Copie o `langEN.xml` original de volta para a pasta `Localization`
3. Confirme a substituição

Também funciona usar **Propriedades → Arquivos instalados → Verificar integridade dos arquivos** na Steam.

---

## ⚠️ Avisos

- Esta é uma tradução **não-oficial** — não tem relação com a Tindalos Interactive, a Focus Entertainment ou a Games Workshop
- Testada na versão **2.0.26100** — atualizações do jogo ou "Verificar integridade" restauram o arquivo original, e pode ser necessário reaplicar
- Textos que estão dentro de imagens, vídeos ou arquivos de áudio não fazem parte do XML e continuam em inglês
- Alguns marcadores de tecla (`[Right-Click Button]`, `[Burn Retro]`, `[All Ahead Full]` etc.) foram mantidos em inglês porque o jogo pode substituí-los por ícones
- 8 entradas do original tinham erros de marcador (por exemplo `\I`, `\O` e `\M` no lugar de `\n`) e foram corrigidas; veja [RELATORIO_MARCADORES.md](RELATORIO_MARCADORES.md)
- Instalações da GOG e da Microsoft Store podem ter outro caminho de pasta e não foram testadas

---

## 🐛 Reportar erros

Encontrou um erro de tradução, texto cortado ou algo que não faz sentido em PT-BR? Abra uma [Issue](https://github.com/crispinhatt/BFGArmadaBR/issues) com:

- Print da tela com o erro
- Contexto (qual missão, menu, nave, facção)
- Sugestão de tradução correta (opcional)

---

## 🔧 Para desenvolvedores

Quer contribuir com melhorias ou criar uma tradução para outro idioma? Veja o arquivo [COMO_FUNCIONA.md](COMO_FUNCIONA.md) para entender a estrutura técnica do projeto.

---

## 📜 Licença

Este projeto está licenciado sob a MIT License.

Você pode usar, modificar, distribuir e até utilizar comercialmente este projeto livremente.

Battlefleet Gothic: Armada © Tindalos Interactive / Focus Entertainment. Battlefleet Gothic, Warhammer 40,000 e todos os nomes, raças, naves, locais e personagens associados são marcas e/ou © Games Workshop Limited, usados sob licença.
Este projeto é uma tradução não-oficial e não possui vínculo com os detentores da propriedade intelectual.
