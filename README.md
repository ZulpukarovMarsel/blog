## Клонировать проект

    git clone 


#### Создать venv и актиvироvать
    python -m venv venv

    🪟 Windows:
    cd .venv/Scripts/activate

    🐧linux and 🍏 OS X:
    source .venv/bin/activate
    

#### Скачать зависимости

    pip install -r requirements.txt

#### Создать и заполнить .env

    cp env.example .env

#### Применить миграции и запустить проект

    sh run.sh

#### Создание приложения

    python ../manage.py startapp <название прилодения> 
