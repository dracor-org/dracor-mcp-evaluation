# DraCor Chat Documentation - Dantons Tod Character Count

## Metadata

- **Date**: Tuesday, July 15, 2025
- **Assistant**: Claude Sonnet 4
- **Query**: "What is the number of dramatis personae in Dantons Tod?"
- **Database**: DraCor (Drama Corpora Project)
- **API Base URL**: https://staging.dracor.org/api/v1/
- **Tools Used**: DraCor MCP (Model Context Protocol) functions

## Initial Query

**Human**: What is the number of dramatis personae in Dantons Tod?

## Step 1: Exploring Available Corpora

**Assistant Action**: Called `DraCor:get_corpora` to retrieve all available drama corpora.

**Tool Used**: `DraCor:get_corpora`
**API Endpoint**: `/corpora`
**Purpose**: Get overview of all available corpora to identify which corpus contains German plays

**Response Summary**: Retrieved 29 corpora including:
- German Drama Corpus (ger/GerDraCor): 736 plays, 15,870 characters
- Shakespeare Drama Corpus (shake/ShakeDraCor): 37 plays
- French Drama Corpus (fre/FreDraCor): 1,940 plays
- Russian Drama Corpus (rus/RusDraCor): 212 plays
- And 25 other corpora in various languages

**Key Finding**: German corpus identified as "ger" with 736 plays and 15,870 total characters across all plays.

## Step 2: Searching for "Dantons Tod" in German Corpus

**Assistant Action**: Called `DraCor:get_plays_in_corpus_by_title_helper` to find plays with "Dantons Tod" in the title within the German corpus.

**Tool Used**: `DraCor:get_plays_in_corpus_by_title_helper`
**API Endpoint**: `/corpora/{corpusname}` (filtered by title)
**Parameters**: 
- `corpus_name`: "ger"
- `title`: "Dantons Tod"

**Response Data**: Found one matching play:
```json
{
  "plays": [
    {
      "wikidataId": "Q920590",
      "subtitle": "Ein Drama",
      "yearPremiered": "1902",
      "commit": "b428f3d4c1acb36a743e52f377b1685fb642c251",
      "source": {
        "url": "http://www.textgridrep.org/textgrid:ksd1.0",
        "name": "TextGrid Repository"
      },
      "uri": "https://staging.dracor.org/api/v1/corpora/ger/plays/buechner-dantons-tod",
      "yearWritten": "1835",
      "id": "ger000085",
      "title": "Dantons Tod",
      "networkSize": 103,
      "name": "buechner-dantons-tod",
      "yearNormalized": 1835,
      "yearPrinted": "1835",
      "authors": [
        {
          "shortname": "Büchner",
          "refs": [
            {
              "type": "wikidata",
              "ref": "Q154014"
            },
            {
              "type": "pnd",
              "ref": "118516906"
            }
          ],
          "name": "Büchner, Georg",
          "fullname": "Georg Büchner"
        }
      ],
      "networkdataCsvUrl": "https://staging.dracor.org/api/v1/corpora/ger/plays/buechner-dantons-tod/networkdata/csv"
    }
  ]
}
```

**Key Findings**:
- Play identifier: `buechner-dantons-tod`
- Play ID: `ger000085`
- Author: Georg Büchner
- Written: 1835
- Network size: 103 (preliminary indicator of character count)

## Step 3: Retrieving Character Information

**Assistant Action**: Called `DraCor:get_play_characters` to get detailed character information for the specific play.

**Tool Used**: `DraCor:get_play_characters`
**API Endpoint**: `/corpora/{corpusname}/plays/{playname}/characters`
**Parameters**:
- `corpus_name`: "ger"
- `play_name`: "buechner-dantons-tod"

**Response Data**: Retrieved detailed information for 103 characters. Each character entry includes:
- Character ID and name
- Number of scenes appeared in
- Gender (MALE/FEMALE/UNKNOWN)
- Network metrics (betweenness, degree, closeness, eigenvector)
- Speech statistics (numOfWords, numOfSpeechActs)
- Whether character is a group (isGroup: true/false)
- Wikidata ID (where available)

