from pyDatalog.pyDatalog import assert_fact, load, ask
import base_conocimiento

def mostrar_resultado(resultado):
  print(resultado)

def pedir_por_pantalla(lista_menu):
  nombre_sintoma = raw_input('Seleccione: ' + str(lista_menu))
  return nombre_sintoma

def almacenar_respuesta_base_dinamica(nombre_sintoma):
  assert_fact( 'respuesta', 'hoja', nombre_sintoma )

def pantalla(lista_menu):
  nombre_sintoma=raw_input('Seleccione: ' + str(lista_menu))
  almacenar_respuesta_base_dinamica(nombre_sintoma)

def usar_regla_diagnostico():
  return base_conocimiento.consultar_diagnostico()

def consultar_base_dinamica():
  print(ask('respuesta(Organo,Sintoma)'))