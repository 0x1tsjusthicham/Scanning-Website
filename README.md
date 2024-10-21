# Vulnerability Scanner

## Description

This project consists of a web vulnerability scanner that can identify potential XSS (Cross-Site Scripting) vulnerabilities in web applications by testing forms and URLs. It has two main files:

- `scanner.py`: Contains the `Scanner` class that handles the crawling, form submission, and XSS testing.
- `vulnerability_scanner.py`: Uses the `Scanner` class to run the scanner on a target website.

## How to Use

1. **Setup**

   Ensure you have Python and the required libraries installed:

   ```bash
   pip install requests beautifulsoup4
   ```

2. **Modify Target URL**

   Edit the `vulnerability_scanner.py` file to specify the `target_url`:

   ```python
   target_url = "website.com"
   data_dict = {"username": 'admin', "password": "password", "Login": "submit"}
   ```

   If the website requires authentication, adjust the `data_dict` accordingly.

3. **Block Links**

   If there are links you want the scanner to avoid, specify them in the `block_links` list:

   ```python
   block_links = ["website.com/logout"]
   ```

4. **Run the Scanner**

   Execute the `vulnerability_scanner.py` script:

   ```bash
   python vulnerability_scanner.py
   ```

   The scanner will start crawling the target website and test forms and links for XSS vulnerabilities.

## Features

- **Crawling**: Automatically extracts and visits all links within the target domain.
- **Form Testing**: Tests all forms found on the web pages for XSS vulnerabilities.
- **Link Testing**: Tests links containing query parameters for potential XSS vulnerabilities.
- **Session Management**: Uses sessions for websites that require login before scanning.

## Example Output

The output will display links and forms that are tested, and will highlight any vulnerabilities detected:

```
[+] Testing form in http://example.com/search
[*******] XSS found in link http://example.com/search in the following form
<form>...</form>
```

## Disclaimer

This tool is for educational purposes only. Use it on websites that you own or have permission to test. The author is not responsible for any misuse or damage caused by this tool.

# 0x1tsjusthicham
