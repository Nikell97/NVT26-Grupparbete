# NVT26-Grupparbete

# Hur du kör programmet
### Ställ in rätt Python environment

Kör följande kommandon i PowerShell från projektets directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
Detta sätter upp en virtual environment för dependencies, så att de inte påverkar andra python projekt.  
Efter installation ställ in så att VS Code och Python använder rätt Interpreter  
Ctr + Shif + P --> Python: Select Interpreter --> Välj din virtual environment, ex på hur den ser ut: Python 3.147 .\venv\Scripts\python.exe (bör ligga under Workspaces inte Global)

### Koppla upp datorn mot rätt nätverk

Scriptet är inställt för att hämta rapport från routern i Nordviks rack.  
Accesspunkterna i det racket är inte konfigurerade med WIFi för VLAN drift.  
Du behöver alltså koppla datorn med ethernetkabel till port Gi0/13 på switchen (den enda porten som ligger i VLAN drift)

### Kör programmet

Nu kan du köra programmet  
Det kommer fråga om lösenord för ssh anslutning. Lösenordet sitter inte i klartext här p.g.a. säkerhetsskäl så meddela gruppmedlemmar vid behov.  
Programmet kommer printa ut information om enhetens värdnamn, modell, programversion, och gränssnittens status och sparar denna informationen i en JSON fil kallad rapport.json.  
Om det redan finns en tidigare sparad rapport.json fil från tidigare körning av scriptet kommer den sparade informationen från tidigare printas ut först så att tidigare och nuvarande information kan jämföras. Ny data skriver över den gammla i rapport.json.  

# Projekt

Inventerings - och statusrapport

MVP (för godkänt)
Läser en enhetslista från fil (använd netmiko för att koppla upp och hämta information från racket), hämtar status från minst en enhet (eller läser sparad utdata) och skriver en rapport med värdnamn, modell, programversion och gränssnittens status

Frivillig utökning
Flera enheter, jämförelse mot förra rapporten, flagga avvikande versioner, HTML-rapport eller JSON

Hur vi andvänt oss av AI

Vi har andvänt oss av chat-gpt som stöd under grupparbetet för att förstå Python koden, få hjälp med felsökning och hitta lösningar när vi har fastnat. Vi har även fått hjälp med kod förslag som vi sedan testat och anpassat till vårat program. AI har varit ett hjälpmedel för oss att lära oss att komma vidare i arbetet.

# Gruppmedlemmar

Mattias Nikell

Martin Storme

Jennie Magnusson

Hanna Tetri





Genomförande

Vi har arbetat med Python för att skapa en inventerings- och statusrapport över nätverksutrustning.

Vi skapade två CSV-filer, enheter.csv och status.csv, som innehåller information om nätverksenheter och deras status.

Vi använde Python och csv.DictReader för att läsa information från filerna.

Vi använde även biblioteket Netmiko för att ansluta till en riktig Cisco-router via SSH.

Genom olika Cisco-kommandon hämtade vi information om routerns hostname, modell, IOS-version och interfacestatus.

Informationen sparades sedan i en JSON-fil som heter rapport.json.

Problem och lösningar

Under arbetet hade vi problem med SSH-anslutningen eftersom Cisco-routern använde äldre teknik.

Vi behövde anpassa SSH-inställningarna för att Netmiko skulle kunna ansluta.

Efter felsökning lyckades vi ansluta och hämta information från routern.

Resultat

Vi har lyckats läsa information från CSV-filer, ansluta till en riktig Cisco-router och skapa en JSON-rapport.

CSV-inläsningen och Netmiko-anslutningen är i nuläget implementerade i två separata Pythonprogram.

Vad vi har lärt oss

Vi har lärt oss hur Python kan användas för att automatisera arbetsuppgifter inom nätverksteknik.

Vi har även fått öva på CSV-filer, for-loopar, SSH, Netmiko, Cisco-kommandon och JSON.

Risto Nordstet
