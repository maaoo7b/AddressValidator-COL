import re
regexNomenclaturasA = "ADMINISTRACIÓN|AD|ADMIN|AGENCIA|AGAGRUPACIÓN|AGP|ALMACEN|ALM|ALTILLO|AL|APARTADO|APTDO|APTO|APT|APARTAMENTO|AUTOPISTA|AUT|AVENIDA|AV|AVE"
regexNomenclaturasB= "BARRIO|BRR|BLOQUE|BL|BLQ|BODEGA|BG|BOULEVAR|BLV"
regexNomenclaturasC= "CALLE|CLL|CL|CAMINO|CN|CARRERA|KRA|CRA|CR|KR|CARRETERA|CARR|CASA|CA|CENTRO COMERCIAL|CC|CIRCUNVALAR|CRV|CIUDADELA|CD|CONJUNTO|CONJ|CONJUNTO RESIDENCIAL|CON|CONSULTORIO|CONS|CSCORREGIMIENTO|CORR"

regex2 = "([0-9]+)?([A-Z]{1})?(#)[0-9]+(-)[0-9]+"
regex = fr"^(${regexNomenclaturasA}|${regexNomenclaturasB}|${regexNomenclaturasC})"+regex2

test_str = ("a \n"
            "babbaba\n"
            "babskljasda\n"
            "a a\n"
            "a\n"
            "a\n"
            "a\n"
            "cracracracra\n"
            "crab\n"
            "crcra\n"
            "cr89W#12-12\n"
            "CONJUNTO RESIDENCIAL89W#12-12\n"
            "BRR89#12-12\n"
            "craW#12-12\n"
            "ADW#12-12\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
