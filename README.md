## Назначение проекта

Помощь в освоении инструмента 
[Код оптимизации (Postback веб-мастера)](https://help.admitad.com/ru/topic/71-kod-optimizatsii-postback-veb-mastera).
Проект позволяет смоделировать распространенные проблемы, с которыми сталкивается веб-мастер при проверке настроек кода 
отпимизации. Данный проект является лишь частью обучения и закрывает популярные проблемы с примемом постбэков сервером 
веб-мастера.


### Краткие характеристики проверок
Существует два эндпоинта для отправки постбэков. Для каждого настроена проверка 
* выбора верного метода (GET/POST);
* присутствия необходимых параметров и их значений.

Для GET запроса дополнительно проверяется корректность передаваемого значениея (длина и тип данных).  

Также для обоих эндпоинтов есть ограничение по количеству запросов в минуту.
