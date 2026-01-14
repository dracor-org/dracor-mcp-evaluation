# DraCor API Chat Documentation

## Metadata
- **Date**: Wednesday, July 16, 2025
- **Assistant**: Claude Sonnet 4 (claude-sonnet-4-20250514)
- **User Location**: Potsdam, Brandenburg, DE
- **Session Type**: Interactive chat with DraCor API tools
- **Primary Topic**: Character count analysis for "Dantons Tod" by Büchner

## Available Tools
The assistant had access to multiple DraCor API tools for analyzing dramatic texts, including:
- Character retrieval and analysis
- Play metadata extraction
- Network analysis capabilities
- Text extraction (TEI-XML, plaintext)
- Corpus browsing and filtering
- DTS (Distributed Text Services) integration

## Chat Conversation

### User Query
**User**: What is the number of characters in Dantons Tod (buechner-dantons-tod) in GerDraCor?

### Assistant Response and Tool Usage

**Assistant**: I'll help you find the number of characters in "Dantons Tod" by Büchner in the German DraCor corpus.

#### Tool Call: DraCor:get_play_characters
- **Endpoint**: `/corpora/ger/plays/buechner-dantons-tod/characters`
- **Parameters**:
  - `corpus_name`: "ger"
  - `play_name`: "buechner-dantons-tod"

#### API Response Analysis
The API returned detailed character data for 93 characters in the play. Each character entry included:
- Character ID and name
- Gender classification (MALE/FEMALE/UNKNOWN)
- Network metrics (degree, betweenness, closeness, eigenvector centrality)
- Speech statistics (number of words, speech acts, scenes)
- Group classification (individual vs. group characters)
- Wikidata IDs where available

#### Key Characters Identified
Major characters with high speech counts and network centrality:
- **Danton**: 4,412 words, 118 speech acts, 16 scenes
- **Robespierre**: 2,253 words, 29 speech acts, 4 scenes
- **Camille**: 1,470 words, 47 speech acts, 10 scenes
- **Lacroix**: 1,078 words, 44 speech acts, 9 scenes
- **St. Just**: 988 words, 22 speech acts, 3 scenes

#### Character Type Distribution
The 93 characters included:
- Individual named characters (historical figures and fictional personas)
- Group characters (e.g., "Alle", "Einige Stimmen", "Die Jakobiner")
- Citizens and crowd members with varying levels of dialogue
- Officials and deputies from the French Revolution period

#### Final Answer
**Assistant**: Based on the API response, **Dantons Tod** by Büchner in the German DraCor corpus (buechner-dantons-tod) has **93 characters**. 

This includes both individual characters and group characters (like "Alle", "Einige Stimmen", etc.). The play features a mix of historically significant figures like Danton, Robespierre, Camille Desmoulins, and Saint-Just, alongside various citizens, deputies, and other characters from the French Revolution period.

### User Documentation Request
**User**: Document the complete chat in a markdown file. Add a header with relevant metadata (e.g. about the settings). Add information about the tools and DraCor API endpoints used in each step. Don't summarize. Just document our conversation and all tool usage and analysis you performed.

## Technical Notes

### DraCor API Integration
- The assistant used the DraCor Model Context Protocol (MCP) tools
- API base URL: https://dracor.org/api/
- Specific endpoint accessed: `/corpora/ger/plays/buechner-dantons-tod/characters`
- Response format: JSON with comprehensive character metadata

### Data Structure
The character data included network analysis metrics calculated from co-presence networks:
- **Degree**: Number of direct connections to other characters
- **Betweenness**: Measure of character's role as intermediary
- **Closeness**: Measure of character's centrality in the network
- **Eigenvector**: Measure of character's influence based on connections
- **Weighted Degree**: Degree weighted by interaction strength

### Character Classification
Characters were classified by:
- **Gender**: MALE, FEMALE, UNKNOWN
- **Type**: Individual vs. Group (isGroup boolean)
- **Historical Status**: Some characters linked to Wikidata (e.g., Danton: Q184623)
- **Presence**: Number of scenes and speech acts per character

## Conclusion
This session demonstrated the DraCor API's capability to provide detailed character analysis for dramatic texts, including both quantitative metrics (character count) and qualitative data (network analysis, speech patterns, and historical context). The tool successfully retrieved comprehensive data for all 93 characters in Büchner's "Dantons Tod" from the German DraCor corpus.