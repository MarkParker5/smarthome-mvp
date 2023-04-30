import time
import levenshtein
import speech_recognizer
from GCloudSpeechSynthesizer import GCloudSpeechSynthesizer
from commands import Command, all_commands


synthesizer = GCloudSpeechSynthesizer()

def find_command(request: str) -> Command | None:
    global all_commands
    
    result_command: Command | None = None
    max_weight = float(0)
    
    for command in all_commands:
        
        full_weight = float(0)
        
        for weight, strings in command.keywords.items():
            for keyword in strings:
                match = weight * max(
                    levenshtein.match_partial(request, keyword),
                    levenshtein.match_words(request, keyword)
                )
                full_weight += match
        
        if full_weight > max_weight:
            max_weight = full_weight
            result_command = command
    
    if max_weight < 1:
        return None
    
    return result_command
        
if __name__ == '__main__':
    print('Preparing...')
    speech_recognizer.listen_noise()
    while True:
        print('Listening...')
        request = speech_recognizer.listen()
        
        if request['status'] == 'error':
            time.sleep(1)
            continue
        elif request['status'] == 'void':
            continue
        
        text = request['text']
        
        print('You:', text)
        if command := find_command(text):
            response = command.runner(text)
        else:
            response = 'I don\'t get it'
        print(f'Assistant: {response}')
        synthesizer.synthesize(response).play()
        