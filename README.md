# Math CORE

Generate yourself some mathcore midi files using custom highly mathematical sequences

## Prerequisites

The following external libraries are required to run the mathcore scripts:

* Python3, pip
* jq
* midiutil

The following commands will get you up and running:

```bash
brew install python3
```

```bash
brew install jq
```

```bash
pip3 install midiutil
```

## Examples

Use the following bash commands to generate midi using one of the strategies below:

### Download sequence from OEIS...

```bash
anum=A216251
curl -L -s "https://oeis.org/search?q=id:$anum&fmt=json" | \
    jq --raw-output '.results[0].data | split(",") | map(tonumber) | map(. + 60) | .[]' | \
    ./app/midify.py - -sep 0.5 -tempo 240 -dur 0.5 > "$anum.mid"
```

### Generate custom sequences using a plugin...

```bash
./app/plugin.py bernoulli_process 40 -kwargs p=0.5 | \
    while read x; do echo $((x * 60)); done | \
    sed 's/^0$/-1/' | \
    ./app/midify.py - -sep 0.5 -tempo 240 -dur 0.5 > bernoulli_process.mid
```
