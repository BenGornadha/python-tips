Inconvénients de l'approche classique avec les IF:

	1.	Code difficile à maintenir : Si tu veux ajouter une nouvelle forme, tu dois modifier la fonction calculate_area, ce qui enfreint le principe Open/Closed (le code devrait être ouvert à l’extension, mais fermé à la modification).
	2.	Complexité croissante : Plus il y a de formes, plus il y a de conditions if et elif, ce qui alourdit le code.
	3.	Manque d’extensibilité : Si on souhaite ajouter des comportements spécifiques pour certaines formes (comme des vérifications additionnelles), cela devient vite complexe.


Avantages du polymorphisme :

	1.	Extensibilité : Si tu veux ajouter une nouvelle forme (par exemple, un pentagone), il suffit de créer une nouvelle sous-classe sans toucher au code existant.
	2.	Élimination des if/else : Le code devient plus propre, et chaque forme gère son propre calcul d’aire indépendamment des autres.
	3.	Principe Open/Closed : Le code est maintenant ouvert à l’extension (ajout de nouvelles formes) mais fermé à la modification (tu n’as pas besoin de modifier le code existant pour ajouter une nouvelle forme).