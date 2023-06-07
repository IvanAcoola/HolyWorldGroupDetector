# HolyWorldGroupDetector
Представленная утилита позволяет узнать группу пользователя (С точностью до дней).

Основные модули:
  - Определитель доната, общается к api сайта. (donate_detector.py)
  - Средство для получения csrf, xsrf, session для обхода защиты. (network_tokens_hooker.py)

Основые библиотеки:
  - requests
  - selenium

