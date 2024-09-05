import datetime
# Isikukoodi autentsuse kontrollimise programm, mis oskab leida vigu isikukoodis.

#--------------------------------------------------------
def exists_ik(ik):
    """
    Kontrollib, kas isikukood on tühi.

    Tagastab True, kui isikukood ei ole tühi, False muul juhul.
    """
    if ik != '':
        return True
    else: 
        print('Puuduv väärtus')
        return False

#--------------------------------------------------------

def patern_ik(ik):
    """
    Kontrollib, kas isikukood on 11 numbrit pikk ning sisaldab ainult täisarve.

    Tagastab True, kui isikukood on 11 numbrit pikk ning sisaldab täisarve, False muul juhul.
    """
    if not isinstance(ik, float):
        try:
            IK = int(ik)
            
            if IK < 0:
                print('Isikukood peab olema positiivne täisarv')
                return False
            
            if len(str(IK)) != 11:
                print('Isikukood peab olema 11 numbrit pikk')
                return False
            
            return True
        
        except ValueError:
            print('Sisestatud väärtus ei ole täisarv')
            return False
    else:
        print('Sisestatud väärtus ei ole täisarv')
        return False

#--------------------------------------------------------
def check_ik_gender(IK):
    """
    Kontrollib, kas esimene number on õige, vastavalt isikukoodi reeglitele.
    Näiteks: esimene number: 5 – aastail 2000–2099 sündinud mees.
    Ei võta arvesse, kas isikukoodi teised numbrid on õiged.
    
    Tagastab True, kui esimene number on õige, False muul juhul.
    """
    gend = int(IK[0])
    if gend > 0 and gend < 7:
        return True
    else:
        print('Esimene number sisestatud valesti')
        return False

#--------------------------------------------------------

def check_ik_year(IK):    
    """
    Kontrollib, kas teine ja kolmas number – sünniaasta kaks viimast numbrit on õige.
    Ei võta arvesse, kas isikukoodi teised numbrid on õiged.
    
    Tagastab True, kui teine ja kolmas number on õige, False muul juhul.
    """
    year = int(IK[1:3])
    century = int(IK[0])
    dateNow = datetime.datetime.now()
    yearNow = dateNow.year
    if century > 4:
        if year > -1 and year <= int(str(yearNow)[2:4]):
            return True
        else:
            print('Teine ja kolmas number - sünniaasta kaks viimast numbrit sisestatud valesti')
            return False
    else:
        return True
    
#--------------------------------------------------------

def check_ik_month(IK):
    """
    Kontrollib, kas neljas ja viies number - sünnikuu number on õige.
    Ei võta arvesse, kas isikukoodi teised numbrid on õiged.
    
    Tagastab True, kui neljas ja viies number on õige, False muul juhul.
    """
    centuryNumb = int(IK[0])
    yearNumb = int(IK[1:3])
    monthNumb = int(IK[3:5])
    dateNow = datetime.datetime.now()
    yearNow = dateNow.year
    monthNow = dateNow.month
    if centuryNumb < 5:
        if monthNumb > 0 and monthNumb <13:
            return True
        else:
            print('Neljas ja viies number - sünnikuu number sisestatud valesti')
            return False
    else:
        if yearNumb == (yearNow - 2000):
            if monthNumb <= monthNow:
                return True
            else:
                print('Neljas ja viies number - sünnikuu number sisestatud valesti')
                return False
        else:
            return True

#--------------------------------------------------------

