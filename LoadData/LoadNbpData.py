import pandas as pd

def split_offer_trans(df, start_row, offer_cols=18, skip_cols=5, trans_cols=18):
    df_data = df.iloc[start_row:82]
    df_data.columns = df_data.iloc[0]  # set headers
    df_data = df_data[1:].reset_index(drop=True)

    offer_df = df_data.iloc[:, :offer_cols]
    trans_df = df_data.iloc[:, offer_cols + skip_cols : offer_cols + skip_cols + trans_cols]
    return offer_df, trans_df

def load_nbp_data():
  """
  Load NBP data from an Excel file and return the offer and transaction prices for primary and secondary markets.
  
  Returns:
      primary_offer, primary_trans, secondary_offer, secondary_trans (DataFrame).
  """
  # Load Excel file
  file_path = "ceny_mieszkan.xlsx"
  sheet_primary = pd.read_excel(file_path, sheet_name="Rynek pierwotny", header=None)
  sheet_secondary = pd.read_excel(file_path, sheet_name="Rynek wtórny", header=None)

  start_row = 6  # Starting row for data extraction

  primary_offer, primary_trans = split_offer_trans(sheet_primary, start_row)
  primary_offer.rename(columns={'Gdynia*': 'Gdynia'}, inplace=True)
  primary_trans.rename(columns={'Gdynia**': 'Gdynia'}, inplace=True)

  secondary_offer, secondary_trans = split_offer_trans(sheet_secondary, start_row)
  secondary_offer.rename(columns={'Gdynia*': 'Gdynia'}, inplace=True)
  secondary_trans.rename(columns={'Gdynia**': 'Gdynia'}, inplace=True)

  return primary_offer, primary_trans, secondary_offer, secondary_trans