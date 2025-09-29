# Bataille Navale - Python / Pygame

Un jeu de **Bataille Navale** développé en Python avec interface graphique Pygame, tir automatique intelligent

## Fonctionnalités

- Grille de 10x10 affichée avec **Pygame**
- Placement de bateaux manuel 
- Phase de tir joueur vs IA
- IA avec tir semi-intelligent :
  - Tir aléatoire jusqu’à toucher un bateau
  - Lorsqu’un bateau est touché, l’IA tente de le couler complètement avant de revenir au hasard
- Indicateur visuel des bateaux détruits (gauche : Joueur, Droite : IA)
- Tests unitaires avec **Pytest**




L'IA peut avoir un défaut dans le cas ou plusieurs navires se touchent. Elle peut penser avoir détruit un navire de 3 alors qu'elle a touché et détruit le navire de 2 et endommagé un autre navire.