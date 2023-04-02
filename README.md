Тесты Регистрации. Файл test_registration.py
1. Тест test_registration_valid_data_success: Успешная регистрация
2. Тест test_registration_short_password: Ошибка для некорректного пароля
Тесты Входа. Файл test_authorization: 
3. Тест test_authorization_from_main_page: вход по кнопке «Войти в аккаунт» на главной
4. Тест test_authorization_from_lk: вход через кнопку «Личный кабинет» 
5. Тест test_authorization_from_registration_form: вход через кнопку в форме регистрации
6. Тест test_authorization_from_restore_password_form: вход через кнопку в форме восстановления пароля
Тесты Личного кабинета. Файл test_lk:
7. Тест test_transfer_to_lk: переход по клику на «Личный кабинет».
8. Тест test_transfer_from_lk_to_constructor: переход по клику на «Конструктор»
9. Тест test_log_out: выход по кнопке «Выйти» в личном кабинете
Тесты Конструктора. Файл test_constructor:
10. Тест test_transfer_to_sauce: переход к разделу «Соусы»
11. Тест test_transfer_to_filling:  переход к разделу «Начинки»
12. Тест test_transfer_to_bread: переход к разделу «Булки»

Фикстура driver: открытие/закрытие сайта
Фикстура login: авторизация 