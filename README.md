# ms-opendata-tools
Nastroje pro zpracovani dat pro MS Open Data Hackathon



## Generovani souboru

Skripty ocekavaji, ze soubory jsou ve slozce [data](data).

Pro generovani slepenych souboru slouzi skript [merge-files.sh](merge-files.sh), ktery slepi dohromady soubory, ktere k sobe tematicky patri.

Bud:

```
./merge-files.sh _sensor.csv klicperova
./merge-files.sh _sensor.csv kratochvilova
./merge-files.sh _sensor.csv opavska
./merge-files.sh _sensor.csv radon
./merge-files.sh _sensor.csv anemometr
./merge-files.sh _sensor.csv venkovni-hluk
```

Nebo:

```
./merge-files.sh _json_v2.csv klicperova
./merge-files.sh _json_v2.csv kratochvilova
./merge-files.sh _json_v2.csv opavska
./merge-files.sh _json_v2.csv radon
./merge-files.sh _json_v2.csv anemometr
./merge-files.sh _json_v2.csv venkovni-hluk
```


Skript [merge.py](merge.py) je skript, ktery soubory skutecne slepuje dohromady. Ocekavane parametry jsou:
`./merge.py vystypni.csv vstup1.csv vstup2.csv`

