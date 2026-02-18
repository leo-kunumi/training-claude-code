# Claude Code Training

## Environment configuration

### Linux


Check if Python is already installed: `python3 --version`

Create virtual environment and install the libraries. You can use Visual Studio terminal or PowerShell.

- Create a virtual environment: `python3 -m venv .venv`
- Activate the virtual environment: `source .venv/bin/activate`
- Install the requirements: `pip install -r requirements.txt`

## Models

When choosing a model, there a few important factors to consider:

- The model's latency (how fast is it?)
- The model's capabilities (how smart is it?)
- The model's cost (how expensive is it?)

The [model comparison table](https://platform.claude.com/docs/en/about-claude/models/overview#model-comparison-table) presents the key features and capabilities of each model in the Claude family.

The logical question is: which model should you use? 

It's a difficult question to answer without knowing the specific tasks and demands of a given application. The choice of model can significantly impact the performance, user experience, and cost-effectiveness of your application:

- Capabilities
  - The first and foremost consideration is whether the model possesses the necessary capabilities to handle the tasks and use cases specific to your application. Different models have varying levels of performance across different domains, such as general language understanding, task-specific knowledge, reasoning abilities, and generation quality. It's essential to align the model's strengths with the demands of your application to ensure optimal results.
- Speed
  - The speed at which a model can process and generate responses is another critical factor, particularly for applications that require real-time or near-real-time interactions. Faster models can provide a more responsive and seamless user experience, reducing latency and improving overall usability. However, it's important to strike a balance between speed and model capabilities, as the fastest model may not always be the most suitable for your specific needs.
- Cost
  - The cost associated with using a particular model is a practical consideration that can impact the viability and scalability of your application. Models with higher capabilities often come with a higher price tag, both in terms of API usage costs and computational resources required. It's crucial to assess the cost implications of different models and determine the most cost-effective option that still meets your application's requirements.

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