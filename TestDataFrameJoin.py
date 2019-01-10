import pandas as pd

df = pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df1 = pd.DataFrame([[2,'abc'],[4,'xyz']],columns=['c','d'])

df2 = pd.merge(df,df1, how='inner',left_on=['b'],right_on=['c'])

l = [1,2,3]
l = (l[0:len(l)-1])
l.append(4)
print(l)
print(df2)