import os
from pathlib import Path
from playwright.sync_api import Page, expect
from pages.demo_page import DemoAppPage


def test_file_upload(page: Page, tmp_path: Path):
    """Example 1: Uploading a file and asserting upload status."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Create a temporary file to upload
    sample_file = tmp_path / "test_doc.txt"
    sample_file.write_text("Playwright file upload test content")

    # Upload file
    demo_page.file_uploader.set_input_files(str(sample_file))

    # Assert that UI reflects uploaded file name
    expect(demo_page.upload_status).to_have_text("Uploaded: test_doc.txt")


def test_file_download(page: Page, tmp_path: Path):
    """Example 2: Triggering file download and asserting downloaded file."""
    demo_page = DemoAppPage(page)
    demo_page.load()

    # Wait for download event when clicking download link
    with page.expect_download() as download_info:
        demo_page.download_link.click()

    download = download_info.value

    # Assert suggested filename
    assert download.suggested_filename == "sample_report.txt"

    # Save to disk and assert file existence
    save_path = tmp_path / download.suggested_filename
    download.save_as(str(save_path))
    assert save_path.exists()
