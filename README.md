# The Funniest One-Line Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/competitions/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/h05meigames2/resignation-letter-25nov26/rank.svg)](https://make.fun/competitions/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/h05meigames2/resignation-letter-25nov26/reward.svg)](https://make.fun/competitions/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

Entry for [The Funniest One-Line Resignation Letter bounty](https://make.fun/competitions/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) ($10, entries close 26 Nov 2026 23:15 WIB).

## The line

> After 4,096 retries, I finally accept the server will never love me back. I quit — please forward my feelings to /dev/null.

## How it works

`main.py` is deterministic Python with no network access and no randomness. It writes the single line (123 characters, under the 140 limit) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

The joke is a retry loop resigning like a tired employee: after 4,096 unanswered attempts it stops blaming the network and accepts the server will never love it back — then asks for its feelings to be forwarded to /dev/null, the one place nothing ever comes back from.

## Run

```bash
python3 main.py
```

With a custom output directory:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
