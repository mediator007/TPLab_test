# TPLab_test
Телеграм бот для возврата скриншота сайта по заданному url.

## Установка 
Перед первым запуском необходимо:

### Установить Chrome

```wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb```

```sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb```

Уточнить версию браузера командой: ```google-chrome --version```,
скачать драйвер необходимой версии с https://chromedriver.chromium.org/downloads 
и положить его в /app/services.

### Подключить переменные окружения

В файле .env-example записать в переменные token, db_user, db_password и adminpassword
актуальные значения, после чего переименовать файл в .env .

## Запуск

Для запуска через docker-compose выполнить команду:

```./run.sh start```

Чтобы удалить все контейнеры и volumes:

```./run.sh stop```
