import pandas as pd

# Read Excel file into a DataFrame
df = pd.read_excel('all.xlsx')

print(len(df))

#a1952 = df[df['FECHA'].dt.year == 1952]

años = range(1952, 1953)

# Bucle anidado para iterar sobre los años
for año in años:
  
    df_anio = df[df['FECHA'].dt.year == año]
    # Save the filtered data to a new Excel file
    df_anio.to_excel(f"{df_anio}.xlsx", index=False)

