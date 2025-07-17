# DraCor French Drama Character Analysis - Session Documentation

## Metadata
- **Date**: July 15, 2025
- **Session Type**: DraCor API Analysis
- **Primary Question**: "What is the mean number of characters in French Drama?"
- **Tools Used**: DraCor API, JavaScript Analysis Tool
- **API Endpoints**: Multiple DraCor endpoints for corpus analysis

## Session Overview
This session involved analyzing the French Drama Corpus in the DraCor database to calculate the mean number of characters per play. The analysis required navigating through various API endpoints to gather the necessary statistical data.

## Step-by-Step Documentation

### Step 1: Initial Corpus Information Request
**User Query**: "What is the mean number of characters in French Drama?"

**Tool Used**: `DraCor:get_corpus`
**API Endpoint**: `/corpora/fre`
**Parameters**: 
- `corpus_name`: "fre"

**Result**: Data exceeded maximum length limit (1,048,576 characters)

### Step 2: Attempting to Get Play List
**Tool Used**: `DraCor:get_minimal_data_of_plays_of_corpus_helper`
**API Endpoint**: Custom helper function for `/corpora/fre`
**Parameters**:
- `corpus_name`: "fre"
- Default pagination settings

**Result**: Successfully retrieved play list with pagination info:
- Total plays: 1,940
- Items per page: 1,940
- Total pages: 1

**Sample Data Retrieved**:
```json
{
  "pagination": {
    "current_page": 1,
    "items_per_page": 1940,
    "total_plays": 1940,
    "total_pages": 1,
    "has_next_page": false,
    "has_previous_page": false
  },
  "plays": [
    {
      "name": "abeille-lyncee",
      "id": "fre000003",
      "title": "Lyncée",
      "yearNormalized": 1678,
      "authors": ["Abeille"]
    }
    // ... additional plays
  ]
}
```

### Step 3: Attempting Full Corpus Metadata
**Tool Used**: `DraCor:get_corpus_metadata`
**API Endpoint**: `/corpora/fre/metadata`
**Parameters**:
- `corpus_name`: "fre"

**Result**: Data exceeded maximum length limit (1,048,576 characters)

### Step 4: Attempting Paginated Metadata
**Tool Used**: `DraCor:get_corpus_metadata_paged_helper`
**API Endpoint**: `/corpora/fre/metadata` (paginated)
**Parameters**:
- `corpus_name`: "fre"
- `items_per_page`: 50
- `page`: 1

**Result**: Error - "name 'corpus' is not defined"

### Step 5: JavaScript Analysis of Initial Data
**Tool Used**: JavaScript Analysis Tool (repl)
**Purpose**: Process the retrieved play data

**Code Executed**:
```javascript
const playData = {
  "pagination": {
    "current_page": 1,
    "items_per_page": 1940,
    "total_plays": 1940,
    "total_pages": 1,
    "has_next_page": false,
    "has_previous_page": false
  },
  "plays": [
    {
      "name": "abeille-lyncee",
      "id": "fre000003",
      "title": "Lyncée",
      "yearNormalized": 1678,
      "authors": ["Abeille"]
    }
  ]
};

console.log("Total plays in French corpus:", playData.pagination.total_plays);
console.log("First few plays:", playData.plays.slice(0, 5));
```

**Output**:
- Total plays in French corpus: 1940
- First few plays: [{"name":"abeille-lyncee","id":"fre000003","title":"Lyncée","yearNormalized":1678,"authors":["Abeille"]}]

### Step 6: Retrieving All Corpora Information
**Tool Used**: `DraCor:get_corpora`
**API Endpoint**: `/corpora`
**Parameters**: None

**Result**: Successfully retrieved comprehensive information about all DraCor corpora, including the French corpus metrics.

**Key French Corpus Data Retrieved**:
```json
{
  "licence": "CC BY-NC-SA 4.0",
  "licenceUrl": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
  "description": "A TEI P5 version of Paul Fièvre's Théâtre Classique",
  "commit": "dc9c2085a9444a959dcf56a07979b03799907f1b",
  "uri": "https://staging.dracor.org/api/v1/corpora/fre",
  "title": "French Drama Corpus",
  "name": "fre",
  "acronym": "FreDraCor",
  "metrics": {
    "text": 1940,
    "sp": 509958,
    "male": 7958,
    "wordcount": {
      "text": 17701440.0,
      "sp": 16295137.0,
      "stage": 393275
    },
    "stage": 48755,
    "characters": 17831,
    "plays": 1940,
    "updated": "2024-10-02T06:35:56.248+02:00",
    "female": 4247
  },
  "repository": "https://github.com/dracor-org/fredracor"
}
```

### Step 7: Final Calculation
**Tool Used**: JavaScript Analysis Tool (repl)
**Purpose**: Calculate the mean number of characters per play

**Code Executed**:
```javascript
// French Drama Corpus statistics
const totalPlays = 1940;
const totalCharacters = 17831;

// Calculate mean number of characters per play
const meanCharacters = totalCharacters / totalPlays;

console.log("French Drama Corpus Statistics:");
console.log("Total plays:", totalPlays);
console.log("Total characters:", totalCharacters);
console.log("Mean number of characters per play:", meanCharacters);
console.log("Mean number of characters per play (rounded):", Math.round(meanCharacters * 100) / 100);
```

**Output**:
- French Drama Corpus Statistics:
- Total plays: 1940
- Total characters: 17831
- Mean number of characters per play: 9.191237113402062
- Mean number of characters per play (rounded): 9.19

## Final Answer
The mean number of characters in French drama is **9.19 characters per play**.

## Data Sources and Methodology
- **Data Source**: DraCor French Drama Corpus (FreDraCor)
- **Corpus Description**: A TEI P5 version of Paul Fièvre's Théâtre Classique
- **License**: CC BY-NC-SA 4.0
- **Total Plays Analyzed**: 1,940 plays
- **Total Characters**: 17,831 characters across all plays
- **Calculation Method**: Simple arithmetic mean (17,831 ÷ 1,940 = 9.19)
- **Last Updated**: October 2, 2024

## API Endpoints Used
1. `/corpora/fre` - French corpus information (failed due to size)
2. `/corpora/fre/metadata` - Corpus metadata (failed due to size)
3. `/corpora` - All corpora information (successful)
4. Helper functions for corpus data retrieval

## Tools and Technologies
- **DraCor API**: Digital Research Infrastructure for European Drama
- **JavaScript Analysis Tool**: For data processing and calculations
- **TEI P5**: Text encoding standard used by the corpus
- **GitHub Repository**: https://github.com/dracor-org/fredracor

## Technical Notes
- Large datasets required pagination or alternative approaches
- Some API endpoints returned data exceeding the maximum response length
- The comprehensive corpora endpoint provided the necessary aggregate statistics
- All calculations were performed using exact values with appropriate rounding for presentation