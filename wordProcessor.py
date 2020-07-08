import npyscreen

def mainScreen(*args):
    F = npyscreen.Form(name='My Test Application')
    F.add(npyscreen.TitleText, name="First Widget")
    F.edit()

def main():
    npyscreen.wrapper_basic(mainScreen)