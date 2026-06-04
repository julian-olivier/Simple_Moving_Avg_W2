import pandas as pd
import matplotlib as plt
import numpy as np 

def main():
    df = pd.read_csv("HW1_Week2/all_stocks_5yr.csv")

    nvdia = df[ df['Name'] == 'NVDA']

    df.plot(x='date', y = 'close')

    plt

if __name__ == "__main__":
    main()