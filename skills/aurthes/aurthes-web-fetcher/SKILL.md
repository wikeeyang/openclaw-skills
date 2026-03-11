---
name: web-fetcher
version: 1.0.0
description: Fetch web pages and convert to Markdown for AI reading. Use when you need to read the content of a specific URL. Automatically tries multiple conversion services for best compatibility.
---

# Web Fetcher

Convert any URL to Markdown format for easy AI reading.

## Usage

When user asks to fetch/read/crawl a URL, use these services in order:

1. **r.jina.ai/** - Most reliable, try first
   ```
   https://r.jina.ai/https://example.com
   ```

2. **markdown.new/** - Good for Cloudflare-protected sites
   ```
   https://markdown.new/https://example.com
   ```

3. **defuddle.md/** - Alternative fallback
   ```
   https://defuddle.md/https://example.com
   ```

## Strategy

1. Try r.jina.ai first
2. If it fails or returns incomplete content, try markdown.new
3. If still failing, try defuddle.md
4. Extract the relevant information from the Markdown response

## Examples

- User: "Read this article" → Fetch with r.jina.ai
- User: "What's on this page?" → Convert URL and extract content
- User: "Crawl this website" → Iterate through pages as needed
