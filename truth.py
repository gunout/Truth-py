#!/usr/bin/env python3
"""
truth.py - Analyse complète d'un nombre
Affiche les conversions, propriétés mathématiques, trigonométrie, hashs, etc.
"""

import math
import hashlib
import crcmod
import base64
from datetime import datetime
import sys

def analyze_number(number):
    """
    Analyse complète d'un nombre et retourne toutes les informations
    """
    results = {}
    
    # Conversion de base
    results['decimal'] = number
    results['hexadecimal'] = hex(number)[2:].upper()
    results['binary'] = bin(number)[2:]
    results['octal'] = oct(number)[2:]
    
    # Propriétés arithmétiques et algébriques
    results['english_words'] = number_to_english(number)
    results['parity'] = "Odd" if number % 2 else "Even"
    results['factors'] = factorize(number)
    results['prime_status'] = "Prime" if is_prime(number) else "Composite"
    results['divisible_by_8'] = [number * i for i in range(2, 10)]
    results['multiplied_by_2'] = number * 2
    results['divided_by_2'] = number / 2
    results['previous_primes'] = find_previous_primes(number, 8)
    results['digit_sum'] = sum(int(d) for d in str(number))
    results['digit_count'] = len(str(number))
    results['log10'] = math.log10(number) if number > 0 else float('inf')
    results['natural_log'] = math.log(number) if number > 0 else float('inf')
    results['fibonacci'] = is_fibonacci(number)
    results['next_number'] = number + 1
    results['previous_number'] = number - 1
    
    # Puissances et racines
    results['square'] = number ** 2
    results['cube'] = number ** 3
    results['square_root'] = math.sqrt(number)
    results['cube_root'] = number ** (1/3)
    
    # Trigonométrie
    results['sin_deg'] = math.sin(math.radians(number))
    results['cos_deg'] = math.cos(math.radians(number))
    results['tan_deg'] = math.tan(math.radians(number))
    results['sin_rad'] = math.sin(number)
    results['cos_rad'] = math.cos(number)
    results['tan_rad'] = math.tan(number)
    results['deg_to_rad'] = math.radians(number)
    results['rad_to_deg'] = math.degrees(number)
    
    # Hash et cryptographie
    results['md5'] = hashlib.md5(str(number).encode()).hexdigest()
    results['crc32'] = crc32_hash(str(number))
    results['sha256'] = hashlib.sha256(str(number).encode()).hexdigest()
    results['sha1'] = hashlib.sha1(str(number).encode()).hexdigest()
    results['base64'] = base64.b64encode(str(number).encode()).decode()
    
    # Programmation
    results['c_hex'] = f"0x{results['hexadecimal']}"
    results['delphi_hex'] = f"${results['hexadecimal']}"
    
    # Date et temps (si c'est un timestamp UNIX raisonnable)
    results['unix_time'] = unix_to_datetime(number)
    
    # Internet
    results['ipv4'] = number_to_ipv4(number)
    
    # Couleur
    results['color_hex'] = f"#{results['hexadecimal'].zfill(6)}"
    results['rgb'] = hex_to_rgb(results['hexadecimal'])
    
    return results

