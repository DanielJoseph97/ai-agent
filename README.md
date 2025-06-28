# AI Coding Agent

A Python-based AI coding agent that can analyze, debug, and improve codebases using Google's Gemini API. This project demonstrates how to build an 
intelligent assistant that can interact with your code through function calling and provide meaningful suggestions for improvements. 

*Note*: I have used Gemini, but any LLM that provides an API key and free tier can be used.

## Features

- **Code Analysis**: Automatically analyzes Python files and identifies potential issues
- **Bug Detection & Fixes**: Identifies bugs and provides detailed explanations and solutions
- **Code Refactoring**: Suggests improvements for code structure and readability
- **Interactive Debugging**: Engages in conversation about code issues and solutions
- **File System Integration**: Can read and analyze multiple files in a project
- **Function Calling**: Uses Gemini's function calling capabilities to interact with your codebase

## Prerequisites

- Python 3+
- Google AI Studio API key (Gemini)
- Git (for version control)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DanielJoseph97/ai-agent.git
cd your-repo-name
```
2. Install required dependencies:
```bash
pip install -r requirements.txt
```
3. Set up your environment variables:
```bash
export GEMINI_API_KEY="your-api-key-here"
```
Or create a ``.env`` file:
```bash
GEMINI_API_KEY=your-api-key-here
```
# Basic Usage
Run the agent on your codebase:
```bash
python3 main.py "enter your prompt within a string like so"
```
The agent can:
1. Scan, read and give you information about your project files (all done through various function calls)
2. Analyze code within a file and fix errors/bugs or potential issues
3. Provide interactive feedback and suggestions
4. Offer to make improvements or fixes

## Example Interactions
```
User: python3 main.py "can you fix the error in ...:"
Agent: I've analyzed your code and found a potential bug in main.py line 15...
User: Can you explain what's wrong?
Agent: The variable 'count' is used before being initialized...
User: How should I fix it?
Agent: You should initialize 'count = 0' before the loop...
```

## Configuration
You can customize the agent's behavior by modifying the configuration in `config.py`:

`MAX_FILES`: Maximum number of files to analyze
`SUPPORTED_EXTENSIONS`: File types to include in analysis
`MODEL_NAME`: Gemini model to use (default: gemini-pro)

## Project Structure
        ├── main.py              # Main agent script
        ├── requirements.txt     # Configuration settings
        ├── functions/
        |   ├── get_files_info.py
            ├── function_caller.py
            ├── get_file_content.py
            ├── run_python_file.py
            ├── write_file.py
        │   ├── file_reader.py   # File system utilities
        │   └── code_analyzer.py # Code analysis functions
        ├── requirements.txt     # Python dependencies
        ├── .env.example        # Environment variables template
        └── README.md           # This file

## Safety & Security
⚠️ **Important Security Notice**: This agent has access to read files in your project directory. Always:

- Review suggested changes before applying them
- Commit your work before running the agent
- Don't run on sensitive codebases without proper precautions
- Be cautious about giving AI tools filesystem access

## Contributing
I'm quite new to Git, Python and working with a CLI. This mini-project was part of the Boot.Dev course.
Expect some errors or functionality missing. New features will be considered as work in progress. Feel free to add or fix any part of the project!

- Fork the repository
- Create a feature branch (git checkout -b feature/amazing-feature)
- Commit your changes (git commit -m 'Add amazing feature')
- Push to the branch (git push origin feature/amazing-feature)
- Open a Pull Request

## Extending the Project
This agent can be extended to:

- Support additional programming languages
- Integrate with different LLM providers (OpenAI, Anthropic, etc.)
- Add more sophisticated code analysis tools
- Implement automated testing capabilities
- Create web interface for easier interaction


## Acknowledgments
Built as part of the [Boot.Dev](https://www.boot.dev/courses/build-ai-agent-python) Python course
Uses Google's Gemini API for AI capabilities
Inspired by tools like Cursor AI and Claude Code

## Troubleshooting
**Common Issues**
- API Key Error: Make sure your Gemini API key is properly set in environment variables.
- File Permission Error: Ensure the agent has read permissions for your project directory.
- Rate Limiting: If you hit API limits, the agent will pause and retry automatically.

## Changelog
**v1.0**
- Initial release
- Basic code analysis and bug detection
- Interactive debugging capabilities
- File system integration

**Disclaimer**: This is an educational project and should be used responsibly. Always review AI-generated code suggestions before implementing them in production environments.
