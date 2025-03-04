import asyncio
import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_api():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the page
        response = await page.goto("https://exo1zfvbv1.execute-api.us-east-1.amazonaws.com/miguelPuentesSiteCounter")

        # Get the response body
        content = await response.json()

        # Test result
        assert "count" in content, "API response did not return any content"


        # Check that the counter has been updated
        count1 = content['count']
        # Navigate to the page
        response2 = await page.goto("https://exo1zfvbv1.execute-api.us-east-1.amazonaws.com/miguelPuentesSiteCounter")

        # Get the response body
        content2 = await response2.json()

        count2 = content2['count']

        assert int(count2) == int(count1) + 1, "The counter didn't update"



        # Close the context and browser
        await context.close()
        await browser.close()


asyncio.run(test_api())
