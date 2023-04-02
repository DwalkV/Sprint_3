class Locators:
    #кнопка «личный кабинет» на главной странице
    lk_from_main_locator = (".//a[@href='/account']")
    #кнопка «войти в аккаунт» на главной странице
    login_from_main_page = (".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    # поле «имя» на странице регистрации и поле email на странице авторизации
    name_or_email_locator = (".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")
    #кнопка «Зарегистрироваться»
    registration_locator = (".//a[@href='/register']")
    # поле email на странице регистрации
    email_field_in_registration = (".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")
    #поле пароль на странице регистрации  и авторизации
    password_field = (".//input[@type='password']")
    #кнопка «Зарегистрироваться» на странице регистрации   и «Войти» на странице авторизации
    log_in = (".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    #поле с почтой в личном кабинете
    email_field_in_lk =  (".//body/div[@id='root']/div[1]/main[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/input[1]")
    #надпись «неверный пароль»
    wrong_password = (".//p[@class='input__error text_type_main-default']")
    #кнопка «Войти» со страницы регистрации и восстановления пароля
    login_from_restore_or_registration =  (".//a[@class='Auth_link__1fOlj']")
    #кнопка «Забыли пароль»
    forgot_password = (".//a[@href='/forgot-password']")
    #надпись «В этом разделе вы можете изменить свои персональные данные» в лк
    lettering_in_lk = (".//p[@class= 'Account_text__fZAIn text text_type_main-default']")
    #кнопка «Конструктор» из ЛК
    conctructor = (".//p[contains(text(),'Конструктор')]")
    #логотип
    logo = (".//div[@class='AppHeader_header__logo__2D0X2']")
    #надпись «Собери бургер»
    take_burger = (".//h1[@class='text text_type_main-large mb-5 mt-10']")
    #кнопка «Выход»
    log_out = (".//button[contains(text(),'Выход')]")
    #надпись «Вход»
    entrance = ("./html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/h2[1]")
    #кнопка «Соусы»
    sauce = (".//span[contains(text(),'Соусы')]")
    #кнопка «Начинки»
    filling = (".//span[contains(text(),'Начинки')]")
    #кнопка «Булки»
    bread = (".//span[contains(text(),'Булки')]")

