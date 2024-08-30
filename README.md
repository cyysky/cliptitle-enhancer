# ClipTitle Enhancer
A Python package that monitors your clipboard for URLs and automatically adds their titles.

![ClipTitle Enhancer Logo](https://github.com/cyysky/cliptitle-enhancer/raw/main/cliptitle_enhancer.png)

**ClipTitle Enhancer** is a clipboard monitoring tool designed to enhance your URL copying experience. Whenever a URL is copied to the clipboard, ClipTitle Enhancer automatically appends the page's title, making it easy to identify the content of the link without having to open it.

## Features
- **Automatic Title Fetching:** Automatically fetches and appends the title of URLs copied to the clipboard.
- **Supports Various Title Sources:** Retrieves the title from Open Graph meta tags, `<h1>` tags, or the page `<title>`.
- **System Tray Integration:** Runs in the background with a convenient system tray icon, allowing you to pause and resume monitoring easily.
- **Notifications:** Notifies you when a title has been successfully added to a URL in the clipboard.
- **Customizable Pause/Resume:** Easily pause or resume clipboard monitoring through the system tray menu.


## Installation

```
pip install cliptitle
```

## Usage

To run from command line:

```
cliptitle
```

To use in a Python script:

```python
from cliptitle import ClipTitleEnhancer

cliptitle = ClipTitleEnhancer()
cliptitle.start()
```

## Development
1. Clone the repository:
   ```bash
   git clone https://github.com/cyysky/cliptitle-enhancer.git


## License

This project is licensed under the MIT License - see the LICENSE file for details.

# LICENSE
MIT License

Copyright 2024 FMCV

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.