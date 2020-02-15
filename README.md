# Transformers and Text Generation using GPT2
We'll look at using the huggingface *transformers* library to generate text and perform some other natural language processing tasks.

The culmination of this NLP extravaganza will be a versitile, tireless, endlessly creative **Excuse Generator** powered by Artificial Intelligence.

```python
goal = 'write a better summary for this document'
tasks = ['contemplate the most important ideas', 'determine the most efficient way to summarize the ideas',
	 'summarize ways to apply to industry', 'discuss next steps']
s = ExcuseSituation(gen, assignment=goal, tasks=tasks, is_team=False, blame_others=False)
s.generate_excuses(count=1)
```

> I was supposed to write a better summary for this document.
> Things were going smoothly, but the problems started when I began to contemplate the most important ideas.
> I wanted to do this, but I couldn't because I would have to spend hours writing down all the details. 
-- The Excuse Generator
