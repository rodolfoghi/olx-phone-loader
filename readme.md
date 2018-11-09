# OLX Phone Loader

A web scraper to get data from [OLX](https://www.olx.com.br/) ads.

# How use

1. Clone or download this repository.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Install [Tesseract](https://github.com/tesseract-ocr/tesseract), instructions [here](https://github.com/tesseract-ocr/tesseract/wiki).
4. Set the value of variable `ocr.pytesseract.tesseract_cmd` on `converter.py`.
5. Set the value of variable `url = ""` on `app.py` file. Example: `url = "https://sp.olx.com.br/?q=super+m%C3%A1rio"`.
6. Run `python app.py` on your prefered terminal.

# How it works

1. Made request to url using `urllib.request` to get the list of ads.
2. Parsed html reponse using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).
3. Made a new request for each ad.
4. Search for phone in response. The phone is a GIF file. :(
5. Save the gif file on images folder.
6. Converts the gif to png and save it.
7. Reads phone text from image using [`pytesseract`](https://pypi.org/project/pytesseract/).
8. Lastly, save the data on csv file using the [`csv`](https://docs.python.org/3/library/csv.html) Python lib.