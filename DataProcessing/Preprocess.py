import pandas as pd

def dodaj_kolumny_daty(df):
  """
  Konwertuje kwartały na daty i dodaje zmienne czasowe

  Returns:
      df (DataFrame): DataFrame z dodanymi kolumnami 'Data', 'rok', 'kwartal_num' i 'indeks_czasowy'.
  """    
  def kwartal_do_daty(kwartal_str):
    """Konwertuje string kwartału na datę"""
    try:
      # Rozdziel kwartał i rok
      czesci = kwartal_str.strip().split()
      if len(czesci) == 3:
        czesci = [czesci[0], czesci[-1]]
      elif len(czesci) != 2:
        return None
          
      kwartal_rom, rok = czesci
      
      # Mapowanie kwartałów rzymskich na miesiące
      kwartaly_map = {
        'I': '01-01',
        'II': '04-01', 
        'III': '07-01',
        'IV': '10-01'
      }
      
      if kwartal_rom in kwartaly_map:
        data_str = f"{rok}-{kwartaly_map[kwartal_rom]}"
        return pd.to_datetime(data_str)
      else:
        return None
          
    except Exception as e:
      print(f"Błąd przy konwersji {kwartal_str}: {e}")
      return None
  
  # Konwersja kwartałów na daty
  df['Data'] = df['Kwartał'].apply(kwartal_do_daty)
  
  # Usuń rekordy z błędnymi datami
  df = df.dropna(subset=['Data'])
  
  # Dodaj zmienne czasowe
  df['rok'] = df['Data'].dt.year
  df['kwartal_num'] = df['Data'].dt.quarter
  df['indeks_czasowy'] = range(len(df))
  
  return df


def polacz_dataframes(df1, df2, df3, on_col='Data'):
  """
  Łączy 3 DataFrames na określonej kolumnie.
  """
  merged_df = pd.merge(df1, df2, on=on_col, how='left')
  merged_df = pd.merge(merged_df, df3, on=on_col, how='left')
  return merged_df