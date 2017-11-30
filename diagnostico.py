# -*- coding: utf-8 -*- 
tratamiento_enfermedad = {
  'moko': """ 
            1. Para el manejo de la enfermedad se requiere con confirmar el diagnóstico por parte del ICA y desarrollar el proceso de 
            erradicación de plantas afectadas y el control de focos de acuerdo con los protocolos de erradicación del ICA.
            2. Una vez se ha identi cado la presencia de moko, desde la planta enferma se toma un radio de 5 metros y se realiza un 
            encerrado con hilo, para un área de 78 m2, que tendrá una frecuencia de supervisión de una vez cada cuatro semanas 
            (zona verde: nada de afectación, zona amarilla: área de seguridad entre el foco y la zona productiva de la finca, 
            zona roja áreas afectadas) para distinguir los diferentes niveles de daño. Así se controlará esta enfermedad en todo el cultivo.
          """
}

def mostrar_tratamiento(enfermedad):
  print(""" 
            ----------------------------------------------------------------------------
                                    Diagnóstico de la Enfermedad
            ----------------------------------------------------------------------------
            Enfermedad: {}
            Tratamiento: {}

    """).format(enfermedad, tratamiento_enfermedad[enfermedad])
