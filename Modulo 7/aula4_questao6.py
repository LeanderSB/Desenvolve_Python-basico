import csv

musicas_por_ano = {}

with open("spotify-2023.csv", "r", encoding="latin-1") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        try:
            ano = int(linha["released_year"])
            if 2012 <= ano <= 2022 and '"' not in linha["track_name"] and '"' not in linha["artist(s)_name"]:
                streams = int(linha["streams"])
                if ano not in musicas_por_ano or streams > musicas_por_ano[ano][3]:
                    musicas_por_ano[ano] = [
                        linha["track_name"],
                        linha["artist(s)_name"],
                        ano,
                        streams
                    ]
        except:
            continue

mais_tocadas = [musicas_por_ano[ano] for ano in sorted(musicas_por_ano)]
for m in mais_tocadas:
    print(m)
