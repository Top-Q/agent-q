# **Agent Q: AI-Powered Test Automation**  

## **📌 Description**  
**Agent Q** is an **AI-powered test automation agent** that seamlessly integrates with your **Python workflow** to perform tasks on a **system under test**.  

By leveraging **LLMs such as GPT**, Agent Q extends their capabilities beyond text-based reasoning, allowing them to **interact with and manipulate the real world** through structured Python code execution. It effectively **adds eyes to the LLM brain**—enabling it to observe environments—and **hands that can perform actions**, making AI more practical and actionable.  

It currently supports **UI testing with Playwright** and **local file system operations** such as **finding and reading files**, but it is **designed to be extendable**, allowing additional tools and capabilities to be integrated.  

The package includes two agents:
- **WebAgent**: Handles Web UI operations using Playwright.
- **FsAgent**: Manages local file system operations, such as searching and reading files.  

Agent Q is designed for extensibility, enabling the creation of new agents for different tasks such as **SQL, HTTP, log analysis, and more**. It not only allows you to **add new tools**, but also makes it easy to **implement custom agents** tailored to your specific needs, ensuring flexibility in automation workflows.  

### **Why Use Agent Q?**
- **Bridges the gap between AI and execution** – Transforms LLM-generated insights into real-world actions.
- **Enhances automation workflows** – Empowers LLMs to interact with web pages, local files, and more.
- **Reduces repetitive prompts** – Executes and remembers successful tasks for future reuse, minimizing unnecessary LLM calls.
- **Customizable for specialized needs** – Provides a framework to easily build your own specialized agents for unique automation scenarios.  

The agent is:

✅ **Powered by SmolAgents** – Uses a **lightweight, flexible agent framework** for AI-based test automation.  
✅ **LLM-Agnostic** – Can work with **any LLM**, including **local models**.  
✅ **Python Code-Based** – Generates **Python code** dynamically for test execution.  
✅ **Efficient & Reusable** – Saves generated code **after successful execution** and **reuses it** when the same task is requested again.  


---

## **✨ Main Features**  
✅ **Automates UI Testing** using **Playwright**.  
✅ **Generates Python Code** dynamically for test scenarios.  
✅ **Caches & Reuses Code** instead of calling an LLM repeatedly.  
✅ **LLM-Agnostic** – Works with **any language model** (GPT-4, Llama, etc.).  
✅ **Easily Extendable** – Add **new tools and capabilities** effortlessly.  

---

## **🔧 Installation & Prerequisites**  
### **📌 Prerequisites**
- Python **3.10+**  
- For web testing: Playwright (`pip install playwright`)  
- `.env` file with API key for the LLM  

### **📦 Installation**
### **📦 Installation with Pipenv**
```bash
   git clone https://github.com/top-q/agent-q.git
   cd agent-q
   pipenv install
```
**Set up Playwright:**  
```bash
   pipenv run playwright install
```

To activate the virtual environment and run commands inside it:
```bash
   pipenv shell
```


---

## **🚀 Usage Examples**  
Here are some example tests using the **WebAgent**:

```python
from src.agent.web_agent.web_agent import WebAgent
from playwright.sync_api import sync_playwright, Page

page = sync_playwright().start().chromium.launch(headless=False).new_page()
agentQ = WebAgent(page, "API_KEY")
agentQ.init_agent()

# Perform a task using AI and generate Python code
page.goto("https://test.site.com/")

# Use the agent to fill in a form 
agentQ.do("Fill the sign in form with username 'admin' and password 'admin' and click on the sign in button")

# Or generate realistic data
agentQ.do("Fill all the login page input fields with realistic data and click on the sign in button")

# To get fields values from the page
credit = agentQ.do("Get the available credit in the page")

# Count the number of elements in the page
count = agentQ.do("Count the number of transaction with state 'Complete' in the page")



```

Here are some example tests using the **FsAgent**:

```python
from src.agent.fs_agent.fs_agent import FsAgent

agentQ = FsAgent("API_KEY")
agentQ.init_agent()
# Perform a task using AI and generate Python code
result = agentQ.do("Count the number of files in the folder 'test_folder'")
assert result == 5

# Perform tasks on the local operating system
result = agentQ.do(f"Get the content of the biggest file in the folder 'test_folder'")
print(result)

result = agentQ.do(f"Count the number of files in the folder 'test_folder' and its sub folders")
assert result == 10

```

---

## **🛠️ How It Works**  
1. **Agent Q Generates Python Code**  
   - The AI generates **Python code** dynamically based on the requested task.  

2. **Code Execution in a Sandbox**  
   - The code runs in an **isolated sandbox environment** using Playwright.  

3. **Code Storage & Reuse**  
   - If execution is **successful**, the code **is saved** to a **code store**.  
   - **Future runs use the stored code** instead of calling the LLM again.  

---

## **🛠️ Extending Agent Q**  
The agent is designed to be easily extendable. You can add **new tools** by defining functions and registering them.  

**Example:** Adding a new tool for taking a screenshot.
```python
from smolagents import tool

@tool
def take_screenshot(filename: str):
    """Take a screenshot of the current page."""
    page.screenshot(path=filename)
    return f"Screenshot saved as {filename}"
```

---

## **🔍 Roadmap / Possible Enhancements**  
- ✅ **More robust assertion checks** (AI-powered page state validation).  
- ✅ **Support for API testing** (Postman-like API interaction).  
- ✅ **Better error handling & logging**.  

---

## **🤝 Contributing**  
If you’d like to contribute:  
1. **Fork the repo**  
2. **Create a new branch** (`feature-new-tool`)  
3. **Submit a pull request**  

