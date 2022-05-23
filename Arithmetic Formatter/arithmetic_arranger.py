"""
Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

"""
def arithmetic_arranger(problems, answer=False):
    # Cek jumlah soal
    if len(problems) > 5:
        return "Error: Too many problems."

    # Input Operator dan Soal
    angka1 = []
    angka2 = []
    operator = []

    for problem in problems:
        # Memecah Inputan
        Pecah = problem.split()
        angka1.append(Pecah[0])
        angka2.append(Pecah[2])
        operator.append(Pecah[1])

    # Cek Operator
    if "/" in operator or "*" in operator:
        return "Error: Operator must be '+' or '-'."

    # Cek apakah inputan berupa angka atau buka
    for i in range(len(angka1)):
        if not angka1[i].isdigit() or not angka2[i].isdigit():
            return "Error: Numbers must only contain digits."
    
    # Cek apakah angka lebih dari 4 digit
    for i in range(len(angka1)):
        if len(angka1[i]) > 4 or len(angka2[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Membuat list untuk keluaran (kelaran terdiri dari 4 baris)
    baris_pertama = []
    baris_kedua = []
    baris_ketiga = []
    baris_keempat = []

    # untuk tes pertama
    for i in range(len(angka1)):
        if len(angka1[i]) > len(angka2[i]):
            baris_pertama.append(" "*2 + angka1[i])
        else:
             baris_pertama.append(" "*(len(angka2[i]) - len(angka1[i]) + 2) + angka1[i])