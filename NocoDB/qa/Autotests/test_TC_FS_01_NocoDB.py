import re
import os
import random
import string
import logging
import pytest
from playwright.sync_api import Page, expect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_TC_FS_01(page: Page):

# 1. Open the website http://localhost:8080/dashboard
    try:
        logger.info("TC_FS_01 Step 1: The website http://localhost:8080/dashboard opens...")
        page.goto("http://localhost:8080/dashboard")
        logger.info("TC_FS_01 Step 1: Website opened successfully!")
    except Exception as e:
        logger.info(f"TC_FS_01 Step 1: Failed. Error: {e}")
        pytest.fail("Test stopped at Step 1")
    
# Precondition: Autorisation
    try:
        logger.info("TC_FS_01 Precondition: Authorization...")
        page.locator("#form_item_email").fill("1@1.net")
        page.locator("#form_item_password").fill("11111111")
        page.get_by_role("button", name="Sign in").click()
        logger.info("TC_FS_01 Precondition: Authorization successful!")
    except Exception as e:
        logger.info(f"Authorization failed. Error: {e}")
        pytest.fail("The authorization prerequisite was not met.")

# 2. Click the Projects button
    try:
        logger.info("TC_FS_01 Step 2: Click the Projects button to navigate to the projects...")
        project_element = page.get_by_text("Project").first
        project_element.wait_for(state="visible", timeout=15000)
    
        project_element.click()
    except Exception as e:
        logger.info(f"TC_FS_01 Step 2: Failed. Error: {e}")
        pytest.fail("Unable to navigate to the Projects section.")

# 3. Select a previously created project from the list
    try:
        logger.info("TC_FS_01 Step 3: Transition to the project is expected...")
        page.get_by_text("Project1", exact=True).click()
    except Exception as e:
        logger.info(f"TC_FS_01 Step 3: Failed. Error: {e}")
        pytest.fail("Unable to navigate to the project.")

# 4. Click on the previously created table in the left sidebar
    try:
        logger.info("TC_FS_01 Step 4: Transition to the table is expected...")
        page.get_by_text("users", exact=True).click()
    except Exception as e:
        logger.info(f"TC_FS_01 Step 4: Failed. Error: {e}")
        pytest.fail("Unable to navigate to the table.")

# 5. On the toolbar in the top right corner, click Tools (represented by an icon showing three vertical lines with horizontal sliders)
    try:
        logger.info("TC_FS_01 Step 5: Transition to the table is expected...")
        page.get_by_test_id("nc-table-tools-btn").click()
    except Exception as e:
        logger.info(f"TC_FS_01 Step 5: Failed. Error: {e}")
        pytest.fail("Unable to navigate to the tools.")

# 6. Go to Manage fields within the Structure section
    try:
        logger.info("TC_FS_01 Step 6: Transition to the Manage field section is expected...")
        page.get_by_test_id("nc-field-add-new").click()
    except Exception as e:
        logger.info(f"TC_FS_01 Step 6: Failed. Error: {e}")
        pytest.fail("Unable to navigate to the Manage field.")

# 7-8. Click New field; Name the field "Title123!@#$""%^&*()_+/*"
    try:
        logger.info("TC_FS_01 Step 7-8: A field is created, a corresponding field...")
        page.get_by_placeholder("Field name (Optional)").fill('Title123!@#$"%^&*()_+/*')
    except Exception as e:
        logger.info(f"TC_FS_01 Step 7-8: Failed. Error: {e}")
        pytest.fail("Failed to create field.")

# 9-10. Click Add description for the Default value setting; Click the Default value field and enter "1234"
    try:
        logger.info("TC_FS_01 Step 9-10: Assigned to Default value...")
        page.get_by_test_id("nc-show-default-value-btn").click()
        page.wait_for_timeout(500)
        page.locator(".nc-default-value-wrapper input").fill("1234")
    except Exception as e:
        logger.info(f"TC_FS_01 Step 9-10: Failed. Error: {e}")
        pytest.fail("Failed to assign a Default value.")

# 11-12. Click Add description; Enter a description that includes a full range of characters and English letters, and numbers for keabord and ensures the text reaches the character limit
    try:
        logger.info("TC_FS_01 Step 11-12: Description being added...")
        page.get_by_role("button", name="add description", exact=False).click()
        text_length = 5000
        all_characters = string.ascii_letters + string.digits + string.punctuation
        huge_mixed_text = ''.join(random.choices(all_characters, k=text_length))

        description_input = page.get_by_test_id("create-field-description-input")
    
        description_input.wait_for(state="visible", timeout=5000)
        description_input.fill(huge_mixed_text)
    except Exception as e:
        logger.info(f"TC_FS_01 Step 11-12: Failed. Error: {e}")
        pytest.fail("Failed to Add description.")

# 13. Click Save changes
    try:
        logger.info("TC_FS_01 Step 13: Saving result...")
        save_btn = page.get_by_role("button", name="Save changes")
        expect(save_btn).to_be_visible()
        save_btn.click()
        logger.info("TC_FS_01 Step 13: Result saved")
    except Exception as e:
        logger.info(f"TC_FS_01 Step 13: Failed. Error: {e}")
        pytest.fail("Save failed.")