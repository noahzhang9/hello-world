import json


dictionary = {}
names = ["DA.json", "DB.json", "DC.json", "DD.json", "DE.json", "DF.json", "DG.json", "DH.json", "DI.json", "DJ.json", "DK.json",
        "DL.json", "DM.json", "DN.json", "DO.json", "DP.json", "DQ.json", "DR.json", "DS.json", "DT.json", "DU.json", "DV.json",
         "DW.json", "DX.json", "DY.json", "DZ.json"]
for name in names:
    with open("Dictionary/" + name) as f:
        data = json.load(f)
        for word in data.keys():
            meanings = data[word]["MEANINGS"]
            meaning = ""
            for key in meanings.keys():
                meaning = meaning + " " + meanings[key][1]
            dictionary[str(word).lower()] = meaning.lower()
