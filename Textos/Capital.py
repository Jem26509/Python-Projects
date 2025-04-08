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
                           "Mpr",
                           "Mrp",
                           "Odata",
                           "Oops",
                           "Pdf",
                           "Po-pi",
                           "Python",
                           "Rad",
                           "Restful",
                           "Sap",
                           "Scrum",
                           "Sql",
                           "Ssff",
                           "Ui5",
                           "Windows",
                           "Workflow",
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
                           "S4", "s4",
                           "Sd", "sd",
                           "Vb", "vb"
                           ]
        self.eotroses = [
                          "(a",
                          "(b",
                          "(c",
                          "(d",
                          "(e",
                          "(f",
                          "(g",
                          "(h",
                          "(i",
                          "(j",
                          "(k",
                          "(l",
                          "(m",
                          "(n",
                          "(o",
                          "(p",
                          "(q",
                          "(r",
                          "(s",
                          "(t",
                          "(u",
                          "(v",
                          "(w",
                          "(x",
                          "(y",
                          "(z"
                          ]
        #print('A', self.txt)

    def capital(self):
        txt, ext = os.path.splitext(self.txt)
        #print('C', txt) #print('D', ext)
        if 'ci n' in txt:
           txt = txt.replace('ci n', 'ción')

        if 'ci N' in txt:
           txt = txt.replace('ci N', 'ción')

        text = txt.split(" ")
        for i in range(0, len(text)):
            if len(text[i]) > 2:
              text[i] = text[i].capitalize()

            if len(text[i]) <= 2:
              text[i] = text[i].lower()

            if len(text[i]) == 1:
              text[i] = text[i].upper()

            if text[i] in self.reservadas:
              text[i] = text[i].upper()

            if text[i].find("(") >= 0:
              otro = text[i].split("(")
              otro[1] = otro[1].capitalize()
              text[i] = "(" + otro[1]

        delimiter = " "
        self.txt = delimiter.join(text) + ext
        self.txt = self.txt.strip()

        return self.txt
