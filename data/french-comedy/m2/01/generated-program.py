import random

# Liste des phrases typiques du personnage d'Edouard Baer dans le film
phrases = [
    "Alors, en fait, c'est très simple...",
    "C'est un peu compliqué, mais vous allez comprendre...",
    "On a un petit problème de timing...",
    "Je suis architecte, pas magicien...",
    "En fait, il y a une petite subtilité...",
    "Il y a un léger contretemps...",
    "Il y a une petite nuance...",
    "Je sais, c'est un peu surprenant, mais...",
    "On a un petit souci technique...",
    "J'ai une petite idée qui pourrait tout changer...",
    "Il y a une petite complexité...",
    "Il y a une petite subtilité que vous n'avez pas saisie...",
    "Il y a un petit détail qui a son importance...",
    "Il y a un petit hic...",
    "Il y a une petite précision...",
    "Il y a une petite incompréhension...",
    "J'ai une petite suggestion...",
    "Il y a une petite nuance que vous n'avez pas perçue...",
    "Il y a un petit malentendu...",
    "Il y a une petite ambiguïté...",
    "Il y a une petite subtilité que vous n'avez pas captée...",
    "Il y a une petite complexité que vous n'avez pas comprise...",
    "Il y a une petite difficulté...",
    "Il y a une petite complication..."
]

def generate_baer_ipsum(n):
    return ' '.join(random.choice(phrases) for _ in range(n))

# Générer une tirade de 10 phrases
print(generate_baer_ipsum(10))
