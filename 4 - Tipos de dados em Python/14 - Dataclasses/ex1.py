# Import dataclass
from dataclasses import dataclass

@dataclass
class WeightEntry:
    # Define the fields on the class
    species: str
    sex: int
    body_mass: int
    flipper_length: str
        
    # Define a property that returns the body_mass / flipper_length
    @property
    def mass_to_flipper_length_ratio(self):
        return self.body_mass / self.flipper_length
    
'''
O código acima demonstra como criar uma dataclass em Python. Dataclasses são uma maneira conveniente de definir classes que são principalmente usadas para armazenar dados. A classe `WeightEntry` possui quatro campos: `species`, `sex`, `body_mass` e `flipper_length`. Além disso, inclui uma propriedade chamada `mass_to_flipper_length_ratio`, que calcula a razão entre a massa corporal e o comprimento da nadadeira.
'''