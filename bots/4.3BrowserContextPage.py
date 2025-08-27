"""
4.3. Two separate contexts in the same browser (two different user sessions)
"""

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

#TS-1: Browser Start 
    browser = p.chromium.launch(headless=False, slow_mo=1500)

#TS-2: new Session with userA
    context_userA = browser.new_context()
    pageA = context_userA.new_page()
    pageA.goto("https://practice.expandtesting.com/login")
    pageA.locator('input[id="username"]').fill("practice")
    pageA.locator('input[id="password"]').fill("SuperSecretPassword!")
    pageA.locator('button[type="submit"]').click()

# TS-3: Verify that we are on the Dashboard area after login
    expect(pageA.get_by_role("heading", name="Welcome to the Secure Area. When you are done click logout below."))
    print(f"User(A): Successfully logged into a secure area!\nPage URL: {pageA.url}")

# # TS-4: End this session
#     pageA.locator('a[href="/logout"]').click()
    
# TS-4: Verify that can we access on the Dashboard?
    pageA2 = context_userA.new_page()
    pageA2.goto("https://practice.expandtesting.com/login")
    expect(pageA2.get_by_role("heading", name="Welcome to the Secure Area. When you are done click logout below."))
    print(f"User(A) in secure area!\nPage URL: {pageA2.url}")

    # pageA.pause()
    
#TS-5: new Session with userB
    context_userB = browser.new_context()
    pageB = context_userB.new_page()
    pageB.goto("https://practice.expandtesting.com/login")
    pageB.locator('input[id="username"]').fill("practice")
    pageB.locator('input[id="password"]').fill("SuperSecretPassword!")
    pageB.locator('button[type="submit"]').click()

# TS-6: Verify that we are on the Dashboard area after login
    expect(pageB.get_by_role("heading", name="Welcome to the Secure Area. When you are done click logout below."))
    print(f"User(B): Successfully logged into a secure area!\nPage Title: {pageB.title()}")

# TS-7: Verify that can we access on the Dashboard?
    pageB2 = context_userB.new_page()
    pageB2.goto("https://practice.expandtesting.com/login")
    expect(pageB2.get_by_role("heading", name="Welcome to the Secure Area. When you are done click logout below."))
    print(f"User(B) in secure area!\nPage URL: {pageB2.url}")

    

    # pageB.pause()
    #browser.close()

