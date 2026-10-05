fragor = [
	"Vad heter Sveriges huvudstad?",
	"Vad blir 5 * 2?",
	"Vilket språk programmerar ni i?",
	"Vilket tecken börjar en kommentar i Python?",
	"Vad skapar [] i Python?",
]

svarsalternativ = [
	["Oslo", "Stockholm", "Köpenhamn"],
	["7", "10", "12"],
	["Python", "HTML", "Excel"],
	["//", "#", "<!--"],
	["en lista", "en funktion", "en loop"],
]

options = ["a", "b", "c"]

ratt_svar = ["b", "b", "a", "b", "a"]
poang = 0

print("Välkommen till miniquizet! Svara med a, b eller c.")

for nummer, fraga in enumerate(fragor, start=1):
	print(f"\nFråga {nummer}: {fraga}")
	for index, alternativ in enumerate(svarsalternativ[nummer - 1]):
		print(f"{options[index]}) {alternativ}")

	while True:
		svar = input("Ditt svar (a, b eller c): ").strip().lower()
		if svar in options:
			break
		print("Ogiltigt svar. Skriv a, b eller c.")

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
