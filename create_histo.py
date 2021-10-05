import pandas as pd
from datetime import date


def create_histogram(file):
    df = pd.read_csv(file)
    df['Month'] = df.apply(lambda row: row['Issue date'][:2], axis=1)
    df1 = df.groupby('Month')['Invoice amount'].sum()
    df2 = df.groupby('Month')['Amount paid'].sum()
    df3 = pd.concat([df1,df2],axis=1)
    img = df3.plot.bar(stacked=False).get_figure()
    img.savefig(f'Invoice_report_{date.today()}.png')
    path = f'Invoice_report_{date.today()}.png'
    return path


#create_histogram('Bank_archive_update.csv')

