# -*- coding: utf-8 -*- 
import os

def limpiar_pantalla():
  os.system('clear')

def mensaje_salida():
    limpiar_pantalla()
    print(""" 
            ----------------------------------------------------------------------------
                                    Usted ha salido de la aplicación
            ----------------------------------------------------------------------------

    """)

def menu_principal():
    print("""
            Sistema Experto Para El Diagnostico de Enfermedades Platano Dominico Harton
            ----------------------------------------------------------------------------

                                            Menu Principal
            ----------------------------------------------------------------------------
            ----------------------------------------------------------------------------
            Que organo de la planta ha sido afectado?
            1. Hoja
            2. Cormo
            3. Seudotallo
            4. Obtener diagnóstico
            5. Salir del programa
    """)
    opcion = raw_input('Digite su opcion: ')
    return opcion

def pantalla_sintoma_menu_hoja():
    print(""" 
            Seleccione los sintomas que presenta la hoja
            ----------------------------------------------------------------------------
            1. Las hojas se secan y se quiebran, pero sin desprenderse de la planta
            2. Se presenta un secamiento de los bordes de las hojas, seguido de una franja de color amarillo intenso
            3. Se observa quemazón en el borde de las hojas más viejas que luego avanza a toda la lámina foliar, 
               ocasionando un amarillamiento total de la hoja.
            4. Amarillamiento de las hojas más adultas a lo largo del margen foliar que continúa hacia la nervadura central 
               hasta quedar las hojas completamente marchitas y de color café.
            5. Retornar al menú principal
    """)
    opcion = raw_input('Digite su opcion: ')
    limpiar_pantalla()
    return opcion

def pantalla_sintoma_cormo():
    print(""" 
            Seleccione los sintomas que presenta el cormo
            ----------------------------------------------------------------------------
            1. Al realizar un corte transversal al cormo se observan líneas de color marrón o negro
            2. Al realizar un corte transversal al cormo se observan un círculo de color marrón a negro que separa 
               la zona central de la zona en donde se forman las raíces.
            3. En el cormo los síntomas que padece son estrías necróticas, oscuras o azuladas que pueden observarse 
               sobre un fondo blanco
            4. Retornar al menú principal
    """)
    opcion = raw_input('Digite su opcion: ')
    return opcion

def pantalla_sintoma_seudotallo():
    print(""" 
            Seleccione los sintomas que presenta el seudotallo
            ----------------------------------------------------------------------------
            1. Al realizar un corte transversal en el seudotallo, aparecen unos puntos café oscuro que corresponden a los haces 
               vasculares taponados y necrosados por la bacteria
            2. El seudotallo posee manchas acuosas, translúcidas, de color amarillento en sus comienzos y 
               rojizo a castaño oscuro en sus últimas instancias
            3. El seudotallo presenta decoloración vascular en su interior
            4. Agrietamiento en la base del pseudotallo
            5. Retornar al menú principal
    """)
    opcion = raw_input('Digite su opcion: ')
    return opcion