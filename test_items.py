import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket(browser,language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    basket = browser.find_element_by_css_selector('button.btn:nth-child(3)')
    print(basket)
    assert basket is not None, 'We cant find basket button'
    time.sleep(10)