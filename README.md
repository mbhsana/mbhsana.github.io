# Site web — Sana Ben Hamida

Site Quarto bilingue (EN à la racine, FR dans `fr/`), publié sur GitHub Pages.

- Chaque `git push` sur `main` reconstruit et publie le site (`.github/workflows/publish.yml`).
- `_hal_list.md` (communications et workshops) est tenu à la main : HAL ne contient que 12 des 31
  communications (novembre 2026). `scripts/hal_publications.py` pourra le régénérer depuis l'idHAL
  `sana-ben-hamida` une fois HAL complet (réactiver `pre-render` dans `_quarto.yml`).

## Règles

- Aucune information personnelle (adresse, téléphone, nom d'usage, adresse mail Dauphine).
- Toute modification se fait dans les deux langues.
- Projets (ANR, etc.) affichés uniquement une fois acceptés.
- Mettre à jour la date du pied de page (`_quarto.yml`) à chaque modification.
