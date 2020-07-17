import time

#def decor for decoration
def decor(dec):
    def wrap():
#the result
        print('+++++++')

        text_matrix='Matrix One'
        for i in text_matrix:
            print(i,end='',flush=True)
            time.sleep(0.01)
        print('')
        dec()
        print('+++++++')
        print('')
        print("yeap you made a matrix no let's do some operations on it")
        print("")

    return wrap
#information for user
Text="we must create a matrix 3X3 , so , you must enter the numbers for it"
for i in Text:
    print(i,end='',flush=True)
    time.sleep(0.01)
print("")
print('------------------',)
print('Enter First Matrix')
#user entered matrixes
metrix_one_one=input("matrix position 1/1: ")
metrix_one_two=input("matrix position 1/2: ")
metrix_one_three=input("matrix position 1/3: ")
metrix_two_one=input("matrix position 2/1: ")
metrix_two_two=input("matrix position 2/2: ")
metrix_two_three=input("matrix position 2/3: ")
metrix_three_one=input("matrix position 3/1: ")
metrix_three_two=input("matrix position 3/2: ")
metrix_three_three=input("matrix position 3/3: ")



Decor_for_system=('-----------------------')

for q in Decor_for_system:
    print(q,end="",flush=True)
    time.sleep(0.01)
print("")
print('Now Enter Matrix Second')
#user entered matrixes
secmetrix_one_one=input("matrix position 1/1: ")
secmetrix_one_two=input("matrix position 1/2: ")
secmetrix_one_three=input("matrix position 1/3: ")
secmetrix_two_one=input("matrix position 2/1: ")
secmetrix_two_two=input("matrix position 2/2: ")
secmetrix_two_three=input("matrix position 2/3: ")
secmetrix_three_one=input("matrix position 3/1: ")
secmetrix_three_two=input("matrix position 3/2: ")
secmetrix_three_three=input("matrix position 3/3: ")

#fill matrix information, witch user gave us

User_Matrix={'1/1':metrix_one_one,"1/2":metrix_one_two,"1/3":metrix_one_three,
             "2/1":metrix_two_one,"2/2":metrix_two_two,"2/3":metrix_two_three,
             "3/1":metrix_three_one,"3/2":metrix_three_two,"3/3":metrix_three_three}

Sec_User_Matrix={'1/1':secmetrix_one_one,"1/2":secmetrix_one_two,"1/3":secmetrix_one_three,
             "2/1":secmetrix_two_one,"2/2":secmetrix_two_two,"2/3":secmetrix_two_three,
             "3/1":secmetrix_three_one,"3/2":secmetrix_three_two,"3/3":secmetrix_three_three}
FInal_Matrix=()

#returns matrix
def text():
    print("",User_Matrix['1/1'],User_Matrix['1/2'],User_Matrix['1/3'],"\n",
      User_Matrix['2/1'],User_Matrix['2/2'],User_Matrix['2/3'],"\n",
      User_Matrix['3/1'],User_Matrix['3/2'],User_Matrix['3/3'])

    print('---------')
    Matrix_Text_Two='Matrix Two'
    for i in Matrix_Text_Two:
        print(i,end='',flush=True)
        time.sleep(0.01)
    print('')
    print("", Sec_User_Matrix['1/1'], Sec_User_Matrix['1/2'], Sec_User_Matrix['1/3'], "\n",
          Sec_User_Matrix['2/1'], Sec_User_Matrix['2/2'], Sec_User_Matrix['2/3'], "\n",
          Sec_User_Matrix['3/1'], Sec_User_Matrix['3/2'], Sec_User_Matrix['3/3'])

result=decor(text)
result()
#operations on matrixes
def Matrix_Operation(x):

#matrix sum
    if x==str('+'):
        print("Matrix Sum Is")
        print("")
        print(int(User_Matrix['1/1']) + int(Sec_User_Matrix['1/1']),
              int(User_Matrix['1/2']) + int(Sec_User_Matrix['1/2']),
              int(User_Matrix['1/3']) + int(Sec_User_Matrix['1/3']))

        print(int(User_Matrix['2/1']) + int(Sec_User_Matrix['2/1']),
              int(User_Matrix['2/2']) + int(Sec_User_Matrix['2/2']),
              int(User_Matrix['2/3']) + int(Sec_User_Matrix['2/3']))

        print(int(User_Matrix['3/1']) + int(Sec_User_Matrix['3/1']),
              int(User_Matrix['3/2']) + int(Sec_User_Matrix['3/2']),
              int(User_Matrix['3/3']) + int(Sec_User_Matrix['3/3']))
