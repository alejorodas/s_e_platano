from pyDatalog import pyDatalog, pyEngine
from pyDatalog.pyDatalog import assert_fact, load, ask
import logging

pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

pyDatalog.create_terms('Organo,Enfermedad, print_, tiene_sintoma, diagnostico, enfermedad, respuesta')
pyDatalog.create_terms('X, Y, Z, Sintoma1, Sintoma2')

lista_menu = ['seca', 'quebradiza', 'no_se_desprende', 'seca_en_bordes', 'franja_color_amarilla_intenso', 'amarillamiento_total', 'amarillamiento']


diagnostico('moko') <= respuesta('hoja','seca') & respuesta('hoja','quebradiza')

def almacenar_respuesta_base_dinamica(nombre_sintoma):
  assert_fact( 'respuesta', 'hoja', nombre_sintoma )

def consultar_base_dinamica():
  print(ask('respuesta(Organo,Sintoma)'))

def print_(x):
    print('Print es {}: ').format(type(x))

def mostrar_resultado(resultado):
  print(resultado)

def pedir_por_pantalla(lista_menu):
  nombre_sintoma = raw_input('Seleccione: ' + str(lista_menu))
  return nombre_sintoma

def pantalla(lista_menu):
  nombre_sintoma=raw_input('Seleccione: ' + str(lista_menu))
  almacenar_respuesta_base_dinamica(nombre_sintoma)

def usar_regla(nombre_sintoma):
  return diagnostico(Enfermedad,nombre_sintoma)

def consultar_diagnostico():
  return diagnostico(Enfermedad)

def main():
  estado = True
  while estado:
    opcion = raw_input('Desea seguir en el programa? [S/N]')
    if opcion == 'N':
      break
    else:
      pantalla(lista_menu)
      # nombre_sintoma = pedir_por_pantalla(lista_menu)
      # resultado = usar_regla(nombre_sintoma)
      # mostrar_resultado(resultado)
  consultar_base_dinamica()
  resultado = consultar_diagnostico()
  mostrar_resultado(resultado)

main()
