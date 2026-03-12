---
name: tronscan-block-info
description: |
  Query TRON latest block, block reward, block time, producer, burned TRX, resource use,
  transaction count.
  Use when user asks "latest block", "block height", "block producer", "block reward", "burned TRX", or network load.
  Do NOT use for real-time TPS/network dashboard (use tronscan-realtime-network); tx by hash (use tronscan-transaction-info).
metadata:
  author: tronscan-mcp
  version: "1.0"
  mcp-server: tronscan
---

# Block Info

## Overview

| Tool | Function | Use Case |
|------|----------|----------|
| getLatestBlock | Latest block | Block number, hash, size, timestamp, witness, tx count |
| getBlocks | Block list | Pagination, sort, filter by producer/time |
| getBlockStatistic | Block statistics | 24h payment total, block count, burn total |

## Use Cases

1. **Latest Block**: Use `getLatestBlock` for current block number, hash, size, timestamp, witness, tx count.
2. **Block Reward**: Reward info can be derived from block data or chain params; block list gives block-level data.
3. **Block Time / Producer**: Use `getLatestBlock` or `getBlocks` for timestamp and witness (producer).
4. **Burned TRX**: Use `getBlockStatistic` for 24h burn total; per-block burn may be in block payload.
5. **Resource Consumption**: Block-level resource use is reflected in block size and tx count; use `getBlockStatistic` for aggregates.
6. **Transaction Count**: Use `getLatestBlock` for tx count in latest block; use `getBlocks` for multiple blocks.
7. **Network Load**: Combine `getLatestBlock`, `getBlocks`, and `getBlockStatistic` for real-time load view.

## MCP Server

- **Prerequisite**: [TronScan MCP Guide](https://mcpdoc.tronscan.org)

## Tools

### getLatestBlock

- **API**: `getLatestBlock` — Get latest confirmed block (number, hash, size, timestamp, witness, tx count)
- **Use when**: User asks for "latest block", "current block", or "block height".
- **Response**: number, hash, size, timestamp, witness, tx count, etc.

### getBlocks

- **API**: `getBlocks` — Get block list with pagination, sort, filter by producer/time range
- **Use when**: User asks for "recent blocks", "blocks by producer", or "blocks in time range".
- **Input**: limit, sort (e.g. `-number`), optional producer address, start/end time.

### getBlockStatistic

- **API**: `getBlockStatistic` — Get block statistics (24h payment total, block count, burn total)
- **Use when**: User asks for "block stats", "24h blocks", or "burned TRX".
- **Response**: 24h payment, block count, burn total, and related aggregates.

## Troubleshooting

For MCP connection and rate limit issues, see [README](../README.md#troubleshooting).

## Notes

- For "block reward", combine block data with `getChainParameters` (Witness category) if reward rules are needed.
- Real-time monitoring: poll `getLatestBlock` and/or `getBlockStatistic` for load and burn.
