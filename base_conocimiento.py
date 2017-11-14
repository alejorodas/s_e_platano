from pyDatalog import pyDatalog

# Organos de la planta
pyDatalog.create_terms('hoja, cormo, seudotallo, raquis, racimos, dedo')

# Predicados y reglas
pyDatalog.create_terms('tiene_sintoma, diagnostico, enfermedad, respuesta')

# Variables
pyDatalog.create_terms('Enfermedad')


+hoja('seca')
+hoja('quebradiza')
+hoja('no_se_desprende')
+hoja('seca_en_bordes')
+hoja('franja_color_amarilla_intenso')
+cormo('linea_color_marron')
+cormo('linea_color_negro')
+seudotallo('puntos_cafes_oscuros')
+raquis('color_rojizo')
+racimos('deformes')
+dedo('deformes')


+hoja('amarillamiento_total')
+seudotallo('manchas_acuosas')
+seudotallo('manchas_translucidas_color_amarillento')
+seudotallo('manchas_translucidas_rojizo')
+seudotallo('debil')


+hoja('amarillamiento')
+hoja('marchita')
+hoja('colo_cafe')
+seudotallo('agriegado')
+seudotallo('agriegado')


+tiene_sintoma('hoja','seca') 
+tiene_sintoma('hoja','quebradiza')


enfermedad('moko') <= tiene_sintoma('hoja','seca') & tiene_sintoma('hoja','quebradiza')
diagnostico('moko') <= respuesta('hoja','seca') & respuesta('hoja','quebradiza')

#diagnostico('moko') <= respuesta('hoja',Sintoma1) & respuesta('hoja',Sintoma2)& (Sintoma1 != Sintoma2)
#diagnostico('moko') <= tiene_sintoma(Organo, Sintoma1), tiene_sintoma(Organo, Sintoma2) & (Sintoma1 != Sintoma2)
#diagnostico(Enfermedad, Sintoma1,Sintoma2) <= tiene_sintoma('hoja',Sintoma1) & tiene_sintoma('hoja',Sintoma2) & (Sintoma1 != Sintoma2) & (Enfermedad == 'moko')

def consultar_diagnostico():
  return diagnostico(Enfermedad)
