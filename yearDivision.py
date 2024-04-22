import time
import pandas as pd

def divideYear():

    print("Iniciando proceso yearDivision...")
    #Con sheet_name=None extrae las dos, ver como acceder a ellas para hacerles a ambas el fix de fechas. 
    #Y ver si realmente te conviene extraerlas juntas.
    df = pd.read_excel('all.xlsx', sheet_name=None, skiprows=range(0),nrows=2500)

    print("Información extraída.")
    time.sleep(1)

    print(df)

    años = range(1955, 1956)
   
    for año in años:

        print("Estoy en el año: ", año)
            
        df_anio = df[df['FECHA'].dt.year == año]
        print("Obtuve el dataset del año: ", año)
        print("Arreglando fecha...")
        df_anio['FECHA'] = df_anio['FECHA'].dt.strftime('%Y/%m/%d')
        print("Se arreglo fecha correctamente...")
        df_anio.to_excel(f"excels/a{año}.xlsx", index=False)

    return "OK"

if __name__ == "__main__":
    divideYear()