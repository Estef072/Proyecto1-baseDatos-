from email import header
from tkinter import NONE
import pandas as pd
filename = 'Team.csv'
data = pd.read_csv(filename , header = 0)
for column in data:
     print(column +"," )

