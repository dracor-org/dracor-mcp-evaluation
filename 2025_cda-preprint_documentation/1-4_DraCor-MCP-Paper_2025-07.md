# DraCor Chat Documentation

## Metadata

**Date:** Tuesday, July 15, 2025  
**Assistant:** Claude Sonnet 4  
**Model:** claude-sonnet-4-20250514  
**Tools Available:** DraCor API tools, Web Search, Artifacts, Analysis Tool  
**Primary Tool Used:** DraCor API  

## Initial Question

**User:** What is the number of characters in Dantons Tod (buechner-dantons-tod) in GerDraCor?

## Step-by-Step Documentation

### Step 1: Tool Selection and API Call

**Tool Used:** `DraCor:get_play_characters`  
**API Endpoint:** `/corpora/{corpusname}/plays/{playname}/characters`  
**Parameters:**
- `corpus_name`: "ger" (German DraCor corpus)
- `play_name`: "buechner-dantons-tod"

**Function Call:**
```
DraCor:get_play_characters(corpus_name="ger", play_name="buechner-dantons-tod")
```

### Step 2: API Response Analysis

**Response Structure:** JSON object containing a "characters" array with 103 character objects.

**Character Data Structure:** Each character object contains:
- `id`: Character identifier
- `name`: Character name
- `sex`: Gender (MALE, FEMALE, UNKNOWN)
- `isGroup`: Boolean indicating if character represents a group
- `numOfWords`: Number of words spoken
- `numOfSpeechActs`: Number of speech acts
- `numOfScenes`: Number of scenes character appears in
- `wikidataId`: Wikidata identifier (where available)
- Network metrics: `degree`, `betweenness`, `closeness`, `eigenvector`, `weightedDegree`

### Step 3: Data Processing

**Method:** Direct count of array elements in the "characters" field.

**Result:** 103 characters total

### Step 4: Character Analysis

**Character Types Identified:**
1. **Historical Figures:** Danton, Robespierre, Camille, St. Just, etc.
2. **Individual Characters:** Julie, Marion, Lucile, etc.
3. **Group Characters:** "Alle" (All), "Einige Stimmen" (Some Voices), "Die Jakobiner" (The Jacobins), etc.
4. **Generic Roles:** "Erster Bürger" (First Citizen), "Zweiter Bürger" (Second Citizen), etc.

**Notable Characters by Speech Volume:**
- Danton: 4,412 words, 118 speech acts
- Robespierre: 2,253 words, 29 speech acts
- Camille: 1,470 words, 47 speech acts
- Lacroix: 1,078 words, 44 speech acts
- St. Just: 988 words, 22 speech acts

### Step 5: Answer Formulation

**Final Answer:** Büchner's "Dantons Tod" in the German DraCor corpus (GerDraCor) has **103 characters**.

**Additional Context Provided:**
- Play represents French Revolution period
- Mix of historical figures and fictional/generic characters
- Includes both individual characters and group voices
- Reflects the play's focus on both individual personalities and mass movements

## Technical Details

**API Response Format:** JSON
**Data Completeness:** Full character list with comprehensive metadata
**Network Analysis:** Characters include social network analysis metrics
**Encoding:** TEI-XML based data structure
**Corpus:** German Drama Corpus (GerDraCor)

## Query Efficiency

**Single API Call:** Question answered with one targeted API call
**Direct Data Access:** No additional processing or filtering required
**Response Time:** Immediate (single tool invocation)
**Data Reliability:** Official DraCor database with structured metadata

## Character Distribution Summary

**Gender Distribution:**
- Male characters: Majority
- Female characters: Minority
- Unknown/Group characters: Various collective voices

**Character Types:**
- Named historical figures
- Named fictional characters
- Generic role-based characters
- Group/collective voices
- Scene-specific characters

**Wikidata Integration:** Many characters linked to Wikidata entities (e.g., Danton: Q184623)

## Conversation Flow

1. **User Question:** Direct inquiry about character count
2. **Tool Selection:** Immediate identification of appropriate DraCor API endpoint
3. **API Call:** Single targeted request to character endpoint
4. **Data Processing:** Count of returned character array
5. **Answer Delivery:** Precise numerical answer with contextual information
6. **Documentation Request:** User requested full conversation documentation

## API Endpoint Details

**Full Endpoint:** `/corpora/ger/plays/buechner-dantons-tod/characters`  
**HTTP Method:** GET  
**Response Type:** JSON  
**Data Source:** DraCor (Drama Corpora project)  
**Corpus Identifier:** "ger" (German corpus)  
**Play Identifier:** "buechner-dantons-tod"  

## Data Validation

**Character Count Verification:** 103 characters confirmed by array length
**Data Integrity:** All character objects contain required fields
**Metadata Completeness:** Full character information including network metrics
**Historical Accuracy:** Character names correspond to historical figures from French Revolution period