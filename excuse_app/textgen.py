import random
import torch
import torch.nn.functional as F
from transformers import GPT2Tokenizer, GPT2LMHeadModel

class TextGenerator:
    def __init__(self, model_name='gpt2', temperature = 0.8, use_gpu=False):
        """
        Model names come from the keys in GPT2_PRETRAINED_CONFIG_ARCHIVE_MAP.
            "gpt2"
            "gpt2-medium"
            "gpt2-large"
            "gpt2-xl"
            "distilgpt2"
        """
        self.use_gpu = use_gpu
        # Load pre-trained model tokenizer (vocabulary)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        # Load pre-trained model (weights)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        # Temperature adds fun, chaos, and unpredictability.
        self.temperature = temperature

        # Set the model in evaluation mode to deactivate the DropOut modules
        # This is IMPORTANT to have reproducible results during evaluation!
        self.model.eval()
        # If you have a GPU, put everything on cuda
        if self.use_gpu:
            self.model.to('cuda')
    
    def generate_word(self, start_text):
        """
        Generate one word (or sub-word, sometimes) to add onto some start text.
        The generated word will contain a leader space if appropriate.
        """
        # Encode text inputs
        indexed_tokens = self.tokenizer.encode(start_text)
        # Convert indexed tokens in a PyTorch tensor
        tokens_tensor = torch.tensor([indexed_tokens])
        # Move the tokens to the GPU.
        if self.use_gpu:
            tokens_tensor = tokens_tensor.to('cuda')
        
        # Predict all tokens
        with torch.no_grad():
            outputs = self.model(tokens_tensor)
            # Use temperature to add more chaos into the selection of words.
            next_token_logits = outputs[0][:, -1, :] / self.temperature   # <--- Temperature
            next_token = torch.multinomial(F.softmax(next_token_logits, dim=-1), num_samples=1) # <-- Temperature

        # get the predicted next sub-word.
        generated_word = self.tokenizer.decode(next_token)
        return generated_word
    
    def generate_sentence(self, start_text, sentence_count=1, up_to_count = None, on_word_generated=None):
        """
        @param start_text The text generated will continue from this starting text.
        @param sentence_count The exact number of sentences to generate. Alternatively, you can use up_to_count.
        @param up_to_count If up_to_count is specified then between 1 and up_to_count sentences will be generated.
        @param on_word_generated An optional callback function that will be called for each word generated.
        """
        if up_to_count:
            sentence_count = random.randint(1, up_to_count)
        text = start_text
        sentence = ''
        reached_end = False
        for _ in range(sentence_count):
            while (not reached_end):
                word = self.generate_word(text)
                # Sometimes it generates token <|endoftext|> and then starts doing a newscast or something.
                if 'endoftext' in word:
                    reached_end = True
                    break
                if on_word_generated:
                    on_word_generated(word)                    
                text += word
                sentence += word
                if '.' in word:
                    break
        return sentence
