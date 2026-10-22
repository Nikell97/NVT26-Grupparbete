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

# Gruppmedlemmar

Mattias Nikell

Martin Storme

Jennie Magnusson

Hanna Tetri

Risto Nordstet
