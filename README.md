# WordPress Transaction Automation 🤖

A Selenium-based Python script that automates bulk transaction creation on a WordPress site using a CSV file of email addresses.

---

## What it does

Reads a list of email addresses from a CSV file and automatically creates a **completed transaction** for each one on a WordPress admin page. The user logs in manually first, then the script handles the rest automatically.

---

## Requirements

- Python 3.x
- Google Chrome + ChromeDriver
- WordPress admin access

### Install dependencies

```bash
pip install selenium
```

---

## Configuration

Before running, set these two variables at the top of the script:

```python
CSV_FILE = 'your_file.csv'   # Path to your CSV file
BASE_URL = "https://..."     # URL of the WordPress transaction page
```

### CSV format

One email address per row, no header needed:

```
user1@example.com
user2@example.com
user3@example.com
```

---

## Usage

```bash
python transaction.py
```

1. The browser will open and navigate to the WordPress page
2. **Log in manually** to WordPress
3. Navigate to the **"Nová transakce"** (New Transaction) page
4. Press **Enter** in the terminal
5. The script will process all emails automatically

---

## Output

The script prints a status message for each row:

```
✅ Úspěšně zpracováno: user1@example.com
❌ Chyba u e-mailu user2@example.com: <error details>
```

---

## ⚠️ Security Notes

- **Never commit your CSV file to GitHub** — it contains sensitive user data
- Make sure `*.csv` is listed in your `.gitignore`

---

## License

MIT
