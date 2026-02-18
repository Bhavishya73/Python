📥 Data Fetcher with Progress Bar (JSON & HTML)

A Python tool that fetches data from a URL, displays a real-time progress bar while downloading, and automatically saves the content as either:

📄 JSON file (if API response is JSON)

🌐 HTML file (if webpage response is HTML)

🚀 Features

✅ Real-time download progress bar (using tqdm)

✅ Automatically detects JSON or HTML

✅ Appends JSON responses into a single file

✅ Saves HTML pages neatly formatted

✅ Handles large responses safely

✅ Clean and beginner-friendly code

📦 Requirements

Install required libraries:

pip install requests tqdm beautifulsoup4

🧠 How It Works

Sends a request to the given URL

Streams the response in chunks

Displays progress bar while downloading

Detects content type:

If JSON → saves to data.json

If HTML → saves to index.html

🧪 Example Usage
extract_data("https://randomuser.me/api/")

📂 Output Files
File Name	Description
data.json	Stores all fetched JSON responses
index.html	Stores HTML content of webpage
🛠 Future Improvements

⏳ Time remaining estimate

📊 Multi-URL batch downloader

🔁 Retry on failed requests

📁 Custom output directory

📤 Convert JSON → Excel

👨‍💻 Author

Bhavishya
Python Developer | Data & API Tools

⭐ Support

If you like this project, don’t forget to:
⭐ Star the repository
🍴 Fork it
🛠 Contribute
