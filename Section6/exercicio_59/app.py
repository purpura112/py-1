def guess_the_number():
    import random

    number_to_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 3
    print("Adivinhe o número entre 1 e 10. Você tem 3 tentativas.")

    for attempt in range(max_attempts):
        guess = int(input(f"Tentativa {attempt + 1}: "))
        attempts += 1

        if guess < number_to_guess:
            print("Muito baixo!")
        elif guess > number_to_guess:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você adivinhou o número {number_to_guess} em {attempts} tentativas.")
            return
    print(f"Você não adivinhou o número. O número era {number_to_guess}.")

guess_the_number()