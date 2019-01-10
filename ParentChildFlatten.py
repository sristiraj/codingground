import pandas as pd
import numpy as np
import itertools

INPUT_FILE_LOCATION = r'C:\Users\Sristi Raj\Documents\WIP\desktop\PRHier.csv'
OUTPUT_FILE_LOCATION = r'C:\Users\Sristi Raj\Documents\WIP\desktop\ParentChild.csv'

def get_level_values(df, level):
    return df.loc[df['parent'].isin(level)]


if __name__ == "__main__":
    print("hello")
    #lst = pd.read_csv(r'C:\Users\Sristi Raj\Documents\WIP\desktop\PRHier.csv')
    #print(lst)
    df = pd.read_csv(INPUT_FILE_LOCATION)
    print(df)
    df = df.sort_values(by=['parent'])
    #print(df)
    level = [0]
    lvl_no = 1
    df_final = pd.DataFrame()
    column_names = ['level0', 'level1']
    while not(df.empty):
        print(level)
        if df_final.empty:
            df_return = get_level_values(df, level)
            df_final = df_return.copy()
            df_final.columns = column_names
        else:
            df_return = get_level_values(df, level)
            column_names.append('level'+str(lvl_no))
            print(column_names)
            df_orig = df_final.copy()
            df_final = pd.merge(df_final, df_return, how='left',left_on=['level'+str(lvl_no-1)], right_on=['parent'])
            x = len(column_names)-1
            col = column_names[0:x]
            df_orig['child'] = np.nan
            print(df_orig)
            #print(col)
            col.append('child')
            print(col)
            df_final = df_final[col]

            # print("Yes")
            # print(df_final)
            # print(df_orig)
            # print("ok")
            df_final = pd.concat([df_final, df_orig], ignore_index=True)
            df_final.drop_duplicates(keep='first', inplace=True)
            second_last_column = 'level'+str(lvl_no-1)
            df_final['child'].fillna(df_final[second_last_column], inplace=True)
            df_final.columns = column_names
        print(df_final)

        level = df_return['child']
        df = df.loc[~df['child'].isin(df_return['child'])]
        #df.drop(df_final.index.values)
        print(df)
        lvl_no = lvl_no + 1
    print(df_final)
    df_final.to_csv(OUTPUT_FILE_LOCATION)