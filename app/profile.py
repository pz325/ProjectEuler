'''
profilee accepts no parameter
'''
import cStringIO
import cProfile
import pstats

class Profiler(object):
    '''
    example: 

    p = Profiler(a_method)
    result = p()
    stats = p.get_stats()
    '''
    def __init__(self, profilee):
        self.profiler = cProfile.Profile()
        self.profilee = profilee

    def __call__(self):
        return self.profiler.runcall(self.profilee)
    
    def get_stats(self):
        stat_stream = cStringIO.StringIO()
        self.profiler.create_stats()
        self.profiler.print_stats()  # sort by 
        pstats.Stats(self.profiler, stream=stat_stream).strip_dirs().sort_stats('calls').print_stats()
        profile_stats = stat_stream.getvalue()
        stat_stream.close()
        return profile_stats