def check_ik_day(IK):
    # kuues ja seitsmes number	– sünnikuupäev (01 jne)
    centuryNumb = int(IK[0])
    yearNumb = int(IK[1:3])
    monthNumb = int(IK[3:5])
    dayNumb = int(IK[5:7])
    dateNow = datetime.datetime.now()
    yearNow = dateNow.year
    monthNow = dateNow.month
    dayNow = dateNow.day
    monthDict = {
    1: 31,   
    2: {'default': 28, 'leap': 29},   
    3: 31,   
    4: 30,   
    5: 31,   
    6: 30,   
    7: 31,   
    8: 31,   
    9: 30,   
    10: 31,  
    11: 30,  
    12: 31 }
    def leap_year(century, year):
        fullYear = 0
        if century in (5, 6):
            fullYear = 2000 + year
        elif century in (3, 4):
            fullYear = 1900 + year
        elif century in (1, 2):
            fullYear = 1800 + year
        else: return 'default' 

        if fullYear % 4 == 0 and (fullYear % 100 != 0 or fullYear % 400 == 0):
            return 'leap'
        else: 
            return 'default'

    if 1 <= centuryNumb <= 6: 

        if not (1 <= dayNumb <= 31):
            print('Kuues ja seitsmes number - sünnikuupäev sisestatud valesti')
            return False
        
        if centuryNumb > 4 and yearNumb == (yearNow - 2000) and monthNumb == monthNow and dayNumb > dayNow:
            print('Kuues ja seitsmes number - sünnikuupäev sisestatud valesti')
            return False
        
        if monthNumb == 2:
            if dayNumb > monthDict[2][leap_year(centuryNumb, yearNumb)]:
                print('Kuues ja seitsmes number - sünnikuupäev sisestatud valesti')
                return False
        else:
            if dayNumb > monthDict[monthNumb]:
                print('Kuues ja seitsmes number - sünnikuupäev sisestatud valesti')
                return False

        return True
        
    else:
        return False

#----------------------------------------------------------------------
def check_ik_kontrollnumber(IK):
    '''
    Kontrollib, kas üheteistkümnes number – kontrollnumber on õige.
    Liidetakse kokku esimese kümne numbri korrutised igale arvule vastava
    järjekorranumbriga (va 10. number, kus kordaja on taas 1) ning leitakse saadud 
    summast jääk jagamisel 11-ga. See jääk ongi kontrollnumber.

    Kui jääk on võrdne kümnega, tehakse arvutus uuesti ning võetakse teguriteks, millega 
    isikukoodi numbreid korrutada, vastavalt 3, 4, 5, 6, 7, 8, 9, 1, 2, 3. Leitaks jääk
    jagamisel 11-ga. Ja see ongi kontrollnumber.

    Kui jääk jälle võrdub 10ga, siis määratakse kontrollnumbriks 0.

    Näide: isikukoodi 37605030299 kontroll. 
    Summa = 1*3 + 2*7 + 3*6 + 4*0 + 5*5 + 6*0 + 7*3 + 8*0 + 9*2 + 1*9 = 108
    108 jääk jagamisel 11-ga on 9 => isikukoodi viimane number peab olema üheksa. 
    '''
    kontNumb = int(IK[-1])
    Summa = 0
    kordajad1 = (1,2,3,4,5,6,7,8,9,1)
    
    for i in range(10):
        Summa += int(IK[i])*kordajad1[i]
        
    Summa2 = 0
    kordajad2 = (3,4,5,6,7,8,9,1,2,3)
    
    if Summa % 11 == 10:
        for i in range(10):
            Summa2 += int(IK[i])*kordajad2[i]

        if Summa2 % 11 == kontNumb:
            return True
        
        elif Summa2 % 11 == 10 and kontNumb == 0:
            return True
        
        else:
            print('Üheteistkümnes number – kontrollnumber sisestatud valesti')
            return False

    elif Summa % 11 == kontNumb:
            return True
    else:
        print('Üheteistkümnes number – kontrollnumber sisestatud valesti')
        return False
    
#----------------------------------------------------------------------
def main_ik_check():
    """
    Funktsioon, mis kontrollib kasutaja sisestatud isikukoodi õigsust.
    
    Programm küsib kasutajalt isikukoodi, kontrollib selle õigsust
    kasutades erinevaid kontrollfunktsioone ning annab tulemuseks
    kas isikukood on sisestatud õigesti või mitte.
    
    Funktsioon on lõpmatu tsükkel, millest saab väljuda
    sisestades "exit".
    """
    while True:
        print('\nProgrammi sulgemiseks sisestage "exit"\n')
        ik = input('Sisestage isikukood:\n')
        
        if ik.lower() == 'exit':
            break
        checks = []
        checks.append(exists_ik(ik))
        if checks[0] == False:
            continue
        checks.append(patern_ik(ik))
        if checks[1] == False:
            continue
        ik = str(ik)
        checks.append(check_ik_gender(ik))
        checks.append(check_ik_year(ik))
        checks.append(check_ik_month(ik))
        checks.append(check_ik_day(ik))
        checks.append(check_ik_kontrollnumber(ik))

        #print(checks)
        result = all(checks)
        if result == True:
            print('Isikukood sisestatud õigesti')
        else:
            print('Isikukood sisestatud valesti')

#----------------------------------------------------------------------

main_ik_check()

# 37605030299 õige

