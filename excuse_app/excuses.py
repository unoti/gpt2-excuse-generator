import random

BlameModeMe = {
    '[my]': 'my',
    '[I]': 'I',
    '[me]': 'me'
}

BlameModeYou = {
    '[my]': 'your',
    '[I]': 'you',
    '[me]': 'you'
}

BlameModeTeam = {
    '[my]': 'our',
    '[I]': 'we',
    '[me]': 'us'
}

BlameModeTeamBlameShift = {
    '[my]': 'their',
    '[I]': 'they',
    '[me]': 'them'
}

INTRO_TEXT = [
    '[my] assignment was to',
    '[I] was supposed to',
    '[I] intended to',
    '[my] goal was to',
    '[my] dream, [my] destiny was to',
    '[I] had every intention to'
]

HOWEVER_TEXT = [
    "Sadly, that didn't work out because",
    "Unfortunately, the problem with that was",
    "[I] couldn't do that because",
]

TASK_INTRO = [
    'Things were going pretty well until [I] got to the part where [I] needed to',
    '[I] hit a serious problem when [I] started to',
    '[I] hit a major roadblock when [I] began to',
    'It was going fine until [I] went to',
    'Things were going smoothly, but the problems started when I began to',
]

TASK_TRANSITION = [
    'The problem was',
    'What stopped [me] dead',
    'Where [I] ran into a roadblock was',
    "[I] couldn't finish this because",
    "[I] was unable to start this because",
    "[I] wanted to do this, but I couldn't because",
    "[I] started on that, but couldn't finish because",
]

EMOTION_TURNAROUND = [
    '[I] feel pretty sad about this because',
    "[I] hope you're not too disappointed and",
    "On the bright side,",
    "We shouldn't worry about it because",
    "But the real problem to focus on here is",
    "[I] am concerned about this because"
]

class ExcuseSituation:
    def __init__(self, text_generator, assignment, tasks=[], is_team=False, blame_others=False, word_callback=None):
        self.excuses = [] # List of excuses we'll build up.
        self.excuse = None # The current excuse we're working on.
        self.word_callback = word_callback
        self.assignment = assignment
        self.tasks = tasks
        self.generator = text_generator
        if is_team:
            if blame_others:
                mode = BlameModeTeamBlameShift
            else:
                mode = BlameModeTeam
        else:
            if blame_others:
                mode = BlameModeYou
            else:
                mode = BlameModeMe
        self.blame_mode = mode
    
    def _out_start_excuse(self):
        """Start the output of a new excuse."""
        self.excuse = ''

    def _out_end_excuse(self):
        """Finish the output of an excuse."""
        self.excuses.append(self.excuse)

    def _out_add(self, text):
        """Add one or more words onto the end of the current excuse."""
        if self.excuse.endswith('.') and text[0] != ' ':
            text = ' ' + text
        text = self._substitute_pronouns(text)
        # If we're starting a new sentence then capitalize.
        if self.excuse == '' or self.excuse.endswith('.'):
            text = text[0].upper() + text[1:]
        if self.word_callback:
            self.word_callback(text)
        self.excuse += text
    
    def _out_choice(self, choices, end_sentence=False):
        """Add one of a random selection of choices to the current excuse."""
        choice = random.choice(choices)
        if end_sentence:
            choice += '.'
        else:
            choice += ' '
        self._out_add(choice)
    
    def generate_excuse(self):
        self._out_start_excuse()
        if random.random() < 0.5 or not self.tasks:
            self.generate_excuse_whole()
        else:
            self.generate_excuse_task()
        if random.random() < 0.5:
            self._out_add(random.choice(EMOTION_TURNAROUND))
            self.generator.generate_sentence(self.excuse, on_word_generated=self._out_add)
        self._out_end_excuse()
        return self.excuse
        
    def generate_excuse_task(self):
        self._out_choice(INTRO_TEXT)
        self._out_add(self.assignment + '.')
        self._out_choice(TASK_INTRO)
        self._out_choice(self.tasks, end_sentence=True)
        self._out_choice(TASK_TRANSITION)
        self.generator.generate_sentence(self.excuse, up_to_count=3, on_word_generated=self._out_add)
        return self.excuse
        
    def generate_excuse_whole(self):
        self._out_choice(INTRO_TEXT)
        self._out_add(self.assignment + '.')
        self._out_choice(HOWEVER_TEXT)
        self.generator.generate_sentence(self.excuse, on_word_generated=self._out_add)

    def generate_excuses(self, count=5):
        for _ in range(count):
            self.generate_excuse()
        return self.excuses
    
    def _substitute_pronouns(self, text):
        for pronoun_from, pronoun_to in self.blame_mode.items():
            text = text.replace(pronoun_from, pronoun_to)
        return text
        