#matrix devision
    if x==str('*'):
        print("Multiplicated Matrix Is")
        print("")
        print(int(User_Matrix['1/1']) * int(Sec_User_Matrix['1/1']) + int(User_Matrix['1/2']) * int(
            Sec_User_Matrix['2/1']) + int(User_Matrix['1/3']) * int(Sec_User_Matrix['3/1']),
              int(User_Matrix['1/1']) * int(Sec_User_Matrix['1/2']) + int(User_Matrix['1/2']) * int(
                  Sec_User_Matrix['2/2']) + int(User_Matrix['1/3']) * int(Sec_User_Matrix['3/2']),
              int(User_Matrix['1/1']) * int(Sec_User_Matrix['1/3']) + int(User_Matrix['1/2']) * int(
                  Sec_User_Matrix['2/3']) + int(User_Matrix['1/3']) * int(Sec_User_Matrix['3/3']))

        print(int(User_Matrix['2/1']) * int(Sec_User_Matrix['1/1']) + int(User_Matrix['2/2']) * int(
            Sec_User_Matrix['2/1']) + int(User_Matrix['2/3']) * int(Sec_User_Matrix['3/1']),
              int(User_Matrix['2/1']) * int(Sec_User_Matrix['1/2']) + int(User_Matrix['2/2']) * int(
                  Sec_User_Matrix['2/2']) + int(User_Matrix['2/3']) * int(Sec_User_Matrix['3/2']),
              int(User_Matrix['2/1']) * int(Sec_User_Matrix['1/3']) + int(User_Matrix['2/2']) * int(
                  Sec_User_Matrix['2/3']) + int(User_Matrix['2/3']) * int(Sec_User_Matrix['3/3']))

        print(int(User_Matrix['3/1']) * int(Sec_User_Matrix['1/1']) + int(User_Matrix['3/2']) * int(
            Sec_User_Matrix['2/1']) + int(User_Matrix['3/3']) * int(Sec_User_Matrix['3/1']),
              int(User_Matrix['3/1']) * int(Sec_User_Matrix['1/2']) + int(User_Matrix['3/2']) * int(
                  Sec_User_Matrix['2/2']) + int(User_Matrix['3/3']) * int(Sec_User_Matrix['3/2']),
              int(User_Matrix['3/1']) * int(Sec_User_Matrix['1/3']) + int(User_Matrix['3/2']) * int(
                  Sec_User_Matrix['2/3']) + int(User_Matrix['3/3']) * int(Sec_User_Matrix['3/3']))

print('for + enter +')
print('for * enter *')
print("")
User_Input = str(input('enter your decision: '))
Matrix_Operation(User_Input)
print("")
Suggestion=' multiply matrix on number : press 1 \n calculate matrix determinant : press 2 \n calculate inverse matrix : press 3 \n for exit just press enter'
for k in Suggestion:
    print(k,end='',flush=True)
    time.sleep(0.01)
User_Decision=str(input(""))
if User_Decision==str('1'):
    User_Number='enter a number which shuld be multiplied on matrix'
    user_number=int(input("Number:"))
    Final_Decision="witch matrix do you want to multiply on {0}? First or Second type F or S! ".format(user_number)
    print(Final_Decision)
    Fin_Decision=str(input('F/S'))
    Fix_Fin_Decision=Fin_Decision.lower()
    if Fix_Fin_Decision=='f' :
        print("")
        print("the result is: ")
        print("")
        print(int(User_Matrix['1/1']) * int(user_number),
              int(User_Matrix['1/2']) * int(user_number),
              int(User_Matrix['1/3']) * int(user_number))

        print(int(User_Matrix['2/1']) * int(user_number),
              int(User_Matrix['2/2']) * int(user_number),
              int(User_Matrix['2/3']) * int(user_number))

        print(int(User_Matrix['3/1']) * int(user_number),
              int(User_Matrix['3/2']) * int(user_number),
              int(User_Matrix['3/3']) * int(user_number))
        print("")
    elif Fix_Fin_Decision=='s':
        print("")
        print("the result is: ")
        print("")

        print(int(Sec_User_Matrix['1/1']) * int(user_number),
              int(Sec_User_Matrix['1/2']) * int(user_number),
              int(Sec_User_Matrix['1/3']) * int(user_number))

        print(int(Sec_User_Matrix['2/1']) * int(user_number),
              int(Sec_User_Matrix['2/2']) * int(user_number),
              int(Sec_User_Matrix['2/3']) * int(user_number))

        print(int(Sec_User_Matrix['3/1']) * int(user_number),
              int(Sec_User_Matrix['3/2']) * int(user_number),
              int(Sec_User_Matrix['3/3']) * int(user_number))
        print("")
#matrix determination
elif User_Decision == str('2'):
    choise=str(input("which matrix determinant do you want ? First or Second type F/S "))
    chois=choise.lower()
    print("")
    if chois == str("f"):
        res = (int(User_Matrix['2/2']) * int(User_Matrix['3/3']) - int(User_Matrix['2/3']) * int(
            User_Matrix['3/2'])) * int(User_Matrix['1/1'])
        res1 = (((int(User_Matrix['2/1'])) * int(User_Matrix['3/3'])) - (
                    int(User_Matrix['2/3']) * int(User_Matrix['3/1']))) * (int(User_Matrix['1/2']))
        res2 = (((int(User_Matrix['2/1'])) * int(User_Matrix['3/2'])) - (
                    int(User_Matrix['2/2']) * int(User_Matrix['3/1']))) * (int(User_Matrix['1/3']))
        print((res) - (res1) + (res2))
    elif chois == str('s'):
        res = (int(Sec_User_Matrix['2/2']) * int(Sec_User_Matrix['3/3']) - int(Sec_User_Matrix['2/3']) * int(
            Sec_User_Matrix['3/2'])) * int(Sec_User_Matrix['1/1'])
        res1 = (((int(Sec_User_Matrix['2/1'])) * int(Sec_User_Matrix['3/3'])) - (
                    int(Sec_User_Matrix['2/3']) * int(Sec_User_Matrix['3/1']))) * (int(Sec_User_Matrix['1/2']))
        res2 = (((int(Sec_User_Matrix['2/1'])) * int(Sec_User_Matrix['3/2'])) - (
                    int(Sec_User_Matrix['2/2']) * int(Sec_User_Matrix['3/1']))) * (int(Sec_User_Matrix['1/3']))
        print((res) - (res1) + (res2))




