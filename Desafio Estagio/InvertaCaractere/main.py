def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida


def main():
    # Solicita a entrada do usuário
    string = input("Digite a string que deseja inverter: ")

    # Inverte a string
    resultado = inverter_string(string)

    # Exibe o resultado
    print(f"String invertida: {resultado}")


if __name__ == "__main__":
    main()

