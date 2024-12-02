from playwright.sync_api import Playwright, sync_playwright,expect
import re

def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://console-integ.reach5.co/")
    #page.wait_for_load_state("networkidle")
    #page.get_by_test_id("identifier").click()
    page.get_by_test_id("identifier").fill("nawel.mele@reach5.co")
    #page.get_by_test_id("password").click()
    #page.get_by_test_id("password").press("CapsLock")
    page.get_by_test_id("password").fill("Motdepasse2023*")
    page.get_by_test_id("submit").click()
    page.wait_for_load_state("networkidle")
    # Here we want to make sure the word Accounts appears in the title h1 on the DOM
    locator = page.locator("h1")
    expect(locator).to_contain_text("Accounts")
    # ---------------------
    context.close()
    browser.close()

""" No need of these two lined with pytest

with sync_playwright() as playwright:
    test_login(playwright)

"""