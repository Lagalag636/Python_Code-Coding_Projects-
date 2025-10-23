from math import gcd
exp_1 = int(input("Input a prime number: "))
exp_2 = int(input("Input another prime number: "))

num_mod = exp_1 * exp_2
oilers_totient = (exp_1 - 1) * (exp_2 - 1)

def propose_public_keys(phi):
    proposals = []
    for e in range(2, phi):  # e must be between 1 and phi
        if gcd(e, phi) == 1:  # e and phi must be coprime
            proposals.append(e)
    return proposals

possible_public_keys = propose_public_keys(oilers_totient)
print("Possible public keys:", possible_public_keys)

public_key = int(input("Choose a public key from the list above: "))

private_key_list = [i for i in range(1, oilers_totient) if (i * public_key) % oilers_totient == 1]
print(private_key_list)
private_key = int(input("Enter a number from the list above: "))
message = int(input("Enter a number to encrypt: "))
encrypted_message = (message ** public_key) % num_mod
print("Encrypted message:", encrypted_message)
decrypted_message = (encrypted_message ** private_key) % num_mod
print("Decrypted message:", decrypted_message)
