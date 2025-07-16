# DraCor Chat Documentation: Character Count Query

## Metadata
- **Date**: Tuesday, July 15, 2025
- **Query**: "What is the number of characters in Der Nollhart?"
- **Assistant**: Claude Sonnet 4
- **Primary Tool**: DraCor API via MCP (Model Context Protocol)
- **API Base URL**: https://staging.dracor.org/api/v1/

## Initial Query
**Human**: What is the number of characters in Der Nollhart?

## Step 1: Explore Available Corpora

**Assistant Action**: Retrieved all available corpora to understand the scope of the DraCor database.

**Tool Used**: `DraCor:get_corpora`
**API Endpoint**: `/corpora`
**Purpose**: Get overview of all drama corpora available in DraCor

**Response Summary**: 
- Retrieved 28 drama corpora from various languages and time periods
- Notable corpora include:
  - German Drama Corpus (ger): 736 plays, 15,870 characters
  - Shakespeare Drama Corpus (shake): 37 plays, 1,433 characters
  - French Drama Corpus (fre): 1,940 plays, 17,831 characters
  - Russian Drama Corpus (rus): 212 plays, 3,707 characters
  - And many others covering languages from Alsatian to Yiddish

**Key Finding**: The German corpus (ger) appeared most likely to contain "Der Nollhart" based on the German title.

## Step 2: Search for "Der Nollhart" in German Corpus

**Assistant Action**: Searched specifically within the German drama corpus for plays containing "Nollhart" in the title.

**Tool Used**: `DraCor:get_plays_in_corpus_by_title_helper`
**API Endpoint**: `/corpora/ger` (filtered by title)
**Parameters**:
- `corpus_name`: "ger"
- `title`: "Nollhart"

**Response Data**:
```json
{
  "plays": [
    {
      "wikidataId": "Q125280256",
      "subtitle": "Diß sind die prophetien sancti Methodii vnd Nollhardi [...]",
      "yearPremiered": "1515",
      "commit": "b428f3d4c1acb36a743e52f377b1685fb642c251",
      "source": {
        "url": "http://www.textgridrep.org/textgrid:n7s9.0",
        "name": "TextGrid Repository"
      },
      "uri": "https://staging.dracor.org/api/v1/corpora/ger/plays/gengenbach-der-nollhart",
      "yearWritten": null,
      "id": "ger000697",
      "title": "Der Nollhart",
      "networkSize": 14,
      "name": "gengenbach-der-nollhart",
      "yearNormalized": 1515,
      "yearPrinted": "1517",
      "authors": [
        {
          "shortname": "Gengenbach",
          "refs": [
            {
              "type": "wikidata",
              "ref": "Q1305022"
            },
            {
              "type": "pnd",
              "ref": "11853842X"
            }
          ],
          "name": "Gengenbach, Pamphilus",
          "fullname": "Pamphilus Gengenbach"
        }
      ],
      "networkdataCsvUrl": "https://staging.dracor.org/api/v1/corpora/ger/plays/gengenbach-der-nollhart/networkdata/csv"
    }
  ]
}
```

**Key Findings**:
- Found exactly one play: "Der Nollhart" by Pamphilus Gengenbach
- Play ID: `ger000697`
- Play name identifier: `gengenbach-der-nollhart`
- Year premiered: 1515
- Year printed: 1517
- Network size: 14 (indicating 14 characters)
- Source: TextGrid Repository

## Step 3: Retrieve Detailed Play Metadata

**Assistant Action**: Retrieved comprehensive metadata for the specific play to get detailed character information.

**Tool Used**: `DraCor:get_play_metadata`
**API Endpoint**: `/corpora/ger/plays/gengenbach-der-nollhart`
**Parameters**:
- `corpus_name`: "ger"
- `play_name`: "gengenbach-der-nollhart"

