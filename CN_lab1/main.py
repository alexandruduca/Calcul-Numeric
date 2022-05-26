import decimal
import math


def exercise_1():
    u = 1.0
    last_u = 0
    while 1.0 + u != 1.0:
        last_u = u
        u /= 10
    return last_u


print(exercise_1())


def exercise_2():
    u = exercise_1()
    a = 1.0
    b = u / 10
    c = u / 10
    print("Addition: " + str((a + b) + c == a + (b + c)))

    a = 0.00000000000000000000000034254
    b = 0.00000000000000000000000535652
    c = 0.00000000000000000000000000327
    print("Multiplication: " + str((a * b) * c == a * (b * c)))


exercise_2()


def P4(a, y):
    return a[0] + y * (a[1] + y * (a[2] + y * (a[3] + y * a[4])))


def Q4(b, y):
    result = b[0] + y * (b[1] + y * (b[2] + y * (b[3] + y * b[4])))
    result_abs = abs(result)
    if result_abs < 1e-12:
        return 1e-12
    else:
        return result


def sinus(x):
    a = [decimal.Decimal("1805490264.690988571178600370234394843221"),
         decimal.Decimal("-164384678.227499837726129612587952660511"),
         decimal.Decimal("3664210.647581261810227924465160827365"),
         decimal.Decimal("-28904.140246461781357223741935980097"),
         decimal.Decimal("76.568981088717405810132543523682")]

    b = [decimal.Decimal("2298821602.638922662086487520330827251172"),
         decimal.Decimal("27037050.118894436776624866648235591988"),
         decimal.Decimal("155791.388546947693206469423979505671"),
         decimal.Decimal("540.567501261284024767779280700089"),
         decimal.Decimal("1.0")]

    result = x * (P4(a, x ** 2) / Q4(b, x ** 2))
    print("Sinus with functions = " + str(result))

    sinus_math = math.sin(1 / 4 * math.pi * float(x))
    print("Sinus with math = " + str(sinus_math))

    print("Absolute value of the difference = " + str(abs(result - decimal.Decimal(str(sinus_math)))))


def cosinus(x):
    a = [decimal.Decimal("1090157078.174871420428849017262549038606"),
         decimal.Decimal("-321324810.993150712401352959397648541681"),
         decimal.Decimal("12787876.849523878944051885325593878177"),
         decimal.Decimal("-150026.206045948110568310887166405972"),
         decimal.Decimal("538.333564203182661664319151379451")]

    b = [decimal.Decimal("1090157078.174871420428867295670039506886"),
         decimal.Decimal("14907035.776643879767410969509628406502"),
         decimal.Decimal("101855.811943661368302608146695082218"),
         decimal.Decimal("429.772865107391823245671264489311"),
         decimal.Decimal("1.0")]

    result = P4(a, x ** 2) / Q4(b, x ** 2)
    print("Cosinus with functions = " + str(result))

    cosinus_math = math.cos(1 / 4 * math.pi * float(x))
    print("Cosinus with math = " + str(cosinus_math))

    print("Absolute value of the difference = " + str(abs(result - decimal.Decimal(str(cosinus_math)))))


def natural_logarithm(x):
    a = [decimal.Decimal("75.151856149910794642732375452928"),
         decimal.Decimal("-134.730399688659339844586721162914"),
         decimal.Decimal("74.201101420634257326499008275515"),
         decimal.Decimal("-12.777143401490740103758406454323"),
         decimal.Decimal("0.332579601824389206151063529971")]

    b = [decimal.Decimal("37.575928074955397321366156007781"),
         decimal.Decimal("-79.890509202648135695909995521310"),
         decimal.Decimal("56.21553482954209427714341740471171"),
         decimal.Decimal("-14.516971195056682948719125661717"),
         decimal.Decimal("1.0")]

    z = (x - 1) / (x + 1)

    result = z * (P4(a, z ** 2) / Q4(b, z ** 2))
    print("ln with functions = " + str(result))

    ln_math = math.log(float(x), math.e)
    print("ln with math = " + str(ln_math))

    print("Absolute value of the difference = " + str(abs(result - decimal.Decimal(str(ln_math)))))


sinus(decimal.Decimal("-0.5"))

cosinus(decimal.Decimal("1"))

natural_logarithm(decimal.Decimal("-1.5"))
