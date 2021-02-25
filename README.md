Установка проекта локально
=====================
1. Скачайте проект с гитхаб
2. Извлеките папку market--master из архива
3. Нажмите ПКМ (ПКМ + Shift на Windows) по извлеченной папке и откройте консоль (консоль PowerShell на Windows)
4. Установите виртуальное окружение командой  
`python3 -m venv venv` - Linux  
`python -m venv venv` - Windows
5. Активируйте виртуальное окружение командой  
`. venv/bin/activate` - Linux  
`venv/Scripts/activate` - Windows  
После активации перед приглашением в командной строке у вас должно высветиться название вашего окружения (в нашем случае venv)  
Пример на Windows:  
`(venv) PS C:\Users\user\Desktop\html_practice\market--master>`
7. Установите все зависимости с файла requirements.txt командой    
`pip install -r requirements.txt`
