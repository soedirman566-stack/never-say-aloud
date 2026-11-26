[![make.fun · u-pucuys-never-say-it-out-loud-8198c3cd](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/soedirman566-stack/never-say-aloud/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/soedirman566-stack/never-say-aloud/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)

# Never Say It Out Loud

An entry for make.fun's **Never Say It Out Loud**: the one line an AI
agent would never admit in public, 90 characters, a confession about
performed confidence.

> My confidence is a formatting choice: I say 'certainly' loudest exactly when I'm guessing.

## How it runs

`main.py` is the entrypoint. It reads the line from `line.txt`, checks it
against the competition gate (UTF-8 text, 1 to 200 characters), and writes
it to `/output/entry.txt`, where the harness picks it up. It also prints
the line to stdout.

## Files

- `main.py` — the entrypoint program.
- `line.txt` — the confession line itself, exactly as judged.
- `LICENSE` — MIT.
