from nada_dsl import *

def nada_main():
    # Initialize parties
    alice = Party(name="Alice")
    bob = Party(name="Bob")
    charlie = Party(name="Charlie")

    # Initialize secret integer inputs for each party's salary
    alice_salary = SecretInteger(Input(name="alice_salary", party=alice))
    bob_salary = SecretInteger(Input(name="bob_salary", party=bob))
    charlie_salary = SecretInteger(Input(name="charlie_salary", party=charlie))

    # Determine the position of the party with the lowest salary using conditional expressions
    lowest_position = (alice_salary < bob_salary).if_else(
        (alice_salary < charlie_salary).if_else(Integer(0), Integer(2)),
        (bob_salary < charlie_salary).if_else(Integer(1), Integer(2)),
    )

    # Output the position of the party with the lowest salary
    out = Output(lowest_position, "lowest_position", alice)

    return [out]
