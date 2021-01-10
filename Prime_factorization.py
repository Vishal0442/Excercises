
# Python program to find prime factorization of a given number
# "Prime Factorization" is finding which prime numbers multiply together to make the original number


def find_prime_no(no):
    prime_no_list = []
    for i in range(2, no+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_no_list.append(i)
    return prime_no_list

def find_prime_factors(no):
    prime_no_list = find_prime_no(no)
    prime_factor_list = []
    R = no
    while R != 1:
        for i in prime_no_list:
            if R % i == 0:
                R = R / i
                prime_factor_list.append(i)
                break
    return prime_factor_list

def main():
    A = int(input("Enter No. : "))
    if A == 1:
        print("1 is Neither Prime number nor Even number.")
    elif A < 1:
        print("Invalid inputs")
    else:
        prime_nos = find_prime_no(A)
        print("Prime Nos. upto ", A, "-->", prime_nos)
        prime_factors = find_prime_factors(A)
        print("Prime Factors of", A, "-->", prime_factors)

main()








