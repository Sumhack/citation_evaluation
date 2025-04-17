# 📊 Citation Quality Evaluator

This project evaluates the quality and necessity of citations in AI-generated text. It uses the OpenAI GPT-4 API to assess how well citations support factual statements in an assistant's response.

## 🚀 Features

- Calculates **Recall**, **Precision**, and **F1 Score** for cited statements.
- Provides explanations (reasoning) for these metrics.
- Determines whether uncited statements **require a citation**.
- Tracks OpenAI **token usage** for cost estimation.
- Outputs results to both **JSON** and **CSV** formats.

---

## 📂 Input Format

The input CSV should contain the following columns:

| Column Name       | Description                                                  |
|------------------|--------------------------------------------------------------|
| `question`        | The user's original question                                 |
| `response`        | The AI assistant's full response                             |
| `context_id`      | An identifier for the context/session                        |
| `statement_index` | Index of the current statement in the response               |
| `statement`       | A single statement from the response                         |
| `citations`       | Citation references (can be empty `[]`)                      |
| `snippets`        | Citation text snippets used to support the statement         |
| `documents`       | Source documents related to the citations                    |

---

## 📤 Output Files

- `output_data_with_usage.json`: Contains detailed evaluation results in JSON format.
- `output_data_with_usage_and_metrics.csv`: Contains tabular results, including:
  - Recall, Precision, F1 Score
  - Reasoning for recall and precision
  - Citation need status and analysis
  - Token usage data

---

## 🧠 Evaluation Logic

### For Statements with Citations:
- **Recall**: Is the statement actually supported by the citations?
- **Precision**: Are the citations relevant to the statement?
- **F1 Score**: Harmonic mean of Recall and Precision.

### For Statements Without Citations:
- The model checks if the statement is a factual claim that **requires a citation** or is an introductory/summary/transition sentence that does not.

---

## ⚙️ Requirements

- Python 3.8+
- OpenAI Python SDK

Install dependencies:

```bash
pip install openai
