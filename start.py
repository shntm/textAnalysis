import config
import pandas as pd

print(config.textMessageDb)
dataset = pd.read_csv(config.textMessageDb)
print(dataset)