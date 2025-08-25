"""
4.1 A Browser contains a Context which contains a Page.
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

#TS-1: Browser Start 
    browser = p.chromium.launch(headless=False, slow_mo=1500)

#TS-2: new Session
    context = browser.new_context()               

#TS-3: new Tab
    page = context.new_page()                     

#TS-4: Print Page title
    page.goto("https://practice-automation.com")
    print(page.title())


    browser.close()
