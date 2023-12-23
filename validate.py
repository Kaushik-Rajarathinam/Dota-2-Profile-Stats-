import re
from grabber import start
def verify(input):
    print('Validating...')
    if input.isnumeric():
        if re.findall(r'\d{17}', input) != []:
            start('64bit', input)
        else:
            start('Steam', input)
    else:
        start('Steam', input)


