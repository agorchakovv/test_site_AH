from AHPages import SearchHelper

#Открываем сайт, кликаем по кнопке установки и сравниваем полученный url с нужным
def test_install(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    #window_before = browser.window_handles[0]   #Запоминаем предыдущую страницу
    main_page.Click_button_install()
    window_after = browser.window_handles[1]     #Запоминаем новую страницу
    browser.switch_to.window(window_after)       #Перемещаемся на новую страницу
    assert browser.current_url == "https://chrome.google.com/webstore/detail/alihelper-shopping-assist/ojclfkinnapkabameogjppmeedlicean"
