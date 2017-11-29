from pyDatalog import pyDatalog, pyEngine
import logging
import controlador
import ui

pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

def menu_hoja():
  estado = True
  while estado:
    opcion = ui.pantalla_sintoma_menu_hoja()
    if opcion == '5':
        break
    else:
       controlador.almacenar_respuesta('hoja',opcion)

def main():
  estado = True
  while estado:
    opcion = ui.menu_principal()
    if opcion == '5':
      ui.mensaje_salida()
      break
    elif opcion == '1':
      menu_hoja()
      
    # elif opcion == '2':
    #   ui.menu_cormo()
    # elif opcion == '3':
    #   ui.menu_seudotallo()
    elif opcion == '4':
      resultado = controlador.usar_regla_diagnostico()
      controlador.mostrar_resultado(resultado)
    else:
      controlador.pantalla(lista_menu)


if __name__ == '__main__':
  main()

