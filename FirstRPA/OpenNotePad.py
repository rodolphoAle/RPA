import pyautogui as mouse
import pyautogui as keyboard

keyboard.hotkey('win','r')
keyboard.sleep(2)

keyboard.typewrite('notepad')

keyboard.press('enter')

keyboard.sleep(2)

keyboard.typewrite('abrindo e escevendo com '
                   'RPA feito em python', interval=0.1)
keyboard.sleep(2)
keyboard.hotkey('ctrl','w')
keyboard.sleep(1)

keyboard.press('tab')

keyboard.sleep(1)
keyboard.press('enter')

