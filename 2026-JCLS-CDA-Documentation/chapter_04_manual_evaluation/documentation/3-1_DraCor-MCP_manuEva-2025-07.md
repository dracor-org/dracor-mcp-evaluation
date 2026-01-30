# DraCor Analysis Documentation

## Metadata
- **Date**: July 15, 2025
- **Query**: "Which drama corpus has the highest mean number of characters?"
- **Tools Used**: DraCor API, JavaScript analysis tool (REPL)
- **API Base URL**: https://staging.dracor.org/api/v1/
- **Analysis Method**: Statistical calculation of mean characters per play across all corpora

## Initial Query
**Human**: Which drama corpus has the highest mean number of characters?

## Step 1: Retrieve All Available Corpora

**Tool Used**: `DraCor:get_corpora`
**API Endpoint**: `/corpora`
**Purpose**: Get comprehensive list of all drama corpora with their metadata and metrics

### API Response Summary
The API returned data for 26 drama corpora with the following key metrics for each:
- `name`: Corpus identifier
- `title`: Full corpus name
- `acronym`: Corpus acronym
- `characters`: Total number of characters in corpus
- `plays`: Total number of plays in corpus
- `metrics`: Various statistics including character counts, word counts, etc.

### Complete Corpora List Retrieved:
1. **Alsatian Drama Corpus (AlsDraCor)** - 375 characters, 30 plays
2. **American Drama Corpus (AmDraCor)** - 762 characters, 40 plays
3. **Bashkir Drama Corpus (BashDraCor)** - 56 characters, 3 plays
4. **Calderón Drama Corpus (CalDraCor)** - 3406 characters, 205 plays
5. **Czech Drama Corpus (CzeDraCor)** - 364 characters, 11 plays
6. **Dutch Drama Corpus (DutchDraCor)** - 2175 characters, 186 plays
7. **English Drama Corpus (EngDraCor)** - 10689 characters, 435 plays
8. **French Drama Corpus (FreDraCor)** - 17831 characters, 1940 plays
9. **Georgian Drama Corpus (GeorgDraCor)** - 17 characters, 1 play
10. **German Drama Corpus (GerDraCor)** - 15870 characters, 736 plays
11. **German Shakespeare Drama Corpus (GerShDraCor)** - 1497 characters, 38 plays
12. **Greek Drama Corpus (GreekDraCor)** - 449 characters, 40 plays
13. **Hungarian Drama Corpus (HunDraCor)** - 1718 characters, 74 plays
14. **Italian Drama Corpus (ItaDraCor)** - 1768 characters, 157 plays
15. **Neo-Latin Drama Corpus (NeoLatDraCor)** - 72 characters, 4 plays
16. **Polish Drama Corpus (PolDraCor)** - 586 characters, 50 plays
17. **Romanian Drama Corpus (RoDraCor)** - 332 characters, 20 plays
18. **Roman Drama Corpus (RomDraCor)** - 405 characters, 36 plays
19. **Russian Drama Corpus (RusDraCor)** - 3707 characters, 212 plays
20. **Shakespeare Drama Corpus (ShakeDraCor)** - 1433 characters, 37 plays
21. **Spanish Drama Corpus (SpanDraCor)** - 580 characters, 25 plays
22. **Swedish Drama Corpus (SweDraCor)** - 769 characters, 68 plays
23. **Tatar Drama Corpus (TatDraCor)** - 30 characters, 3 plays
24. **Test Drama Corpus (TestDraCor)** - 93 characters, 4 plays
25. **Ukrainian Drama Corpus (UDraCor)** - 1091 characters, 45 plays
26. **Yiddish Drama Corpus (YiDraCor)** - 119 characters, 8 plays

## Step 2: Statistical Analysis

**Tool Used**: JavaScript analysis tool (REPL)
**Purpose**: Calculate mean characters per play for each corpus and rank them

### Calculation Method
```javascript
meanCharacters = totalCharacters / totalPlays
```

