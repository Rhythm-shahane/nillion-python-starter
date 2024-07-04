from nada_dsl import *

def nada_main():
    # Initialize parties
    abhishek = Party(name="Abhishek")
    devansh = Party(name="Devansh")
    prathamesh = Party(name="Prathamesh")

    # Initialize secret integer inputs for each party's salary
    abhishek_salary = SecretInteger(Input(name="abhishek_salary", party=abhishek))
    devansh_salary = SecretInteger(Input(name="devansh_salary", party=devansh))
    prathamesh_salary = SecretInteger(Input(name="prathamesh_salary", party=prathamesh))

    # Determine the position of the party with the highest salary using conditional expressions
    highest_position = (abhishek_salary > devansh_salary).if_else(
        (abhishek_salary > prathamesh_salary).if_else(Integer(0), Integer(2)),
        (devansh_salary > prathamesh_salary).if_else(Integer(1), Integer(2)),
    )

    # Determine the position of the party with the lowest salary using conditional expressions
    lowest_position = (abhishek_salary < devansh_salary).if_else(
        (abhishek_salary < prathamesh_salary).if_else(Integer(0), Integer(2)),
        (devansh_salary < prathamesh_salary).if_else(Integer(1), Integer(2)),
    )

    # Output the position of the party with the highest salary
    highest_out = Output(highest_position, "highest_position", abhishek)
    # Output the position of the party with the lowest salary
    lowest_out = Output(lowest_position, "lowest_position", abhishek)

    return [highest_out, lowest_out]
