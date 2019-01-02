import suds
import pandas as pd
import numpy as np

CONFIG_FILE = r"C:\Users\Sristi Raj\Desktop\obis1-query_12\FILE_COMPARE_CONFIG.xlsx"


def readfile(filelocation, filetype, excludeheaderrows):
    if filetype == 'LOCAL_EXCEL':
        if excludeheaderrows == 0:
            df = pd.read_excel(filelocation)
        else:
            df = pd.excel(filelocation, skiprows=excludeheaderrows)
    return df


if __name__ == "__main__":
    df = pd.read_excel(CONFIG_FILE)
    nd = np.ndarrar()
    for i, row in df.iterrows():
        df1 = readfile(row['FILE_LOCATION1'], row['FILE_TYPE1'], row['EXCLUDE_HEADER_ROWS'])
        df2 = readfile(row['FILE_LOCATION2'], row['FILE_TYPE2'], row['EXCLUDE_HEADER_ROWS'])

        if df1.equals(df2):
            print("Equal")
            nd.
        else:
            print("Not equal")
