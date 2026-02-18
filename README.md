# Claude Code Training

## Notes

### Models

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

### Tokens

Most Large Language Models don't "think" in full words, but instead work with a series of word-fragments called tokens. Tokens are the small building blocks of a text sequence that Claude processes, understands, and generates texts with. When we provide a prompt to Claude, that prompt is first turned into tokens and passed to the model. The model then begins generating its output one token at a time.

For Claude, a token approximately represents 3.5 English characters, though the exact number can vary depending on the language used.

The `max_tokens parameter` allows us to set an upper limit on how many tokens Claude generates for us. As an illustration, suppose we ask Claude to write us a poem and set max_tokens to 10. Claude will start generating tokens for us and immediately stop as soon as it hits 10 tokens. This will often lead to truncated or incomplete outputs. 
We can also check the `stop_reason` property on the response Message object to see WHY the model stopped generating. In this case, we can see that it has a value of "max_tokens" which tells us the model stopped generating because it hit our max token limit!

If we ask the same task with max_tokens equals to 500, the poem will be generated, and the stop_reason may be `end_turn`, which is the model's way of telling us that it naturally finished generating. It wrote us a poem and had nothing else to say, so it stopped!

Changing max_tokens won't alter how Claude generates the output, it just gives the model room to keep generating (with a high max_tokens value) or truncates the output (with a low max_tokens value).

It's important to note that the models don't "know" about max_tokens when generating content. Changing max_tokens won't alter how Claude generates the output, it just gives the model room to keep generating (with a high max_tokens value) or truncates the output (with a low max_tokens value).

It's also important to know that increasing max_tokens does not ensure that Claude actually generates a specific number of tokens. If we ask Claude to write a joke and set max_tokens to 1000, we'll almost certainly get a response that is much shorter than 1000 tokens.

Understanding tokens is crucial when working with Claude, particularly for the following reasons:

- API limits: The number of tokens in your input text and the generated response count towards the API usage limits. Each API request has a maximum limit on the number of tokens it can process. Being aware of tokens helps you stay within the API limits and manage your usage efficiently.
- Performance: The number of tokens Claude generates directly impacts the processing time and memory usage of the API. Longer input texts and higher max_tokens values require more computational resources. Understanding tokens helps you optimize your API requests for better performance.
- Response quality: Setting an appropriate max_tokens value ensures that the generated response is of sufficient length and contains the necessary information. If the max_tokens value is too low, the response may be truncated or incomplete. Experimenting with different max_tokens values can help you find the optimal balance for your specific use case.

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