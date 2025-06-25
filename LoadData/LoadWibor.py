def load_wibor():
  """
  Funkcja wczytuje dane WIBOR z pliku CSV i przetwarza je.
  
  Returns:
      df_wibor (DataFrame): Przetworzony DataFrame z danymi WIBOR.
  """
  import pandas as pd

  # Wczytaj plik CSV
  df_wibor = pd.read_csv("wibor.csv")

  # Dodaj jeden dzień do każdej daty w kolumnie 'Data'
  df_wibor['Data'] = pd.to_datetime(df_wibor['Data']) + pd.Timedelta(days=1)
  df_wibor = df_wibor[['Data', 'Zamkniecie']]
  # Zmień nazwę kolumny 'Zamkniecie' na 'WIBOR'
  df_wibor.rename(columns={'Zamkniecie': 'WIBOR'}, inplace=True)

  return df_wibor
