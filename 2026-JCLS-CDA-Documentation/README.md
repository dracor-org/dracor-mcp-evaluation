# Agentic DraCor – Evaluation Documentation (JCLS CDA Special Issue)

This directory contains the documentation, curated benchmark data, scripts, and experimental results accompanying the article

> **Agentic DraCor. Implementing and Evaluating MCP-Enabled Tool Use for Humanities Data**  
> Peer Trilcke, Ingo Börner, Henny Sluyter-Gäthje, Daniil Skorinkin, Frank Fischer, Carsten Milling  
> *Journal of Computational Literary Studies*, Special Issue (CDA Workshop)

---

## Structure of this folder

The folder is organized along the logical structure of the article:

chapter_01_introduction/ Documentation of example interactions
chapter_04_manual_evaluation/ Manual (phenomenological) evaluation experiments
chapter_05_automated_evaluation/ Automated evaluation pipeline, benchmarks, and results


Each chapter folder contains documentation and artefacts relevant to the corresponding section of the paper.

---

## Manual Evaluation (`chapter_04_manual_evaluation`)

This section documents the **manual evaluation (manuEva)** experiments conducted via the Claude Desktop interface with a locally running DraCor MCP server.

It includes:
- Markdown transcripts of documented interactions
- Commentary notes by the researchers
- References to the evaluation criteria used in the paper (answer correctness, tool-call efficiency, tool-use reliability)

These materials form the empirical basis for Chapter 4 of the article.

---

## Automated Evaluation (`chapter_05_automated_evaluation`)

This section contains the full documentation of the **automated evaluation pipeline (autoEva)** described in Chapter 5.

### Contents

- `scripts/`  
  Python scripts used to run the evaluation, collect model responses, and compute metrics.

- `curated_data/`  
  Manually curated benchmark data used for evaluation, including:
  - gold-standard answers
  - lists of valid tools per task
  - reference tool chains
  - expected optimal tool-chain lengths

- `results/`  
  Model outputs for the two tested LLMs (Claude Sonnet-4, Haiku-4-5).

- `results_analysed/`  
  Efficiency evaluation results for the two tested LLMs (Claude Sonnet-4, Haiku-4-5) that were derived from the `results/`. Corresponds to 5.2 in the paper.

-  `results_validated` 
  Reliability evaluation data for the two tested LLMs (Claude Sonnet-4, Haiku-4-5). This is the data used for the evaluation in part 5.2.3 in the paper.

- `notebooks/`  
  Evaluation and validation notebooks used during analysis.

- `figures/`  
  Plots and diagrams used in the article.

### Evaluation criteria

The automated evaluation operationalizes the following criteria:

- **Answer Correctness** (direct and normalized match)
- **Tool-Call Efficiency**
  - Tool-Call Complexity
  - Tool-Call Absurdity
  - Tool-Call Error Rate
- **Tool-Use Reliability**, operationalized via
  - number of unique answers
  - Gini impurity as a diversity measure

The evaluation focuses on *reliability-as-repeatability*, not on semantic plausibility.

---

## Scope and limitations

These materials are **not intended as a general-purpose MCP benchmarking framework**.  
They document a concrete experimental setup tied to:

- specific versions of the DraCor MCP server
- specific versions of Anthropic models
- a defined set of research-oriented prompts

Due to rapid changes in LLM tooling, exact reproduction may require version alignment, which is discussed in the article.

---

## Relation to archived versions

A long-term archived version of this repository, including this documentation, will be deposited on **Zenodo** in connection with the final publication of the article.

---

## License

Unless stated otherwise, documentation and code in this folder are released under **CC BY 4.0**.

