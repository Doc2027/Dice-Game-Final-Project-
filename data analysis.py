import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


fruit_prices = {"apple" : 3.49,
                 "banana" : 1.29,
                 "cherries" : 3.89}
fruit_prices.keys()
fruit_prices.values()
fruit_prices.items()

fruit_prices["banana"]

peach_price = fruit_prices.get("peach")
type(peach_price)
print(peach_price)