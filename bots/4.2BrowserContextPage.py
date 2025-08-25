"""
4.2 A Brower contains Multiple tabs (pages) in the same context (shared session)
"""

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

#TS-1: Browser Start 
    browser = p.chromium.launch(headless=False, slow_mo=1500)

#TS-2: new Session
    context = browser.new_context()

#TS-3: new Tab-1
    page1 = context.new_page()
    page1.goto("https://practice.expandtesting.com/login")
    page1.locator('input[id="username"]').fill("practice")
    page1.locator('input[id="password"]').fill("SuperSecretPassword!")
    page1.locator('button[type="submit"]').click()

#TS-4: new Tab-2
    page2 = context.new_page()
    page2.goto("https://practice.expandtesting.com/login")

# TS-5: Verify that we are on the Tab-2 with same session
    expect(page2.get_by_role("heading", name="Welcome to the Secure Area. When you are done click logout below."))
    print(f"Successfully Login,You logged into a secure area!\nPage Title: {page2.title()}")


    #browser.close()
