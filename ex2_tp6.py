
from dataclasses import dataclass, asdict
import json


# Classe pour representer un film
@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        if not isinstance(self.titre, str) or not self.titre.strip():
            raise ValueError("Titre invalide")

        if not isinstance(self.realisateur, str) or not self.realisateur.strip():
            raise ValueError("Realisateur invalide")

        if type(self.annee) != int or self.annee <= 0:
            raise ValueError("Annee invalide")

        if isinstance(self.note, bool) or not isinstance(self.note, (int, float)):
            raise ValueError("La note doit etre numerique")

        if not 0 <= self.note <= 10:
            raise ValueError("La note doit etre entre 0 et 10")

    # Convertir les informations du film en JSON
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    # Verifier si le film date d'avant 2000
    def est_classique(self):
        return self.annee < 2000

    # Recuperer un film a partir d'un JSON
    @classmethod
    def from_json(cls, chaine):
        donnees = json.loads(chaine)
        return cls(**donnees)

    # Comparaison des films selon leur note
    def __lt__(self, autre):
        if not isinstance(autre, Film):
            return NotImplemented
        return self.note < autre.note


# Exemple d'utilisation
if __name__ == "__main__":

    film1 = Film("Titanic", "James Cameron", 1997, 9.5)
    film2 = Film("Inception", "Christopher Nolan", 2010, 8.8)
    film3 = Film("Interstellar", "Christopher Nolan", 2014, 9.2)

    # Affichage des informations
    print(film1.to_json())

    # Verification du classique
    print("Film classique :", film1.est_classique())

    # Chargement depuis JSON
    film_charge = Film.from_json(film2.to_json())
    print("Film charge :", film_charge)

    # Classement selon les notes
    films = [film1, film2, film3]
    films_tries = sorted(films)

    print("Films classes par note :")
    for film in films_tries:
        print(film.titre, "-", film.note)


    # Creation d'une liste de favoris en JSON
    favoris = [film1, film3]

    donnees_favoris = json.dumps(
        [asdict(film) for film in favoris],
        ensure_ascii=False
    )

    print("Liste des favoris :", donnees_favoris)
