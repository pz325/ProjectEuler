'''
not thread safe
profilee accepts no parameter
'''
import cStringIO
import cProfile
import sys

class Profiler(object):
    '''
    example: 

    p = Profiler(a_method)
    result = p()
    stats = p.get_stats
    '''
    def __init__(self, profilee):
        self.profiler = cProfile.Profile()
        self.profilee = profilee

    def __call__(self):
        return self.profiler.runcall(self.profilee)
    
    def get_stats(self):
        stream = cStringIO.StringIO()
        self.profiler.create_stats()
        old_stdout, sys.stdout = sys.stdout, stream
        self.profiler.print_stats(1)
        sys.stdout = old_stdout
        profile_stats = stream.getvalue()
        stream.close()
        return profile_stats

