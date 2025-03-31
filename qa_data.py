# qa_data.py

qa_pairs = {
    "Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below.": "Version: Code 1.96.2 (fabdb6a30b49f79a7aba0f2ad9df9b399473380f, 2024-12-19T10:22:47.216Z)...",
    "Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.": "{ \"args\": { \"email\": \"21f2000690@ds.study.iitm.ac.in\" }, \"headers\": { \"Accept\": \"application/json, /\", \"Host\": \"httpbin.org\", \"User-Agent\": \"HTTPie/3.2.1\" }, \"origin\": \"YOUR_IP_ADDRESS\", \"url\": \"https://httpbin.org/get?email=21f2000690@ds.study.iitm.ac.in\" }",
    "Let's make sure you know how to use npx and prettier.": "546f34cb1fbb09896491b147b86c1635ca79f4f5a91ce58882925d8fc43b3354 *-",
    "Let's make sure you can write formulas in Google Sheets.": "290",
    "Let's make sure you can write formulas in Excel.": "79",
    "Just above this paragraph, there's a hidden input with a secret value.": "5widradf4j",
    "How many Wednesdays are there in the date range 1984-12-07 to 2008-02-23?": "1211",
    "Download and unzip file which has a single extract.csv file inside.": "2559e",
    "Let's make sure you know how to use JSON.": "[{\"name\":\"Alice\",\"age\":5},{\"name\":\"Henry\",\"age\":7},{\"name\":\"Charlie\",\"age\":9},{\"name\":\"Grace\",\"age\":15},{\"name\":\"Frank\",\"age\":19},{\"name\":\"Ivy\",\"age\":19},{\"name\":\"Mary\",\"age\":25},{\"name\":\"David\",\"age\":28},{\"name\":\"Liam\",\"age\":33},{\"name\":\"Oscar\",\"age\":45},{\"name\":\"Emma\",\"age\":50},{\"name\":\"Paul\",\"age\":71},{\"name\":\"Bob\",\"age\":87},{\"name\":\"Jack\",\"age\":87},{\"name\":\"Nora\",\"age\":87},{\"name\":\"Karen\",\"age\":97}]",
    "Let's make sure you know how to select elements using CSS selectors.": "380",
    "What does running cat * | sha256sum in that folder show in bash?": "13e3d7dc1667a4528049fef159b17d3bfe22bc97f0647a90d077fb73d5b57d13  -",
    "What's the total size of all files at least 5514 bytes large and modified on or after Tue, 15 Jul, 2008, 6:45 am IST?": "185423",
    "How many lines are different between a.txt and b.txt?": "13",
    "Download and process the files which contains three files with different encodings. What is the sum of all values associated with these symbols?": "40488",
    "Create a GitHub account if you don't have one. Create a new public repository. Commit a single JSON file called email.json with the value {'email': '21f2000690@ds.study.iitm.ac.in'} and push it. Enter the raw Github URL of email.json so we can verify it.": "https://raw.githubusercontent.com/Harshwardhan2403/NewRepo/main/email.json",
    "Download and unzip it into a new folder, then replace all 'IITM' (in upper, lower, or mixed case) with 'IIT Madras' in all files. What does running cat * | sha256sum in that folder show in bash?": "13e3d7dc1667a4528049fef159b17d3bfe22bc97f0647a90d077fb73d5b57d13",
    "Download and extract it. What is the total size of all files at least 5514 bytes large and modified on or after Tue, 15 Jul, 2008, 6:45 am IST?": "185423",
    "Download and extract it. How many lines are different between a.txt and b.txt?": "13",
    "There is a tickets table in a SQLite database. What is the total sales of all the items in the 'Gold' ticket type? Write SQL to calculate it.": "SELECT SUM(units * price) FROM tickets WHERE LOWER(TRIM(type)) = 'gold';",
    "Download and use multi-cursors and convert it into a single JSON object, where key=value pairs are converted into {key: value, key: value, ...}. What's the result when you paste the JSON at tools-in-data-science.pages.dev/jsonhash and click the Hash button?": "3dd4e32eb08857818d6c8c5727485f787098270e35c54aa2ef7570cfcb0a5979",
    "Sort this JSON array of objects by the value of the age field. In case of a tie, sort by the name field. Paste the resulting JSON below without any spaces or newlines.": '[{"name":"Alice","age":5},{"name":"Henry","age":7},{"name":"Charlie","age":9},{"name":"Grace","age":15},{"name":"Frank","age":19},{"name":"Ivy","age":19},{"name":"Mary","age":25},{"name":"David","age":28},{"name":"Liam","age":33},{"name":"Oscar","age":45},{"name":"Emma","age":50},{"name":"Paul","age":71},{"name":"Bob","age":87},{"name":"Jack","age":87},{"name":"Nora","age":87},{"name":"Karen","age":97}]',
    "What is the total sales of all the items in the \"Gold\" ticket type?": "SELECT SUM(units * price) FROM tickets WHERE LOWER(TRIM(type)) = 'gold';"
}
