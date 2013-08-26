'''
This is a self-contained flask application
'''
from flask import Flask
from flask import request
import settings
import cStringIO
import cProfile
import sys

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def index():
    return 'hello'


# HTTP GET /solution/2/?profile=true
@app.route('/solution/<int:problem_id>')
def solution(problem_id):
    try:
        do_profile = request.args.get('profile', '')

        module = __import__('solutions.problem{0}'.format(problem_id), fromlist=['solution'])
        if do_profile == 'true':
            profiler = cProfile.Profile()
            result = profiler.runcall(module.solution)
            profiler.create_stats()
            profile_result_stream = cStringIO.StringIO()
            old_stdout, sys.stdout = sys.stdout, profile_result_stream
            profiler.print_stats(1)
            sys.stdout = old_stdout
            profile_result = '<pre>{0}</pre>'.format(profile_result_stream.getvalue())
            return '<h3>Result: {0} </h3>{1}'.format(result, profile_result)
        else:
            result = module.solution()
            return '<h3>Result: {0} </h3>'.format(result)
    except ImportError:
        return 'Not solved'
    except KeyError:
        return 'Bad request'
    except Exception:
        return 'Unknown error'


if __name__ == '__main__':
    app.run()
