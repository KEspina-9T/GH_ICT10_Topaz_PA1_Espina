#Working with Tuples for SW2
from pyscript import display, document # type: ignore (quick fix feature)

def convert_temp(e):
    document.getElementById('output').innerHTML=""
    Ftemp = float(document.getElementById('Ftemp').value)
    temp =  float((Ftemp - 32) * 5/9)

    display (f"You're temperature in Celsius is {temp}°", target="output")
    if temp > 37.7:
        display(f'You have a Fever! Make sure to get a check up!', target='output')
    else:
        display(f'You do not have a Fever!', target='output')
   

    

