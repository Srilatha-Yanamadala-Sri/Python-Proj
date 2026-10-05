fragor = [
	"Vad heter Sveriges huvudstad? (a) Oslo, (b) Stockholm, (c) Köpenhamn",
	"Vad blir 5 * 2? (a) 7, (b) 10, (c) 12",
	"Vilket språk programmerar ni i? (a) Python, (b) HTML, (c) Excel",
	"Vilket tecken börjar en kommentar i Python? (a) //, (b) #, (c) <!--",
	"Vad skapar [] i Python? (a) en lista, (b) en funktion, (c) en loop",
]

ratt_svar = ["b", "b", "a", "b", "a"]
poang = 0

print("Välkommen till miniquizet! Svara med a, b eller c.")

for nummer, fraga in enumerate(fragor, start=1):
	print(f"\nFråga {nummer}: {fraga}")
	svar = input("Ditt svar: ").strip().lower()

	if svar == ratt_svar[nummer - 1]:
		print("Rätt!")
		poang += 1
	else:
		print(f"Inte riktigt. Rätt svar är {ratt_svar[nummer - 1]}.")

print(f"\nDu fick {poang} av {len(fragor)} poäng.")

if poang >= 4:
	print("Bra jobbat!")
else:
	print("Försök igen!")
