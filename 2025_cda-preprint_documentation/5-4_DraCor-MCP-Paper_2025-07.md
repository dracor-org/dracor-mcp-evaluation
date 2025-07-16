# DraCor Chat Documentation - "Die entführte Dose" Protagonist Analysis

## Metadata

**Date:** Tuesday, July 15, 2025  
**Assistant:** Claude Sonnet 4  
**Query:** "Who is the protagonist in 'Die entführte Dose'?"  
**DraCor API:** https://staging.dracor.org/api/v1/  
**Tools Used:** DraCor API functions via MCP (Model Context Protocol)  

## Initial Query

**Human:** Who is the protagonist in "Die entführte Dose"?

## Step 1: Explore Available Corpora

**Tool Used:** `DraCor:get_corpora`  
**API Endpoint:** `/corpora`  
**Purpose:** Get overview of all available drama corpora to identify which corpus might contain the German play

**Response:** Retrieved list of 29 corpora including:
- Alsatian Drama Corpus (als)
- American Drama Corpus (am)
- German Drama Corpus (ger) - 736 plays
- German Shakespeare Drama Corpus (gersh)
- And 25 other language-specific corpora

**Analysis:** Since "Die entführte Dose" is a German title, the German Drama Corpus (ger) with 736 plays was the most likely candidate.

## Step 2: Search for Play by Title

**Tool Used:** `DraCor:get_plays_in_corpus_by_title_helper`  
**API Endpoint:** `/corpora/ger` (filtered by title)  
**Parameters:**
- `corpus_name`: "ger"
- `title`: "Die entführte Dose"

**Response:** Found one matching play:
```json
{
  "plays": [
    {
      "wikidataId": "Q124217835",
      "subtitle": "Ein Lustspiel in einem Aufzuge",
      "yearPremiered": "1740",
      "yearWritten": "1740",
      "id": "ger000665",
      "title": "Die entführte Dose",
      "networkSize": 5,
      "name": "schlegel-die-entfuehrte-dose",
      "yearNormalized": 1740,
      "yearPrinted": "1762",
      "authors": [
        {
          "shortname": "Schlegel",
          "name": "Schlegel, Johann Elias",
          "fullname": "Johann Elias Schlegel"
        }
      ]
    }
  ]
}
```

**Key Information Extracted:**
- Play ID: `ger000665`
- Play name: `schlegel-die-entfuehrte-dose`
- Author: Johann Elias Schlegel
- Year: 1740
- Genre: Comedy (Lustspiel)
- Network size: 5 characters

## Step 3: Retrieve Character Information

**Tool Used:** `DraCor:get_play_characters`  
**API Endpoint:** `/corpora/ger/plays/schlegel-die-entfuehrte-dose/characters`  
**Parameters:**
- `corpus_name`: "ger"
- `play_name`: "schlegel-die-entfuehrte-dose"

**Response:** Retrieved detailed character data:

### Character: Foppendorf
- **Sex:** MALE
- **Scenes:** 3
- **Speech Acts:** 42
- **Word Count:** 895
- **Network Metrics:**
  - Degree: 4
  - Betweenness: 0.5
  - Closeness: 1
  - Eigenvector: 0.523563311209037
  - Weighted Degree: 5

### Character: Glocke
- **Sex:** MALE
- **Scenes:** 1
- **Speech Acts:** 13
- **Word Count:** 222
- **Network Metrics:**
  - Degree: 1
  - Betweenness: 0
  - Closeness: 0.5714285714285714
  - Eigenvector: 0.16965100981173123
  - Weighted Degree: 1

### Character: Dratmann
- **Sex:** MALE
- **Scenes:** 2
- **Speech Acts:** 27
- **Word Count:** 379
- **Network Metrics:**
  - Degree: 3
  - Betweenness: 0
  - Closeness: 0.8
  - Eigenvector: 0.482044255930127
  - Weighted Degree: 4

### Character: Charlottchen
- **Sex:** FEMALE
- **Scenes:** 1
- **Speech Acts:** 1
- **Word Count:** 16
- **Network Metrics:**
  - Degree: 3
  - Betweenness: 0
  - Closeness: 0.8
  - Eigenvector: 0.482044255930127
  - Weighted Degree: 3

### Character: Christinchen
- **Sex:** FEMALE
- **Scenes:** 1
- **Speech Acts:** 2
- **Word Count:** 38
- **Network Metrics:**
  - Degree: 3
  - Betweenness: 0
  - Closeness: 0.8
  - Eigenvector: 0.482044255930127
  - Weighted Degree: 3

## Step 4: Retrieve Additional Play Metadata

**Tool Used:** `DraCor:get_play_metadata`  
**API Endpoint:** `/corpora/ger/plays/schlegel-die-entfuehrte-dose`  
**Parameters:**
- `corpus_name`: "ger"
- `play_name`: "schlegel-die-entfuehrte-dose"

**Response:** Retrieved comprehensive play metadata including:

### Play Structure
- **Segments:** 4 scenes
- **Genre:** Comedy (normalizedGenre: "Comedy")
- **All-in-segment:** 4 (characters appearing together)
- **All-in-index:** 1

### Scene Distribution
1. **Scene 1:** Foppendorf, Glocke
2. **Scene 2:** (no speakers listed)
3. **Scene 3:** Foppendorf, Dratmann
4. **Scene 4:** Charlottchen, Christinchen, Foppendorf, Dratmann

### Character Relationships
- Charlottchen and Christinchen are siblings
- Glocke is associated with Foppendorf

### Publication Information
- **Original Source:** "Johann Elias Schlegel: Die entführte Dose. Ein Lustspiel in einem Aufzuge. In: Joh. Elias Schlegels Werke. Zweyter Theil. Herausgegeben von Johann Heinrich Schlegeln. Kopenhagen und Leipzig: Mummische Buchhandlung 1762, S. 619–635."
- **Wikidata ID:** Q124217835

## Analysis and Conclusion

**Evidence for Foppendorf as Protagonist:**

1. **Speech Activity:** Highest number of speech acts (42) and word count (895)
2. **Scene Presence:** Appears in 3 out of 4 scenes (75% of the play)
3. **Network Centrality:** 
   - Highest degree centrality (4)
   - Highest betweenness centrality (0.5)
   - Perfect closeness centrality (1)
   - Highest eigenvector centrality (0.523)
4. **Relationship Centrality:** Other characters are associated with him (Glocke)

**Final Answer:** Foppendorf is the protagonist of "Die entführte Dose" by Johann Elias Schlegel (1740), as evidenced by his dominant presence in speech, scenes, and network centrality metrics.

## API Endpoints Used

1. `/corpora` - List all available drama corpora
2. `/corpora/ger` (filtered by title) - Search for plays by title in German corpus
3. `/corpora/ger/plays/schlegel-die-entfuehrte-dose/characters` - Get character information and network metrics
4. `/corpora/ger/plays/schlegel-die-entfuehrte-dose` - Get complete play metadata

## Tools and Methods

- **DraCor API:** Comprehensive digital drama corpus analysis
- **Network Analysis:** Character centrality metrics (degree, betweenness, closeness, eigenvector)
- **Quantitative Analysis:** Speech acts, word counts, scene presence
- **Metadata Analysis:** Publication information, character relationships, play structure