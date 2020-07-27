try:
    from subprocess import call
    import sys
    import ctypes
    messageBox = ctypes.windll.user32.MessageBoxW
    print('Downloading HazPy Developer Package')
    call('CALL conda.bat activate hazus_env && CALL conda.bat install -c nhrap-dev hazpy -f -y', shell=True)
    messageBox(0, u"hazpy switched to hazpy-dev.", u"HazPy", 0x1000)
except:
    messageBox(0, u"Unexpected error:" + sys.exc_info()[0] + u" | If this problem persists, please ask your developers to write better code.", u"HazPy", 0x1000)