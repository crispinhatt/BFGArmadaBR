# 🔧 Como funciona — Documentação Técnica

Este documento explica a estrutura técnica da tradução para quem quiser contribuir, corrigir termos ou criar traduções para outros idiomas.

---

## Estrutura do jogo

O Battlefleet Gothic: Armada usa a **Unreal Engine 4**. Os textos não ficam nos arquivos `.pak` do jogo, e sim em um arquivo XML solto:

```
BattleFleetGothic\Content\Localization\langEN.xml
```

A pasta `Content` tem `Localization`, `Movies`, `Paks` e `Splash`. O único `.pak` (aberto no FModel) não contém nenhum arquivo de localização, por isso a tradução é só a substituição desse XML.

Especificações do arquivo:

- **Codificação:** UTF-16 LE com BOM (`encoding="unicode"`), quebras de linha CRLF
- **Raiz:** `<root short_language="EN">`
- **Entradas:** 6.139 (5.329 com texto e 810 vazias)
- **Tamanho:** ~1,8 MB

---

## Estrutura do XML

Cada entrada é uma tag cujo **nome é a chave** e cujo conteúdo é o texto:

```xml
<Menu_Main_Options_Tooltip_Content>Customize game settings</Menu_Main_Options_Tooltip_Content>
```

A tradução PT-BR substitui o texto entre as tags, sem mexer em nomes de tags, ordem ou cabeçalho.

Particularidades do arquivo original:

- Uma tag tem apóstrofo no nome (`Game_ProperNoun_System_CyclN'man_Title`), então o arquivo **não é XML válido** para parsers estritos. O jogo usa um parser tolerante, e os scripts do projeto também.
- 6 ocorrências de chaves repetidas (por exemplo `Menu_Bindings_Pause` e `Weaponry_Chaos_Khorne_Battery_MLB_Tooltip_Title`), às vezes com textos diferentes. No JSON elas aparecem como `Chave`, `Chave#2`.
- Algumas entradas têm quebras de linha reais (CRLF) no meio do texto e 2 entradas têm o separador de linha U+2028.
- Os nomes de teclas começam com espaço não separável (U+00A0).

---

## Categorias de termos

Os prefixos das chaves indicam o tipo de texto:

| Prefixo | Descrição |
| --- | --- |
| `Dialogue_` | Diálogos, legendas e cinemáticas da campanha |
| `Weaponry_` | Armas e atributos |
| `Menu_` | Menus, opções, teclas, tela de frota |
| `Game_` | Nomes, patentes, tripulações |
| `Upgrade_` | Melhorias |
| `Skill_` | Habilidades ativas e tripulações |
| `Favor_` | Favores das facções |
| `Ship_` | Características de naves |
| `Tooltips_` | Dicas de terreno e ordens |
| `Briefing_` | Briefings de missão |
| `Traits_` | Traços |
| `TutoWindow_`, `Tutobox_` | Tutoriais |
| `Loading_` | Dicas de carregamento |
| `StellarMap_` | Mapa estelar |
| `Achievement_` | Conquistas |
| `RankingSystem_`, `EliteMode_`, `Leaderboard_` | Ranking, Modo Elite e placar |

---

## Placeholders preservados

Os seguintes tokens especiais foram preservados nas traduções:

| Token | Significado |
| --- | --- |
| `{0}`, `{1}`, … `{9}` | Variáveis numéricas (valores, porcentagens, nomes) |
| `\n` | Quebra de linha (barra invertida + n, literal) |
| `[SpaceBar]`, `[W]`, `[A]`, `[S]`, `[D]` | Teclas |
| `[Right-Click Button]`, `[Left Mouse Button]`, `[Middle Mouse Button]`, `[Burn Retro]`, `[All Ahead Full]` | Ações/teclas (mantidas em inglês) |
| CRLF real, U+2028, U+00A0 | Quebras e espaços especiais em entradas específicas |

**Atenção:** alterar esses elementos pode quebrar a exibição dos textos.

---

## Ferramentas utilizadas

| Ferramenta | Uso |
| --- | --- |
| [FModel](https://fmodel.app) | Conferir que o `.pak` do jogo não contém arquivos de localização |
| Python 3 | Scripts de extração, validação e geração do XML |
| Claude (conversa) | Tradução dos 5.329 termos, em 80 blocos |

---

## Scripts do projeto

| Script | Função |
| --- | --- |
| `scripts/GERAR_XML.py` | Gera o `langEN.xml` traduzido a partir do `langEN.xml` original e do `bfga_ptbr.json` |

Uso:

```
python scripts/GERAR_XML.py <langEN.xml original> bfga_ptbr.json <saida/langEN.xml>
```

O script preserva o cabeçalho, a ordem e as quebras de linha, e avisa se `{0}`…`{9}` ou `\n` diferirem do original. As 7 entradas que aparecem como aviso são correções intencionais de erros do original (veja [RELATORIO_MARCADORES.md](RELATORIO_MARCADORES.md)).

---

## Como contribuir com melhorias

1. Faça fork deste repositório
2. Edite o arquivo `bfga_ptbr.json` — cada entrada tem:

```json
"Chave_Do_Termo": {
  "termo": "Chave_Do_Termo",
  "original": "Texto em inglês",
  "traducao": "Texto em português"
}
```

3. Gere o novo XML:

```
python scripts/GERAR_XML.py langEN.original.xml bfga_ptbr.json langEN.xml
```

4. Substitua o `langEN.xml` na pasta `Localization` do jogo
5. Teste no jogo e abra um Pull Request com suas melhorias

Respeite o [GLOSSARIO.md](GLOSSARIO.md) e preserve os placeholders.

---

## Como criar tradução para outro idioma

O processo é o mesmo: traduza o campo `traducao` do JSON para o idioma desejado e gere o XML com o script. Como o jogo só traz o arquivo `langEN.xml`, ele continua sendo o arquivo substituído.

---

## Histórico de versões

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0.0 | Out/2026 | Primeira versão — 5.329 termos traduzidos |
