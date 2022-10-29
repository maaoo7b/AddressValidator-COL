import re
regexNomenclaturasA = "Administracion|Ad|Admin|Adelante|Adl|Aeropuerto|Aer|Agencia|Ag|Agrupacion|Agp|Avenida Carrera|Ak|Almacen|Alm|Altillo|Al|Al lado|Ald|Apartado|Aptdo|Apto|Apt|Ap|Apartamento|Atras|Atr|Autopista|Aut|Avenida|Av|Ave|Anillo Vial|Avial"
regexNomenclaturasB = "Barrio|Brr|Bloque|Bl|Blq|Bodega|Bg|Boulevard|Blv"
regexNomenclaturasC = "Calle|Cll|Cl|Camino|Cn|Carrera|Cra|Cr|Kr|Kra|Carretera|Carr|Crt|Casa|Ca|Caserio|Cas|Centro Comercial|Cc|Centro|Cen|Circunvalar|Crv|Ciudadela|Cd|Conjunto|Conj|Conjunto Residencial|Con|Consultorio|Cons|Corregimiento|Corr|Callejon|Clj"
regexNomenclaturasD = "Departamento|Depto|Dpto|Deposito|Dp|Deposito Sotano|Ds|Diagonal|Dia|Dg"
regexNomenclaturasE = "Edificio|Ed|Entrada|En|Esq|Esquina|ESTE|Etapa|Et|Exterior|Ex|Ext|Escalera|Es"
regexNomenclaturasF = "Finca|Fca"
regexNomenclaturasG = "Garaje|Ga|Garaje Sotano|Gs|Glorieta|Gt"
regexNomenclaturasH = "Hacienda|Hc|Hangar|Hg"
regexNomenclaturasI = "Interior|In|Inspeccion Policia|Ip|Inspeccion Departamental|Ipd|Inspeccion Municipal|Ipm"
regexNomenclaturasK = "Kilometro|Km"
regexNomenclaturasL = "Local|Lc|Lote|Lt|Lugar"
regexNomenclaturasM = "Manzana|Mz|Modulo|Md|Municipio|Mcp|Mcpio|Mnpio|Muelle|Mll"
regexNomenclaturasN = "NORTE"
regexNomenclaturasO = "OCCIDENTE|OESTE|Oficina|Of|ORIENTE"
regexNomenclaturasP = "Parcela|Pa|Parque|Par|Parqueadero|Pq|Pasaje|Pj|Paseo|Ps|Penthouse|Ph|Piso|P|Planta|Pl|Porteria|Por|Predio|Pd|Puente|Pte|Puesto|Pt|Poste|Pos|Paraje|Prj"
regexNomenclaturasR = "Round Point|Rp"
regexNomenclaturasS = "Salon|Sa|Salon Comunal|Sc|Sector|Sec|Salida|Sd|Semisotano|Ss|Solar|Sl|Sotano|St|Suite|Su|SUR|Super Manzana|SM"
regexNomenclaturasT = "Terminal|Ter|Terraza|Tz|Torre|To|Transversal|Transv|Tv"
regexNomenclaturasU = "Unidad|Un|Unidad Residencial|Ur|Urbanizacion|Urb"
regexNomenclaturasV = "Variante|Vte|Vereda|Vda|Via"
regexNomenclaturasZ = "Zona|Zn|Zona Franca|Zf"

cadenaNomenclaturas = regexNomenclaturasA+"|"+regexNomenclaturasB+"|"+regexNomenclaturasC+"|"+regexNomenclaturasD+"|"+regexNomenclaturasE+"|"+regexNomenclaturasF+"|"+regexNomenclaturasG+"|"+regexNomenclaturasH+"|"+regexNomenclaturasI+"|"+regexNomenclaturasK+"|"+regexNomenclaturasL+"|"+regexNomenclaturasM+"|"+regexNomenclaturasN+"|"+regexNomenclaturasO+"|"+regexNomenclaturasP+"|"+regexNomenclaturasR+"|"+regexNomenclaturasS+"|"+regexNomenclaturasT+"|"+regexNomenclaturasU+"|"+regexNomenclaturasV+"|"+regexNomenclaturasZ
regex = r"^(("+cadenaNomenclaturas+")){1} ?([0-9A-Z ]+)? ?(#|-|No)?([0-9A-Z ]+) ?(("+cadenaNomenclaturas+")|(#|No|-))?([ A-Z0-9]+)? ?(("+cadenaNomenclaturas+")|(#|No|-| ?)) ?([ 0-9A-Z])+(-|\/){0,}[A-Z0-9]+$"

def readAddresses(fileAdresses):
    file = open(fileAdresses)
    addresses = file.read()
    matches = re.finditer(regex, addresses, re.MULTILINE)
    validAddresses(matches)


def validAddresses(matches):
    file = open('validAdresses.txt', 'w', encoding='utf-8')
    for matchNum, match in enumerate(matches, start=1):
        print("Match {matchNum} : {match}".format(matchNum=matchNum, start=match.start(),end=match.end(), match=match.group()))
        file.write('Dirección: ' + match.group() + ' ----> VÁLIDA\n')
    file.close()