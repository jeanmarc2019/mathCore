# Math CORE

## Example

### Download sequence from OEIS...

```bash
anum=A216251
curl -L -s "https://oeis.org/search?q=id:$anum&fmt=json" | \
    jq --raw-output '.results[0].data | split(",") | map(tonumber) | map(. + 60) | .[]' | \
    ./src/midify.py - -sep 0.5 -tempo 240 -dur 0.5 > "$anum.mid"
```

### Generate custom sequences using a plugin...

```bash
./src/plugin.py bernoulli_process 40 -kwargs p=0.5 | \
    while read x; do echo $((x * 60)); done | \
    sed 's/^0$/-1/' | \
    ./src/midify.py - -sep 0.5 -tempo 240 -dur 0.5 > bernoulli_process.mid
```
