from __future__ import division
from traits.api import *
from traitsui.api import View, Item, Group, HSplit, Handler
import options as op
import numpy as np 
import plotter as plt
from traitsui.message import auto_close_message, error, message

class OptionVals(HasTraits):
    K = CFloat(100, desc='strike')
    T = CFloat(100, desc='time to maturity (days)')
    op_type = CStr('c', desc='call or put (c/p)')
    quantity = CInt(1, desc='amount')
    
class UnderlyingVals(HasTraits):
    vol = CFloat(.1, desc='volatility')
    r = CFloat(0.05, desc='interest rate')



class Container(HasTraits):
    optionVals = Instance(OptionVals, ())
    underlyingVals = Instance(UnderlyingVals, ())

    results_string = String()
    op_list = []
    buy_op = Button("Buy Option")
    sell_op = Button("Sell Option")
    empty_basket = Button("Empty Basket")
    
    pnl = Button("Plot PNL")
    delta = Button("Plot Delta")
    gamma = Button("Plot Gamma")
    theta = Button("Plot Theta")
    vega = Button("Plot Vega")
    rho = Button("Plot Rho")

    pnl_dynamic = Button("Plot PNL")
    delta_dynamic = Button("Plot Delta")
    gamma_dynamic = Button("Plot Gamma")
    theta_dynamic = Button("Plot Theta")
    vega_dynamic = Button("Plot Vega")
    rho_dynamic = Button("Plot Rho")

    view = View(
                Group(
                    Group(
                        HSplit(
                            Group(
                                Item('optionVals', style='custom', show_label=False),
                                Item('results_string', style='custom', show_label=False, springy=True, height=-50, width=-100, tooltip="Current basket (Strike/Time/Type/Position)",), label="Enter Values",
                            ),
                            Group(
                                Item('buy_op', show_label=False),
                                Item('sell_op', show_label=False),
                                Item('empty_basket', show_label=False), label="Choose Position"
                            ), 
                        ), label="Option Input", dock='tab',
                    ),
                    Group(
                        HSplit(
                            Group(
                                Item('underlyingVals', style='custom', show_label=False),
                                Item('results_string', style='custom', show_label=False, springy=True, height=-50, width=-100, tooltip="Current basket (Strike/Time/Type/Position)",),
                                label="Set Underlying Parameters", 
                            ),      
                            Group(
                                Item('pnl', show_label=False),
                                Item('delta', show_label=False),
                                Item('gamma', show_label=False),
                                Item('theta', show_label=False),
                                Item('vega', show_label=False),
                                Item('rho', show_label=False),
                                label="Choose Risk"
                            ),
                        ),
                        label="Static vs Underlying", dock='tab', 
                    ),
                    Group(
                        HSplit(
                            Group(
                                Item('results_string', style='custom', show_label=False, springy=True, height=-50, width=-100, tooltip="Current basket (Strike/Time/Type/Position)",),
                                label="Current Basket", 
                            ),      
                            Group(
                                Item('pnl_dynamic', show_label=False),
                                Item('delta_dynamic', show_label=False),
                                Item('gamma_dynamic', show_label=False),
                                Item('theta_dynamic', show_label=False),
                                Item('vega_dynamic', show_label=False),
                                Item('rho_dynamic', show_label=False),
                                label="Choose Risk", 
                            ),
                        ),
                        label="Dynamic vs Underlying", dock='tab', 
                    ), 
                layout='tabbed'), dock='vertical', width=500, resizable=True, title='Option Visualizer',
            )

    def _buy_op_fired(self):
        op1 = op.Option(self.optionVals.K, self.optionVals.T, self.optionVals.op_type, 'l')
        for i in xrange(self.optionVals.quantity):
            self.op_list.append(op1)
        self.add_line(
                "{0}/{1}/{2}/{3}"
                    .format(self.optionVals.K, self.optionVals.T, self.optionVals.op_type, self.optionVals.quantity)
                )

    def _sell_op_fired(self):
        op1 = op.Option(self.optionVals.K, self.optionVals.T, self.optionVals.op_type, 's')
        for i in xrange(self.optionVals.quantity):
            self.op_list.append(op1)
        self.add_line(
                "{0}/{1}/{2}/{3}"
                    .format(self.optionVals.K, self.optionVals.T, self.optionVals.op_type, -self.optionVals.quantity)
                )

    def _empty_basket_fired(self):
        self.op_list = []
        self.results_string = ''
    def add_line(self, string):
        self.results_string = string + '\n' + self.results_string

    def _pnl_fired(self):
        plt.plot_static_risk(self.op_list, op.Option.price, self.underlyingVals.vol, self.underlyingVals.r)
    def _delta_fired(self):
        plt.plot_static_risk(self.op_list, op.Option.delta, self.underlyingVals.vol, self.underlyingVals.r)
    def _gamma_fired(self):
        plt.plot_static_risk(self.op_list, op.Option.gamma, self.underlyingVals.vol, self.underlyingVals.r)
    def _theta_fired(self):
        plt.plot_static_risk(self.op_list, op.Option.theta, self.underlyingVals.vol, self.underlyingVals.r)
    def _vega_fired(self):
        plt.plot_static_risk(self.op_list, op.Option.vega, self.underlyingVals.vol, self.underlyingVals.r)
    def _rho_fired(self):
        plt.plot_static_risk(self.op_list, op.Option.rho, self.underlyingVals.vol, self.underlyingVals.r)

    def _pnl_dynamic_fired(self):
        plt.plot_dynamic_risk(self.op_list, op.Option.price)
    def _delta_dynamic_fired(self):
        plt.plot_dynamic_risk(self.op_list, op.Option.delta)
    def _gamma_dynamic_fired(self):
        plt.plot_dynamic_risk(self.op_list, op.Option.gamma)
    def _theta_dynamic_fired(self):
        plt.plot_dynamic_risk(self.op_list, op.Option.theta)
    def _vega_dynamic_fired(self):
        plt.plot_dynamic_risk(self.op_list, op.Option.vega)
    def _rho_dynamic_fired(self):
        plt.plot_dynamic_risk(self.op_list, op.Option.rho)




container = Container(optionVals=OptionVals())
container.configure_traits()