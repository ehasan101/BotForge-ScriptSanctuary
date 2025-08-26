
from playwright.sync_api import sync_playwright, expect


base_url = "https://practice.expandtesting.com"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False, slow_mo=1500)
    page = browser.new_page()
    
#TS-1: Navigate to the login page
    page.goto(f"{base_url}/login")
    
#TS-2: Fill with credentials
    page.locator('input[id="username"]').fill("practice")
    page.locator('input[id="password"]').fill("SuperSecretPassword!")
    
#TS-3: click login button
    page.locator('button[type="submit"]').click()
    
#TS-4: Verify successful login
    expect(page.get_by_role("heading", name="Welcome to the Secure Area. When you are done click logout below."))
    print(f"4. Successfully logged into a secure area!\nPage Title: {page.title()}")

    page.pause()

#TS-5: click logout button
    page.locator('a.button[href="/logout"]').click()
    
#TS-6: Verify successful logout
    expect(page.get_by_role("heading", name="You logged out of the secure area!"))
    print(f"6. Successfully logout from secure area!\nPage Title: {page.title()}")

    

    browser.close()