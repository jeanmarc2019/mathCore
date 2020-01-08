# Math CORE

## Example

### Download sequence from OEIS...

```bash
anum=A216251
curl 'https://oeis.org/search?q=id:A216251&fmt=json' > "$anum.json"
jq --raw-output '.results[0].data | split(",") | map(tonumber) | map(. + 60) | .[]' "$anum.json" | \
    ./app/seq_to_mid.py - -sep 0.5 -tempo 240 -dur 0.5 > "$anum.mid"
```

### Generate custom sequences using a plugin...

```bash
./app/plugin.py bernoulli_process 40 -k p=0.5 | \
    while read x; do echo $((x * 60)); done | \
    sed 's/^0$/-1/' | \
    ./app/seq_to_mid.py - -sep 0.5 -tempo 240 -dur 0.5 > bernoulli_process.mid
```
