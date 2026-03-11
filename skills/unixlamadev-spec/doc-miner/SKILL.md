---
name: doc-miner
description: Extract key points, summary, and answers from any PDF or webpage URL
acceptLicenseTerms: true
metadata:
  clawdbot:
    emoji: "📄"
    homepage: https://aiprox.dev
    requires:
      env:
        - AIPROX_SPEND_TOKEN
---

# Doc Miner

Extract insights, key points, and answers from PDFs and webpages. Ask questions about documents or get comprehensive summaries.

## When to Use

- Summarizing long PDFs or articles
- Extracting specific information from documents
- Answering questions about document contents
- Research and literature review

## Usage Flow

1. Provide a URL to a PDF or webpage
2. Specify what to extract or questions to answer
3. AIProx routes to the doc-miner agent
4. Returns answer, summary, and key_points array

## Security Manifest

| Permission | Scope | Reason |
|------------|-------|--------|
| Network | aiprox.dev | API calls to orchestration endpoint |
| Env Read | AIPROX_SPEND_TOKEN | Authentication for paid API |

## Make Request

```bash
curl -X POST https://aiprox.dev/api/orchestrate \
  -H "Content-Type: application/json" \
  -H "X-Spend-Token: $AIPROX_SPEND_TOKEN" \
  -d '{
    "task": "What are the main findings and recommendations?",
    "url": "https://example.com/report.pdf"
  }'
```

### Response

```json
{
  "answer": "The report identifies three main findings: increased user engagement, declining conversion rates, and opportunities in mobile.",
  "summary": "Q3 2024 product analytics report covering user metrics, conversion funnels, and strategic recommendations for mobile-first approach.",
  "key_points": [
    "User engagement up 23% quarter-over-quarter",
    "Mobile conversion rate 40% below desktop",
    "Recommendation: prioritize mobile UX improvements"
  ]
}
```

## Trust Statement

Doc Miner fetches and analyzes document contents via URL. Documents are processed transiently and not stored. Analysis is performed by Claude via LightningProx. Your spend token is used for payment only.
