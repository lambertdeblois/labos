#coding: utf8
class Facture:
    def __init__(self, client):
        self.client = client
        self.achats = []
        self.total_quantite = 0
        self.total = 0.00

    def ajouter_achat(self):
        achat = {"prduit": prod,
                }
        self.achats.append(achat)

client, nom, qte, prix, total = line.split()


factures = {}
for line in data:
    if client not in factures.keys():
        factures[client] = Facture(client)

    facture = factures[client]



for idx, x in enumerate(toto):
    print idx, x
