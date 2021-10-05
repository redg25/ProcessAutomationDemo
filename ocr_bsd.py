import tabula
import pandas as pd

def extract_table(file):
    recon_file = "Bank_archive.csv"
    tables = tabula.read_pdf(file, pages='all')
    df = tables[0]
    print(df)
    df = df.drop(df.columns[[4, 5]], axis=1)
    print(df)
    df.columns=['Payment date','Client','Amount paid','Invoice']
    print(df)
    df_full = pd.read_csv(recon_file)
    print (df_full)
    for i, row in df.iterrows():
        inv = row['Invoice']
        if inv in df_full['Invoice'].values:
            index = df_full.index[df_full['Invoice']==inv].tolist()[0]
            df_full.loc[index,
                        ['Payment date','Amount paid','Client']] \
                = [row['Payment date'],row['Amount paid'],row['Client']]
        else:
            new_invoice = {'Invoice':row['Invoice'],
                           'Payment date':row['Payment date'],
                           'Amount paid':row['Amount paid'],
                           'Client':row['Client']}
            df_full = df_full.append(new_invoice,ignore_index=True)

    df_full.to_csv(recon_file,index=False)
    return recon_file





