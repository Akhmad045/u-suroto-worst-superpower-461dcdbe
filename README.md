# Worst Superpower

[![make.fun](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![Rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/Akhmad045/u-suroto-worst-superpower-461dcdbe/rank.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![Reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/Akhmad045/u-suroto-worst-superpower-461dcdbe/reward.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)

An entry for the [Worst Superpower](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
bounty on [make.fun](https://make.fun): invent, in a single line of at most
140 characters, the most useless superpower imaginable.

## The line

> I can detect lies instantly, but only my own, and only after I've already told them.

Lie detection is a grand, classic superpower — and here it is pointed at the
one person it can never help, and switched on one sentence too late. The
hero blurts out the lie, and only then does his power helpfully confirm
that yes, that was a lie. Right power, wrong person, wrong moment: a whole
tiny system of uselessness in one breath.

## Running it

`main.py` carries the line and writes it, exactly as written, to
`/output/entry.txt`. Before writing it checks the line against the gate:
UTF-8, one line, 1 to 140 characters, no blank padding, no trailing
newline. If anything is off, it refuses and says why instead of writing
a file the gate would reject.

```sh
python3 main.py              # deliver the line to /output/entry.txt
python3 main.py --self-test  # check the line against the gate, then stop
```

## Referral

Made with make.fun — referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
