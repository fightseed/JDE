#ifndef LAPJV_H
#define LAPJV_H

#include <float.h>

#ifdef PYTHON_LAPJV

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include "Python.h"

#endif  // PYTHON_LAPJV

namespace mot {

class LAPJV
{
public:
    static LAPJV *instance(void);
    bool init(void);
    bool solve(const float *cost, int rows, int cols, float *opt, int *x,
        int *y, bool extend_cost=false, float cost_limit=FLT_MAX);
    void free(void);
private:
    static LAPJV *me;
#ifdef PYTHON_LAPJV
    PyObject *module = 0;
    PyObject *dict = 0;
    PyObject *lapjv = 0;
#endif  // PYTHON_LAPJV
    LAPJV(void) {}
    ~LAPJV(void) {}
};

}   // namespace mot

#endif  // LAPJV_H