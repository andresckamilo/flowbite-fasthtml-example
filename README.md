# Flowbite FastHTML Example

This repository serves as a guide and example for integrating FastHTML with Tailwind CSS and Flowbite, using the hero section as an example.

## Part 1: Running the Example

### Requirements

- Python 3.7+
- Node.js and npm

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/andresckamilo/flowbite-fasthtml-example.git
   cd flowbite-fasthtml-example
   ```

2. Install Python dependencies:
   ```
   pip install python-fasthtml
   ```

3. Install Node.js dependencies:
   ```
   npm install
   ```

### Running the Application

1. In one terminal, compile Tailwind CSS:
   ```
   npx tailwindcss -i ./src/styles/main.css -o ./static/dist/css/output.css --watch
   ```

2. In another terminal, start the FastHTML application:
   ```
   uvicorn src.app:app --reload
   ```

3. Open your browser and visit `http://localhost:8000`

## Part 2: Setting Up Your Own Project

This section guides you through setting up a similar project from scratch.

### 1. Create Project Structure

```
mkdir fasthtml-tailwind-flowbite
cd fasthtml-tailwind-flowbite
mkdir -p src/styles static/dist/css
```

### 2. Install Dependencies

```
pip install python-fasthtml
npm init -y
npm install -D tailwindcss flowbite
```

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

### 4. Set Up CSS

Create `src/styles/main.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 5. Create FastHTML Application

Create `src/app.py`:

```python
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
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```

### 6. Create Components

Create `src/components.py` and add your components.

### 7. Run Your Application

Follow the same steps as in Part 1 to run your application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
