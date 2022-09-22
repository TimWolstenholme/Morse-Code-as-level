# Skeleton Program for the AQA AS Summer 2018 examinationTea
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS Programmer Team
# developed in a Python 3 environment


# Version Number : 1.6

SPACE = ' '
EOL = '#'
EMPTYSTRING = ''

def ReportError(s):
    print('{0:<5}'.format('*'),s,'{0:>5}'.format('*')) 
     
def StripLeadingSpaces(Transmission): 
    TransmissionLength = len(Transmission)
    if TransmissionLength > 0:
        FirstSignal = Transmission[0]
        while FirstSignal == SPACE and TransmissionLength > 0:
            TransmissionLength -= 1
            Transmission = Transmission[1:]
            if TransmissionLength > 0:
                FirstSignal = Transmission[0]
    if TransmissionLength == 0:
        ReportError("No signal received")
    return Transmission

def StripTrailingSpaces(Transmission): 
    LastChar = len(Transmission) - 1
    while Transmission[LastChar] == SPACE:
        LastChar -= 1
        Transmission = Transmission[:-1]
    return Transmission    

def GetTransmission():
    FileName = input("Enter file name: ")
    print(list(FileName).count('.'))
    if (FileName.strip()[-4:] != '.txt' and '.'in list(FileName)) or list(FileName).count('.')>1:
            ReportError("The file must be a txt")
            Transmission=EMPTYSTRING
            return Transmission
    elif '.' not in list(FileName):
        FileName+='.txt'

    try:
        FileHandle = open(FileName, 'r')
        Transmission = FileHandle.readline()
        FileHandle.close()
        Transmission = StripLeadingSpaces(Transmission)
        if len(Transmission) > 0:
            Transmission = StripTrailingSpaces(Transmission)
            Transmission = Transmission + EOL
    except:
        ReportError("No transmission found")
        Transmission = EMPTYSTRING
    return Transmission

def GetNextSymbol(i, Transmission):
    if Transmission[i] == EOL:
        print()
        print("End of transmission")
        Symbol = EMPTYSTRING
    else:
        SymbolLength = 0
        Signal = Transmission[i]
        while Signal != SPACE and Signal != EOL:
            i += 1
            Signal = Transmission[i]
            SymbolLength += 1
        if SymbolLength == 1:
            Symbol = '.'
        elif SymbolLength == 3:
            Symbol = '-'
        elif SymbolLength == 0: 
            Symbol = SPACE
        else:
            ReportError("Non-standard symbol received") 
            Symbol = EMPTYSTRING
    return i, Symbol 

def GetNextLetter(i, Transmission):
    SymbolString = EMPTYSTRING
    LetterEnd = False
    while not LetterEnd:
        i, Symbol = GetNextSymbol(i, Transmission)
        if Symbol == SPACE:
            LetterEnd = True
            i += 4
        elif Transmission[i] == EOL:
            LetterEnd = True
        elif Transmission[i + 1] == SPACE and Transmission[i + 2] == SPACE:
            LetterEnd = True
            i += 3
        else:
            i += 1
        SymbolString = SymbolString + Symbol
    return i, SymbolString

def Decode(CodedLetter, Dash, Letter, Dot):
    CodedLetterLength = len(CodedLetter)
    Pointer = 0
    for i in range(CodedLetterLength):
        Symbol = CodedLetter[i]
        if Symbol == SPACE:
            return SPACE
        elif Symbol == '-':
            Pointer = Dash[Pointer]
        else:
            Pointer = Dot[Pointer]
    return Letter[Pointer]

def ReceiveMorseCode(Dash, Letter, Dot): 
    PlainText = EMPTYSTRING
    MorseCodeString = EMPTYSTRING
    Transmission = GetTransmission() 
    LastChar = len(Transmission) - 1
    i = 0
    while i < LastChar:
        i, CodedLetter = GetNextLetter(i, Transmission)
        MorseCodeString = MorseCodeString + SPACE + CodedLetter
        PlainTextLetter = Decode(CodedLetter, Dash, Letter, Dot)
        PlainText = PlainText + PlainTextLetter
    print(MorseCodeString)
    print(PlainText)

def SendMorseCode(MorseCode):
    PlainText = input("Enter your message (uppercase letters and spaces only): ")
    PlainTextLength = len(PlainText)
    MorseCodeString = EMPTYSTRING
    for i in range(PlainTextLength):
        PlainTextLetter = PlainText[i]
        if PlainTextLetter == SPACE:
            Index = 0
        else: 
            Index = ord(PlainTextLetter) - ord('A') + 1
        CodedLetter = MorseCode[Index]
        MorseCodeString = MorseCodeString + CodedLetter + SPACE
    print(MorseCodeString)

def DisplayMenu():
    print()
    print("Main Menu")
    print("=========")
    print("R - Receive Morse code")
    print("S - Send Morse code")
    print("X - Exit program")
    print()

def GetMenuOption():
    MenuOption = EMPTYSTRING
    while len(MenuOption) != 1:
        MenuOption = input("Enter your choice: ")
    return MenuOption
        
def SendReceiveMessages():
    Dash = [20,23,0,0,24,1,0,17,0,21,0,25,0,15,11,0,0,0,0,22,13,0,0,10,0,0,0]
    Dot = [5,18,0,0,2,9,0,26,0,19,0,3,0,7,4,0,0,0,12,8,14,6,0,16,0,0,0]
    Letter = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    MorseCode = [' ','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']

    ProgramEnd = False
    while not ProgramEnd:
        DisplayMenu() 
        MenuOption = GetMenuOption()
        if MenuOption == 'R':
            ReceiveMorseCode(Dash, Letter, Dot)
        elif MenuOption == 'S':
            SendMorseCode(MorseCode) 
        elif MenuOption == 'X':
            ProgramEnd = True
        

if __name__ == "__main__":
    SendReceiveMessages()
