# Documentation

## HTML Files

1. **Upload File Form (HTML + Bootstrap Styling):**
   - This page provides a form that allows users to upload either a CSV or XLSX file. The form includes a file input field and a submit button, styled using Bootstrap.

2. **Display Uploaded File Data (HTML + Bootstrap Styling):**
   - Once the file is successfully uploaded, this page will display the file's contents (with headings), styled using Bootstrap.

## Endpoint

- **Live URL:** [https://rehansemri.pythonanywhere.com/](https://rehansemri.pythonanywhere.com/)
  - Handles both GET and POST requests.

### 1. GET Request
   - Serves the upload form, allowing the user to select and submit a file for upload.

### 2. POST Request
   - Receives the uploaded file.
   - Validates the file type:
     - If the file is a CSV or XLSX, it reads the data using Pandas and sends the file's contents (with headers) to be displayed on the second HTML page.
     - If the file type is neither CSV nor XLSX, an error message is shown, and the upload form is re-rendered for the user to try again.
