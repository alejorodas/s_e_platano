from pyDatalog import pyDatalog, pyEngine
from pyDatalog.pyDatalog import assert_fact, load, ask
import logging
import controlador
import ui

pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

pyDatalog.create_terms('diagnostico, enfermedad, respuesta')

lista_menu = ['seca', 'quebradiza', 'no_se_desprende', 'seca_en_bordes', 'franja_color_amarilla_intenso', 'amarillamiento_total', 'amarillamiento']

def main():
  estado = True
  while estado:
    ui.menu_principal()
    opcion = raw_input('Digite su opcion: ')
    if opcion == '7':
      break
    elif opcion == '1':
      ui.menu_hoja()
      opcion = raw_input('Digite su opcion: ')
    # elif opcion == '':
    #   #corno
    # elif opcion == '':
    #   #seudotallo
    # elif opcion == '':
    #   #raquis
    # elif opcion == '':
    #   #racimos
    # elif opcion == '':
    #   #dedos
    else:
      controlador.pantalla(lista_menu)

  controlador.consultar_base_dinamica()
  resultado = controlador.usar_regla_diagnostico()
  controlador.mostrar_resultado(resultado)

main()
