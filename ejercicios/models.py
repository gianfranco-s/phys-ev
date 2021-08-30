from django.db import models
import re
import os

# Un modelo se representa por medio de una clase
class Ejercicio(models.Model):
    # Usar models hará que sea un poco más fácil la generación 
    titulo = models.CharField(max_length=50)   # 50 caracteres máximo
    tema = models.CharField(max_length=50)     # 50 caracteres máximo
    enunciado = models.TextField()
    algoritmo = models.TextField(null=True)

    def __str__(self):
        return self.titulo      # Representación en string
        
    def __makeAlgoritmo(self):
        '''
        Crea un módulo en base al algoritmo cargado por el usuario.
        '''

        os.makedirs('./temp_data', exist_ok=True)
        print("")
        print("")
        print(os.getcwd())
        print(os.listdir('.'))
        print("")
        print("")

        with open('./temp_data/algoritmo.py','w') as algoritmo_file:
            algoritmo_file.write(self.algoritmo)
            # Cambiar el nombre de archivo para que incluya <username+timestamp>
        
        return

    def __eraseAlgoritmo(self):
        '''
        Borra el algoritmo creado por __makeAlgoritmo.
        '''
        os.remove("./temp_data/algoritmo.py")
        
        return
        
    
    def redactar(self):             # Inactiva. Faltan revisiones.
        '''
        Dentro del enunciado, identifica,
        * las variables de enunciado
        * los resultados calculados
        
        Devuelve una cadena con todo lo anterior reemplazado 
        por los valores indicados en 'datos' y 'respuestas'.
        '''

        self.__makeAlgoritmo()             # Crea la librería "algoritmo"

        from temp_data import algoritmo     # "algoritmo" debe devolver los datos y las respuestas calculadas
        
        enunciado = self.enunciado
        datos,respuestas = algoritmo.ejercicio()
        
            
        dat_enunc = []                                  # Aquí se guardan los datos que pide el enunciado
        res_enunc = []                                  # Aquí se guardan las respuestas que pide el enunciado
        
        palabras = re.split(r'\s',enunciado)

        for variable in palabras:
            if '#' in variable:
                idx0 = variable.find('#') + 1            # Índice inicial de la variable = ubicación del caracter '#' + 1 (para eliminar el '#')

                if variable[idx0-2] == '{' and variable[-1] == '}':
                    resp_en = variable[idx0:-1]
                    res_enunc.append(resp_en)

                else:
                    dato_en = variable[idx0:]               # Recortar la variable, para excluir todos los caracteres que hayan antes de #
                    
                    if dato_en[-1].isalnum() is False:      # Si el último caracter *no* es alfanumérico, lo borra.
                        dato_en = variable[:-1]

                    dat_enunc.append(dato_en)
        
        for variable in dat_enunc+res_enunc:
            if variable.isalnum() is False:          # Si la variable incluye caracteres alfanuméricos, levantar excepción.
                    raise ValueError(f'Error al definir {variable}. Las variables no pueden contener caracteres alfanuméricos.')
                
            if variable[0].isdigit():                # Si la variable empieza con números, levantar excepción.
                raise ValueError(f'Error al definir {variable}. Las variables no pueden empezar con números.')
        
        # ---
        # Verificar si los las variables establecidas en el enunciado se corresponden con las variables del algoritmo, y levantar warning
        # set(variable_enunciado).intersection(set(variable_algoritmo))
        # ---
        
        # Agregar '#' para todos los elementos de dat_enunc
        old_dat_enunc = ['#'+variable for variable in dat_enunc]    # Es la manera Pythonica

        # Agregar '{#' <variable> '}' para todos los elementos de res_enunc
        old_res_enunc = ['{#'+variable+'}' for variable in res_enunc]    # Es la manera Pythonica


        # Reemplazar los datos numéricos en el enunciado.
        for i,item in enumerate(dat_enunc):
            enunciado = enunciado.replace(old_dat_enunc[i],str(datos[item]))

        # Reemplazar las respuestas por los valores calculados.    
        for i,item in enumerate(res_enunc):
            # enunciado = enunciado.replace(old_res_enunc[i],'<Tu respuesta>')      # Para la interacción con el usuario.
            enunciado = enunciado.replace(old_res_enunc[i],str(respuestas[item]))

        # Suma entre variables de enunciado y resultados calculados
        var_y_res = enunciado.count('#') # Para decidir si se realizó correctamente la conversión
        
        self.__eraseAlgoritmo()
        return enunciado