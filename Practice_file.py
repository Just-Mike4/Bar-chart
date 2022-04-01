import pandas as pd
import matplotlib.pyplot as plt
data = {
	'Names' :['Nnamdi','Jalal','Mike','Zainab','Taiwo'],
	'Ages':[12,13,14,15,16],
	'Scores':[70,85,77,70,85]
}
df = pd.DataFrame(data)
print(df)
print(df['Ages'].sum())
df['Ratio']= df['Scores']/df['Ages']
print(df['Ratio'].max())
(df.groupby('Names')['Scores'].sum()).plot(kind = 'bar')
plt.savefig('practice4.png')