'''
This is a self-contained flask application
'''
from module_manager import ModuleManager
from profile import Profiler

from flask import Flask
from flask import request
from flask import render_template
import settings
from werkzeug.contrib.cache import SimpleCache
import traceback

app = Flask(__name__)
app.config.from_object(settings)
cache = SimpleCache()
module_manager = ModuleManager()

@app.route('/')
def index():
    return 'hello'

# HTTP GET /solution/2?profile=true
@app.route('/solution/<int:problem_id>')
def solution(problem_id):
    '''
    do calculation only: 
    1) module is loaded for the first time
    2) module source file is modified since last time module was loaded
    3) no cached result and/or profile_stats (if requesting profile_stats)
    '''
    try:
        # load solution module, using ModuleManager
        module_name = 'solutions.problem{0}'.format(problem_id)
        do_calculation = module_manager.add_module(module_name)
        module = module_manager.get_module(module_name)
    except ImportError:
        return render_template('solution.html',
            problem_id=problem_id) 

    problem_content = module.__doc__

    try:
        do_profile = request.args.get('profile', '')

        # check cache
        result_key = 'problem_{0}_result'.format(problem_id)
        result = cache.get(result_key)
        profile_stats_key = 'problem_{0}_profile_stats'.format(problem_id)
        profile_stats = cache.get(profile_stats_key)
        if result == None:
            do_calculation = True
        if do_profile == 'true' and profile_stats == None:
            do_calculation = True
        # do calculation
        if do_calculation:
            if do_profile == 'true':
                p = Profiler(module.solution)
                result = p()
                profile_stats = p.get_stats()
            else:
                result = module.solution()
                profile_stats = ''
            # update cache
            cache.set(result_key, result)
            cache.set(profile_stats_key, profile_stats)

        # render template
        return render_template("solution.html",
            problem_id=problem_id,
            problem_content=problem_content,
            result=result,
            profile_stats=profile_stats)

    except KeyError:
        return render_template('error.html'), 404

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    error_traceback = ''
    error_traceback = traceback.format_exc(e)
    return render_template('500.html', error_traceback=error_traceback), 500

if __name__ == '__main__':
    app.run()
