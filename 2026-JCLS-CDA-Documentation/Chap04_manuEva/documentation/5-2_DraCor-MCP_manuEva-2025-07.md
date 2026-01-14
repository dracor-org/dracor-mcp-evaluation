# DraCor Chat Documentation - Emilia Galotti Protagonist Query

## Metadata
- **Date**: Tuesday, July 15, 2025
- **Model**: Claude Sonnet 4 (claude-sonnet-4-20250514)
- **Query Type**: Literary character analysis using DraCor API
- **Primary Tool**: DraCor API functions
- **Corpus**: German Drama Corpus (ger)
- **Play**: lessing-emilia-galotti

## Chat Session Documentation

### Initial User Query
**User**: "Who is the protagonist in Emilia Galotti?"

### Assistant Response Process

#### Step 1: Tool Selection and API Call
The assistant identified this as a question about a specific play and selected the DraCor API to retrieve character information.

**Tool Used**: `DraCor:get_play_characters`
**API Endpoint**: `/corpora/{corpusname}/plays/{playname}/characters`
**Parameters**:
- `corpus_name`: "ger" (German Drama Corpus)
- `play_name`: "lessing-emilia-galotti"

#### Step 2: API Response Data
The DraCor API returned comprehensive character data including network metrics for all 13 characters in the play:

**Complete Character List with Metrics**:

1. **Der Prinz**
   - Scenes: 17
   - Sex: MALE
   - Betweenness: 0.46717171717171724
   - Degree: 8
   - Words: 4002
   - Closeness: 0.75
   - ID: "der_prinz"
   - Speech Acts: 157
   - Eigenvector: 0.32076106311648156
   - Weighted Degree: 20

2. **Der Kammerdiener**
   - Scenes: 2
   - Sex: MALE
   - Betweenness: 0
   - Degree: 1
   - Words: 33
   - Closeness: 0.4444444444444444
   - ID: "der_kammerdiener"
   - Speech Acts: 6
   - Eigenvector: 0.05575792046031641
   - Weighted Degree: 2

3. **Conti**
   - Scenes: 2
   - Sex: MALE
   - Betweenness: 0
   - Degree: 1
   - Words: 604
   - Closeness: 0.4444444444444444
   - ID: "conti"
   - Speech Acts: 24
   - Eigenvector: 0.05575792046031641
   - Weighted Degree: 2

4. **Marinelli**
   - Scenes: 19
   - Sex: MALE
   - Betweenness: 0.24696969696969698
   - Degree: 9
   - Words: 4343
   - Closeness: 0.8
   - ID: "marinelli"
   - Speech Acts: 221
   - Eigenvector: 0.4489846359321899
   - Weighted Degree: 30

5. **Camillo Rota**
   - Scenes: 1
   - Sex: MALE
   - Betweenness: 0
   - Degree: 1
   - Words: 78
   - Closeness: 0.4444444444444444
   - ID: "camillo_rota"
   - Speech Acts: 6
   - Eigenvector: 0.05575792046031641
   - Weighted Degree: 1

6. **Claudia**
   - Scenes: 13
   - Sex: FEMALE
   - Betweenness: 0.04545454545454544
   - Degree: 7
   - Words: 1581
   - Closeness: 0.6
   - ID: "claudia"
   - Speech Acts: 73
   - Eigenvector: 0.38292603187412266
   - Weighted Degree: 19

7. **Pirro**
   - Scenes: 4
   - Sex: MALE
   - Betweenness: 0.026515151515151516
   - Degree: 5
   - Words: 263
   - Closeness: 0.5454545454545454
   - ID: "pirro"
   - Speech Acts: 25
   - Eigenvector: 0.2719436343371554
   - Weighted Degree: 7

8. **Odoardo**
   - Scenes: 12
   - Sex: MALE
   - Betweenness: 0.05505050505050505
   - Degree: 6
   - Words: 2441
   - Closeness: 0.6666666666666666
   - ID: "odoardo"
   - Speech Acts: 108
   - Eigenvector: 0.3542503929627511
   - Weighted Degree: 15

9. **Angelo**
   - Scenes: 2
   - Sex: MALE
   - Betweenness: 0
   - Degree: 2
   - Words: 487
   - Closeness: 0.48
   - ID: "angelo"
   - Speech Acts: 28
   - Eigenvector: 0.1253177208861109
   - Weighted Degree: 2

10. **Emilia**
    - Scenes: 7
    - Sex: FEMALE
    - Betweenness: 0.05505050505050505
    - Degree: 6
    - Words: 1702
    - Closeness: 0.6666666666666666
    - ID: "emilia"
    - Speech Acts: 64
    - Eigenvector: 0.3513647060457318
    - Weighted Degree: 13

11. **Appiani**
    - Scenes: 5
    - Sex: MALE
    - Betweenness: 0.003787878787878788
    - Degree: 4
    - Words: 852
    - Closeness: 0.5217391304347826
    - ID: "appiani"
    - Speech Acts: 48
    - Eigenvector: 0.2529584931569895
    - Weighted Degree: 8

12. **Battista**
    - Scenes: 4
    - Sex: MALE
    - Betweenness: 0.012121212121212121
    - Degree: 4
    - Words: 152
    - Closeness: 0.6
    - ID: "battista"
    - Speech Acts: 11
    - Eigenvector: 0.26144507771860326
    - Weighted Degree: 7

13. **Orsina**
    - Scenes: 6
    - Sex: FEMALE
    - Betweenness: 0.012121212121212121
    - Degree: 4
    - Words: 2111
    - Closeness: 0.6
    - ID: "orsina"
    - Speech Acts: 64
    - Eigenvector: 0.2619466686163178
    - Weighted Degree: 8

#### Step 3: Data Analysis and Response Formation
The assistant analyzed the character data and determined that despite network metrics showing other characters with higher quantitative measures (such as Marinelli with the highest number of scenes and speech acts), Emilia Galotti is the protagonist based on:

1. **Title Character Status**: The play is named after her
2. **Narrative Centrality**: The plot revolves around her fate
3. **Thematic Significance**: She represents the central conflict of virtue versus corruption

#### Step 4: Final Response
The assistant provided a comprehensive answer identifying Emilia Galotti as the protagonist, explaining:
- Her role as the title character
- Her position as the central figure around whom the tragedy revolves
- The plot elements involving her (Prince's obsession, Marinelli's machinations, engagement to Appiani)
- The thematic significance of her character in relation to the play's exploration of virtue, corruption, and power

### Technical Documentation
- **API Endpoint Used**: `/corpora/ger/plays/lessing-emilia-galotti/characters`
- **Response Format**: JSON with character objects containing network analysis metrics
- **Data Fields Retrieved**: Character names, network centrality measures, speech statistics, scene presence
- **Analysis Method**: Literary interpretation combined with quantitative character data from DraCor's network analysis

### Conclusion
The query was successfully answered using DraCor's character analysis endpoint, which provided both quantitative network metrics and character identification data that supported the literary analysis identifying Emilia Galotti as the protagonist of Lessing's tragedy.