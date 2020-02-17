import random

class BlameModeMe:
    my = 'my'
    i = 'I'
    me = 'me'

class BlameModeYou:
    my = 'your'
    i = 'you'
    me = 'you'

class BlameModeTeam:
    my = 'our'
    i = 'we'
    me = 'us'

class BlameModeTeamBlameShift:
    my = 'their'
    i = 'they'
    me = 'them'

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
    "Unfortunately, there was a serious problem with that",
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
    def __init__(self, text_generator, assignment, tasks=[], is_team=False, blame_others=False):
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
        self.mode = mode
    
    def generate_excuse(self):
        if random.random() < 0.5 or not self.tasks:
            text = self.generate_excuse_whole()
        else:
            text = self.generate_excuse_task()
        if random.random() < 0.5:
            text += random.choice(EMOTION_TURNAROUND)
            more = self.generator.generate_sentence(text)
            text = self._list_to_text([text, more])
        return text
        
    def generate_excuse_task(self):
        background = [random.choice(INTRO_TEXT), self.assignment, '.']
        background += [random.choice(TASK_INTRO), random.choice(self.tasks), '.']
        background += [random.choice(TASK_TRANSITION)]
        background_text = self._list_to_text(background)
        text = self.generator.generate_sentence(background_text, up_to_count=3)
        return self._prep_result(background_text + text)
        
    def generate_excuse_whole(self):
        # Lead-in text, setting up the situation.
        background = [random.choice(INTRO_TEXT), self.assignment, '.']
        background += [random.choice(HOWEVER_TEXT)]
        
        background_text = self._list_to_text(background)
        text = self.generator.generate_sentence(background_text)
        return self._prep_result(background_text + text)

    def generate_excuses(self, count=5):
        result = []
        for _ in range(count):
            result.append(self.generate_excuse())
        return result
            
    def _list_to_text(self, chunk_list):
        words = []
        for entry in chunk_list:
            entry = entry.replace('[I]', self.mode.i)
            entry = entry.replace('[my]', self.mode.my)
            entry = entry.replace('[me]', self.mode.me)
            words.append(entry)
        return ' '.join(words)
    
    def _prep_result(self, excuse_text):
        return excuse_text[0].upper() + excuse_text[1:] # Capitalize sentence
        