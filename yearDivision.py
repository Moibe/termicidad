import pandas as pd
import time

def divideYear():

    print("Entré correctamente a yearDivision...")

    # Read Excel file into a DataFrame
    df = pd.read_excel('all.xlsx', skiprows=range(0),nrows=26000)
    

    
    print(len(df))
    #print(df)

    #a1952 = df[df['FECHA'].dt.year == 1952]

    años = range(1952, 1953)

    # Bucle anidado para iterar sobre los años
    # for año in años:

    #     print("Estoy en el año: ", año)
    #     time.sleep(1)
    
    #     df_anio = df[df['FECHA'].dt.year == año]
    #     print("Obtuve df_anio el dataset.")
    #     time.sleep(10)
    #     print("Es esto: ", df_anio)
    #     # Save the filtered data to a new Excel file
    #     #df_anio.to_excel(f"{df_anio}.xlsx", index=False)

    # return "OK"


if __name__ == "__main__":
    # Code that should only run when the script is executed directly
    print("Running the script directly...")
    divideYear()