def load_inflation_data():
  """
  Load inflation data from an Excel file and return a DataFrame with quarterly CPI data.
  """
  import pandas as pd
  # odczyt danych o inflacji
  inflacja_path = "bazowa.xlsx"
  sheet_inflacja = pd.read_excel(inflacja_path, sheet_name="dane_kwartalne", header=None)

  df_inflacja = sheet_inflacja.iloc[25:100][[0, 1, 6]]
  # Rename columns for clarity
  df_inflacja.columns = ['Kwartał', 'CPI_Y2Y', "CPI_Q2Q"]

  return df_inflacja

