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
                        ["t pico","típico"],
                        ["est s","estás"],
                        ["dec logo", "decálogo"],
                        ["success factors", "successfactors"],
                        ["sap script","sapscript"],
                        ["smart forms","smartforms"],
                        ["adobe forms","adobeforms"],
                        ["ooabap","oo abap"],
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
                        "Ats",
                        "Aws",
                        "Azure",
                        "Badi",
                        "Badis",
                        "Bapi",
                        "Bapis",
                        "Bdc",
                        "Bbp",
                        "Bds",
                        "Bi", 
                        "Bpmn",
                        "Brf",
                        "Bte",
                        "Btp",
                        "Bwp",
                        "Cda",
                        "Cds",
                        "Ci-cd",
                        "Cmod",
                        "Copa",
                        "Cpi",
                        "Cpwi",
                        "Crud",
                        "Csv",
                        "Cuni",
                        "Dax",
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
                        "J2c",
                        "Java",
                        "Jira",
                        "Json",
                        "Lean",
                        "Linux",
                        "Lsmw",
                        "Ltmom",
                        "Mba",
                        "Mpr",
                        "Mrp",
                        "N1mepi",
                        "Note",
                        "O2c",
                        "Ooalv",
                        "Oops",
                        "Pdf",
                        "Pfcg",
                        "Pld",
                        "Pl-sql",
                        "Pmbok",
                        "Po-pi",
                        "Pqr",
                        "Ptp",
                        "Rad",
                        "Rap",
                        "Rfc",
                        "Rise",
                        "Ricefw",
                        "Sap",
                        "Scrum",
                        "Se11",
                        "Snote",
                        "Spau",
                        "Sql",
                        "Sqvi",
                        "Ssff",
                        "Su01",
                        "Sq01",
                        "Sq02",
                        "Tvarvc",
                        "Ui5",
                        "Uml",
                        "Vpc",
                        "Windows",
                        "Wms",
                        "X-road",
                        "Aa", "aa",
                        "Ai", "ai",
                        "Bi", "bi",
                        "Bp", "bp",
                        "Cd", "cd",
                        "Ci", "ci",
                        "Co", "co",
                        "Fi", "fi",
                        "Hp", "hp",
                        "Hr", "hr",
                        "Ia", "ia",
                        "It", "it",
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
      #Excepciones x Símbolos
      self.Excep_03 = [
                        "(",
                        "-",
                        "_"
                     ]
      #Excepciones x Palabra Clave
      self.Excep_04 = [
                        ["Adobeforms","AdobeForms"],
                        ["APIS", "APIs"],
                        ["BADIS", "BADIs"],
                        ["Chatgpt","ChatGPT"],
                        ["Devops","DevOps"],
                        ["Gaps", "GAPs"],
                        ["Github","GitHub"],
                        ["Jbpm","jBPM"],
                        ["Keepassxc","KeePassXC"],
                        ["Kpis","KPIs"],
                        ["Odata","OData"],
                        ["Sapscript","SapScript"],
                        ["Smartforms","SmartForms"],
                        ["Successfactors", "SuccessFactors"],
                        ["T-code", "T-Code"],
                        ["Wifi","WiFi"]
                     ]
      #Excepciones x Gramática
      self.Excep_05 = [
                        ["Del", "del"],
                        #["Los", "los"],
                        #["Las", "las"],
                        #["Una", "una"],
                        ["For", "for"],
                        ["no", "No"],
                        ["up","Up"]
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

         #Excepciones x Símbolo
         for j in self.Excep_03:
            if text[i].find(j) >= 0:
               otro = text[i].split(j)
               otro[1] = otro[1].capitalize()
               delimiter = j
               text[i] = delimiter.join(otro)

         #Excepciones x Palabra Clave
         for j in self.Excep_04:
            if j[0] in text[i]:
               text[i] = text[i].replace(j[0], j[1])

         #Excepciones x Gramática
         if i != 0:
            for j in self.Excep_05:
               if j[0] == text[i]:
                  text[i] = text[i].replace(j[0], j[1])


      delimiter = " "
      self.txt = delimiter.join(text) + ext
      self.txt = self.txt.strip()

      return self.txt