**Sample Character Entries**:

1. **Danton** (Main character):
```json
{
  "numOfScenes": 16,
  "sex": "MALE",
  "wikidataId": "Q184623",
  "betweenness": 0.39198930397241427,
  "degree": 43,
  "numOfWords": 4412,
  "closeness": 0.5885134195522181,
  "id": "danton",
  "numOfSpeechActs": 118,
  "name": "Danton",
  "isGroup": false,
  "eigenvector": 0.16326106724659753,
  "weightedDegree": 71
}
```

2. **Robespierre** (Major character):
```json
{
  "numOfScenes": 4,
  "sex": "MALE",
  "betweenness": 0.2237852566769281,
  "degree": 36,
  "numOfWords": 2253,
  "closeness": 0.5218892588481934,
  "id": "robespierre",
  "numOfSpeechActs": 29,
  "name": "Robespierre",
  "isGroup": false,
  "eigenvector": 0.30553196604975674,
  "weightedDegree": 38
}
```

3. **Group Characters** (e.g., crowd voices):
```json
{
  "numOfScenes": 1,
  "sex": "UNKNOWN",
  "betweenness": 0,
  "degree": 15,
  "numOfWords": 6,
  "closeness": 0.3721093818693397,
  "id": "leute",
  "numOfSpeechActs": 1,
  "name": "Leute",
  "isGroup": true,
  "eigenvector": 0.2024097360687322,
  "weightedDegree": 15
}
```

## Character Analysis

**Total Character Count**: 103 dramatis personae

**Character Categories**:
- **Individual Characters**: Named historical figures (Danton, Robespierre, Camille, St. Just, etc.)
- **Generic Individual Characters**: Citizens, deputies, prisoners, etc. (e.g., "Erster Bürger", "Ein Lyoner")
- **Group Characters**: Crowd voices and collective speakers (e.g., "Alle", "Viele Stimmen", "Die Jakobiner")

**Gender Distribution** (from character data):
- Male characters: Majority
- Female characters: Including Julie, Marion, Lucile, Rosalie, Adelaide, various "Weib" characters
- Unknown gender: Primarily group characters and crowd voices

**Character Roles**:
- **Historical Figures**: Danton, Robespierre, Camille Desmoulins, St. Just, Legendre, etc.
- **Citizens and Common People**: Various "Bürger" (citizens), "Fuhrmann" (coachmen), etc.
- **Officials**: Deputies, presidents, jailers, executioners
- **Women**: Wives, prostitutes, citizens
- **Crowd Voices**: "Einige Stimmen" (some voices), "Viele Stimmen" (many voices), "Alle" (all)

## Final Answer

**Question**: What is the number of dramatis personae in Dantons Tod?

**Answer**: 103 dramatis personae

**Source**: DraCor German Drama Corpus, play ID ger000085 (buechner-dantons-tod)

**Verification**: The number was confirmed through the DraCor API character endpoint, which provided detailed information for each of the 103 speaking characters in Georg Büchner's "Dantons Tod" (Danton's Death).

## Technical Details

**API Calls Made**:
1. `GET /corpora` - Retrieved all available corpora
2. `GET /corpora/ger` (filtered by title) - Found the specific play
3. `GET /corpora/ger/plays/buechner-dantons-tod/characters` - Retrieved character data

**Data Source**: TextGrid Repository (http://www.textgridrep.org/textgrid:ksd1.0)

**Play Metadata**:
- Year Written: 1835
- Year Printed: 1835
- Year Premiered: 1902
- Wikidata ID: Q920590
- Author Wikidata ID: Q154014 (Georg Büchner)

**Network Analysis Results**:
- Network size: 103 (matches character count)
- Most central character: Danton (highest betweenness centrality: 0.392)
- Most connected character: Danton (degree: 43)
- Character with most words: Danton (4,412 words)
- Character with most speech acts: Danton (118 speech acts)

This documentation represents the complete interaction with the DraCor API to answer the specific question about the number of dramatis personae in "Dantons Tod".