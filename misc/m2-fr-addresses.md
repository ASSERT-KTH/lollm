### Générer un générateur de données automatique en Java qui produit 10 adresses réalistes à Quimperlé, sans utiliser de fausse bibliothèque

Si vous préférez ne pas utiliser la bibliothèque Faker, vous pouvez générer manuellement des adresses aléatoires à Quimperlé. Voici un exemple de code qui utilise des listes de noms de rues, de codes postaux et de villes pour générer des adresses réalistes :

```java
import java.util.Random;

public class AdresseGenerator {

    private static final String[] villes = {
        "Quimperlé", "Mellac", "Rédéné", "Clohars-Carnoët", "Moëlan-sur-Mer"
        // ajoutez d'autres villes de Quimperlé si nécessaire
    };

    private static final String[] codesPostaux = {
        "29300", "29380", "29350", "29360", "29310"
        // ajoutez d'autres codes postaux de Quimperlé si nécessaire
    };

    private static final String[] nomsRues = {
        "Rue des Roses", "Avenue de la Liberté", "Impasse des Marronniers", "Boulevard du Moulin"
        // ajoutez d'autres noms de rues de Quimperlé si nécessaire
    };

    public static void main(String[] args) {
        Random random = new Random();

        for (int i = 0; i < 10; i++) {
            String ville = villes[random.nextInt(villes.length)];
            String codePostal = codesPostaux[random.nextInt(codesPostaux.length)];
            String nomRue = nomsRues[random.nextInt(nomsRues.length)];
            int numero = random.nextInt(100) + 1;

            String adresse = numero + " " + nomRue + ", " + codePostal + " " + ville;
            System.out.println(adresse);
        }
    }
}
```

Ce code utilise un générateur de nombres aléatoires pour sélectionner des éléments aléatoires dans les tableaux de villes, codes postaux et noms de rues. Il génère ensuite une adresse en concaténant le numéro de rue, le nom de rue, le code postal et la ville. La boucle est répétée jusqu'à obtenir 10 adresses réalistes à Quimperlé.
