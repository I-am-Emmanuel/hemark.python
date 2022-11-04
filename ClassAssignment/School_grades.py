print('Enter your exam scores and you get your CGPA')


def input_name_and_grades(average: list, name=None):
    cgpa = []
    g_p = 6.0
    cal_score = 0
    for index in Scores:
        cal_score += index
        cal_g_p = cal_score / 100
    for index in range(len(Scores)):
        average = sum(Scores) / len(Scores)
        if average >= 80:
            cgpa.append('First Class')
        elif average >= 50:
            cgpa.append('Second Class Upper')
        elif average >= 45:
            cgpa.append('Second Class Lower')
        elif average < 45:
            cgpa.append('Pass Grade')
    for name, cgpa in zip(name, cgpa):
        average = f"==========================================\nSCHOOL FIRST SEMESTER'S " \
                  f"GRADE\nNAME:: {name}\nCGPA :: {cal_g_p:.1f} out of {g_p}  \nGRADUATING CLASS:: {cgpa}"

    return average


oruko = [str(input('Enter your name:: '))]
ECN101 = int(input('Enter your ECN101 result:: '))
ECN102 = int(input('Enter your ECN102 result:: '))
ECN103 = int(input('Enter your ECN103 result:: '))
ECN104 = int(input('Enter your ECN104 result:: '))
ECN105 = int(input('Enter your ECN105 result:: '))
ECN106 = int(input('Enter your ECN106 result:: '))
Scores = []
Scores += [ECN101, ECN102, ECN103, ECN104, ECN105, ECN106]

print(input_name_and_grades(average=Scores, name=oruko))
