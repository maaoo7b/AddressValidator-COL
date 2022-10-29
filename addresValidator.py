import re
regexNomenclaturasA = "Administracion|Ad|Admin|Agencia|Agrupacion|Agp|Almacen|Alm|Altillo|Al|Apartado|Aptdo|Apto|Apt|Ap|Apartamento|Autopista|Aut|Avenida|Av|Ave"
regexNomenclaturasB = "Barrio|Brr|Bloque|Bl|Blq|Bodega|Bg|Boulevar|Blv"
regexNomenclaturasC = "Calle|Cll|Cl|Camino|Cn|Carrera|Cra|Cr|Kr|Kra|Carretera|Carr|Casa|Ca|Centro Comercial|Cc|Circunvalar|Crv|Ciudadela|Cd|Conjunto|Conj|Conjunto Residencial|Con|Consultorio|Cons|Corregimiento|Corr"
regexNomenclaturasD = "Departamento|Depto|Dpto|Deposito|Dp|Deposito Sotano|Ds|Diagonal|Dia|Dg"
regexNomenclaturasE = "Edificio|Ed|Entrada|En|Esq|Esquina|ESTE|Etapa|Et|Exterior|Ex|Ext"
regexNomenclaturasF = "Finca|Fca"
regexNomenclaturasG = "Garaje|Ga|Garaje Sotano|Gs"
regexNomenclaturasH = "Hacienda|Hc"
regexNomenclaturasI = "Interior|In"
regexNomenclaturasK = "Kilometro|Km"
regexNomenclaturasL = "Local|Lc|Lote|Lt|Lugar"
regexNomenclaturasM = "Manzana|Mz|Modulo|Md|Municipio|Mcp|Mcpio|Mnpio"
regexNomenclaturasN = "NORTE"
regexNomenclaturasO = "OCCIDENTE|OESTE|Oficina|Of|ORIENTE"
regexNomenclaturasP = "Parcela|Pa|Parque|Par|Parqueadero|Pq|Pasaje|Pj|Paseo|Ps|Penthouse|Ph|Piso|P|Planta|Pl|Porteria|Por|Predio|Pd|Puente|Pte|Puesto|Pt"
regexNomenclaturasS = "Salon|Sa|Salon Comunal|Sc|Sector|Sec|Semisotano|Ss|Solar|Sl|Sotano|St|Suite|Su|SUR|Super Manzana|SM"
regexNomenclaturasT = "Terminal|Ter|Terraza|Tz|Torre|To|Transversal|Transv|Tv"
regexNomenclaturasU = "Unidad|Un|Unidad Residencial|Ur|Urbanizacion|Urb"
regexNomenclaturasV = "Variante|Vte|Vereda|Vda|Via"
regexNomenclaturasZ = "Zona|Zn"

cadenaNomenclaturas = regexNomenclaturasA+"|"+regexNomenclaturasB+"|"+regexNomenclaturasC+"|"+regexNomenclaturasD+"|"+regexNomenclaturasE+"|"+regexNomenclaturasF+"|"+regexNomenclaturasG+"|"+regexNomenclaturasH+"|"+regexNomenclaturasI+"|"+regexNomenclaturasK+"|"+regexNomenclaturasL+"|"+regexNomenclaturasM+"|"+regexNomenclaturasN+"|"+regexNomenclaturasO+"|"+regexNomenclaturasP+"|"+regexNomenclaturasS+"|"+regexNomenclaturasT+"|"+regexNomenclaturasU+"|"+regexNomenclaturasV+"|"+regexNomenclaturasZ
regex = r"^(("+cadenaNomenclaturas+")){1} ?([0-9A-Z ]+)? ?(#|-|No)?([0-9A-Z ]+) ?(("+cadenaNomenclaturas+")|(#|No|-))?([ A-Z0-9]+)? ?(("+cadenaNomenclaturas+")|(#|No|-| ?)) ?([ 0-9A-Z])+(-|\/){0,}[A-Z0-9]+$"

def readAddresses(fileAdresses):
    file = open(fileAdresses)
    addresses = file.read()
    matches = re.finditer(regex, addresses, re.MULTILINE)
    validAddresses(matches)


def validAddresses(matches):
    file = open('validAdresses.txt', 'w', encoding='utf-8')
    for matchNum, match in enumerate(matches, start=1):
        print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),end=match.end(), match=match.group()))
        file.write('Dirección: ' + match.group() + ' ----> VÁLIDA\n')
    file.close()