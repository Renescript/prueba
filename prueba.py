import pandas as pd;
import numpy as np;


df = pd.read_excel('Registro Inicial.xlsx');

df.fillna({'Ley: 19.664 Estamento': 'Sin Estamento','Ley: 18.834 Estamento': 'Sin Estamento'});

df["course1"]= df["¿Cuál o cuáles cursos le interesan?"].str.split(",", n = 1, expand = False);

atributos = df['course1'];



arregloCursos = [];

def recorrerListaDeCursos(atributos):

    
    for i in atributos:
        cadena = ",".join(i)

        if ("," in cadena):
            cadena2 = cadena.split(", ")

            for x in cadena2:
                arregloCursos.append(x)
        else:
            arregloCursos.append(cadena)
            
    return arregloCursos

recorrerListaDeCursos(atributos);

cursosUnicos = pd.unique(arregloCursos);


df['firstname'] = df['Nombres'].str.title();

df['lastname'] = df['Apellidos'].str.title();


def transformarAString(telefono):
    telefonoString = repr(telefono)
    return telefonoString

df['TeléfonoNuevo'] = df['Teléfono'].apply(transformarAString);
    
df['TeléfonoNuevo'] = df['TeléfonoNuevo'].str.extract('.*(\d{8})', expand = False);



rut = df['RUT'].replace({' ':''}, regex=True);


rutsErroneos = [];

def devolverRut(rut):
    for i in rut:
        rutStr = str(i)
        if(len(rutStr) < 7):
            data = df.loc[df['RUT']==rutStr]
            np.savetxt(r'C:\Users\rpara\OneDrive\Escritorio\data.txt', data, fmt='%s')
            rutsErroneos.append(rutStr)
        else:
            df['RUT'] = df['RUT']
            
    return rutsErroneos

devolverRut(rut);


df['username'] = df['RUT'];


rutsConCuatroDigitos = [];

def obtenerCuatroNumerosRUT(rut):
    for i in rut:
        rutStr = str(i)
        rutsConCuatroDigitos.append(rutStr[0:4])

obtenerCuatroNumerosRUT(rut);


df['password'] = rutsConCuatroDigitos;


df['email'] = df['Dirección de correo electrónico'];


df['role1'] = 5;


df['institución'] = df['Establecimiento'];


df['profile_field_RUT'] = df['RUT'];




for i in cursosUnicos:
    tablaDinamica = df[df['¿Cuál o cuáles cursos le interesan?'].str.contains(i)]

    tablaDinamica.to_csv(f"{i}.csv",
                 sep= ",",
                 columns = {'username','password','firstname','lastname','email','course1','role1','institución','profile_field_RUT'})


