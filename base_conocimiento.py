from pyDatalog import pyDatalog

# Organos de la planta
pyDatalog.create_terms('hoja, cormo, seudotallo, raquis, racimos, dedo')

# Predicados y reglas
pyDatalog.create_terms('tiene_sintoma, diagnostico, enfermedad, respuesta')

# Variables
pyDatalog.create_terms('Enfermedad')

# Moko
+hoja('seca')
+hoja('quebradiza')
+hoja('no_se_desprende')
+hoja('seca_en_bordes')
+hoja('franja_color_amarilla_intenso')
+cormo('linea_color_marron')
+cormo('linea_color_negro')
+cormo('circulo_color_marron')
+seudotallo('puntos_cafes_oscuros')
+raquis('color_rojizo')
+racimos('deformes')
+dedo('deformes')

# Pudricioon acuosa del pseudotallo bacteriosis (Dickeya chrysanthemi)
+hoja('quemazon_hojas_viejas')
+hoja('amarillamiento_total')
+seudotallo('manchas_acuosas_translucidas_color_amarillento')
+seudotallo('manchas_acuosas_translucidas_rojizo')
+seudotallo('debil')

# Mal de Panama
+hoja('amarillamiento')
+hoja('marchita')
+hoja('colo_cafe')
+seudotallo('agriegado')
+seudotallo('decoloracion_vascular')
+cormo('estrias_necroticas')
+cormo('estrias_oscuras')
+cormo('estrias_azuladas')

# Moko
+tiene_sintoma('hoja','seca') 
+tiene_sintoma('hoja','quebradiza')
+tiene_sintoma('hoja','no_se_desprende')
+tiene_sintoma('hoja','seca_en_bordes')
+tiene_sintoma('hoja','franja_color_amarilla_intenso')
+tiene_sintoma('cormo','linea_color_marron')
+tiene_sintoma('cormo','linea_color_negro')
+tiene_sintoma('seudotallo','puntos_cafes_oscuros')


# Moko o madurabiche 
enfermedad('moko') <= tiene_sintoma('hoja','seca') & \
                      tiene_sintoma('hoja','quebradiza') & \
                      tiene_sintoma('hoja','no_se_desprende') & \
                      tiene_sintoma('hoja','seca_en_bordes') & \
                      tiene_sintoma('hoja','franja_color_amarilla_intenso') & \
                      tiene_sintoma('cormo','linea_color_marron') & \
                      tiene_sintoma('cormo','linea_color_negro') & \
                      tiene_sintoma('seudotallo','puntos_cafes_oscuros')




diagnostico('moko') <= respuesta('hoja','seca') & respuesta('hoja','quebradiza') & \
                      respuesta('hoja','no_se_desprende') & \
                      respuesta('hoja','seca_en_bordes') & \
                      respuesta('hoja','franja_color_amarilla_intenso') & \
                      respuesta('cormo','linea_color_marron') & \
                      respuesta('cormo','linea_color_negro') & \
                      respuesta('seudotallo','puntos_cafes_oscuros')

#diagnostico('moko') <= respuesta('hoja',Sintoma1) & respuesta('hoja',Sintoma2)& (Sintoma1 != Sintoma2)
#diagnostico('moko') <= tiene_sintoma(Organo, Sintoma1), tiene_sintoma(Organo, Sintoma2) & (Sintoma1 != Sintoma2)
#diagnostico(Enfermedad, Sintoma1,Sintoma2) <= tiene_sintoma('hoja',Sintoma1) & tiene_sintoma('hoja',Sintoma2) & (Sintoma1 != Sintoma2) & (Enfermedad == 'moko')

def consultar_diagnostico():
  return diagnostico(Enfermedad)

def almacenar_respuesta_base_dinamica(organo,nombre_sintoma):
  assert_fact( 'respuesta', organo, nombre_sintoma )
