#Tarea 1
import math
import datetime
import collections
from datetime import datetime,timedelta,date

class Tarea1:
    def __init__(self, titulo):
        self.mensaje=titulo
    
    def ejercicio1(self):
        print("'Hola mundo' --> string\nVerdadero --> Booleano\n  -->None\n„1 --> syntax error\n„c' --> syntax error\n256 --> entero\n8>19 --> Booleano")

    def ejercicio2(self):
        x=(5-3*2)+9>3*5*14%3
        print(f"(5-3*2)+9>3*5*14%3 = {x} --> {type(x)}")
        x=2*(4-10+8)/2*36*(1/2)
        print(f"2*(4-10+8)/2*36*(1/2) = {x}--> {type(x)}")
        x=260/12+54%3-85%7
        print(f"260/12+54%3-85%7 = {x}--> {type(x)}")
        x=(48<2*30)or(2*7<12)
        print(f"(48<2*30)||(2*7<12) = {x}--> {type(x)}")
        x=((8>2)or(932<23))and 4==2
        print(f"((8>2)||(932<23))&& 4==2 = {x}--> {type(x)}")

    def ejercicio3(self):
        lista=[0]*2
        opc=['primer', 'segundo']
        indice=0
        while indice<2:
            while lista[indice]<=0:
                lista[indice]=int(input(f"Ingrese {opc[0+indice]} numero"))
            indice+=1
        print(f"La suma es: {sum(lista)}")
        print(f"La resta es: {lista[0]-lista[1]}")
        print(f"La multiplicacion es: {lista[0]*lista[1]}")
        print(f"La division es: {(lista[0]/lista[1]):.2f}")
        print(f"El modulo es: {lista[0]%lista[1]}")


    def ejercicio4(self):
        a=int(input("Ingrese a"))
        b=int(input("Ingrese b"))
        c=int(input("Ingrese c"))
        d = b**2-4*a*c
        if d < 0:
            print("NO existe Solucion")
        elif d == 0:
            x = (-b+math.sqrt(b**2-4*a*c))/2*a
            print("Tiene una unica solucion: ", x)
        else:
            x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
            x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
            print("Tiene dos soluciones: ", x1, " y", x2)
    
    def ejercicio5(self):
        a=float(input("Ingrese primer lado del triangulo: "))
        b=float(input("Ingrese segundo lado del trinagulo: "))
        c=math.sqrt((a**2+b**2))
        return c

    def ejercicio6(self):
        numero=int(input("Ingrese un número: "))
        res=numero%2
        if res==0:
            print("0 - par")
        else:
            print("1 - impar")

    def ejercicio7(self):
        binario=int(input("ingrese numero binario de 4 digitos: "))
        binario=str(binario)
        c=0
        for i in binario:
            if i in "1":
                c+=1
        if c%2==0:
            print('Su bit da paridad')
        else:
            print("Su bit no da paridad!")

    def ejercicio8(self):
        binario=input("Ingrese numero binario de 4 digitos: ")
        bin1=int(binario,2)
        print(f"Su valor en decimal es: {bin1}")

    def ejercicio9(self):
        numero=int(input("Ingrese un numero de 4 digitos: "))
        m=numero/1000
        m=int(m)
        resid=numero-(m*1000)
        resid1=resid/100
        c=int(resid1)
        residc=resid-(c*100)
        d=residc/10
        d=int(d)
        u=residc%10
        print(f"Unidades: {u}")
        print(f"Decenas: {d}")
        print(f"Centenas: {c}")
        print(f"Unidades de mil: {m}")

    def ejercicio10(self):
        fecha=int(input("ingrese una fecha ['ddmmaa']: "))
        year=fecha%10000
        if year % 4 != 0:
            print(f"El año {year}, No es bisiesto")
        elif year % 4 == 0 and year % 100 != 0:
            print("El año {year}, Es bisiesto")
        elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
            print("El año {year}, No es bisiesto")
        elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            print("El año {year}, Es bisiesto")

    def ejercicio11(self):
        numero=int(input("Ingrese un numero de 5 digitos: "))
        lista=[]
        lista=str(numero)
        invert=lista[::-1]
        if lista==invert:
            print(f"El numero {numero}, es copicua")
        else:
            print(f"El numero {numero}, no es copicua")

    def ejercicio12(self):
        lista=[0]*2
        alt=['Horas', 'Minutos']
        indice=0
        while indice<2:
            while lista[indice]<=0:
                lista[indice]=int(input(f"Ingrese {alt[0+indice]}"))
            indice+=1
        segundos=(lista[0]*3600)+(lista[1]*60)
        print(f"Su equivalencia en segundos es: {segundos} Segundos")

    def ejercicio13(self):
        seg=int(input("Ingrese numero entero: "))
        dias=int(seg/86400);hora=int(seg/3600);minutos=int(seg/60)
        print(f"El numero ingresado equivale a: {dias} Dias, {hora} Horas, {minutos} Minutos")
    
    def ejercicio14(self):
        abc=['A','B','C']
        lista=[0]*3
        indice=0
        while indice<3:
            while lista[indice]<=0:
                lista[indice]=int(input(f"Ingrese numero {abc[0+indice]}: "))
            indice+=1
        ma=max(lista)
        mi=min(lista)
        if lista[0]==mi:
            del lista[0]
        elif lista[1]==mi:
            del lista[1]
        else:
            del lista[2]
        print(f"El numero mayor es: {max(lista)}")
        print(f"El segundo numero mayor es: {min(lista)}")

    def ejercicio15(self):
        Hentrada=['']*2
        opc=['Hora de entrada', 'Horario AM(A) O PM(P)']
        indice=0
        while indice<2:
            while Hentrada[indice]<='':
                Hentrada[indice]=input(f"Ingrese {opc[0+indice]}: ")
            indice+=1
        Hsalida=['']*3
        opc=['Hora de salida', 'Horario AM(A) O PM(P)']
        indice=0
        while indice<2:
            while Hsalida[indice]<='':
                Hsalida[indice]=input(f"Ingrese {opc[0+indice]}: ")
            indice+=1
        Htot=[Hsalida[0],Hentrada[0]]
        Htot=Htot[0-1]
        x = [i for i in str(Htot)]
        lista=['']*2
        lista [0]= x[0]+x[1]
        lista [1]= x[2]+x[3]
        Hora = int(lista[0])*4
        minutos=int(lista[1])
        if minutos>30:
            Hora+=2.50
            print(f"Su valor a pagar es de: ${Hora}" )
        else:
            print(f"Su valor a pagar es de: ${Hora}" )

    def ejercicio16(self):
        peso=float(input("Ingrese su peso en libras: "))
        estatura=int(input("Ingrese su estatura en centimetros: "))
        peso=peso*0.453592
        estatura=estatura/100
        imc=peso/estatura**2
        if imc<16:
            print(f"Su peso en Kg es: {peso:.2f}\nSu IMC es de: {imc:.2f}\nFue calificado a la categoria: 'Criterio de ingreso' ")
        elif imc>=16 and imc<=16.9:
            print(f"Su peso en Kg es: {peso:.2f}\nSu IMC es de: {imc:.2f}\nFue calificado a la categoria: 'Infra peso' ")
        elif imc>=17 and imc<=18.4:
            print(f"Su peso en Kg es: {peso:.2f}\nSu IMC es de: {imc:.2f}\nFue calificado a la categoria: 'Bajo peso' ")
        elif imc>=18.5 and imc<=24.9:
            print(f"Su peso en Kg es: {peso:.2f}\nSu IMC es de: {imc:.2f}\nFue calificado a la categoria: 'Peso normal' ")
        elif imc >=25 and imc<=29.9:
            print(f"Su peso en Kg es: {peso:.2f}\nSu IMC es de: {imc:.2f}\nFue calificado a la categoria: 'Sobrepeso' ")
        elif imc>=30 and imc<=34.9:
            print(f"Su peso en Kg es: {peso:.2f}\nSu IMC es de: {imc:.2f}\nFue calificado a la categoria: 'Obesidad pre-mórbida' ")
        elif imc>=40 and imc<=45:
            print(f"Su peso en Kg es: {peso:.2f}\nSu IMC es de: {imc:.2f}\nFue calificado a la categoria: 'Obesidad mórbida' ")
        else:
            print(f"Su peso en Kg es: {peso:.2f}\nSu IMC es de: {imc:.2f}\nFue calificado a la categoria: 'Obesidad híper-mórbida' ")

    def ejercicio17(self,mes,dia):
        fin=['2014']
        fin.append(mes)
        fin.append(dia)
        for i in range(len(fin)):
            fin[i]=int(fin[i])
        fin=datetime(fin[0],fin[1],fin[2])
        inicio=datetime(2014,1,1)
        res=abs(fin-inicio).days
        print(f"Han transcurrido {res} dias")

    def ejercicio18(self,numero):
        meses=["Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        numero+=-1
        if numero>=0 and numero <=11:
            print(meses[numero])
        else:
            print("Error, numero inexistente")

    def ejercicio19(self,monto):
        if monto>1000:
            dc=monto*0.20
            monto-=dc
            print(f"Su total a pagar es de: {monto:.2f}")
        else:
            print(f"Su total a pagar es de: {monto:.2f}")

    def ejercicio20(self,numero):
        num=str(numero)
        print(f"El numero {numero}, tiene {len(num)} digitos")

    def ejercicio21(self, numero):
        num=str(numero)
        if num==num[::-1]:
            print(f"El numero {numero}, es copicua")
        else:
            print(f"El numero {numero}, no copicua")

    def ejercicio22(self, numero):
        c=0
        for i in range(1, numero+1):
            if numero%i==0:
                c+=1
        if c==2:
            print(f"El numero {numero}, Es primo")
        else:
            print(f"El numero {numero}, No es primo")

    def ejercicio23(self):
        fact=int(input("Ingrese un numero: "))
        facto=1
        if fact>=1:
            for i in range (1,fact+1):
                facto=facto*i
        print(f"El factorial de {fact}, es: {facto}")

    def ejercicio24(self):
        validacion=False
        while validacion==False:
            clave=input("Ingrese su contraseña: ")
            if len(clave)==10:
                print("Igreso de contraseña exitoso!")
                validacion=True
            else:
                print("Error, la contraseña debe tener 10 digitos, vuelva a intentar!")
                validacion=False        

    def ejercicio25(self, sec_num):
        sec_numm=[]
        indice=0
        c=0
        while indice<len(sec_num):
            sec_numm.append(sec_num[c]/10)
            indice+=1
            c+=1
        mayor=max(sec_numm)
        menor=min(sec_numm)
        print(f"EL mayor es: {mayor:.0f}, el menor es: {menor:.0f}")

    def ejercicio26(self):
        edad=[20,18,32,19,22,40]
        peso=[42,52,49,47,50,46]
        estatura=[1.45,1.63,1.52,1.70,1.68,1.57]
        prom_edad=(sum(edad))/len(edad)
        prom_peso=(sum(peso))/len(peso)
        prom_estatura=(sum(peso))/len(estatura)
        c=0
        x=0
        while c<8:
            x+=(edad.count(18+c))
            c+=1  
        c=1
        TreSeis=0  
        while c<150:
            TreSeis+=(edad.count(36+c))
            c+=1
        c=0
        contPos=0
        while c<36:
            contPos=[i for i,x in enumerate(edad) if x>=18 and x<=35]
            c+=1
        suma=0
        c=0
        while c<len(contPos):
            suma+=peso[contPos[0+c]]
            c+=1
        print(f"El promedio de edades de todas las personas es de: {prom_edad:.2f}")
        print(f"El promedio de peso de todas las personas es de: {prom_peso:.2f}")
        print(f"El promdedio de estatura de todas las personas es de: {prom_estatura:.2f}")
        print(f"Hay {x}, personas con edad de entre [18-25] ")
        print(f"Hay {TreSeis}, personas mayor(es) a 36 años")
        print(f"El promedio de peso entre las personas de 18 a 35 años es: {suma/len(contPos):.2f}")

    def ejercicio27(self):
        print("Tabla del 1")
        for f in range(1,11):
            print(f'1 x {f} = {1 * f}')
        print("\n")
        print("Tabla del 2")
        for f in range(1,11):
            print(f'2 x {f} = {2 * f}')
        print("\n")
        print("Tabla del 3")
        for f in range(1,11):
            print(f'3 x {f} = {3 * f}')
        print("\n")
        print("Tabla del 4")
        for f in range(1,11):
            print(f'4 x {f} = {4 * f}')
        print("\n")
        print("Tabla del 5")
        for f in range(1,11):
            print(f'5 x {f} = {5 * f}')
        print("\n")
        print("Tabla del 6")
        for f in range(1,11):
            print(f'6 x {f} = {6 * f}')
        print("\n")
        print("Tabla del 7")
        for f in range(1,11):
            print(f'7 x {f} = {7 * f}')
        print("\n")
        print("Tabla del 8")
        for f in range(1,11):
            print(f'8 x {f} = {8 * f}')
        print("\n")
        print("Tabla del 9")
        for f in range(1,11):
            print(f'9 x {f} = {9 * f}')
        print("\n")
        print("Tabla del 10")
        for f in range(1,11):
            print(f'10 x {f} = {10 * f}')

    def ejercicio28(self):
        for i in range(0,7):
            for j in range(0, i+1):
                print("|" + str(i) + "|" + str(j) + "|")

    def ejercicio29(self):
        c=0
        numerospos=0
        while True:
            numeros=int(input("Ingrese una serie de números positivos: "))
            if numeros==0:
                break
            elif numeros > 1:
                numerospos+=numeros
                c+=1
                prom=numerospos/c
        return prom

    def ejercicio30(self):
        c=0
        edades_mayores=0
        while True:
            print("presione [enter] para dejar de ingresar notas!")
            edades=(input("ingrese las edades a promediar:"))
            if edades=='':
                break
            elif edades >= "18":
                edades=int(edades)
                edades_mayores+=edades
                c+=1
                prom=edades_mayores/c
        return prom
    def ejercicio31(self, base, expo):
        result=base**expo
        return result

    def ejercicio32(self):
        lado=float(input("Ingrese el valor de uno de los lados del pentágono!:"))
        perimetro=5*lado
        return perimetro

    def ejercicio33(self):
        def CalculaSalario(pagoHora, horas):
            pagoHora=int(pagoHora)
            horas=int(horas)
            conc=[]
            if horas>40:
                extra=horas-40
                Hnormal=horas-extra
                ph=Hnormal*pagoHora
                pe=(pagoHora*0.35+pagoHora)*extra
                totSemana=ph+pe
                horas*=pagoHora
                conc.append(totSemana),conc.append(ph),conc.append(pe)
            else:
                ph=pagoHora*horas
                conc.append(ph)
            return conc
        empleados=['']*15
        abc=['1','','','2','','','3','','','4','','','5']
        indice=0
        while indice<=14:
            if indice==0 or indice==3 or indice==6 or indice==9 or indice==12:
                while empleados[indice]<='':
                    empleados[indice]=input(f"Ingrese su identificacion Empleado {abc[0+indice]}: ")
                indice+=1
            elif indice==1 or indice==4 or indice==7 or indice==10 or indice==13:
                while empleados[indice]<='':
                    empleados[indice]=input(f"Ingrese el pago por hora: ")
                indice+=1
            else:
                while empleados[indice]<='':
                    empleados[indice]=input(f"Ingrese las horas trabajadas durante la semana: ")
                indice+=1
        conc=CalculaSalario(empleados[1], empleados[2])
        if len(conc)==3:
            print(f"{empleados[0]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin Horas extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[0]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[4], empleados[5])
        if len(conc)==3:
             print(f"{empleados[3]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[3]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[7], empleados[8])
        if len(conc)==3:
            print(f"{empleados[6]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[6]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[10], empleados[11])
        if len(conc)==3:
            print(f"{empleados[9]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[9]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[13], empleados[14])
        if len(conc)==3:
            print(f"{empleados[12]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[12]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")

    def ejercicio34(self):
        def MillasAKilometros(millas):
            kilom=millas*1.60935
            return kilom
        ciudades=['']*12
        abc=['A','B','','C','D','','F','G','','H','I']
        indice=0
        while indice<=11:
            if indice==0 or indice==1 or indice==3 or indice==4 or indice==6 or indice==7 or indice==9 or indice==10:
                while ciudades[indice]<='':
                    ciudades[indice]=input(f"Ingrese ciudad {abc[0+indice]}: ")
                indice+=1
            else:
                while ciudades[indice]<='':
                    ciudades[indice]=input(f"Ingrese distancia entre ciudades en millas: ")
                indice+=1
        print(f"\nEntre {ciudades[0]} y {ciudades[1]}, hay {MillasAKilometros(int(ciudades[2])):.2f} Km de distancia\n")
        print(f"Entre {ciudades[3]} y {ciudades[4]}, hay {MillasAKilometros(int(ciudades[5])):.2f} Km de distancia\n")
        print(f"Entre {ciudades[6]} y {ciudades[7]}, hay {MillasAKilometros(int(ciudades[8])):.2f} Km de distancia\n")
        print(f"Entre {ciudades[9]} y {ciudades[10]}, hay {MillasAKilometros(int(ciudades[11])):.2f} Km de distancia\n")
    
c=0       
while c==0:
    opc=int(input("Ingrese el número del ejercicio a realizar, entre [1-34]: "))
    if opc==1:
        tareaVariable=Tarea1("ejercicio 1")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio1()
        c=1
    elif opc==2:
        tareaVariable=Tarea1("ejercicio 2")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio2()
        c=1
    elif opc==3:
        tareaVariable=Tarea1("ejercicio 3")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio3()
        c=1
    elif opc==4:
        tareaVariable=Tarea1("ejercicio 4")
        print(tareaVariable.mensaje)
        res=tareaVariable.ejercicio4()
        c=1
    elif opc==5:
        tareaVariable=Tarea1("ejercicio 5")
        print(tareaVariable.mensaje)
        result=tareaVariable.ejercicio5()
        print(f"La hipotenusa del triangulo es: {result:.2f}")
    elif opc==6:
        tareaVariable=Tarea1("ejercicio 6")
        print(tareaVariable.mensaje)
        res=tareaVariable.ejercicio6()
        c=1
        pass
    elif opc==7:
        tareaVariable=Tarea1("ejercicio 7")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio7()
        c=1
    elif opc==8:
        tareaVariable=Tarea1("ejercicio 8")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio8()
        c=1
    elif opc==9:
        tareaVariable=Tarea1("ejercicio 9")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio9()
        c=1
    elif opc==10:
        tareaVariable=Tarea1("ejercicio 10")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio10()
        c=1
    elif opc==11:
        tareaVariable=Tarea1("ejercicio 11")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio11()
        c=1
    elif opc==12:
        tareaVariable=Tarea1("ejercicio 12")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio12()
        c=1
    elif opc==13:
        tareaVariable=Tarea1("ejercicio 13")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio13()
        c=1
    elif opc==14:
        tareaVariable=Tarea1("ejercicio 14")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio14()
        c=1
    elif opc==15:
        tareaVariable=Tarea1("ejercicio 15")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio15()
        c=1
        pass
    elif opc==16:
        tareaVariable=Tarea1("ejercicio 16")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio16()
        c=1
    elif opc==17:
        tareaVariable=Tarea1("ejercicio 17")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio17(input("ingrese el mes en numero del año 2014:  "),input("ingrese el dia en numero del año 2014:  "))
        c=1
    elif opc==18:
        tareaVariable=Tarea1("ejercicio 18")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio18(int(input("ingrese un numero entre [1 - 12]:  ")))
        c=1
    elif opc==19:
        tareaVariable=Tarea1("ejercicio 19")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio19(float(input("ingrese el monto de su compra: ")))
        c=1
    elif opc==20:
        tareaVariable=Tarea1("ejercicio 20")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio20(int(input("Ingrese un numero: ")))
        c=1
    elif opc==21:
        tareaVariable=Tarea1("ejercicio 21")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio21(int(input("ingrese un numero: ")))
        c=1
    elif opc==22:
        tareaVariable=Tarea1("ejercicio 22")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio22(int(input("Ingrese un numero entero: ")))
        c=1
    elif opc==23:
        tareaVariable=Tarea1("ejercicio 23")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio23()
        c=1
    elif opc==24:
        tareaVariable=Tarea1("ejercicio 24")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio24()
        c=1
    elif opc==25:
        tareaVariable=Tarea1("ejercicio 25")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio25([10,20,30,150,230,580,50])
        c=1
    elif opc==26:
        tareaVariable=Tarea1("ejercicio 26")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio26()
        c=1
    elif opc==27:
        tareaVariable=Tarea1("ejercicio 27")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio27()
        c=1
    elif opc==28:
        tareaVariable=Tarea1("ejercicio 28")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio28()
        c=1
    elif opc==29:
        tareaVariable=Tarea1("ejercicio 29")
        print(tareaVariable.mensaje)
        prom=tareaVariable.ejercicio29()
        print(f"El promeido de la serie es: {prom:.2f} ")
        c=1
    elif opc==30:
        tareaVariable=Tarea1("ejercicio 30")
        print(tareaVariable.mensaje)
        prom=tareaVariable.ejercicio30()
        print(f"El promeido de edades mayores a 18 es de: {prom:.2f} ")
        c=1
    elif opc==31:
        tareaVariable=Tarea1("ejercicio 31")
        print(tareaVariable.mensaje)
        print(tareaVariable.ejercicio31(10,4))
        c=1
        pass
    elif opc==32:
        tareaVariable=Tarea1("ejercicio 32")
        print(tareaVariable.mensaje)
        perimetro=tareaVariable.ejercicio32()
        print(f"el perimetro del pentágono es: {perimetro:.2f}")
        c=1
        pass
    elif opc==33:
        tareaVariable=Tarea1("ejercicio 33")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio33()
        c=1
    elif opc==34:
        tareaVariable=Tarea1("ejercicio 34")
        print(tareaVariable.mensaje)
        tareaVariable.ejercicio34()
        c=1
    else:
        print("Opcion incorrecta! Vuelva a intentar: ")
    if True:
        opc=input("Desea acceder a otro ejercicio? [s/n]")
        if opc=='s':
            c=0
        else:
            c=1
            print("Gracias por revisar los ejercicios <3")


