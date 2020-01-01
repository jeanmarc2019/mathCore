# Math CORE

Example:

```bash
curl 'https://oeis.org/search?q=id:A216251&fmt=json' > A216251.json
jq --raw-output '.results[0].data | split(",") | .[]' A216251.json |  ./app/mathCore.py - -sep 0.5 -tempo 240 -dur 0.5 > A216251.mid
```