def number_to_english(n):
    """Convertit un nombre en mots anglais"""
    if n == 0:
        return "zero"
    
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]
    
    def convert_hundreds(num):
        if num == 0:
            return ""
        elif num < 10:
            return units[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + (" " + units[num % 10] if num % 10 != 0 else "")
        else:
            return units[num // 100] + " hundred" + (" " + convert_hundreds(num % 100) if num % 100 != 0 else "")
    
    if n < 0:
        return "negative " + number_to_english(-n)
    
    parts = []
    chunk_count = 0
    
    while n > 0:
        chunk = n % 1000
        if chunk != 0:
            part = convert_hundreds(chunk)
            if chunk_count > 0:
                part += " " + thousands[chunk_count]
            parts.append(part)
        n //= 1000
        chunk_count += 1
    
    return " ".join(reversed(parts))

def factorize(n):
    """Factorise un nombre"""
    if n < 2:
        return [n]
    
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n):
    """Vérifie si un nombre est premier"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_previous_primes(n, count):
    """Trouve les nombres premiers précédents"""
    primes = []
    candidate = n - 1
    while len(primes) < count and candidate > 1:
        if is_prime(candidate):
            primes.append(candidate)
        candidate -= 1
    return primes

def is_fibonacci(n):
    """Vérifie si un nombre est dans la suite de Fibonacci"""
    if n < 0:
        return False
    x = 5 * n * n
    return math.isqrt(x + 4) ** 2 == x + 4 or math.isqrt(x - 4) ** 2 == x - 4

def crc32_hash(data):
    """Calcule le CRC32"""
    crc32 = crcmod.predefined.Crc('crc-32')
    crc32.update(data.encode())
    return crc32.hexdigest()

def unix_to_datetime(timestamp):
    """Convertit un timestamp UNIX en datetime"""
    try:
        if 0 <= timestamp <= 2000000000:  # Timestamps UNIX raisonnables
            return datetime.fromtimestamp(timestamp).strftime('%A, %d %B %Y at %H:%M:%S UTC')
    except (ValueError, OSError):
        pass
    return "Invalid or out-of-range timestamp"

def number_to_ipv4(n):
    """Convertit un nombre en IPv4"""
    if 0 <= n <= 0xFFFFFFFF:
        return f"{(n >> 24) & 0xFF}.{(n >> 16) & 0xFF}.{(n >> 8) & 0xFF}.{n & 0xFF}"
    return "Invalid IPv4 address"

def hex_to_rgb(hex_str):
    """Convertit une valeur hex en RGB"""
    hex_str = hex_str.zfill(6)
    try:
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)
        return (r, g, b)
    except ValueError:
        return (0, 0, 0)

def display_results(results):
    """Affiche les résultats de manière formatée"""
    print("=" * 80)
    print(f"ANALYSE COMPLÈTE DU NOMBRE {results['decimal']}")
    print("=" * 80)
    
    print("\nNOTATIONS, TRANSLATING INTO NUMBER SYSTEM")
    print(f"Decimal number {results['decimal']}")
    print(f"    {results['decimal']} to hexadecimal value")
    print(f"        {results['hexadecimal']}")
    print(f"    {results['decimal']} to binary value")
    print(f"        {results['binary']}")
    print(f"    {results['decimal']} to octal value")
    print(f"        {results['octal']}")
    
    print(f"\nHexadecimal number {results['hexadecimal']}")
    print(f"    {results['hexadecimal']} to decimal value")
    print(f"        {results['decimal']}")
    print(f"    {results['hexadecimal']} to binary value")
    print(f"        {results['binary']}")
    print(f"    {results['hexadecimal']} to octal value")
    print(f"        {results['octal']}")
    
    print(f"\nBinary number {results['binary']}")
    print(f"    {results['binary']} to decimal value")
    print(f"        {results['decimal']}")
    print(f"    {results['binary']} to hexadecimal value")
    print(f"        {results['hexadecimal']}")
    print(f"    {results['binary']} to octal value")
    print(f"        {results['octal']}")
    
    print(f"\nOctal number {results['octal']}")
    print(f"    {results['octal']} to decimal value")
    print(f"        {results['decimal']}")
    print(f"    {results['octal']} to hexadecimal value")
    print(f"        {results['hexadecimal']}")
    print(f"    {results['octal']} to binary value")
    print(f"        {results['binary']}")
    
    print("\nBASIC ARITHMETIC AND ALGEBRAIC PROPERTIES")
    print(f"    Number {results['decimal']} in English, number {results['decimal']} in words:")
    print(f"        {results['english_words']}")
    print(f"    Parity")
    print(f"        {results['parity']} Number {results['decimal']}")
    print(f"    Factorization, multipliers, divisors of {results['decimal']}")
    factors_str = ', '.join(map(str, results['factors'])) if len(results['factors']) > 1 else f"{results['factors'][0]}, 1"
    print(f"        {factors_str}")
    print(f"    Prime or Composite Number")
    print(f"        {results['prime_status']} Number {results['decimal']}")
    print(f"    First 8 numbers divisible by integer number {results['decimal']}")
    print(f"        {', '.join(map(str, results['divisible_by_8']))}")
    print(f"    The number {results['decimal']} multiplied by two equals")
    print(f"        {results['multiplied_by_2']}")
    print(f"    The number {results['decimal']} divided by 2")
    print(f"        {results['divided_by_2']}")
    print(f"    8 prime numbers list before the number")
    print(f"        {', '.join(map(str, results['previous_primes']))}")
    print(f"    Sum of decimal digits")
    print(f"        {results['digit_sum']}")
    print(f"    Number of digits")
    print(f"        {results['digit_count']}")
    print(f"    Decimal logarithm for {results['decimal']}")
    print(f"        {results['log10']}")
    print(f"    Natural logarithm for {results['decimal']}")
    print(f"        {results['natural_log']}")
    print(f"    Is it Fibonacci number?")
    print(f"        {'Yes' if results['fibonacci'] else 'No'}")
    print(f"    The number on 1 is more than number {results['decimal']},")
    print(f"    next number")
    print(f"        number {results['next_number']}")
    print(f"    The number on one is less than number {results['decimal']},")
    print(f"    previous number")
    print(f"        {results['previous_number']}")
    
    print("\nPOWERS, ROOTS")
    print(f"    {results['decimal']} raising to the second power")
    print(f"        {results['square']}")
    print(f"    {results['decimal']} raising to the third power")
    print(f"        {results['cube']}")
    print(f"    Square root of {results['decimal']}")
    print(f"        {results['square_root']}")
    print(f"    Cubic, cube root of the number {results['decimal']} =")
    print(f"        {results['cube_root']}")
    
    print("\nTRIGONOMETRIC FUNCTIONS, TRIGONOMETRY")
    print(f"    sine, sin {results['decimal']} degrees, sin {results['decimal']}°")
    print(f"        {results['sin_deg']:.10f}")
    print(f"    cosine, cos {results['decimal']} degrees, cos {results['decimal']}°")
    print(f"        {results['cos_deg']:.10f}")
    print(f"    tangent, tg {results['decimal']} degrees, tg {results['decimal']}°")
    print(f"        {results['tan_deg']:.10f}")
    print(f"    sine, sin {results['decimal']} radians")
    print(f"        {results['sin_rad']}")
    print(f"    cosine, cos {results['decimal']} radians")
    print(f"        {results['cos_rad']}")
    print(f"    tangent, tg {results['decimal']} radians equals")
    print(f"        {results['tan_rad']}")
    print(f"    {results['decimal']} degrees, {results['decimal']}° =")
    print(f"        {results['deg_to_rad']} radians")
    print(f"    {results['decimal']} radians =")
    print(f"        {results['rad_to_deg']} degrees, {results['rad_to_deg']}°")
    
    print("\nCHECKSUMS, HASHES, CRYPTOGRAPHY")
    print(f"    Hash MD5({results['decimal']})")
    print(f"        {results['md5']}")
    print(f"    CRC-32, CRC32({results['decimal']})")
    print(f"        {results['crc32']}")
    print(f"    SHA-256 hash, SHA256({results['decimal']})")
    print(f"        {results['sha256']}")
    print(f"    SHA1, SHA-1({results['decimal']})")
    print(f"        {results['sha1']}")
    print(f"    Base64")
    print(f"        {results['base64']}")
    
    print("\nPROGRAMMING LANGUAGES")
    print(f"    C++, CPP, C value {results['decimal']}")
    print(f"        {results['c_hex']}")
    print(f"    Delphi, Pascal value for number {results['decimal']}")
    print(f"        {results['delphi_hex']}")
    
    print("\nDATE AND TIME")
    print(f"    Convert UNIX-timestamp {results['decimal']} to date and time")
    print(f"        {results['unix_time']}")
    
    print("\nINTERNET")
    print(f"    Convert the number to IPv4 Internet network address, long2ip")
    print(f"        {results['ipv4']}")
    print(f"    {results['decimal']} in Wikipedia:")
    print(f"        {results['decimal']}")
    
    print("\nOTHER PROPERTIES OF THE NUMBER")
    print(f"    Short link to this page DEC")
    print(f"        https://bikubik.com/en/{results['decimal']}")
    print(f"    Short link to this page HEX")
    print(f"        https://bikubik.com/en/x{results['hexadecimal']}")
    print(f"    Phone number")
    print(f"        {str(results['decimal'])[:3]}-{str(results['decimal'])[3:5]}-{str(results['decimal'])[5:7]}")
    
    print("\nCOLOR BY NUMBER")
    print(f"    RGB color by number {results['decimal']}, by hex value")
    print(f"        {results['color_hex']} - {results['rgb']}")
    print(f"    HTML CSS color code {results['color_hex']}")
    print(f"        .color-mn {{ color: {results['color_hex']}; }}")
    print(f"        .color-bg {{ background-color: {results['color_hex']}; }}")
    
    print("\nCOLOR FOR CURRENT NUMBER")
    print(f"    {results['color_hex']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python truth.py <number>")
        print("Example: python truth.py 1612519")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
        results = analyze_number(number)
        display_results(results)
    except ValueError:
        print("Erreur: Veuillez entrer un nombre valide")
        sys.exit(1)

if __name__ == "__main__":
    main()