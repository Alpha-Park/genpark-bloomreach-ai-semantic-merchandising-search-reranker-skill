#!/usr/bin/env python3
import json
import sys
from client import BloomreachAISemanticMerchandisingReranker

from typing import Any, Dict, List, Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit("MCP requires the mcp package. Run: python -m pip install -r requirements.txt") from exc

mcp = FastMCP('genpark-bloomreach-ai-semantic-merchandising-search-reranker-skill')

@mcp.tool()
def rerank_catalog(query: str = "", catalog_items: Optional[List[Dict[str, Any]]] = None, merchandising_rules: Optional[Dict[str, Any]] = None) -> str:
    """Rerank supplied catalog items using semantic and merchandising signals."""
    return json.dumps(BloomreachAISemanticMerchandisingReranker().rerank_catalog(query, catalog_items if catalog_items is not None else [], merchandising_rules if merchandising_rules is not None else {}))

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        reranker = BloomreachAISemanticMerchandisingReranker()
        catalog = [
            {"id": "p1", "title": "White Runner Trainers", "category": "Footwear", "price": 120.0, "margin_rate": 0.45, "stock": 15, "tags": ["sneakers", "running"]},
            {"id": "p2", "title": "Vintage Leather Boots", "category": "Footwear", "price": 250.0, "margin_rate": 0.30, "stock": 0, "tags": ["boots", "leather"]},
            {"id": "p3", "title": "Everyday Cotton Tee", "category": "Apparel", "price": 35.0, "margin_rate": 0.50, "stock": 50, "tags": ["t-shirt", "basic"]}
        ]
        res = reranker.rerank_catalog("comfortable sneakers", catalog, {"boost_categories": ["Footwear"]})
        assert res["results_count"] == 3
        assert res["top_products"][0]["id"] == "p1"
        print(f"[TEST PASS] Bloomreach Reranker Passed! Top Pick: {res['top_products'][0]['title']}")
        sys.exit(0)

    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
