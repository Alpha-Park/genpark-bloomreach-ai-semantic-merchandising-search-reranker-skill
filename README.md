# genpark-bloomreach-ai-semantic-merchandising-search-reranker-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![MCP SDK](https://img.shields.io/badge/MCP-SDK_Required-blue?style=for-the-badge)](requirements.txt)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

Bloomreach-inspired AI Semantic E-Commerce Search & Merchandising Reranker. Parses customer shopping intent, expands synonyms, applies visual/category boost & bury rules, and balances semantic relevance against gross margin & stock availability.

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

---

## 🌟 Key Features

- **Standard-Library Client**: The core algorithms use the standard library; the MCP server requires Python 3.10+ and the MCP SDK.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Public Repository**: Source and documentation are maintained under `Alpha-Park`.

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
from client import BloomreachAISemanticMerchandisingReranker

def main():
    reranker = BloomreachAISemanticMerchandisingReranker()
    catalog = [
        {"id": "p1", "title": "White Runner Trainers", "category": "Footwear", "price": 120.0, "margin_rate": 0.45, "stock": 15, "tags": ["sneakers", "running"]},
        {"id": "p2", "title": "Vintage Leather Boots", "category": "Footwear", "price": 250.0, "margin_rate": 0.30, "stock": 0, "tags": ["boots", "leather"]},
        {"id": "p3", "title": "Merino Wool Pullover", "category": "Apparel", "price": 85.0, "margin_rate": 0.60, "stock": 25, "tags": ["sweater", "hoodie"]}
    ]
    rules = {"boost_categories": ["Footwear"], "bury_categories": ["Apparel"]}
    result = reranker.rerank_catalog("athletic sneakers", catalog, rules)
    print("--- Bloomreach AI Discovery Rerank Output ---")
    print(f"Query: {result['query']} | Intent Tokens: {result['intent_analysis']['expanded_tokens']}")
    for idx, item in enumerate(result['top_products'], 1):
        print(f"{idx}. {item['title']} - Score: {item['discovery_score']} (Stock: {item['stock']}, Margin: {item['margin_rate']})")

if __name__ == "__main__":
    main()

```

### 2. Run as Model Context Protocol (MCP) Server

The core Python client uses only the standard library. Running the MCP server requires **Python 3.10+** and the official **`mcp>=1.0.0,<2` SDK**. From the repository directory:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

On Windows, use `.venv\Scripts\python.exe` instead. Configure the MCP client to use this environment's Python executable. The server runs locally over stdio; the GitHub repository URL is not a remote MCP endpoint.


Start standard JSON-RPC 2.0 server over `stdio`:

```bash
.venv/bin/python mcp_server.py
```

Validate the MCP connection with a client by completing `initialize` and requesting `tools/list`.

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)
