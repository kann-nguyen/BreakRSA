from decimal import Decimal, getcontext

def factorize_rsa(N):
    getcontext().prec = 1100
    N = Decimal(N)
    sqrt_N = N.sqrt().to_integral_value(rounding='ROUND_FLOOR')
    
    for k in range(1, 2**20):
        A = sqrt_N + k
        
        abs_p_q = abs(A * A - N).sqrt().to_integral_value(rounding='ROUND_FLOOR')
        
        if abs_p_q * abs_p_q == A * A - N:
            p = A - abs_p_q
            q = A + abs_p_q
            return int(p), int(q)
    
    return None

def decrypt_rsa(ciphertext, p, q, e):
    def mod_inverse(a, m):
        m0, x0, x1 = m, 0, 1
        if m == 1: return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += m0
        return x1

    phi_N = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_N)
    
    plaintext = pow(ciphertext, d, p * q)
    
    return plaintext

def hex_to_ascii_pkcs1(hex_str):
    hex_str = hex_str.lstrip('0x')
    index = hex_str.find('00')
    
    if index != -1:
        ascii_hex = hex_str[index+2:]
    else:
        return None
    
    ascii_message = ''.join(chr(int(ascii_hex[i:i+2], 16)) for i in range(0, len(ascii_hex), 2))
    
    return ascii_message

def main():
    N = int("17976931348623159077293051907890247336179769789423065727343008115"
            "77326758055056206869853794492129829595855013875371640157101398586"
            "47833778606925583497541085196591615128057575940752635007475935288"
            "71082364994994077189561705436114947486504671101510156394068052754"
            "0071584560878577663743040086340742855278549092581")
    
    ciphertext = int("22096451867410381776306561134883418017410069787892831071731839143676135600120"
                     "53800428232965047350942434394621975151225646583996794288946076454204058156474"
                     "89880137348641204523252293201764879166664029975091887299716905260832220677716"
                     "00019329260870009579993724077458967773697817571267229951148662959627934791540")
    
    e = 65537
    
    p, q = factorize_rsa(N)
    
    plaintext_hex = hex(decrypt_rsa(ciphertext, p, q, e))
    
    ascii_message = hex_to_ascii_pkcs1(plaintext_hex)
    
    print("Bài tập 4: \n")

    if ascii_message is not None:
        print("Decrypted message:", ascii_message)
    else:
        print("Error: Failed to extract plaintext.")

if __name__ == "__main__":
    main()
