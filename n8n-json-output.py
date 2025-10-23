# Récupère tous les items envoyés par le nœud précédent
items = $input.all()

text = items[0]["json"]["text"]

return [{"json": {"texte_extrait": text}}]
