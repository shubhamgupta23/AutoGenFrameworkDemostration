# AutoGen Framework

## Prerequisites

-   **Python:** 3.10 or later (recommended: 3.11)
-   **Node.js:** 18.x or later (recommended: 20 LTS)

## Dependencies

Install the required packages:

``` bash
pip install -U "autogen-agentchat"
pip install "autogen-ext[openai]"
pip install -U "autogen-ext[mcp]"
pip install python-dotenv
```

## Installation Steps

### 1. Create a virtual environment

``` bash
python -m venv .venv
```

Activate it:

**Windows**

``` bash
.venv\Scripts\activate
```

**Linux/macOS**

``` bash
source .venv/bin/activate
```

### 2. Upgrade pip

``` bash
python -m pip install --upgrade pip
```

### 3. Install dependencies

``` bash
pip install -U "autogen-agentchat"
pip install "autogen-ext[openai]"
pip install -U "autogen-ext[mcp]"
pip install python-dotenv
```

``` OR 
pip install -r requirements.txt
```

### 4. Create a `.env` file

``` env
OPENAI_API_KEY=your_api_key_here
```

### 5. Verify installation

``` bash
python -c "import autogen_agentchat; print('AutoGen installed successfully!')"
```

## Project Structure

``` text
project/
├── .env
├── README.md
├── requirements.txt
└── src/
```

## Author

**Shubham Gupta**

Senior SDET | Automation Engineer | AI Testing Enthusiast
