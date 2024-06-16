from decimal import Decimal, InvalidOperation, getcontext

def factorize_rsa_1(N):
    # Đặt độ chính xác cao để xử lý số lớn
    getcontext().prec = 1100  # Đặt độ chính xác đủ lớn để xử lý các phép toán
    
    # Chuyển đổi N sang kiểu Decimal
    N = Decimal(N)
    
    # Tìm A gần với sqrt(N)
    A = N.sqrt().to_integral_value(rounding='ROUND_CEILING')
    
    # Tính x từ A và N
    x2 = A * A - N
    x = x2.sqrt().to_integral_value(rounding='ROUND_FLOOR')
    
    # Kiểm tra nếu x là số nguyên
    if x * x == x2:
        p = A - x
        q = A + x
        return int(p), int(q)
    else:
        return None
    
def factorize_rsa_2(N):
    getcontext().prec = 1100
    N = Decimal(N)
    sqrt_N = N.sqrt().to_integral_value(rounding='ROUND_FLOOR')
    
    for k in range(1, 2**20):
        A = sqrt_N + k
        x2 = A * A - N
        x = x2.sqrt().to_integral_value(rounding='ROUND_FLOOR')
        
        if x * x == x2:
            p = A - x
            q = A + x
            return int(p), int(q)
    
    return None

def factorize_rsa_3(N):
    getcontext().prec = 1100
    N = Decimal(N)
    sqrt_N = N.sqrt().to_integral_value(rounding='ROUND_FLOOR')
    
    # Compute the upper bound based on the given condition
    upper_bound = N.sqrt() / 4
    
    # Start searching from sqrt_N - upper_bound up to sqrt_N + upper_bound
    min_A = sqrt_N - upper_bound
    max_A = sqrt_N + upper_bound
    
    # Iterate over the range of A values
    for A in range(int(min_A), int(max_A) + 1):
        try:
            # Calculate 3p - 2q and check if it satisfies the condition
            x = (3 * A - 2 * N / A).sqrt().to_integral_value(rounding='ROUND_FLOOR')
            p_candidate = A - x
            q_candidate = A + x
            
            # Check if p_candidate and q_candidate are valid factors
            if p_candidate * q_candidate == N:
                return int(p_candidate), int(q_candidate)
            
            # Early termination if factors found
            if p_candidate * q_candidate > N:
                break
        
        except:
            continue
    
    return None
def main():
    N1 = int("17976931348623159077293051907890247336179769789423065727343008115"
            "77326758055056206869853794492129829595855013875371640157101398586"
            "47833778606925583497541085196591615128057575940752635007475935288"
            "71082364994994077189561705436114947486504671101510156394068052754"
            "0071584560878577663743040086340742855278549092581")
    
    N2 = int("6484558428080716696628242653467722787263437207069762630604390703787"
            "9730861808111646271401527606141756919558732184025452065542490671989"
            "2428844841839353281972988531310511738648965962582821502504990264452"
            "1008852816733037111422964210278402893076574586452336833570778346897"
            "15838646088239640236866252211790085787877")
    
    N3 = int("72006226374735042527956443552558373833808445147399984182665305798191"
            "63556901883377904234086641876639384851752649940178970835240791356868"
            "77441155132015188279331812309091996246361896836573643119174094961348"
            "52463970788523879939683923036467667022162701835329944324119217381272"
            "9276147530748597302192751375739387929")
    
    result1 = factorize_rsa_1(N1)
    result2 = factorize_rsa_2(N2)
    result3 = factorize_rsa_3(N3)
    print("\nCâu hỏi 1: \n")
    if result1:
        p, q = result1
        print(f"p = {p}")
        print(f"q = {q}")
    else:
        print("Không tìm thấy thừa số nguyên tố của N.")
    print("\nCâu hỏi 2: \n")
    if result2:
        p, q = result2
        print(f"p = {p}")
        print(f"q = {q}")
    else:
        print("Không tìm thấy thừa số nguyên tố của N.")
    print("\nCâu hỏi 3: \n")
    if result3:
        p , q = result3
        print(f"p = {p}")
        print(f"q = {q}")
    else:
        print("Không tìm thấy thừa số nguyên tố của N.")

if __name__ == "__main__":
    main()
