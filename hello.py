import os
import subprocess

# 1. Грязный метод: использование eval для выполнения строки как кода
code_str = "print('Hello appsec world (via eval)')"
eval(code_str)

# 2. Еще более грязный метод: использование системного шелла
# Это "bad practice", так как ведет к инъекциям команд
os.system("echo 'Hello appsec world (via os.system)'")

# 3. Использование subprocess через оболочку
subprocess.run("echo 'Hello appsec world (via subprocess)'", shell=True)
