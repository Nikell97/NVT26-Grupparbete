# NVT26-Grupparbete

# Ställ in rätt Python environment

Kör följande kommandon i PowerShell från projektets directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
Detta sätter upp en virtual environment för dependencies, så att de inte påverkar andra python projekt.  
Efter installation ställ in så att VS Code och Python använder rätt Interpreter  
Ctr + Shif + P --> Python: Select Interpreter --> Välj din virtual environment, ex på hur den ser ut: Python 3.147 .\venv\Scripts\python.exe (bör ligga under Workspaces inte Global)

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
