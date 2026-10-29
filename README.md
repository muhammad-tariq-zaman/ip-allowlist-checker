# ip-allowlist-checker

Check IP addresses against a CIDR allowlist file and print ALLOWED or DENIED for each.

## How to run

```sh
python3 main.py allowlist.txt 10.1.2.3 192.168.1.1
```

## Example output

```
10.1.2.3: ALLOWED
192.168.1.1: DENIED
```

Standard library only. Run the tests with `python3 -m unittest discover`.
