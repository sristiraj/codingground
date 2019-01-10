import pandas as pd
import numpy as np
import itertools


def get_level_values(df, level):
    return df.loc[df['parent'].isin(level)]


if __name__ == "__main__":
    print("hello")
    lst = np.array([[0,1],[1, 2],[1, 3],[2, 4],[2, 5],[4, 6],[3,7],[6,9],[7,10],[10,15],[15,20]])
    #print(lst)
    df = pd.DataFrame(lst, columns=['parent', 'child'])
    #print(df)
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
            df_final = pd.merge(df_final, df_return, how='left',left_on=['level'+str(lvl_no-1)], right_on=['parent'])
            x = len(column_names)-1
            col = column_names[0:x]
            #print(col)
            col.append('child')
            print(col)
            df_final = df_final[col]
            df_final.columns = column_names
        print(df_final)

        level = df_return['child']
        df = df.loc[~df['child'].isin(df_return['child'])]
        #df.drop(df_final.index.values)
        print(df)
        lvl_no = lvl_no + 1
    print(df_final)
    df_final.to_csv(r'C:\Users\Sristi Raj\Documents\WIP\desktop\ParentChild.csv')