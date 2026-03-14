# toksum

A command-line tool for counting tokens and estimating costs across 300+ Large Language Models (LLMs) from 34+ providers.

[![PyPI version](https://badge.fury.io/py/toksum.svg)](https://badge.fury.io/py/toksum)
[![Python Support](https://img.shields.io/pypi/pyversions/toksum.svg)](https://pypi.org/project/toksum/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features


- **🎯 Production Ready v1.0.1**: Comprehensive support for 300+ models across 34+ providers including OpenAI, Anthropic, Google, Meta, Mistral, Microsoft, Amazon, Nvidia, IBM, Salesforce, BigCode, Databricks, Voyage AI, and many more
- **Comprehensive Multi-LLM Support**: Count tokens for 300+ models across 34 providers including OpenAI, Anthropic, Google, Meta, Mistral, Microsoft, Amazon, Nvidia, IBM, Salesforce, BigCode, Databricks, Voyage AI, and many more
- **Accurate Tokenization**: Uses official tokenizers (tiktoken for OpenAI) and optimized approximations for all other providers
- **Cost Estimation**: Estimate API costs based on token counts and current pricing
- **CLI Friendly**: Simple command-line interface for quick usage
- **Well Tested**: Comprehensive test suite with high coverage
- **Global Model Coverage**: Support for models optimized for Chinese, Russian, and other languages
- **Enterprise & Code Models**: Specialized support for enterprise AI models and code generation models

## Supported Models

### OpenAI Models (49 models)
- GPT-4 (all variants including gpt-4, gpt-4-32k, gpt-4-turbo, gpt-4o, gpt-4o-mini, etc.)
- **O1 Models** (o1-preview, o1-mini, o1-preview-2024-09-12, o1-mini-2024-09-12)
- **NEW: Vision Models** (gpt-4-vision, gpt-4-vision-preview-0409, gpt-4-vision-preview-1106)
- GPT-3.5 Turbo (all variants including instruct)
- Legacy models (text-davinci-003, text-davinci-002, gpt-3, etc.)
- Embedding models (text-embedding-ada-002, text-embedding-3-small, text-embedding-3-large)

### Anthropic Models (27 models)
- Claude-3 (Opus, Sonnet, Haiku with full and short names)
- Claude-3.5 (Sonnet, Haiku 3.5, Computer Use models)
- Claude-2 (2.1, 2.0, **NEW: 2.1-200k, 2.1-100k**)
- Claude-1 (legacy models including 1.3, 1.3-100k)
- Claude Instant (all variants including **NEW: instant-2, instant-2.0**)

### Google Models (16 models)
- Gemini Pro, Gemini Pro Vision
- Gemini 1.5 Pro, Gemini 1.5 Flash (including latest variants)
- Gemini 2.0 (gemini-2.0-flash-exp, gemini-2.0-flash, gemini-exp-1206, gemini-exp-1121)
- Gemini 1.0 Pro, Gemini 1.0 Pro Vision
- Gemini Ultra
- **NEW: PaLM Models** (palm-2, palm-2-chat, palm-2-codechat)

### Meta Models (12 models)
- LLaMA-2 (7B, 13B, 70B)
- LLaMA-3 (8B, 70B)
- LLaMA-3.1 (8B, 70B, 405B)
- LLaMA-3.2 (1B, 3B)
- LLaMA-3.3 (70B, 70B-instruct)

### Mistral Models (10 models)
- Mistral (7B, Large, Medium, Small, Tiny)
- Mistral Large 2 (mistral-large-2, mistral-large-2407)
- Mixtral (8x7B, 8x22B)
- Legacy Mistral 8x7B

### Cohere Models (9 models)
- Command (standard, light, nightly)
- Command-R (standard, plus, **NEW: with 2024 variants**)

### xAI Models (4 models)
- Grok (1, 1.5, 2, beta)

### Alibaba Models (20 models)
- Qwen-1.5 series (0.5B to 110B parameters)
- Qwen-2 series (0.5B to 72B parameters)
- **NEW: Qwen-2.5** (qwen-2.5-72b, qwen-2.5-32b, qwen-2.5-14b, qwen-2.5-7b)
- Qwen-VL (vision-language variants)

### Baidu Models (8 models)
- ERNIE (4.0, 3.5, 3.0, Speed, Lite, Tiny)
- ERNIE Bot (standard and 4.0)

### Huawei Models (5 models)
- PanGu-α (2.6B, 13B, 200B)
- PanGu-Coder (15B and base)

### Yandex Models (4 models)
- YaLM (100B, 200B)
- YaGPT (1, 2)

### Stability AI Models (7 models)
- StableLM Alpha (3B, 7B base and tuned)
- StableLM Zephyr (3B)

### TII Models (6 models)
- Falcon (7B, 40B, 180B with instruct and chat variants)

### EleutherAI Models (12 models)
- GPT-Neo (125M, 1.3B, 2.7B)
- GPT-NeoX (20B)
- Pythia (70M to 12B)

### MosaicML/Databricks Models (8 models)
- MPT (7B, 30B with chat and instruct variants)
- DBRX (base and instruct)

### Replit Models (3 models)
- Replit Code (v1, v1.5, v2 - 3B parameters)

### MiniMax Models (5 models)
- ABAB (5.5 to 6.5 chat variants)

### Aleph Alpha Models (4 models)
- Luminous (Base, Extended, Supreme, Supreme Control)

### DeepSeek Models (10 models)
- DeepSeek-Coder (1.3B to 33B, instruct)
- DeepSeek-VL (1.3B, 7B)
- DeepSeek-LLM (7B, 67B)
- **NEW: DeepSeek V3** (deepseek-v3, deepseek-v3-base)

### Tsinghua KEG Lab Models (5 models)
- ChatGLM (6B variants: ChatGLM, ChatGLM2, ChatGLM3)
- GLM-4 (standard and vision)

### RWKV Models (7 models)
- RWKV-4 (169M to 14B parameters)
- RWKV-5 World

### Community Fine-tuned Models (13 models)
- Vicuna (7B, 13B, 33B)
- Alpaca (7B, 13B)
- WizardLM (7B, 13B, 30B)
- Orca Mini (3B, 7B, 13B)
- Zephyr (7B Alpha, Beta)

### Perplexity Models (5 models)
- PPLX (7B, 70B online and chat variants)
- CodeLlama 34B Instruct

### Hugging Face Models (5 models)
- Microsoft DialoGPT (medium, large)
- Facebook BlenderBot (400M, 1B, 3B variants)

### AI21 Models (4 models)
- Jurassic-2 (Light, Mid, Ultra, Jumbo Instruct)

### Together AI Models (3 models)
- RedPajama INCITE Chat (3B, 7B)
- Nous Hermes LLaMA2 13B

### Microsoft Models (4 models)
- **NEW: Phi Models** (phi-3-mini, phi-3-small, phi-3-medium, phi-3.5-mini)
- Optimized for coding and reasoning tasks
- Enterprise-ready AI models

### Amazon Models (3 models)
- **NEW: Titan Models** (titan-text-express, titan-text-lite, titan-embed-text)
- Enterprise-focused text generation and embedding
- AWS Bedrock integration

### Nvidia Models (2 models)
- **NEW: Nemotron Models** (nemotron-4-340b, nemotron-3-8b)
- Technical and scientific content optimization
- GPU-accelerated training

### IBM Models (3 models)
- **NEW: Granite Models** (granite-13b-chat, granite-13b-instruct, granite-20b-code)
- Enterprise AI with security and compliance focus
- Code generation and business applications

### Salesforce Models (3 models)
- **NEW: CodeGen Models** (codegen-16b, codegen-6b, codegen-2b)
- Specialized for code generation across multiple programming languages
- Open-source code understanding

### BigCode Models (3 models)
- **NEW: StarCoder Models** (starcoder, starcoder2-15b, starcoderbase)
- Multi-language code generation and understanding
- Trained on diverse programming languages

### Databricks Models (5 models)
- **NEW: Databricks Models** (dbrx-instruct, dbrx-base, dolly-v2-12b, dolly-v2-7b, dolly-v2-3b)
- High-quality instruction-following and base models

### Voyage AI Models (6 models)
- **NEW: Voyage AI Models** (voyage-2, voyage-large-2, voyage-code-2, voyage-finance-2, voyage-law-2, voyage-multilingual-2)
- State-of-the-art embedding models for various domains


**Total: 300+ models across 34+ providers**

## Installation

```bash
pip install scripts
```

### Optional Dependencies

For exact OpenAI token counts, install `tiktoken`:
```bash
pip install tiktoken
```

For other providers, the CLI uses built-in approximations (no additional dependencies required).

## CLI Quick Start

```bash
scripts --model gpt-4 "Hello, world!"
```

## CLI Usage Examples

### Basic Token Counting

```bash
scripts --model gpt-4 "The quick brown fox jumps over the lazy dog."
```

### Count Tokens from a File

```bash
scripts --model claude-3-opus-20240229 --file input.txt
```

### Cost Estimation

```bash
scripts --model gpt-4 --cost "Your text here"
```

### Output Token Pricing

```bash
scripts --model gpt-4 --cost --output-tokens "Model response text"
```

### List Supported Models

```bash
scripts --list-models
```

### Verbose Output

```bash
scripts --verbose --cost --file large_document.txt gpt-4
```

## CLI Reference

```
Usage: toksum [TEXT ...]

Positional arguments:
  TEXT ...              One or more text segments

Options:
  -m, --model MODEL     Model name (e.g., gpt-4, claude-3-opus-20240229)
  -f, --file PATH       Read input text from file (repeatable, split by blank lines)
  -u, --url URL         Read input text from URL (repeatable, split by blank lines)
  -l, --list-models     List all supported models
  -c, --cost            Show cost estimate along with token count
      --currency CUR    Currency for cost output (USD or INR)
      --output-tokens   Use output token pricing
  -v, --verbose         Show detailed output
```

## How It Works

### OpenAI Models
Uses the official `tiktoken` library to get exact token counts using the same tokenizer as OpenAI's API.

### Anthropic Models
Uses a smart approximation algorithm based on:
- Character count analysis
- Whitespace and punctuation detection
- Anthropic's guidance of ~4 characters per token
- Adjustments for different text patterns

The approximation is typically within 10-20% of actual token counts for English text.

## Development

### Setup Development Environment

```bash
git clone https://github.com/kactlabs/toksum.git
cd scripts
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov=scripts --cov-report=html
```

### Code Formatting

```bash
black scripts tests examples
```

### Type Checking

```bash
mypy scripts
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v1.0.1
- **Production Ready**: Stable v1.0.1 release with comprehensive support for 300+ models across 34+ providers
- **Accurate Tokenization**: Official tokenizers for OpenAI plus optimized approximations for other providers
- **Cost Estimation**: Up-to-date pricing support with input/output token cost breakdowns
- **CLI Experience**: Streamlined command-line usage with files, URLs, and verbose reporting
- **Quality & Coverage**: Extensive test suite and multilingual model coverage for global usage

## Acknowledgments

- [tiktoken](https://github.com/openai/tiktoken) for OpenAI tokenization
- [Anthropic](https://www.anthropic.com/) for Claude model guidance
- The open-source community for inspiration and best practices
