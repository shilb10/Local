from __future__ import division
import options as op
import numpy as np 
import matplotlib.pyplot as pt 
from matplotlib.widgets import Slider
from traitsui.message import auto_close_message, error, message

def plot_static_risk(op_list, func, vol, r):
    if len(op_list) == 0:
        auto_close_message('\n Basket is empty \n', 2.0, 'Error', )
        return
    op1 = max_strike_op(op_list)
    op2 = max_time_op(op_list)
    op3 = min_strike_op(op_list)
    S = np.arange(op3.K*.5, op1.K*1.5, .05)
    for t in np.arange(op2.T*.9, op2.T, .1):
        i = (t/(op2.T) -.9)*(1.0/.1)
        risk = [getattr(ops, "{0}".format(func.__name__))(S, t, vol, r) for ops in op_list]
        plot_risk = [sum(j) for j in zip(*risk)]
        pt.plot(S, plot_risk, color=pt.cm.RdYlBu(i))
    pt.show()

def plot_dynamic_risk(op_list, func):
    if len(op_list) == 0:
        auto_close_message('\n Basket is empty \n', 2.0, 'Error', )
        return
    op1 = max_strike_op(op_list)
    op2 = max_time_op(op_list)
    op3 = min_strike_op(op_list)
    S = np.arange(op3.K*.5, op1.K*1.5, .05)
    ax = pt.subplot(111)
    pt.subplots_adjust(left=0.15, bottom=0.35)
    vol = .1
    r = .05
    t = op2.T*.8
    risk_list = [getattr(ops, "{0}".format(func.__name__))(S, t, vol, r) for ops in op_list]
    plot_risk = [sum(j) for j in zip(*risk_list)]
    risk, = pt.plot(S, plot_risk)
    pt.xlabel('Underlying')
    pt.ylabel('{0}'.format(func.__name__))
    axcolor = 'lightgoldenrodyellow'
    axvol = pt.axes([0.15, 0.2, 0.55, 0.03], axisbg=axcolor)
    axtime = pt.axes([0.15, 0.15, 0.55, 0.03], axisbg=axcolor)
    axrate = pt.axes([0.15, 0.1, 0.55, 0.03], axisbg=axcolor)
    svol = Slider(axvol, 'vol', 0.0, 1.0, valinit=0.1)
    stime = Slider(axtime, 'time', 0.0, op2.T, valinit=op2.T*.8)
    srate = Slider(axrate, 'rate', 0.0, .2, valinit=0.05)
    def update(val):
        risk_list = [getattr(ops, "{0}".format(func.__name__))(S, stime.val, svol.val, srate.val) for ops in op_list]
        plot_risk = [sum(j) for j in zip(*risk_list)]
        risk.set_ydata(plot_risk)
        ax.set_ylim(min(plot_risk), max(plot_risk))
        pt.draw()

    svol.on_changed(update)
    stime.on_changed(update)
    srate.on_changed(update)
    pt.show()


def max_strike_op(op_list):
    op1 = op.Option(0, 0, 'c', 'l')
    for ops in op_list:
        if op1.K < ops.K:
            op1 = ops
    return op1

def min_strike_op(op_list):
    op1 = op.Option(10**6, 0, 'c', 'l')
    for ops in op_list:
        if op1.K > ops.K:
            op1 = ops
    return op1

def min_time_op(op_list):
    op1 = op.Option(0, 10**6, 'c', 'l')
    for ops in op_list:
        if op1.T > ops.T:
            op1 = ops
    return op1

def max_time_op(op_list):
    op1 = op.Option(0, 0, 'c', 'l')
    for ops in op_list:
        if op1.T < ops.T:
            op1 = ops
    return op1