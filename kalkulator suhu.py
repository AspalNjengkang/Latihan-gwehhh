suhu = float(input("Masukkan nilai suhu : "))
jenis = input("Masukkan satuan suhu : ")

if jenis == "Celcius":
    print(
        "Celcius    :", suhu, 
        "\nFahrenheit :", (9/5) * suhu + 32,
        "\nKelvin     :", suhu + 273,15,
        "\nReamur     :", suhu * (4/5),
        "\nRankine    :", (suhu + 273.15) * 9/5
    )

elif jenis == "Fahrenheit":
    print(
        "Celcius    :", (suhu - 32) * 5/9,
        "\nFahrenheit :", suhu, 
        "\nKelvin     :", (suhu + 459.67) * 5/9,
        "\nReamur     :", 4/9 * (suhu - 32),
        "\nRankine    :", suhu + 459.67
    )

elif jenis == "Kelvin":
    print("Celcius    :", suhu - 273,15,
        "\nFahrenheit :", (suhu * 9/5) - 459.67,
        "\nKelvin     :", suhu, 
        "\nReamur     :", (suhu - 273) * (4/5),
        "\nRankine    :", suhu * 9/5
    )

elif jenis == "Reamur":
    print("Celcius    :", suhu / 0.8,
        "\nFahrenheit :", (suhu * 2.25) + 32,
        "\nKelvin     :", (suhu / 0.8) + 273.15,
        "\nReamur     :", suhu, 
        "\nRankine    :", (suhu * 2.25) + 491.67 
    )

elif jenis == "Rankine":
    print(
        "Celcius    :", (suhu - 491.67) * 5/9,
        "\nFahrenheit :", suhu - 459.67,
        "\nKelvin     :", suhu * 5/9,
        "\nReamur     :", (suhu / 1.8 + 273.15) * 0.8,
        "\nRankine    :", suhu
    )

else : print("Salaaaaaahhhh")

print("tipe suhu  : ",type(suhu))