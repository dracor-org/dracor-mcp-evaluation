# DraCor Chat Documentation: Character Count in Dantons Tod

## Metadata

**Date**: July 15, 2025  
**Query**: "What is the number of characters in Dantons Tod?"  
**Assistant**: Claude Sonnet 4  
**DraCor API**: https://staging.dracor.org/api/v1/  
**Primary Corpus**: German Drama Corpus (ger)  
**Play**: buechner-dantons-tod (Büchner's Dantons Tod)  
**Final Answer**: 103 characters

## Chat Conversation

### Initial Query
**Human**: What is the number of characters in Dantons Tod?

### Assistant Response Process

**Assistant**: I'll look up information about the number of characters in "Dantons Tod" (Danton's Death) by Georg Büchner using the DraCor database.

## Tool Usage Documentation

### Step 1: Get Available Corpora
**Tool**: DraCor:get_corpora  
**API Endpoint**: `/corpora`  
**Purpose**: Retrieve list of all available corpora to identify the appropriate corpus for German drama

**Function Call**:
```
DraCor:get_corpora()
```

**Key Results**: 
- Found 29 corpora available
- Identified German Drama Corpus (ger) as relevant corpus
- Corpus details:
  - Name: "ger"
  - Title: "German Drama Corpus"  
  - Acronym: "GerDraCor"
  - Contains 736 plays
  - 15,870 total characters across all plays
  - Repository: https://github.com/dracor-org/gerdracor

### Step 2: Search for Dantons Tod by Title
**Tool**: DraCor:get_plays_in_corpus_by_title_helper  
**API Endpoint**: `/corpora/ger` (filtered by title)  
**Purpose**: Find the specific play "Dantons Tod" within the German corpus

**Function Call**:
```
DraCor:get_plays_in_corpus_by_title_helper(
  corpus_name="ger",
  title="Dantons Tod"
)
```

**Key Results**:
- Found 1 matching play
- Play details:
  - ID: "ger000085"
  - Name: "buechner-dantons-tod"
  - Title: "Dantons Tod"
  - Subtitle: "Ein Drama"
  - Author: Georg Büchner (Q154014)
  - Year Written: 1835
  - Year Premiered: 1902
  - Network Size: 103
  - Wikidata ID: Q920590
  - URI: https://staging.dracor.org/api/v1/corpora/ger/plays/buechner-dantons-tod

### Step 3: Get Character Details
**Tool**: DraCor:get_play_characters  
**API Endpoint**: `/corpora/ger/plays/buechner-dantons-tod/characters`  
**Purpose**: Retrieve detailed information about all characters in the play

**Function Call**:
```
DraCor:get_play_characters(
  corpus_name="ger",
  play_name="buechner-dantons-tod"
)
```

**Complete Character Data**: 103 characters total

#### Major Characters (Selection):
1. **Danton** (ID: danton)
   - Sex: MALE
   - Scenes: 16
   - Speech Acts: 118
   - Words: 4,412
   - Degree: 43
   - Wikidata: Q184623

2. **Robespierre** (ID: robespierre)
   - Sex: MALE
   - Scenes: 4
   - Speech Acts: 29
   - Words: 2,253
   - Degree: 36

3. **Camille** (ID: camille)
   - Sex: MALE
   - Scenes: 10
   - Speech Acts: 47
   - Words: 1,470
   - Degree: 29

4. **St. Just** (ID: st_just)
   - Sex: MALE
   - Scenes: 3
   - Speech Acts: 22
   - Words: 988
   - Degree: 18

#### Character Categories:
- **Individual Named Characters**: Historical figures (Danton, Robespierre, Camille, etc.)
- **Generic Characters**: Citizens, deputies, prisoners, executioners
- **Group Characters**: "Viele Stimmen" (Many Voices), "Alle" (All), "Einige Stimmen" (Some Voices)
- **Gender Distribution**: Male, Female, and Unknown (for group characters)

#### Character Examples by Type:
- **Historical Figures**: Danton, Robespierre, Camille, St. Just, Legendre
- **Female Characters**: Julie, Marion, Lucile, Rosalie, Adelaide
- **Citizens**: Various numbered citizens (Erster Bürger, Zweiter Bürger, etc.)
- **Officials**: Deputies, presidents, guards, executioners
- **Groups**: "Leute" (People), "Die Jakobiner" (The Jacobins), "Alle" (All)

### Network Analysis Data
The character data includes network analysis metrics:
- **Degree**: Number of connections to other characters
- **Betweenness**: Measure of character's role as intermediary
- **Closeness**: Measure of centrality in the network
- **Eigenvector**: Measure of influence based on connections

### Final Answer Compilation
**Assistant**: Based on the data from the DraCor database, **"Dantons Tod" (Danton's Death) by Georg Büchner contains 103 characters**.

This number includes all speaking characters in the play, ranging from major protagonists like Danton, Robespierre, Camille, and St. Just to minor characters, citizens, groups of people (like "Viele Stimmen" - many voices), and even collective characters like "Alle" (all). The play features a wide variety of character types including historical figures, ordinary citizens, deputies, prisoners, and executioners, reflecting the turbulent social and political atmosphere of the French Revolution that Büchner depicted in his drama.

## Technical Details

### API Endpoints Used:
1. `/corpora` - List all available corpora
2. `/corpora/ger` - German corpus content (filtered by title)
3. `/corpora/ger/plays/buechner-dantons-tod/characters` - Character data for the play

### Data Processing:
- No additional processing required
- Direct count from API response
- Character count confirmed by network size metadata (103)

### Verification:
- Network size from play metadata: 103
- Character array length: 103
- Values match, confirming accuracy