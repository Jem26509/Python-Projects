import os

class Capital:
   def __init__(self, texto):
      self.txt = texto
      #Excepciones por Ortografía
      self.Excep_01 = [
                        ["ci n","ción"],
                        ["c mo","cómo"],
                        ["gu a", "guía"],
                        ["h bitos", "hábitos"],
                        ["bolet n", "boletín"],
                        ["m todo", "método"],
                        ["pol tica", "política"],
                        ["gesti n", "gestión"],
                        ["ingenier a", "ingeniería"],
                        ["c digo", "código"],
                        [" d a ", " día "],
                        ["s 4 hana", "s4 hana"],
                        ["s4hana", "s4 hana"],
                        ["s 4hana", "s4 hana"],
                        ["tcode", "t-code"],
                        ["t code", "t-code"],
                        [" is h ", " is-h "],
                        ["auditor as ","auditorías "],
                        ["wi fi","wifi"],
                        ["almac n","almacén"],
                        ["p gina","página"],
                        ["f sica","física"],
                        ["at mico","atómico"],
                        ["categor a","categoría"],
                        [" docx",""]
                     ]
      #Excepciones x Palabra Reservada
      self.Excep_02 = [
                        "Abap",
                        "Adt", 
                        "Agile",
                        "Alv",
                        "Amdp",
                        "Apis",
                        "Ariba",
                        "Asap",
                        "Aws",
                        "Azure",
                        "Badi",
                        "Badis",
                        "Bapi",
                        "Bapis",
                        "Bbp",
                        "Bds",
                        "Bi", 
                        "Brf",
                        "Btp",
                        "Bwp",
                        "Cda",
                        "Cds",
                        "Ci-cd",
                        "Cmod",
                        "Cpi",
                        "Cpwi",
                        "Dax",
                        "Devops",
                        "Dra",
                        "E2e",
                        "Ec2",
                        "Ecc",
                        "Erp",
                        "Ewm",
                        "Fhir",
                        "Fico",
                        "Fiori",
                        "Git",
                        "Hana",
                        "Hcm",
                        "Hl7",
                        "Html",
                        "Idocs",
                        "Idoc",
                        "Is-h",
                        "Java",
                        "Jira",
                        "Linux",
                        "Lsmw",
                        "Mpr",
                        "Mrp",
                        "N1mepi",
                        "Note",
                        "Odata",
                        "Oops",
                        "Pdf",
                        "Pld",
                        "Pl-sql",
                        "Pmbok",
                        "Po-pi",
                        "Ptp",
                        "Python",
                        "Rad",
                        "Rfc",
                        "Sap",
                        "Scrum",
                        "Se11",
                        "Snote",
                        "Spau",
                        "Sql",
                        "Sqvi",
                        "Ssff",
                        "Ui5",
                        "Uml",
                        "Vpc",
                        "Windows",
                        "X-road",
                        "Aa", "aa",
                        "Ai", "ai",
                        "Bi", "bi",
                        "Bp", "bp",
                        "Co", "co",
                        "Fi", "fi",
                        "Hp", "hp",
                        "Hr", "hr",
                        "Ia", "ia",
                        "Mm", "mm",
                        "Nw", "nw",
                        "Oo", "oo",
                        "Pi", "pi",
                        "Pm", "pm",
                        "Po", "po",
                        "Pp", "pp",
                        "Pr", "pr",
                        "Ps", "ps",
                        "Qa", "qa",
                        "R3", "r3",
                        "Rn", "rn",
                        "S4", "s4",
                        "Sd", "sd",
                        "Ui", "ui",
                        "Vb", "vb",
                        "Wf", "wf"
                     ]
      #Excepciones x Palabra Clave
      self.Excep_03 = [
                        ["T-code", "T-Code"],
                        ["APIS", "APIs"],
                        ["BADIS", "BADIs"],
                        ["Gaps", "GAPs"],
                        ["Wifi","WiFi"],
                        ["Chatgpt","ChatGPT"]
                     ]
      #Excepciones x Gramática
      self.Excep_04 = [
                        ["Del", "del"],
                        ["Los", "los"],
                        ["Las", "las"],
                        ["Una", "una"],
                        ["For", "for"]
                     ]


   def capital(self):
      txt, ext = os.path.splitext(self.txt)
      txt = txt.lower()
      txt = txt.strip()

      #Excepciones por Ortografía
      for i in self.Excep_01:
         if i[0] in txt:
            txt = txt.replace(i[0], i[1])

      text = txt.split(" ")
      for i in range(0, len(text)):
         if i == 0:
            text[i] = text[i].capitalize()

         if len(text[i]) == 1:
            text[i] = text[i].upper()

         if len(text[i]) > 2:
            text[i] = text[i].capitalize()

         #Excepciones x Guión
         if text[i-1].find("-") >= 0:
            text[i] = text[i].capitalize()

         #Excepciones x Palabra Reservada
         if text[i] in self.Excep_02:
            text[i] = text[i].upper()

         #Excepciones x Paréntesis
         if text[i].find("(") >= 0:
            otro = text[i].split("(")
            otro[1] = otro[1].capitalize()
            text[i] = "(" + otro[1]

         #Excepciones x Guión
         if text[i].find("-") >= 0:
            otro = text[i].split("-")
            otro[1] = otro[1].capitalize()
            text[i] = otro[0] + "-" + otro[1]

         #Excepciones x Guión Bajo
         if text[i].find("_") >= 0:
            otro = text[i].split("_")
            otro[1] = otro[1].capitalize()
            text[i] = "_" + otro[1]

         #Excepciones x Palabra Clave
         for j in self.Excep_03:
            if j[0] in text[i]:
               text[i] = text[i].replace(j[0], j[1])

         #Excepciones x Gramática
         if i != 0:
            for j in self.Excep_04:
               if j[0] == text[i]:
                  text[i] = text[i].replace(j[0], j[1])


      delimiter = " "
      self.txt = delimiter.join(text) + ext
      self.txt = self.txt.strip()

      return self.txt
