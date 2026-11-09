# Task 3: Web Scraper for News Headlines

## Project Overview
This project is part of my Python Developer Internship. The objective is to scrape news headlines from [The Hacker News](https://thehackernews.com/) using Python.

The scraper fetches the website's HTML content, parses it using BeautifulSoup, extracts all `<h2>` elements, and saves their text into a `.txt` file.

## Technologies Used
- **Python** – Programming language
- **Requests** – To fetch HTML content from the website
- **BeautifulSoup** – To parse HTML and extract headlines
- **OS** – To set the working directory

## Project Structure

```text
PyDev_Task_3/
│
├── scraper.py
├── myfile.txt
└── README.md
```

## How It Works

1. Import the required Python libraries.
2. Set the project working directory using the OS module.
3. Send an HTTP GET request to The Hacker News website using Requests.
4. Parse the received HTML content using BeautifulSoup.
5. Find all `<h2>` elements containing the target text.
6. Extract and clean the headline text using `.text.strip()`.
7. Save the extracted headlines into `myfile.txt`, with each headline on a separate line.

## Installation

Install the required external libraries:

```bash
pip install requests beautifulsoup4
```

## How to Run

Run the Python scraper:

```bash
python scraper.py
```

## Output

The extracted headlines are saved in `myfile.txt`.

Each headline is stored on a separate line. The file is opened in write mode, so its previous contents are overwritten when the script runs again.

## Learning Outcomes

- Understanding HTTP GET requests.
- Fetching HTML content using Requests.
- Parsing HTML using BeautifulSoup.
- Extracting HTML elements using `find_all()`.
- Understanding text extraction and whitespace cleaning.
- Writing scraped data into a text file using Python file handling.

## Author
**Parth Nilesh Kabade**

Python Developer Internship – Task 3
