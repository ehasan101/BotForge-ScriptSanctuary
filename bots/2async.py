
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    
    base_url = "https://practice.expandtesting.com"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()
        
#TS-1: Navigate to the login page
        await page.goto(f"{base_url}/login")
        
#TS-2: Fill with credentials
        await page.locator('input[id="username"]').fill("practice")
        await page.locator('input[id="password"]').fill("SuperSecretPassword!")
        
#TS-3: click login button
        await page.locator('button[type="submit"]').click()

        # await page.pause()

#TS-4: Verify successful login
        await expect(page.get_by_role("heading", name="Welcome to the Secure Area. When you are done click logout below.")).to_be_visible()
        title_after_login = await page.title()
        print(f"4. Successfully logged into a secure area!\nPage Title: {title_after_login}")

        # await page.pause()

#TS-5: click logout button
        await page.locator('a.button[href="/logout"]').click()
        
        
#TS-6: Verify successful logout
        await expect(page.get_by_role("heading", name="Test Login page for Automation Testing Practice")).to_be_visible()
        title_after_logout = await page.title()
        print(f"6. Successfully logged out from secure area!\nPage Title: {title_after_logout}")

        await browser.close()


asyncio.run(main())
