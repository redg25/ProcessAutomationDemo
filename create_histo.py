import pandas as pd
from datetime import date


def create_histogram(recon_file):
    """ Takes the csv main recon file and genetate a bar diagram comparing invoices paid vs invoices issued by month
    :param recon_file: csv main recon file
    :return: the path of the image diagram as a string
    """
    df = pd.read_csv(recon_file)
    #Extract Month from the Issue Date column
    df['Month'] = df.apply(lambda row: row['Issue date'][:2], axis=1)
    # Group by month the total invoice amount and the amount paid
    # and concatenate them into one single dataframe
    df1 = df.groupby('Month')['Invoice amount'].sum()
    df2 = df.groupby('Month')['Amount paid'].sum()
    df3 = pd.concat([df1,df2],axis=1)
    # Generate a bar diagram and save it as a png image
    img = df3.plot.bar(stacked=False).get_figure()
    img.savefig(f'Invoice_report_{date.today()}.png')
    path = f'Invoice_report_{date.today()}.png'
    return path



