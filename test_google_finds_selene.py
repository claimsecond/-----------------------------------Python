from selene.support.shared import browser
from selene import *


browser.config.hold_browser_open = True
browser.open('https://google.com/ncr')
browser.element('[name=q]').type('selene').press_enter()
browser.element('[id=search]').should(have.text('User-oriented Web UI'))