### JavaScript Code Executed:
```javascript
// Data from the DraCor API response
const corporaData = [
  { name: "als", acronym: "AlsDraCor", title: "Alsatian Drama Corpus", characters: 375, plays: 30 },
  { name: "am", acronym: "AmDraCor", title: "American Drama Corpus", characters: 762, plays: 40 },
  { name: "bash", acronym: "BashDraCor", title: "Bashkir Drama Corpus", characters: 56, plays: 3 },
  { name: "cal", acronym: "CalDraCor", title: "Calderón Drama Corpus", characters: 3406, plays: 205 },
  { name: "cze", acronym: "CzeDraCor", title: "Czech Drama Corpus", characters: 364, plays: 11 },
  { name: "dutch", acronym: "DutchDraCor", title: "Dutch Drama Corpus", characters: 2175, plays: 186 },
  { name: "eng", acronym: "EngDraCor", title: "English Drama Corpus", characters: 10689, plays: 435 },
  { name: "fre", acronym: "FreDraCor", title: "French Drama Corpus", characters: 17831, plays: 1940 },
  { name: "georg", acronym: "GeorgDraCor", title: "Georgian Drama Corpus", characters: 17, plays: 1 },
  { name: "ger", acronym: "GerDraCor", title: "German Drama Corpus", characters: 15870, plays: 736 },
  { name: "gersh", acronym: "GerShDraCor", title: "German Shakespeare Drama Corpus", characters: 1497, plays: 38 },
  { name: "greek", acronym: "GreekDraCor", title: "Greek Drama Corpus", characters: 449, plays: 40 },
  { name: "hun", acronym: "HunDraCor", title: "Hungarian Drama Corpus", characters: 1718, plays: 74 },
  { name: "ita", acronym: "ItaDraCor", title: "Italian Drama Corpus", characters: 1768, plays: 157 },
  { name: "neolat", acronym: "NeoLatDraCor", title: "Neo-Latin Drama Corpus", characters: 72, plays: 4 },
  { name: "pol", acronym: "PolDraCor", title: "Polish Drama Corpus", characters: 586, plays: 50 },
  { name: "ro", acronym: "RoDraCor", title: "Romanian Drama Corpus", characters: 332, plays: 20 },
  { name: "rom", acronym: "RomDraCor", title: "Roman Drama Corpus", characters: 405, plays: 36 },
  { name: "rus", acronym: "RusDraCor", title: "Russian Drama Corpus", characters: 3707, plays: 212 },
  { name: "shake", acronym: "ShakeDraCor", title: "Shakespeare Drama Corpus", characters: 1433, plays: 37 },
  { name: "span", acronym: "SpanDraCor", title: "Spanish Drama Corpus", characters: 580, plays: 25 },
  { name: "swe", acronym: "SweDraCor", title: "Swedish Drama Corpus", characters: 769, plays: 68 },
  { name: "tat", acronym: "TatDraCor", title: "Tatar Drama Corpus", characters: 30, plays: 3 },
  { name: "test", acronym: "TestDraCor", title: "Test Drama Corpus", characters: 93, plays: 4 },
  { name: "u", acronym: "UDraCor", title: "Ukrainian Drama Corpus", characters: 1091, plays: 45 },
  { name: "yi", acronym: "YiDraCor", title: "Yiddish Drama Corpus", characters: 119, plays: 8 }
];

// Calculate mean characters per play for each corpus
const results = corporaData.map(corpus => ({
  ...corpus,
  meanCharacters: corpus.characters / corpus.plays
}));

// Sort by mean characters per play (descending)
results.sort((a, b) => b.meanCharacters - a.meanCharacters);
```

## Step 3: Results Analysis

### Complete Rankings (Mean Characters per Play):

1. **German Shakespeare Drama Corpus (GerShDraCor)**: 39.39 characters per play
   - Total characters: 1497, Total plays: 38

2. **Shakespeare Drama Corpus (ShakeDraCor)**: 38.73 characters per play
   - Total characters: 1433, Total plays: 37

3. **Czech Drama Corpus (CzeDraCor)**: 33.09 characters per play
   - Total characters: 364, Total plays: 11

4. **English Drama Corpus (EngDraCor)**: 24.57 characters per play
   - Total characters: 10689, Total plays: 435

5. **Ukrainian Drama Corpus (UDraCor)**: 24.24 characters per play
   - Total characters: 1091, Total plays: 45

6. **Test Drama Corpus (TestDraCor)**: 23.25 characters per play
   - Total characters: 93, Total plays: 4

