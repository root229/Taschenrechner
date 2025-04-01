print("Hallo User!")

a = float(input("Erste Zahl: "))
operator = input("Gib den Rechenoperator (+, -, *, /) ein: ")
b = float(input("Zweite Zahl: "))

if operator == "+":
    c = a + b
elif operator == "-":
    c = a - b
elif operator == "*":  # Hier war das Problem
    c = a * b
elif operator == "/":
    if b != 0:
        c = a / b
    else:
        c = "Fehler: Division durch 0!"
else:
    c = "Ungültiger Operator!"

print("Ergebnis:", c)