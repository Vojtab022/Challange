def convert_ip_address(ip_address, is_binary_to_decimal=True):
    if is_binary_to_decimal:
        # Převod z binárního na decimální
        binary_bytes = ip_address.split('.')
        decimal_bytes = []
        for byte in binary_bytes:
            decimal_value = 0
            for bit in byte:
                decimal_value = decimal_value * 2 + int(bit)
            decimal_bytes.append(str(decimal_value))
        return '.'.join(decimal_bytes)
    else:
        # Převod z decimálního na binární
        decimal_bytes = ip_address.split('.')
        binary_bytes = []
        for byte in decimal_bytes:
            decimal_value = int(byte)
            binary_value = ''
            for _ in range(8):
                binary_value = str(decimal_value % 2) + binary_value
                decimal_value //= 2
            binary_bytes.append(binary_value)
        return '.'.join(binary_bytes)

# Funkce pro získání volby od uživatele
def get_conversion_choice():
    while True:
        print("Vyberte převod 1) pro binární na decimální, 2) pro decimální na binární): ")
        choice = input()
        if choice == '1' or choice == '2':
            return int(choice)
        else:
            print("Neplatná volba. Zadejte 1 nebo 2.")

# Funkce pro získání adresy od uživatele
def get_ip_address():
    print("Zadejte IPv4 adresu: ")
    ip_address = input().strip()
    return ip_address

# Hlavní funkce
def main():
    # Získání volby od uživatele
    conversion_choice = get_conversion_choice()
    
    # Získání adresy od uživatele
    ip_address = get_ip_address()
    
    # Převedení adresy podle volby uživatele
    is_binary_to_decimal = (conversion_choice == 1)
    result = convert_ip_address(ip_address, is_binary_to_decimal)
    
    if result:
        if is_binary_to_decimal:
            print("IPv4 adresa v decimálním formátu:", result)
        else:
            print("IPv4 adresa v binárním formátu:", result)

# Spuštění hlavní funkce
if __name__ == "__main__":
    main()
