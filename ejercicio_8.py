cord_a=input("Ingrese la primera coordenada (norte, sur, este, oeste): ").lower()
cord_b=input("Ingrese la segunda coordenada (norte, sur, este, oeste): ").lower()

#coords=["norte","oeste","sur","este"]

if cord_a==cord_b:
    print("Usted esta en la misma coordenada")

elif (cord_a=="norte" and cord_b=="sur") or (cord_a=="sur" and cord_b=="norte") or (cord_a=="oeste" and cord_b=="este") or (cord_a=="este" and cord_b=="oeste"):
    print(f"Recto hacia el {cord_b}")

elif (cord_a=="norte" and cord_b=="este") or (cord_a=="este" and cord_b=="norte"):
    print ("Noreste")

elif (cord_a=="norte" and cord_b=="oeste") or (cord_a=="oeste" and cord_b=="norte"):
    print ("Noroeste")

elif (cord_a == "sur" and cord_b == "este") or (cord_a == "este" and cord_b == "sur"):
    print("Sureste")

elif (cord_a == "sur" and cord_b == "oeste") or (cord_a == "oeste" and cord_b == "sur"):
    print("Suroeste")





