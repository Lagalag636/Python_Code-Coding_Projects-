import math

# An isotope has half-life T.
# Return the amount of a starting mass N0
# of the isotope that remains after time t,
def compute_Nt(N0, t, T):
    return N0 * (0.5) ** (t / T)


# Return the half-life of an isotope given that
# a mass N0 decays to Nt after time t
def compute_T(N0, Nt, t):
    if N0 <= 0 or Nt <= 0 or t <= 0 or Nt > N0:
        raise ValueError("Invalid input values. Ensure N0 > Nt > 0 and t > 0.")

    return t / (math.log(N0 / Nt) / math.log(2))


if __name__ == '__main__':
    choice = input("Would you like the amount of material (N) or the half-life (T)? ").strip().upper()
    if choice == 'N':                     # Calculate amount of material
        # TODO: Read N0, t, and T from one line of input and compute Nt
        data_input = input("Enter N0, t, and T separated by spaces: ").strip().split()
        N0 = float(data_input[0])
        t = float(data_input[1])
        T = float(data_input[2])
        Nt = compute_Nt(N0, t, T)         # Call the function to compute Nt
        print(f'Nt = {Nt:.4f}')
    elif choice == 'T':                    # Calculate half-life
        # TODO: Read N0, Nt, and t from one line of input and compute T
        data_input = input("Enter N0, Nt, and t separated by spaces: ").strip().split()
        N0 = float(data_input[0])
        Nt = float(data_input[1])
        t = float(data_input[2])
        T = compute_T(N0, Nt, t)         # Call the function to compute T
        print(f'T = {T:.4f}')
    else:
        print("invalid choice")
