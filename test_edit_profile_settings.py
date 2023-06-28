from selene import browser, have, be


def test_edit_settings():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url('https://edvibe.com/TeacherAccount/lessons'))

    #Открытие настроек
    browser.element('.tabs .tab-item:nth-child(4)').click()

    #Поле Имя
    browser.element('.profile-form > div:nth-child(1) .form-control').type('!')
    browser.element('div.col-auto.ml-5 > div').click()

    #Поле Телефон
    browser.element('.profile-form > div:nth-child(4) .form-control').type('0')
    browser.element('.col-auto.ml-5 .ui-button-base').click()

    #Поле родной язык (изменение на англ.)
    browser.element('.profile-form > div:nth-child(6) .ui-select').click()
    browser.element('.ui-options.active .scroll-content .option:nth-child(2)').click()
    browser.element('.col-auto.ml-5 .ui-button-base').click()
    browser.element('.profile-form > div:nth-child(6) .ui-select .no-select-text').should(have.exact_text('English'))

    #Поле Интерфейс (изменение на русский)
    browser.element('.profile-form > div:nth-child(7) .ui-select').click()
    browser.element('.ui-options.active .scroll-content .option:nth-child(2)').click()
    browser.element('.col-auto.ml-5 .ui-button-base').click()
    browser.element('.profile-form > div:nth-child(7) .ui-select .no-select-text').should(have.exact_text('Russian'))

    #Поле Страна (изменение на Казахстан)
    browser.element('.profile-form > div:nth-child(8) .ui-select').click()
    browser.element('.ui-options.active .scroll-content .option:nth-child(3)').click()
    browser.element('.accept .ui-button-base').click()
    browser.element('.col-auto.ml-5 .ui-button-base').click()
    browser.element('.profile-form > div:nth-child(8) .image-title > div').should(have.exact_text('Kazakhstan'))

    #Поле Часовой пояс (изменение на +4)
    browser.element('.ui-dropdown.timezone').click()
    browser.element('.ui-options.active .scroll-content .option:nth-child(17)').click()
    browser.element('.col-auto.ml-5 .ui-button-base').click()
    browser.element('.ui-dropdown.timezone .ui-select .no-select-text').should(have.text('(UTC+4)'))

    #Поле Skype
    browser.element('.profile-form > div:nth-child(10) .form-control').type('my skype')
    browser.element('.col-auto.ml-5 .ui-button-base').click()

    #Поле Ссылка на звонок (выбор Zoom)
    browser.element('div.ui-select.with-input').click()
    browser.element('.ui-options.active .options').click()
    browser.element('div.ui-button-base.btn-save.default').click()
    browser.element('.ui-select.with-input .image-title > div').should(have.exact_text('Zoom'))

    #Поле Рассылка для учеников (включение рассылки и выбор времени)
    browser.element('.label-with-toggle .slider').click()
    browser.element('.label-container .placeholder').click()
    browser.element('.options .option:nth-child(2)').click()
    browser.wait_until(browser.element('.ui-button-base.btn-save.default').should(be.visible))
    browser.element('.ui-button-base.btn-save.default').click()
    browser.element('.label-with-toggle .ui-toggle-switcher').should(have.css_class('checked'))
    browser.element('.multiselect-dropdown .ui-dropdown .ui-select').should(have.css_class('idforgetelement'))