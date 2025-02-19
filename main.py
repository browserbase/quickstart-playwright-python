import os
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright
from browserbase import Browserbase

load_dotenv()

BROWSERBASE_API_KEY = os.environ[bb_live_Qw8BrpunXIku36_v9Gno_fKpWtA]
BROWSERBASE_PROJECT_ID = os.environ[bebf0f9f-e391-45db-9c6c-7b8855a171c2]

bb = Browserbase(api_key=BROWSERBASE_API_KEY)


def run(playwright: Playwright) -> None:
    # Create a session on Browserbase
    session = bb.sessions.create(project_id=BROWSERBASE_PROJECT_ID)
    print("Session replay URL:", f"https://browserbase.com/sessions/{session.id}")

    # Connect to the remote session
    chromium = playwright.chromium
    browser = chromium.connect_over_cdp(session.connect_url)
    context = browser.contexts[0]
    page = context.pages[0]

    # Execute Playwright actions on the remote browser tab
    page.goto("https://browserbase.com/")
    page_title = page.title()
    print(page_title)

    # Close the browser
    page.close()
    browser.close()
    print("Done!")


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
