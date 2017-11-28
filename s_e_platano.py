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
    opcion = ui.menu_principal()
    if opcion == '4':
      break
    elif opcion == '1':
      sintoma_seleccionado = ui.menu_hoja()
      controlador.almacenar_respuesta('hoja',sintoma_seleccionado)
    # elif opcion == '2':
    #   ui.menu_cormo()
    # elif opcion == '3':
    #   ui.menu_seudotallo()
    else:
      controlador.pantalla(lista_menu)

  controlador.consultar_base_dinamica()
  resultado = controlador.usar_regla_diagnostico()
  controlador.mostrar_resultado(resultado)

main()
