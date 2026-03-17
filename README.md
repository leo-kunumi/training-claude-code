# Claude Code Training


## Environment configuration

### Linux


Check if Python is already installed: `python3 --version`

Create virtual environment and install the libraries. You can use Visual Studio terminal or PowerShell.

- Create a virtual environment: `python3 -m venv .venv`
- Activate the virtual environment: `source .venv/bin/activate`
- Install the requirements: `pip install -r requirements.txt`

## ToDos

- Ask Claude Code for help [ask Claude Code for help](https://code.claude.com/docs/en/how-claude-code-works#ask-claude-code-for-help)
- Built-in commands also guide you through setup:
  - `/init` walks you through creating a CLAUDE.md for your project
  - `/agents` helps you configure custom subagents
  - `/doctor` diagnoses common issues with your installation
- [Explore before implementing](https://code.claude.com/docs/en/how-claude-code-works#explore-before-implementing)
- [Give Claude something to verify agains](https://code.claude.com/docs/en/how-claude-code-works#give-claude-something-to-verify-against)
- Read "Prompting best practices"

## Links

- [Claude code homepage](https://claude.com/product/claude-code)
- [Claude code documentation](https://code.claude.com/docs/en/overview)

## Tutorials

- [Get started with Python](https://platform.claude.com/docs/en/get-started#python)
- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
- [anthropic api fundamentals](https://github.com/anthropics/courses/tree/master/anthropic_api_fundamentals)
- [Anthropic's Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [GitHub Spec Kit Tutorial with Claude Code: The End of Vibe Coding?](https://youtu.be/-9obEHJkQc8)
- [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

# Github

Set local user for a single, specific repository (Local Setting). If you want to use a different name or email address for a specific project, navigate to that repository's directory in the terminal and run the commands without the --global flag: 

```bash
cd name-of-your-repository
git config user.name "A Different Name"
git config user.email "another_email@example.com"
```