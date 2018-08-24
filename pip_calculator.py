#Pip calculator

def main():
    while True:
        your_currency = input("Your currency: ")
        numerator = input("First currency in pair: ")
        denominator = input("Second currency in pair: ")
        while your_currency == denominator:
            amount = risk()
            value_per_pip = vpp(amount)
            pips_per_unit = ppu(value_per_pip)
            print(pips_per_unit)
            print("\n")
            break
        while your_currency == numerator:
            amount = risk()
            convert = conversion(amount,your_currency,numerator,denominator)
            value_per_pip = vpp(convert)
            pips_per_unit = ppu(value_per_pip)
            print(pips_per_unit)
            print("\n")
            break
        while your_currency != numerator or denominator:
            amount = risk()
            convert = conversion(amount,your_currency,numerator,denominator)
            value_per_pip = vpp(convert)
            pips_per_unit = ppu(value_per_pip)
            print(pips_per_unit)
            print("\n")
            break
        continue
        
def risk():
    """calculates the amount of money being risked"""

    capital = int(input("Total Capital: "))
    percentage = int(input("Percent of capital risked: "))
    amount_risked = (capital * (percentage/100))

    return amount_risked

def conversion(amount,your_currency,numerator,denominator):
    """converts your currency into the new currency"""
    conv = float(input("What is the conversion between " + your_currency + " and " + denominator + ": "))
    if your_currency == numerator:
        final_convert = float((conv/1)*amount)

    if your_currency != numerator:
        final_convert = float((1/conv)*amount)
    
    return final_convert

def vpp(amount):
    """divides the amount risked by the stop to find the value per pip"""

    ppt = int(input("Pips per trade: "))
    v_per_pip = ((amount)/(ppt))
    return v_per_pip
    

def ppu(value_per_pip):
    """determines each pip move per 1 unit of currency"""

    value_ratio = int(input("Known unit per 1: "))
    sub_total = (value_ratio)/1
    total = (float(value_per_pip) * float(sub_total))
    return total
    

main()
