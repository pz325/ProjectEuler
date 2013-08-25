'''
This is a self-contained flask application
'''
from flask import Flask
import settings
import time

app = Flask(__name__)
app.config.from_object(settings)

@app.route('/')
def index():
    return 'hello'

@app.route('/solution/<int:problem_id>')
def solution(problem_id):
    try:
        module = __import__('solutions.problem{0}'.format(problem_id), fromlist=['solution'])
        start_time = time.time()
        result = module.solution()
        run_time = time.time() - start_time
        return 'Result: {0} (in {1} seconds)'.format(result, run_time)
    except ImportError:
        return 'Not solved'
    except Exception:
        return 'Unknown error'

if __name__ == '__main__':
    app.run()
