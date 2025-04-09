import os

class Capital:
    def __init__(self, texto):
        self.txt = texto
        self.reservadas = [
                           "Abap",
                           "Adt", 
                           "Agile",
                           "Alv",
                           "Apis",
                           "Ariba",
                           "Aws",
                           "Azure",
                           "Badi",
                           "Badis",
                           "Bapi",
                           "Bapis",
                           "Bi", 
                           "Brf",
                           "Btp",
                           "Cds",
                           "Ci-cd",
                           "Cpi",
                           "Dax",
                           "Devops",
                           "Dra",
                           "Ec2",
                           "Ewm",
                           "Fhir",
                           "Fico",
                           "Fiori",
                           "Git",
                           "Hana",
                           "Hl7",
                           "Idocs",
                           "Is-h",
                           "Java",
                           "Jira",
                           "Linux",
                           "Lsmw",
                           "Mpr",
                           "Mrp",
                           "Note",
                           "Odata",
                           "Oops",
                           "Pdf",
                           "Pl-sql",
                           "Po-pi",
                           "Ptp",
                           "Python",
                           "Rad",
                           "Sap",
                           "Scrum",
                           "Snote",
                           "Sql",
                           "Sqvi",
                           "Ssff",
                           "Ui5",
                           "Windows",
                           "X-road",
                           "Aa", "aa",
                           "Ai", "ai",
                           "Bi", "bi",
                           "Bp", "bp",
                           "Co", "co",
                           "Fi", "fi",
                           "Hr", "hr",
                           "Ia", "ia",
                           "Mm", "mm",
                           "Nw", "nw",
                           "Oo", "oo",
                           "Pm", "pm",
                           "Po", "po",
                           "Pp", "pp",
                           "Ps", "ps",
                           "Qa", "qa",
                           "R3", "r3",
                           "S4", "s4",
                           "Sd", "sd",
                           "Vb", "vb",
                           "Wf", "wf"
                           ]
        self.otros = [ "(a", "(b", "(c", "(d", "(e", "(f", "(g", "(h", "(i", "(j", "(k", "(l", "(m",
                       "(n", "(o", "(p", "(q", "(r", "(s", "(t", "(u", "(v", "(w", "(x", "(y", "(z" ]


    def capital(self):
        txt, ext = os.path.splitext(self.txt)
        txt = txt.lower()


        #Excepciones por Ortografía
        if 'ci n' in txt:
           txt = txt.replace('ci n', 'ción')

        if 'ci N' in txt:
           txt = txt.replace('ci N', 'ción')

        if 'c mo' in txt:
           txt = txt.replace('c mo', 'cómo')

        if 'gu a' in txt:
           txt = txt.replace('gu a', 'guía')

        if 'h bitos' in txt:
           txt = txt.replace('h bitos', 'hábitos')

        if 'bolet n' in txt:
           txt = txt.replace('bolet n', 'boletín')

        if 'm todo' in txt:
           txt = txt.replace('m todo', 'método')

        if 'pol tica' in txt:
           txt = txt.replace('pol tica', 'política')

        if 'gesti n' in txt:
           txt = txt.replace('gesti n', 'gestión')

        if 'ingenier a' in txt:
           txt = txt.replace('ingenier a', 'ingeniería')


        #Excepciones por Palabras Clave
        if 's 4 hana' in txt:
           txt = txt.replace('s 4 hana', 's4 hana')

        if 'tcode' in txt:
           txt = txt.replace('tcode', 't-code')

        if 't code' in txt:
           txt = txt.replace('t code', 't-code')


        text = txt.split(" ")
        for i in range(0, len(text)):
            if i == 0:
               text[i] = text[i].capitalize()

            #if len(text[i]) == 1:
            #  text[i] = text[i].upper()

            if len(text[i]) > 2:
              text[i] = text[i].capitalize()

            #Excepciones x Palabra Reservada
            if text[i] in self.reservadas:
              text[i] = text[i].upper()

            #Excepciones x Paréntesis
            if text[i].find("(") >= 0:
              otro = text[i].split("(")
              otro[1] = otro[1].capitalize()
              text[i] = "(" + otro[1]

            #Excepciones x Palabra Clave
            if 'T-code' in text[i]:
              text[i] = text[i].replace('T-code', 'T-Code')

            if 'APIS' in text[i]:
              text[i] = text[i].replace('APIS', 'APIs')

            if 'BADIS' in text[i]:
              text[i] = text[i].replace('BADIS', 'BADIs')


        delimiter = " "
        self.txt = delimiter.join(text) + ext
        self.txt = self.txt.strip()

        return self.txt
