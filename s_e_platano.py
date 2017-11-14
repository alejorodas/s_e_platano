from pyDatalog import pyDatalog, pyEngine
from pyDatalog.pyDatalog import assert_fact, load, ask
import logging
import controlador

pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

pyDatalog.create_terms('diagnostico, enfermedad, respuesta')

lista_menu = ['seca', 'quebradiza', 'no_se_desprende', 'seca_en_bordes', 'franja_color_amarilla_intenso', 'amarillamiento_total', 'amarillamiento']

def main():
  estado = True
  while estado:
    opcion = raw_input('Desea seguir en el programa? [S/N]')
    if opcion == 'N':
      break
    else:
      controlador.pantalla(lista_menu)

  controlador.consultar_base_dinamica()
  resultado = controlador.usar_regla_diagnostico()
  controlador.mostrar_resultado(resultado)

main()
