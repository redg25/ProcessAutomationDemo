import tabula
import pandas as pd


def get_table_from_file(file):
    """ Get a pdf with onne or more tables and return a dataframe with the values from the first table
    :param file: a pdf with at least one table
    :return: pandas.dataframe
    """
    tables = tabula.read_pdf(file, pages='all')
    return tables[0]


def invoices_recon(df,recon_file):
    """ Merge the new invoice data withe the main recon file using pandas.
    :param df: a pandas.dataframe with the new invoices data
    :param recon_file: a csv file with the main recon data
    :return: a csv file with the updated main recon file
    """
    #Remove extra blank columns from tabula extraction
    df = df.drop(df.columns[4:6], axis=1)
    #Rename columns to match main recon file
    df.columns=['Payment date','Client','Amount paid','Invoice']
    #Get a dataframe from the main recon file
    df_full = pd.read_csv(recon_file)
    for i, row in df.iterrows():
        inv = row['Invoice']
        # If the invoice from the input file is in the main recon file, fill in 'Payment date','Amount paid','Client'
        # into the corresponding row in the main recon file
        if inv in df_full['Invoice'].values:
            index = df_full.index[df_full['Invoice']==inv].tolist()[0]
            df_full.loc[index,
                        ['Payment date','Amount paid','Client']] \
                = [row['Payment date'],row['Amount paid'],row['Client']]
        # Else create a new row on the main recon file
        else:
            new_invoice = {'Invoice':row['Invoice'],
                           'Payment date':row['Payment date'],
                           'Amount paid':row['Amount paid'],
                           'Client':row['Client']}
            df_full = df_full.append(new_invoice,ignore_index=True)

    df_full.to_csv(recon_file,index=False)
    return recon_file





