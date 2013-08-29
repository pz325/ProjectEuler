'''
Manage module loading time
'''

import os.path

class ModuleManager(object):
    """Manages loaded modules in the runtime.

    Responsible for monitoring and reporting about file modification times.
    Modules can be loaded from source or precompiled byte-code files.  When a
    file has source code, the ModuleManager monitors the modification time of
    the source file even if the module itself is loaded from byte-code.
    """
    def __init__(self):
        self._modules = {}  # dict, key: module_name, value: module
        self._modification_times = {}  # dict, key: module_name, value: time
    
    def add_module(self, module_name):
        '''
        @return module reloaded
        '''
        reloaded = False
        if module_name not in self._modules:
            module = self.load_module(module_name)
            self._modules[module_name] = module
            self._modification_times[module_name] = self.get_module_file_mtime(module)
            reloaded = True
        else:
            if self.is_module_file_modified(module_name):
                self.reload_module(module_name)
                reloaded = True
        return reloaded

    def reload_module(self, module_name):
        module = self.load_module(module_name)
        self._modules[module_name] = module
        self._modification_times[module_name] = self.get_module_file_mtime(module)

    def get_module(self, module_name):
        if module_name in self._modules:
            return self._modules[module_name]
        else:
            return None

    def has_module(self, module_name):
        return module_name in self._modules

    def is_module_file_modified(self, module_name):
        module = self._modules[module_name]
        mtime = self._modification_times[module_name]
        if mtime != os.path.getmtime(self.get_module_file(module)):
            return True
        else: 
            return False

    @staticmethod
    def get_module_file(module):
        module_file = module.__file__
        if module_file is None:
            return None
        source_file = module_file[:module_file.rfind('py') + 2]
        if os.path.isfile(source_file):
            return source_file
        else:
            return module_file

    @staticmethod
    def load_module(module_name):
        module = __import__(module_name, fromlist=[''])
        return module

    @staticmethod
    def get_module_file_mtime(module):
        module_file = ModuleManager.get_module_file(module)
        mtime = os.path.getmtime(module_file)
        return mtime

if __name__ == '__main__':
    module_manager = ModuleManager()
    module_name = 'solutions.problem2'
    reloaded = module_manager.add_module(module_name)
    module = module_manager.get_module(module_name)
    print module, 'is reloaded: ', reloaded
    result = module.solution()
    print 'module.solution() result: ', result
    print 'module source file is modified: ', module_manager.is_module_file_modified(module_name)
    reloaded = module_manager.add_module(module_name)
    print module, 'is reloaded: ', reloaded
