# NVT26-Grupparbete

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
