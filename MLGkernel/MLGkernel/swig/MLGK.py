# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_MLGK')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_MLGK')
    _MLGK = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_MLGK', [dirname(__file__)])
        except ImportError:
            import _MLGK
            return _MLGK
        try:
            _mod = imp.load_module('_MLGK', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _MLGK = swig_import_helper()
    del swig_import_helper
else:
    import _MLGK
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class Params(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Params, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Params, name)
    __repr__ = _swig_repr

    def __init__(self, e, g, r, l, t, b):
        this = _MLGK.new_Params(e, g, r, l, t, b)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def set_paths(self, data, features):
        return _MLGK.Params_set_paths(self, data, features)

    def set_save_path(self, save):
        return _MLGK.Params_set_save_path(self, save)

    def show(self):
        return _MLGK.Params_show(self)
    GROW = _MLGK.Params_GROW
    DOUBLE = _MLGK.Params_DOUBLE
    __swig_setmethods__["eta"] = _MLGK.Params_eta_set
    __swig_getmethods__["eta"] = _MLGK.Params_eta_get
    if _newclass:
        eta = _swig_property(_MLGK.Params_eta_get, _MLGK.Params_eta_set)
    __swig_setmethods__["gamma"] = _MLGK.Params_gamma_set
    __swig_getmethods__["gamma"] = _MLGK.Params_gamma_get
    if _newclass:
        gamma = _swig_property(_MLGK.Params_gamma_get, _MLGK.Params_gamma_set)
    __swig_setmethods__["radius"] = _MLGK.Params_radius_set
    __swig_getmethods__["radius"] = _MLGK.Params_radius_get
    if _newclass:
        radius = _swig_property(_MLGK.Params_radius_get, _MLGK.Params_radius_set)
    __swig_setmethods__["levels"] = _MLGK.Params_levels_set
    __swig_getmethods__["levels"] = _MLGK.Params_levels_get
    if _newclass:
        levels = _swig_property(_MLGK.Params_levels_get, _MLGK.Params_levels_set)
    __swig_setmethods__["grow_or_double"] = _MLGK.Params_grow_or_double_set
    __swig_getmethods__["grow_or_double"] = _MLGK.Params_grow_or_double_get
    if _newclass:
        grow_or_double = _swig_property(_MLGK.Params_grow_or_double_get, _MLGK.Params_grow_or_double_set)
    __swig_setmethods__["data_path"] = _MLGK.Params_data_path_set
    __swig_getmethods__["data_path"] = _MLGK.Params_data_path_get
    if _newclass:
        data_path = _swig_property(_MLGK.Params_data_path_get, _MLGK.Params_data_path_set)
    __swig_setmethods__["features_path"] = _MLGK.Params_features_path_set
    __swig_getmethods__["features_path"] = _MLGK.Params_features_path_get
    if _newclass:
        features_path = _swig_property(_MLGK.Params_features_path_get, _MLGK.Params_features_path_set)
    __swig_setmethods__["save_path"] = _MLGK.Params_save_path_set
    __swig_getmethods__["save_path"] = _MLGK.Params_save_path_get
    if _newclass:
        save_path = _swig_property(_MLGK.Params_save_path_get, _MLGK.Params_save_path_set)
    __swig_setmethods__["num_threads"] = _MLGK.Params_num_threads_set
    __swig_getmethods__["num_threads"] = _MLGK.Params_num_threads_get
    if _newclass:
        num_threads = _swig_property(_MLGK.Params_num_threads_get, _MLGK.Params_num_threads_set)
    __swig_destroy__ = _MLGK.delete_Params
    __del__ = lambda self: None
Params_swigregister = _MLGK.Params_swigregister
Params_swigregister(Params)

class MLGdataset(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MLGdataset, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MLGdataset, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _MLGK.new_MLGdataset(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _MLGK.delete_MLGdataset
    __del__ = lambda self: None

    def condense(self, nlevels, leaf_radius=2):
        return _MLGK.MLGdataset_condense(self, nlevels, leaf_radius)

    def computeGram(self, levels, radius):
        return _MLGK.MLGdataset_computeGram(self, levels, radius)

    def loadGraphs(self, filename):
        return _MLGK.MLGdataset_loadGraphs(self, filename)

    def loadDiscreteFeatures(self, filename, numFeatures):
        return _MLGK.MLGdataset_loadDiscreteFeatures(self, filename, numFeatures)

    def loadFeatures(self, filename):
        return _MLGK.MLGdataset_loadFeatures(self, filename)

    def saveGram(self, filename):
        return _MLGK.MLGdataset_saveGram(self, filename)

    def fillGram(self, npmatrix):
        return _MLGK.MLGdataset_fillGram(self, npmatrix)
    __swig_setmethods__["graphs"] = _MLGK.MLGdataset_graphs_set
    __swig_getmethods__["graphs"] = _MLGK.MLGdataset_graphs_get
    if _newclass:
        graphs = _swig_property(_MLGK.MLGdataset_graphs_get, _MLGK.MLGdataset_graphs_set)
    __swig_setmethods__["gamma"] = _MLGK.MLGdataset_gamma_set
    __swig_getmethods__["gamma"] = _MLGK.MLGdataset_gamma_get
    if _newclass:
        gamma = _swig_property(_MLGK.MLGdataset_gamma_get, _MLGK.MLGdataset_gamma_set)
    __swig_setmethods__["eta"] = _MLGK.MLGdataset_eta_set
    __swig_getmethods__["eta"] = _MLGK.MLGdataset_eta_get
    if _newclass:
        eta = _swig_property(_MLGK.MLGdataset_eta_get, _MLGK.MLGdataset_eta_set)
    __swig_setmethods__["levels"] = _MLGK.MLGdataset_levels_set
    __swig_getmethods__["levels"] = _MLGK.MLGdataset_levels_get
    if _newclass:
        levels = _swig_property(_MLGK.MLGdataset_levels_get, _MLGK.MLGdataset_levels_set)
    __swig_setmethods__["radius"] = _MLGK.MLGdataset_radius_set
    __swig_getmethods__["radius"] = _MLGK.MLGdataset_radius_get
    if _newclass:
        radius = _swig_property(_MLGK.MLGdataset_radius_get, _MLGK.MLGdataset_radius_set)
    __swig_setmethods__["grow"] = _MLGK.MLGdataset_grow_set
    __swig_getmethods__["grow"] = _MLGK.MLGdataset_grow_get
    if _newclass:
        grow = _swig_property(_MLGK.MLGdataset_grow_get, _MLGK.MLGdataset_grow_set)
    __swig_setmethods__["gram"] = _MLGK.MLGdataset_gram_set
    __swig_getmethods__["gram"] = _MLGK.MLGdataset_gram_get
    if _newclass:
        gram = _swig_property(_MLGK.MLGdataset_gram_get, _MLGK.MLGdataset_gram_set)
MLGdataset_swigregister = _MLGK.MLGdataset_swigregister
MLGdataset_swigregister(MLGdataset)

# This file is compatible with both classic and new-style classes.


