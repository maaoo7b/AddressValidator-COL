import re
regexNomenclaturasA = "Administracion|Ad|Admin|Agencia|Agrupacion|Agp|Almacen|Alm|Altillo|Al|Apartado|Aptdo|Apto|Apt|Apartamento|Autopista|Aut|Avenida|Av|Ave"
regexNomenclaturasB = "Barrio|Brr|Bloque|Bl|Blq|Bodega|Bg|Boulevar|Blv"
regexNomenclaturasC = "Calle|Cll|Cl|Camino|Cn|Carrera|Cra|Cr|Kr|Kra|Carretera|Carr|Casa|Ca|Centro Comercial|Cc|Circunvalar|Crv|Ciudadela|Cd|Conjunto|Conj|Conjunto Residencial|Con|Consultorio|Cons|Corregimiento|Corr"
regexNomenclaturasD = "Departamento|Depto|Dpto|Deposito|Dp|Deposito Sotano|Ds|Diagonal|Dia|Dg"
regexNomenclaturasE = "Edificio|Ed|Entrada|En|Esq|Esquina|ESTE|Etapa|Et|Exterior|Ex|Ext"
regexNomenclaturasF = "Finca|Fca"
regexNomenclaturasG = "Garaje|Ga|Garaje Sotano|Gs"
regexNomenclaturasH = "Hacienda|Hc"
regexNomenclaturasI = "Interior|In"
regexNomenclaturasK = "Kilometro|Km"
regexNomenclaturasL = "Local|Lc|Lote|Lt"
regexNomenclaturasM = "Manzana|Mz|Modulo|Md|Municipio|Mcp|Mcpio|Mnpio"
regexNomenclaturasN = "NORTE"
regexNomenclaturasO = "OCCIDENTE|OESTE|Oficina|Of|ORIENTE"
regexNomenclaturasP = "Parcela|Pa|Parque|Par|Parqueadero|Pq|Pasaje|Pj|Paseo|Ps|Penthouse|Ph|Piso|P|Planta|Pl|Porteria|Por|Predio|Pd|Puente|Pte|Puesto|Pt"
regexNomenclaturasS = "Salon|Sa|Salon Comunal|Sc|Sector|Sec|Semisotano|Ss|Solar|Sl|Sotano|St|Suite|Su|SUR|Super Manzana|SM"
regexNomenclaturasT = "Terminal|Ter|Terraza|Tz|Torre|To|Transversal|Transv|Tv"
regexNomenclaturasU = "Unidad|Un|Unidad Residencial|Ur|Urbanizacion|Urb"
regexNomenclaturasV = "Variante|Vte|Vereda|Vda"
regexNomenclaturasZ = "Zona|Zn|"

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
cadenaNomenclaturas = regexNomenclaturasA+"|"+regexNomenclaturasB+"|"+regexNomenclaturasC
print(cadenaNomenclaturas)
regex = r"^((Avenida|Barrio|Calle|Cll|Carrera|Cra|Cr|Kra|Centro Comercial|Conjunto Residencial|Edificio|Ed|Finca|Km|Local|Torre|Transversal|Unidad Residencial|Vereda)){1} ?([0-9A-Z ]+)? ?(#|-)?([0-9A-Z ]+) ?((Avenida|Barrio|Calle|Cll|Carrera|Cra|Cr|Kra|Centro Comercial|Conjunto Residencial|Edificio|Ed|Finca|Km|Local|Torre|Transversal|Unidad Residencial|Vereda)|(#|No|-))?([ A-Z0-9]+)? ?((Avenida|Ap|Altillo|Barrio|Calle|Cll|Carrera|Cra|Centro Comercial|Conjunto Residencial|Edificio|Ed|Finca|Ga|Km|Local|Torre|Unidad Residencial|Vereda)|(#|No|-| ?)) ?([ 0-9A-Z])+(-|\/){0,}[A-Z0-9]+$"

test_str = ("EdSANFRANCISCO\n"
            "Ed SAN FRANCISCO\n"
            "Edificio SAN FRANCISCO\n"
            "Vereda LA VISTA Km 8 Finca ROSITA\n"
            "Vereda LA VISTA Km 8\n"
            "Transversal 23B # 27-30 ASODEA\n"
            "Cll12#16-22\n"
            "Cll 12 # 16-22\n"
            "Cra10No10-22\n"
            "Cra 10 No 10-22\n"
            "Carrera9AvenidaELSOL7-35\n"
            "Carrera 9 Avenida EL SOL 7-35\n"
            "EdificioMURANO9Calle9-45\n"
            "Edificio MURANO 9 Calle 9-45\n"
            "Carrera9BIS#22-06\n"
            "Carrera 9BIS # 22-06\n"
            "Calle23#9BIS28\n"
            "Calle 23 # 9BIS 28\n"
            "Calle 29 # 9-45\n"
            "Calle29#9-45\n"
            "Cra89A#12-12\n"
            "Cra 89A # 12-12\n"
            "Torre QW Cll 24 9A-58\n"
            "TorreQWCll249A-58\n"
            "Ed MURANO 9 Calle 24 9-06\n"
            "Edificio ANA VICTORIA Cll 24 9A-58\n"
            "Edificio ANA VICTORIA Calle 24 9A-58\n"
            "EdificioMEDITROPOLISLocal102\n"
            "Edificio MEDITROPOLIS Local 102\n"
            "Centro Comercial IWOKA Local 111A\n"
            "Centro ComercialIWOKALocal111A\n"
            "Cr 10 No 21-157\n"
            "Cr10No21-157\n"
            "Kra 9A No 23-55\n"
            "Kra9ANo23-55\n"
            "Cr 10A # 29-12\n"
            "Cr10A#29-12\n\n"
            "Carrera Calle\n"
            "Cra 10 # 10-22/28\n"
            "Edificio RAUDALITO Carrera 11 # 14-107\n"
            "Edificio ALAMEDA Kra 10 # 13-27\n"
            "Torre DEL RECREO Cll 29A # 9-35\n"
            "Edificio ALAMEDA Cra 10 # 13-27\n"
            "Conjunto Residencial IWOKA Cr 10 No 21-157\n"
            "Ed VILLA ROSITA Cll 42 No 9A 11/19\n\n"
            "Kra 9A # 23-55 Barrio EL ROBLE\n"
            "Cra 10A # 29-12 Torre KDIEZ APTO 103\n"
            "Torre GIRALDA Cra 9A # 29-30\n"
            "Calle 7 10A 19 Ap 203\n"
            "Calle 7 10A 23 Ga 9\n"
            "Carrera 13A #1-31 Ga 01 EDIFICIO TURQUESA\n"
            "Calle 1A 13A Ap 601\n"
            "Calle 1A 13A Altillo 601\n"
            "Calle 1A 13A 13 Ap 201\n"
            "Carrera 13#2A-38 SUR\n\n"
            "Edificio MEDITROPOLIS II Unidad Residencial SECTOR 3\n"
            "Corregimiento UVITA\n"
            "Carrera CCC\n\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))


# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
