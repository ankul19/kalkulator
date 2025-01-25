def kalkulator():
print("Kalkulator")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")

wybor = input("Wybierz operacje 1-4:")
a = float(input("Podaj Pierwsza liczbe:"))
b = float(input("Podaj druga liczbe:"))

if wybor == "1":
print(f"Wynik: {a + b}")
elif wybor == "2":
print(f"Wynik: {a - b}")
elif wybor == "3":
print(f"Wynik: {a * b}")
elif wybor == "4":
if b != 0:
print(f"Wynik: {a / b}")
else
print ("Blad: dzielenie przez zero!")
else:
print("Niepoprawny wybor!")

if __name__ == "__main__":
kalkulator()