7. **Hungarian Drama Corpus (HunDraCor)**: 23.22 characters per play
   - Total characters: 1718, Total plays: 74

8. **Spanish Drama Corpus (SpanDraCor)**: 23.20 characters per play
   - Total characters: 580, Total plays: 25

9. **German Drama Corpus (GerDraCor)**: 21.56 characters per play
   - Total characters: 15870, Total plays: 736

10. **American Drama Corpus (AmDraCor)**: 19.05 characters per play
    - Total characters: 762, Total plays: 40

11. **Bashkir Drama Corpus (BashDraCor)**: 18.67 characters per play
    - Total characters: 56, Total plays: 3

12. **Neo-Latin Drama Corpus (NeoLatDraCor)**: 18.00 characters per play
    - Total characters: 72, Total plays: 4

13. **Russian Drama Corpus (RusDraCor)**: 17.49 characters per play
    - Total characters: 3707, Total plays: 212

14. **Georgian Drama Corpus (GeorgDraCor)**: 17.00 characters per play
    - Total characters: 17, Total plays: 1

15. **Calderón Drama Corpus (CalDraCor)**: 16.61 characters per play
    - Total characters: 3406, Total plays: 205

16. **Romanian Drama Corpus (RoDraCor)**: 16.60 characters per play
    - Total characters: 332, Total plays: 20

17. **Yiddish Drama Corpus (YiDraCor)**: 14.88 characters per play
    - Total characters: 119, Total plays: 8

18. **Alsatian Drama Corpus (AlsDraCor)**: 12.50 characters per play
    - Total characters: 375, Total plays: 30

19. **Polish Drama Corpus (PolDraCor)**: 11.72 characters per play
    - Total characters: 586, Total plays: 50

20. **Dutch Drama Corpus (DutchDraCor)**: 11.69 characters per play
    - Total characters: 2175, Total plays: 186

21. **Swedish Drama Corpus (SweDraCor)**: 11.31 characters per play
    - Total characters: 769, Total plays: 68

22. **Italian Drama Corpus (ItaDraCor)**: 11.26 characters per play
    - Total characters: 1768, Total plays: 157

23. **Roman Drama Corpus (RomDraCor)**: 11.25 characters per play
    - Total characters: 405, Total plays: 36

24. **Greek Drama Corpus (GreekDraCor)**: 11.22 characters per play
    - Total characters: 449, Total plays: 40

25. **Tatar Drama Corpus (TatDraCor)**: 10.00 characters per play
    - Total characters: 30, Total plays: 3

26. **French Drama Corpus (FreDraCor)**: 9.19 characters per play
    - Total characters: 17831, Total plays: 1940

## Final Answer

**The German Shakespeare Drama Corpus (GerShDraCor) has the highest mean number of characters per play with 39.39 characters per play.**

### Key Details:
- **Corpus**: German Shakespeare Drama Corpus (GerShDraCor)
- **Mean Characters per Play**: 39.39
- **Total Characters**: 1497
- **Total Plays**: 38
- **Description**: Contains German translations of Shakespeare's plays published by Schlegel and Tieck

### Analysis Notes:
- The German Shakespeare corpus narrowly beats the original Shakespeare corpus (38.73 characters per play)
- Shakespeare's works consistently show high character counts due to their complexity and scope
- The French corpus, despite having the most characters overall (17,831), has the lowest mean (9.19) due to its large number of plays (1,940)
- Smaller corpora with few plays can show high variability in mean calculations

## Tools and Endpoints Summary

### DraCor API Tools Used:
1. **`DraCor:get_corpora`**
   - Endpoint: `/corpora`
   - Purpose: Retrieved metadata and metrics for all 26 drama corpora
   - Data obtained: Character counts, play counts, and descriptive information

### Analysis Tools Used:
1. **JavaScript REPL (analysis tool)**
   - Purpose: Statistical calculation and ranking
   - Operations: Mean calculation, array sorting, data formatting
   - Output: Complete ranked list of corpora by mean characters per play

### Data Processing Steps:
1. API data extraction
2. Mean calculation (characters/plays)
3. Descending sort by mean
4. Formatted output with rankings

This documentation provides a complete record of the methodology, tools, and data used to answer the initial research question about which drama corpus has the highest mean number of characters.