# HolyWorldGroupDetector
Представленная утилита позволяет узнать группу пользователя (С точностью до дней).

## Описание

Основные модули:
  - Определитель доната, общается к api сайта. (donate_detector.py)
  - Средство для получения csrf, xsrf, session для обхода защиты. (network_tokens_hooker.py)

Основые библиотеки:
  - requests
  - selenium
## Использование

```
nickname = "test"
tokens = network_tokens_hooker.get_session_data()
donate_getter = donate_detector.HolyworldRequester(*tokens)
donate_getter.get_user_info(nickname)
```

Готовое решение для использования - main.py

## Установка

Клонируем репозиторий
```
git clone https://github.com/IvanAcoola/HolyWorldGroupDetector.git
cd HolyWorldGroupDetector
```
Создаем окружение и загружаем библиотеки
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Запуск
```
python3 main.py
```



***Запрещается использование в вредоносных целях***
