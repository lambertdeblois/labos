#coding: utf8

#def taxes(taxe):

class Facture(object):
    def __init__(self, client):
        self.client = client
        self.achats = []
        self.total_quantite = 0
        self.total = 0.00
        self.ouvrire_facture()

    def ouvrire_facture(self):
        facture = open(self.client+".txt", "w+")
        contenu = """
        Client numero %s

                        No de produit    Qte     Prix       Total (tx)
        """ % self.client
        facture.write(contenu)

    def ajouter_achat(self, nom, qte, prix, taxes):
        float(qte)
        float(prix)
        self.achats.append([nom, float(qte), float(prix), taxes])
        facture = open(self.client+".txt", "a+")
        total = float(qte) * float(prix)
        self.total = self.total + total
        if taxes == 'FP':
            total = total * 1.05 * 1.09
        elif taxes == 'F':
            total = total * 1.05
        elif taxes == 'P':
            total = total * 1.09

        contenu = """
        Produit #%d          %s      %d        %0.2f              %0.2f

        """ % (len(self.achats), nom, float(qte), float(prix), total)

        facture.write(contenu)


    def fermer_facture(self):
        facture = open(self.client+".txt", "a+")
        total_articles = 0
        for each in factures[self.client]:
            total_articles = total_articles + self.achats[1]
            contenu = ""
        if total_articles > 100:
            rabais = self.total * .85
            contenu = """

            Total avant rabais :   %0.2f
            Rabais :    %0.2f
            Total :
            """ % (self.total, rabais)
        else:
            contenu = """

            Total :
            """ % (self.total)
        facture.write(contenu)

factures = {}
with open("exlabo1.txt") as commandes:
    for lignes in commandes:
        client, nom, qte, prix, taxes = lignes.split()
        #print client, nom, qte, prix, taxes
        if client not in factures.keys():
            factures[client] = Facture(client)
        facture = factures[client]
        facture.ajouter_achat(nom, float(qte), float(prix), taxes)

for idx, x in enumerate(facture.keys()):
    print idx, x

print factures.keys()
for each in facture.keys():
    factures[each].fermer_facture
