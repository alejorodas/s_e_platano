import base_conocimiento
import diagnostico

def mostrar_resultado(resultado):
  diagnostico.mostrar_tratamiento(resultado.v()[0])

def usar_regla_diagnostico():
  return base_conocimiento.consultar_diagnostico()

def almacenar_respuesta(organo,sintoma_seleccionado):
  #Moko
  if(sintoma_seleccionado == '1'):
    base_conocimiento.almacenar_respuesta_base_dinamica(organo,'seca')
  elif (sintoma_seleccionado == '2'):
    base_conocimiento.almacenar_respuesta_base_dinamica(organo,'quebradiza')
