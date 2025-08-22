from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1500)
    page = browser.new_page()

# TS-1: Go to the first page
    page.goto("https://practice-automation.com")
    print(f"1. Starting page: {page.url}")

# TS-2: Go to second page 
    page.get_by_role("link", name="Window Operations").click()
    page.locator('//b[normalize-space(.)="Replace Window"]').click()
    print(f"2. Navigated to: {page.url}")


# TS-3: Now go back Home Pahe
    page.go_back()
    page.wait_for_load_state()
    page.go_back()
    page.wait_for_load_state()
    print(f"3. After go_back(): {page.url}")


# TS-4: Verify we are on the home page
    expect(page.get_by_role("heading", name="Welcome to your software automation practice website!"))
    print(f"4. Successfully navigated to Home Page: {page.url}")


# TS-5: Now we move forward
    page.go_forward()
    page.wait_for_load_state()
    print(f"5. After go_forward(): {page.url}")

# TS-6: Reload page
    page.reload()
    page.wait_for_load_state()
    print(f"6. After reload(): {page.url}")



    browser.close()