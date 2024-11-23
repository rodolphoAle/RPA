import pyautogui

choice = pyautogui.confirm('Clique para selecionar a opção desejada',
                           buttons=['Excel','Word','Notepad'])

if choice == 'Excel':

    #comand to open execel
    pyautogui.hotkey('win')
    pyautogui.sleep(1)
    pyautogui.typewrite('excel')
    pyautogui.sleep(0.1)
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    #typing in file
    pyautogui.typewrite('Voce escolheu abrir o excel', interval=0.1)
    pyautogui.sleep(1)

    #close the file
    pyautogui.hotkey('alt','f4')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    print('Voce escolheu abrir o execel')
elif choice == 'Word':
    # comand to open execel
    pyautogui.hotkey('win')
    pyautogui.sleep(1)
    pyautogui.typewrite('word')
    pyautogui.sleep(0.1)
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    # typing in file
    pyautogui.typewrite('Voce escolheu abrir o word', interval=0.1)
    pyautogui.sleep(1)

    # close the file
    pyautogui.hotkey('alt', 'f4')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    print('Voce escolheu abrir o Word')
else:
    # comand to open execel
    pyautogui.hotkey('win')
    pyautogui.sleep(1)
    pyautogui.typewrite('notepad')
    pyautogui.sleep(0.1)
    pyautogui.press('enter')
    pyautogui.sleep(1.5)

    # typing in file
    pyautogui.typewrite('Voce escolheu abrir o notepad', interval=0.1)
    pyautogui.sleep(1)

    # close the file
    pyautogui.hotkey('alt', 'f4')
    pyautogui.press('tab')
    pyautogui.press('enter')
    print('Voce escolheu abrir o Notepad')