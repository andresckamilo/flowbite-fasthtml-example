# FastHTML with Tailwind CSS and Flowbite

This project demonstrates how to set up a FastHTML application with Tailwind CSS and Flowbite, creating a modern and responsive web application using Python.

## Requirements

- Python 3.7+
- Node.js and npm

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fasthtml-tailwind-flowbite.git
   cd fasthtml-tailwind-flowbite
   ```

2. Install Python dependencies:
   ```
   pip install fasthtml
   ```

3. Install Node.js dependencies:
   ```
   npm install
   ```

## Project Structure

```
fasthtml-tailwind-flowbite/
├── src/
│   ├── app.py
│   ├── components.py
│   └── styles/
│       └── main.css
├── static/
│   └── dist/
│       └── css/
│           └── output.css
├── tailwind.config.js
├── package.json
└── README.md
```

## Configuration

### 1. Set up FastHTML (app.py)

Create `src/app.py` with the following content:

```python
from dataclasses import dataclass

from fasthtml.common import *
from fasthtml.core import FastHTML
from starlette.staticfiles import StaticFiles
from components import hero_section

app = FastHTMLWithLiveReload(
    hdrs=(Link(rel="stylesheet", href="/static/dist/css/output.css"),)
)
app.mount("/static", StaticFiles(directory="../static"), name="static")

rt: app.route = app.route

@rt("/", methods=["GET"])
async def index():
    return hero_section()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
```

### 2. Create components (components.py)

Create `src/components.py` and define your components, such as the `hero_section()`.

### 3. Configure Tailwind CSS

Create `tailwind.config.js` in the project root:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.py", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin")
  ],
}
```

### 4. Set up your CSS

Create `src/styles/main.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 5. Compile Tailwind CSS

Run the following command to compile and watch for changes:

```
npx tailwindcss -i ./src/styles/main.css -o ./static/dist/css/output.css --watch
```

## Running the Application

1. In one terminal, run the Tailwind CSS compiler:
   ```
   npx tailwindcss -i ./src/styles/main.css -o ./static/dist/css/output.css --watch
   ```

2. In another terminal, start the FastHTML application:
   ```
   python src/app.py
   ```

3. Open your browser and visit `http://localhost:8080`

## Adding Flowbite Components

You can now use Flowbite components in your FastHTML application. Refer to the Flowbite documentation for available components and add them to your `components.py` file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

