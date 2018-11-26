import pandas as pd
import numpy as np



if __name__ == "__main__":
    """read csv format xlsx"""
    df = pd.read_csv("bank.csv").replace(np.nan,"",regex=True)
    df.to_excel("bank.xlsx",index=False)
