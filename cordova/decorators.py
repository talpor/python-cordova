import os


def chdir_context(func):
    def wrapped(*args, **kwargs):
        self = args[0]
        cwd = os.getcwd()
        os.chdir(self.path)
        ret = func(*args, **kwargs)
        os.chdir(cwd)
        return ret
    return wrapped


def for_all_methods(decorator):
    def decorate(cls):
        for attr, val in cls.__dict__.iteritems():
            if callable(val) and not attr.startswith("__"):
                setattr(cls, attr, decorator(val))
        return cls
    return decorate
