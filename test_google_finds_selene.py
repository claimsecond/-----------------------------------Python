from selene.support.shared import browser
from selene import *

browser.config.hold_browser_open = False
browser.config.browser_name = 'firefox'
browser.open('https://google.com/ncr')
browser.element('[name=q]').type('selene').press_enter()
browser.element('[id=search]').should(
    have.text('User-oriented Web UI browser tests in Python'))
browser.all('#rso>div').should(have.size(12))