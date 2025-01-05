# The Cahn-Hilliard Equation and Patterns Occurring in Nature


# What is the Cahn-Hilliard Equation? 
The Cahn-Hilliard equation illustrates binary phase separation across numerous contexts. In all of its applications, the two binary phases separate to form discrete components. 

This equation is written as: 

∂φ/∂t = M ∇² (φ³ - φ - ε² ∇²φ)

where:
- φ is the order parameter representing the local concentration difference between two phases,
- M is the mobility, controlling the speed of phase separation,
- ε is a parameter related to the width of the interface between phases,
- ∇² denotes the Laplacian operator.

# Applications of Cahn-Hilliard
The Cahn-Hilliard equation has extensive applications specifically in material science and biology. In the context of biology, the Cahn-Hilliard equation is relevant in biological membrane dynamics, tissue morphology, and cell aggregation mechanisms. In biological membranes, the equation models phase separation in cell membranes and thus helps to explain how biological membranes form complex structures. Specifically, it captures lipid bilayer separation and reorganization processes. Additionally, it can simulate how cells cluster and separate, which provides insights into wound healing processes and tissue morphology. In tissue morphogenesis, the equation can model how cell populations/tumor cells segregate and form distinct regions. The Cahn-Hilliard equation is so effective at modeling biological processes because it essentially models how systems naturally minimize free energy, leading to spontaneous pattern formations. This mirrors many biological processes where such complex structures emerge from simple interaction rules. 

In the context of material science, the equation is fundamental to understanding how materials separate into distinct phases, and it can predict such pattern formation at microscopic scales. The Cahn-Hilliard equation describes spinodal decomposition (a mechanism by which a single thermodynamic phase spontaneously separates into two components) in alloys and can predict microstructure formation in metals and ceramics. Additionally, it can simulate crystal growth and polymer blend morphology. In material science, the Cahn-Hilliard equation handles both kinetic and thermodynamic aspects and like in biology, it incorporates free energy minimization into the calculations.  

# Animals Prints and Patterns
Interestingly, in biology, the principle of phase separation translates to how some discrete patterns form in nature, specifically animal prints and patterns! I have simulated the Cahn-Hilliard equation's production of several prints and patterns appearing in nature: zebras, leopards, giraffes, and honeycombs. 

### Cahn-Hilliard Pattern Comparisons with Animal Patterns

#### Zebra Pattern
| **Simulation** | **Real Zebra** |
|------------------------------|----------------|
| <img src="https://raw.githubusercontent.com/daniellew77/CahnHilliardAnimals/main/zebra_simulation.gif" width="500"> | <img src="https://s.abcnews.com/images/International/zebra-stripes-02-gty-jc-190221_hpEmbed_3x2_992.jpg" width="350"> |


#### Giraffe Pattern
| **Simulation** | **Real Giraffe** |
|------------------------------|----------------|
| <img src="https://raw.githubusercontent.com/daniellew77/CahnHilliardAnimals/main/giraffe_simulation.gif" width="500"> | <img src="https://www.nczoo.org/sites/default/files/styles/medium_large_800x800_/public/2020-06/19-10-01-RNP-The-spots-of-each-giraffe-are-like-a-fingerprint--every-one-is-unique.jpg.webp?itok=b_YvkNik" width="400"> |


#### Leopard Pattern
| **Simulation** | **Real Leopard** |
|------------------------------|----------------|
| <img src="https://raw.githubusercontent.com/daniellew77/CahnHilliardAnimals/main/leopard_simulation.gif" width="525"> | <img src="https://www.shutterstock.com/image-illustration/leopard-pattern-print-animal-260nw-2538939839.jpg" width="400"> |


#### Honeycomb Pattern
| **Simulation** | **Real Honeycomb** |
|------------------------------|----------------|
| <img src="https://raw.githubusercontent.com/daniellew77/CahnHilliardAnimals/main/honey_simulation.gif" width="500"> | <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtiVEUrCTGm4O6fK2YIXwrWu8TIEIoUuuKVQ&s" width="400"> |


