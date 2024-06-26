#C = K - 273
#K = C + 273
def mainpro():
    mainmenu = input(""" 
A/ Convert Celsius To Kelvin
B/ Convert Kelvin To Celsius
""").upper()

    if mainmenu == 'A':
        C = input('Enter Celsuis Degree(int): ')
        try:
            K = int(C) + 273
            print(K)
        except ValueError as error:
            print(f'{error} Its Not Intger')
        except:
            print('Opps: An Error Ocourd ...!')
    if mainmenu == 'B':
        K = input('Enter Kelvin Degree(int): ')
        try:
            C = int(K) - 273
            print(C)
        except ValueError as error:
            print(f'{error} Its Not Intger')
        except:
            print('Opps: An Error Ocourd ...!')
    secmenu = input("""
A/ Contunie
B/ Exit
"""
).upper()
    if secmenu == 'A':
        mainpro()
    if secmenu == 'B':
        print('See You Later ...!')
        exit(1)


mainpro()
