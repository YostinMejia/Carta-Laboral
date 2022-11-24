from docxtpl import DocxTemplate
import sqlite3 as sql

def crear_carta_laboral(cc: str, incluye_salario:bool):
    con = sql.connect("empleados.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM empleados WHERE cc = ?",(cc,))
    datos = cur.fetchall()
    con.close()

    if len(datos) != 0:

        nombre = datos[0][1]
        inicio_contrato = datos[0][2]
        cargo = datos[0][3]
        termino_contrato = datos[0][4]
        salario = datos[0][5]

        if incluye_salario:

            documento = DocxTemplate("plantillas/salario_carta_laboral.docx")
            actualizar = {"nombre_solicitante": nombre, "cc": cc, "inicio_contrato": inicio_contrato, "cargo": cargo, "termino_contrato": termino_contrato, "salario": salario}

        else:
            documento = DocxTemplate("plantillas/no_salario_carta_laboral.docx")
            actualizar = {"nombre_solicitante": nombre, "cc": cc, "inicio_contrato": inicio_contrato, "cargo": cargo, "termino_contrato": termino_contrato}
      
        documento.render(actualizar)
        documento.save(f"documentos/{cc}_carta_laboral.docx")


        return("DOCUMENTO CREADO")

    else:
        return("CC erronea")
