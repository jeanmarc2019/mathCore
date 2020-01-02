# Math CORE

Example:

```bash
anum=A216251
curl 'https://oeis.org/search?q=id:A216251&fmt=json' > "$anum.json"
jq --raw-output '.results[0].data | split(",") | map(tonumber) | map(. + 60) | .[]' "$anum.json" | \
    ./app/mathCore.py - -sep 0.5 -tempo 240 -dur 0.5 > "$anum.mid"
```
