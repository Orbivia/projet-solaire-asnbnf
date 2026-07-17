SolaExpert ASNBNF - Calculateur Solaire Autonome


📱 Aperçu de l'Application

L'application est conçue pour être utilisée de manière fluide sur smartphone (mobile-first) comme sur ordinateur de bureau. Elle accompagne l'installateur à travers 4 étapes clés :

1. 📍 Localisation & Ensoleillement

API PVGIS : Récupération automatique des données d'ensoleillement (Commission Européenne) en cliquant sur une carte interactive.

Mode Manuel (Facteur F) : L'utilisateur peut régler l'inclinaison et l'orientation cardinale. Le système calcule dynamiquement le facteur de perte lié à l'orientation pour simuler le rendement réel du terrain.

2. 💡 Bilan de Consommation

Saisie robuste des équipements : définition de la quantité, des heures d'utilisation et du nombre de jours par semaine (bridé à 7 jours).

Sécurité des saisies : Alertes si l'utilisation dépasse 24h ou si les heures de nuit dépassent les heures totales.

Consommation de Nuit : Le système isole spécifiquement l'énergie consommée la nuit. Cette donnée est cruciale pour le dimensionnement strict du parc de batteries.

3. ⚙️ Paramètres Techniques

Ajustement fin des rendements (onduleur, câbles, chaleur).

Technologie de Batterie : Un menu déroulant (Lithium, Plomb Gel, Plomb Ouvert) définit automatiquement la Profondeur de Décharge (DoD) adéquate pour prolonger la durée de vie du stockage.

Choix de l'architecture de stockage (Tension du parc en 12V/24V/48V, et tension unitaire de la batterie en 2V ou 12V).

4. 📊 Synthèse et Dimensionnement

Recommandations d'achats exactes : L'application recommande par exemple un arrondissement du nombre de panneaux au chiffre pair supérieur (pour s'adapter aux régulateurs MPPT modernes).

Schéma unifilaire généré en direct : Un schéma de câblage SVG (Panneaux, Régulateur, Batteries en série/parallèle) se dessine automatiquement en fonction du calcul final, sans rechargement de la page.

🧮 Méthodologie et Formules de Calcul

Le calculateur utilise des formules standards, validées pour le déploiement sur le terrain en zone isolée :

1. Bilan Énergétique Journalier ($E_j$)

Le besoin total est calculé en lissant l'utilisation sur la semaine :

$$E_j (Wh/j) = \sum \left( P \times Qté \times H_{jour} \times \left(\frac{Jours/semaine}{7}\right) \right)$$

2. Énergie à Produire ($E_p$)

On prend en compte l'ensemble des pertes du système (Rendement Global).

$$E_p = \frac{E_j}{R_{global}}$$

Où $R_{global}$ = $R_{onduleur} \times R_{régulateur} \times R_{batteries} \times R_{cables} \times R_{chaleur} \times R_{inclinaison\_orientation}$ (Le Facteur F).

3. Dimensionnement du Parc Solaire

La Puissance Crête ($P_c$) nécessaire est calculée selon l'irradiation locale de référence ($Ir$).

$$P_c (W_c) = \left( \frac{E_p}{Ir} \right) \times 1000$$

Le nombre de panneaux est calculé, puis arrondi au nombre pair supérieur.

4. Dimensionnement du Parc Batterie (Stockage)

La formule de l'énergie à stocker ($E_{stock}$) garantit une sécurité totale. Le système doit stocker assez d'énergie pour faire face à la nuit qui arrive ($E_{nuit}$), additionné de l'énergie nécessaire pour survivre au nombre de jours sans soleil voulus ($J_{auto}$).

$$E_{stock} = E_{nuit} + (E_j \times J_{auto})$$

La Capacité théorique du parc ($C_{th}$ en Ah) est ensuite calculée en fonction de la Profondeur de Décharge (DoD) choisie via le type de batterie :

$$C_{th} = \frac{E_{stock}}{U_{sys} \times DoD}$$

Enfin, une marge de sécurité de 20% (facteur 0.8 d'endommagement) est appliquée pour obtenir la capacité réelle à installer ($C_{reelle}$) :

$$C_{reelle} = \frac{C_{th}}{0.8}$$

(Note : le rendement de la batterie $r_{bat}$ est utilisé pour majorer le parc de panneaux solaires, mais n'est volontairement pas réintégré ici pour éviter un double surdimensionnement erroné).

5. Section de Câblage (Chute de tension $\Delta V$)

Pour éviter les incendies et les pertes, la section ($S$ en $mm^2$) est calculée avec une tolérance de chute de tension de 3% max, puis arrondie à la section commerciale supérieure (ex: 4, 6, 10, 16 mm²).

$$S = \frac{\rho \times 2 \times L \times I}{\Delta V_{max}}$$
.
