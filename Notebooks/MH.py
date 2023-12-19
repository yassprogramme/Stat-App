### Metropolis-Hastings algorithm ### 

import numpy as np
import matplotlib.pyplot as plt
import math

#Exemple
def target_distribution(x):
    return (1 / np.sqrt(2 * math.pi)) * np.exp(- x**2 / 2) * (1 + np.sin(x))
#Exemple
def proposal_distribution(x, sigma = 1):
    return np.random.normal(x, 3)  #Loi normale de moyenne x (ici on prend Q(x,.) = N(x,3))


def MH(target_distribution, proposal_distribution, iterations = 10000, initial_value = 0):
    samples = [initial_value]

    for _ in range(iterations):
        current_sample = samples[-1]
        
        # Proposition d'un nouvel échantillon
        proposed_sample = proposal_distribution(current_sample)

        # Calcul du rapport d'acceptation
        acceptance_ratio = min(1, target_distribution(proposed_sample) / target_distribution(current_sample))

        # Acceptation ou rejet de l'échantillon proposé
        if np.random.rand() < acceptance_ratio:
            samples.append(proposed_sample)
        else:
            samples.append(current_sample)

    return np.array(samples)

# Exécution de l'algorithme
samples = MH(target_distribution, proposal_distribution)

# Affichage des résultats
plt.hist(samples, bins = 50, density = True, alpha = 0.5, color = 'blue', label = 'Échantillon généré avec la méthode de Metropolis-Hastings')
x_values = np.linspace(-5, 5, 100000)
plt.plot(x_values, target_distribution(x_values), 'r', label = 'Distribution cible')
plt.title('Méthode de Metropolis-Hastings')
plt.legend()
plt.show()
