# Site web — Sana Ben Hamida

Site Quarto bilingue (EN à la racine, FR dans `fr/`), publié sur GitHub Pages.

- Chaque `git push` sur `main` reconstruit et publie le site (`.github/workflows/publish.yml`).
- Reconstruction automatique le 1er de chaque mois pour rafraîchir les publications.
- `scripts/hal_publications.py` régénère `_hal_list.md` depuis l'idHAL `sana-ben-hamida`
  (communications uniquement ; revues, ouvrages et chapitres sont tenus à la main dans
  `publications.qmd` et `fr/publications.qmd`).

## Règles

- Aucune information personnelle (adresse, téléphone, nom d'usage, adresse mail Dauphine).
- Toute modification se fait dans les deux langues.
- Projets (ANR, etc.) affichés uniquement une fois acceptés.
- Mettre à jour la date du pied de page (`_quarto.yml`) à chaque modification.
