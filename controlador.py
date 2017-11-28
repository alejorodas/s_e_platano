import base_conocimiento

def mostrar_resultado(resultado):
  print(resultado)

def pedir_por_pantalla(lista_menu):
  nombre_sintoma = raw_input('Seleccione: ' + str(lista_menu))
  return nombre_sintoma

def pantalla(lista_menu):
  nombre_sintoma=raw_input('Seleccione: ' + str(lista_menu))
  almacenar_respuesta_base_dinamica(nombre_sintoma)

def usar_regla_diagnostico():
  return base_conocimiento.consultar_diagnostico()

def almacenar_respuesta(organo,sintoma_seleccionado):
  #Moko
  if(sintoma_seleccionado == '1'):
    base_conocimiento.almacenar_respuesta_base_dinamica(organo,'seca')
  elif (sintoma_seleccionado == '2'):
    base_conocimiento.almacenar_respuesta_base_dinamica(organo,'quebradiza')
