
from dataclasses import dataclass, asdict, replace
import json


# Classe qui contient les informations d'un livre
@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    # Transformer le livre en format JSON
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    # Creer un nouveau livre avec un prix reduit
    def promo(self, prix_reduit):
        if prix_reduit <= 0 or prix_reduit >= self.prix:
            raise ValueError("Prix de promotion invalide.")

        return replace(self, prix=prix_reduit)


# Recuperer un livre depuis une chaine JSON
def charger_livre(chaine):
    donnees = json.loads(chaine)
    return Livre(**donnees)


# Comparer deux livres selon leur prix
def comparer_prix(livre1, livre2):
    return sorted([livre1, livre2], key=lambda livre: livre.prix)


# Exemple de test
if __name__ == "__main__":

    livre1 = Livre("1984", "George Orwell", 1949, 9.90)
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupery", 1943, 15.50)

    # Affichage des informations
    print("Livre 1 :", livre1.to_json())

    # Application d'une reduction
    livre_promo = livre1.promo(7.90)
    print("Livre apres promotion :", livre_promo.to_json())

    # Chargement depuis JSON
    livre_charge = charger_livre(livre1.to_json())
    print("Livre charge :", livre_charge)

    # Classement des livres par prix
    print("Livres classes par prix :")
    for livre in comparer_prix(livre1, livre2):
        print(livre.titre, "-", livre.prix, "€")
