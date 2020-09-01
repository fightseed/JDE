"""
generated by MindSpore studio

"""

import te.lang.cce
from te import tvm
from topi import generic


def JDEcoder(shape, dtype, num_classes, num_boxes, conf_thresh, iou_thresh,
    biases, masks, strides, kernel_name = "JDEcoder", need_build = True, need_print = False):
    """
    
    Parameters
    ----------

    kernel_name : kernel name, default value is "JDEcoder"

    need_buid : if need to build CCEC kernel, default value is False

    need_print : if need to print the ir, default value is False

    Returns
    -------
    None
        
    """
   
    """
    TODO:
    Please refer to the TE DSL Manual, And code here with TE DSL.
    """
    
    check_list = ["float16", "float32"]
    if not (dtype.lower() in check_list):
        raise RuntimeError(
            "JDEcoder only support %s while dtype is %s" % (",".join(check_list), dtype))
    
    if num_classes < 1:
        raise RuntimeError("num_classes must be > 1")
    
    inp_dtype = dtype.lower()
    inp_tensor = tvm.placeholder(shape, name='inp_tensor', dtype=inp_dtype)
    
    with tvm.target.cce():
        res = inp_tensor
        sch = generic.auto_schedule(res)
    
    config = {"print_ir": need_print,
              "need_buid": need_build,
              "name": kernel_name,
              "tensor_list": [inp_tensor, res]}
    
    te.lang.cce.cce_build_code(sch, config)

#if __name__ == "__main__":   
#    JDEcoder((1, 536, 10, 18), "float16", 1, 4, 0.5, 0.45, (6, 16, 8, 23, 11, 32, 16, 45, 21, 64, 30, 90, 43, 128, 60, 180, 85, 255, 120, 360, 170, 420, 340, 320), (8, 9, 10, 11, 4, 5, 6, 7, 0, 1, 2, 3), (32, 16, 8))