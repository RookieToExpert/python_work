#Import an entire module
import pizza

# Using as to Give a Module an Alias
import pizza as p
p.make_pizza(16, 'pepperoni')

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Impoort a method from module instead of import a whole module
# You can import as many methods as you want.
# ex: from module_name import function_0, function_1, function_2
from pizza import make_pizza
make_pizza(16, 'pepperoni')

# Import all functions in a Module: 
from pizza import *

# Using as to Give a Function an Alias
from pizza import make_pizza as mp
mp(16, 'pepperoni')