**Response Data** (Character Section):
```json
{
  "play": {
    "allInSegment": 1,
    "wikidataId": "Q125280256",
    "segments": [
      {
        "type": "scene",
        "speakers": [
          "der_bapst",
          "der_bruder",
          "birgitta",
          "sybilla_chumea",
          "der_keyser",
          "methodius",
          "der_kueng_von_franckenreich",
          "der_byschoff_von_mentz",
          "der_pfaltzgraff",
          "der_venediger",
          "der_duerck",
          "der_eydtgenosz",
          "der_lantzknecht",
          "der_jud"
        ],
        "number": 1
      }
    ],
    "normalizedGenre": "Comedy",
    "subtitle": "Diß sind die prophetien sancti Methodii vnd Nollhardi [...]",
    "yearPremiered": "1515",
    "commit": "b428f3d4c1acb36a743e52f377b1685fb642c251",
    "corpus": "ger",
    "uri": "https://staging.dracor.org/api/v1/corpora/ger/plays/gengenbach-der-nollhart",
    "authors": [
      {
        "shortname": "Gengenbach",
        "refs": [
          {
            "type": "wikidata",
            "ref": "Q1305022"
          },
          {
            "type": "pnd",
            "ref": "11853842X"
          }
        ],
        "name": "Gengenbach, Pamphilus",
        "fullname": "Pamphilus Gengenbach"
      }
    ],
    "yearWritten": null,
    "id": "ger000697",
    "title": "Der Nollhart",
    "allInIndex": 1,
    "name": "gengenbach-der-nollhart",
    "yearNormalized": 1515,
    "yearPrinted": "1517",
    "originalSource": "Pamphilus Gengenbach: Der Nollhart. Diß sind die prophetien sancti Methodii vnd Nollhardi. welche von wort zů wort nach jnhalt der matery vnd anzeigūg der figurē sind gespilt worden jm . xvc . vnd. xvij . Jor, vff der herren fastnacht von etlichen ersamen vnd geschicktē Burgeren einer loblichen stat Basel. In: Pamphilus Gengenbach. Herausgegeben von Karl Goedeke. Hannover: Rümpler 1856, S. 77–116.",
    "characters": [
      {
        "sex": "MALE",
        "id": "der_bapst",
        "name": "Der Bapst",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "der_bruder",
        "name": "Der Bruder (Nollhart)",
        "isGroup": false
      },
      {
        "sex": "FEMALE",
        "id": "birgitta",
        "name": "Birgitta",
        "isGroup": false
      },
      {
        "sex": "FEMALE",
        "id": "sybilla_chumea",
        "name": "Sybilla Chumea",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "der_keyser",
        "name": "Der Keyser",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "methodius",
        "name": "Methodius",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "der_kueng_von_franckenreich",
        "name": "Der Küng von Franckenreich",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "der_byschoff_von_mentz",
        "name": "Der Byschoff von Mentz",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "der_pfaltzgraff",
        "name": "Der Pfaltzgraff",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "der_venediger",
        "name": "Der Venediger",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "der_duerck",
        "name": "Der Dürck",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "der_eydtgenosz",
        "name": "Der Eydtgenosz",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "der_lantzknecht",
        "name": "Der Lantzknecht (Bruder Veit)",
        "isGroup": false
      },
      {
        "sex": "MALE",
        "id": "der_jud",
        "name": "Der Jud",
        "isGroup": false
      }
    ],
    "libretto": false,
    "source": {
      "url": "http://www.textgridrep.org/textgrid:n7s9.0",
      "name": "TextGrid Repository"
    }
  }
}
```

## Final Answer Compilation

**Assistant Analysis**: Based on the comprehensive metadata retrieved from the DraCor API, the play "Der Nollhart" by Pamphilus Gengenbach contains exactly **14 characters**.

**Character Breakdown**:
1. Der Bapst (The Pope) - Male
2. Der Bruder (Nollhart) (The Brother/Nollhart) - Male
3. Birgitta - Female
4. Sybilla Chumea - Female
5. Der Keyser (The Kaiser/Emperor) - Male
6. Methodius - Male
7. Der Küng von Franckenreich (The King of France) - Male
8. Der Byschoff von Mentz (The Bishop of Mainz) - Male
9. Der Pfaltzgraff (The Count Palatine) - Male
10. Der Venediger (The Venetian) - Male
11. Der Dürck (The Turk) - Male
12. Der Eydtgenosz (The Confederate) - Male
13. Der Lantzknecht (Bruder Veit) (The Lansquenet/Brother Veit) - Male
14. Der Jud (The Jew) - Male

**Additional Context**:
- Genre: Comedy
- Historical significance: Early 16th-century German play dealing with prophecies
- Character composition: 12 male characters, 2 female characters
- All characters appear in a single scene
- The play features religious, political, and social figures typical of the period

## Tools and API Endpoints Summary

1. **DraCor:get_corpora** → `/corpora` - Retrieved all available drama corpora
2. **DraCor:get_plays_in_corpus_by_title_helper** → `/corpora/ger` (filtered) - Found specific play by title
3. **DraCor:get_play_metadata** → `/corpora/ger/plays/gengenbach-der-nollhart` - Retrieved detailed character information

## Data Sources
- Primary source: DraCor API (https://staging.dracor.org/api/v1/)
- Original text source: TextGrid Repository (http://www.textgridrep.org/textgrid:n7s9.0)
- Historical source: Pamphilus Gengenbach. Herausgegeben von Karl Goedeke. Hannover: Rümpler 1856, S. 77–116
- Wikidata reference: Q125280256