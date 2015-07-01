from __future__ import division
import numpy as np 
import matplotlib.pyplot as pt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm


class Option(object):
    def __init__(self, strike, maturity, op_type, pos):
        self.K = strike
        self.T = maturity
        self.op_type = op_type
        self.pos = pos

    def d1(self, S, t, vol, r):
        #Computes d1 used in pricing and greeks
        return np.multiply(
                np.true_divide(1,
                    np.multiply(vol, 
                        np.power(
                            np.subtract(self.T, t),.5))),
                np.add(
                    np.log(
                        np.true_divide(S,self.K)), 
                    np.multiply(r + vol**2/2,
                        np.subtract(self.T, t))))

    def d2(self, S, t, vol, r):
        #Computes d2 used in pricing and greeks
        return  np.subtract(self.d1(S, t, vol, r), 
                np.multiply(vol,
                    np.power(
                        np.subtract(self.T, t), .5)))

    def price(self, S, t, vol, r):
        #Computes price using Black-Sholes
        if t > self.T:
            return np.zeros(len(S))
        d1 = self.d1(S, t, vol, r)
        d2 = self.d2(S, t, vol, r)
        p = np.subtract(
                np.multiply(norm.cdf(d1), S), 
                np.multiply(norm.cdf(d2), 
                    np.multiply(self.K, 
                        np.exp(
                            np.multiply(-r, 
                                np.subtract(self.T, t))))))
        if self.op_type == 'c':
            if self.pos == 'l':
                return p
            else:
                return np.multiply(-1, p) 
        else:
            if self.pos == 'l':
                return np.add(
                    np.subtract(
                        np.multiply(self.K,
                            np.exp(
                                np.multiply(-r, 
                                    np.subtract(self.T, t)))),
                        S),
                    p)
            else:
                return np.multiply(-1, 
                        np.add(
                            np.subtract(
                                np.multiply(self.K,
                                    np.exp(
                                        np.multiply(-r, 
                                            np.subtract(self.T, t)))),
                                S),
                            p))

    ###Some greeks below###
    def delta(self, S, t, vol, r):
        if t > self.T:
            return np.zeros(len(S))
        if self.op_type == 'c':
            return norm.cdf(self.d1(S, t, vol, r))
        else:
            return np.subtract(
                    norm.cdf(self.d1(S, t, vol, r)), 1)

    def gamma(self, S, t, vol, r):
        #Same for call and put
        if t > self.T:
            return np.zeros(len(S))
        return np.true_divide(norm.pdf(self.d1(S, t, vol, r)), 
                np.multiply(S, 
                    np.multiply(vol,
                        np.power(
                            np.subtract(self.T, t), .5))))

    def vega(self, S, t, vol, r):
        #Same for call and put
        if t > self.T:
            return np.zeros(len(S))
        return np.multiply(S, 
                np.multiply(norm.pdf(self.d1(S, t, vol, r)), 
                    np.power(
                        np.subtract(self.T, t), .5)))

    def theta(self, S, t, vol, r):
        if t > self.T:
            return np.zeros(len(S))
        if self.op_type == 'c':
            return np.subtract(
                    np.true_divide(
                        np.multiply(-vol, 
                            np.multiply(S, norm.pdf(self.d1(S, t, vol, r)))), 
                        np.multiply(2,
                            np.power(
                                np.subtract(self.T, t), .5))),
                    np.multiply(r,
                        np.multiply(self.K,
                            np.multiply(
                                np.exp(
                                    np.multiply(-r,
                                        np.subtract(self.T, t))),
                                norm.cdf(self.d2(S, t, vol, r))))))
        else:
            return np.add(
                    np.true_divide(
                        np.multiply(-vol, 
                            np.multiply(S, norm.pdf(self.d1(S, t, vol, r)))), 
                        np.multiply(2,
                            np.power(
                                np.subtract(self.T, t), .5))),
                    np.multiply(r,
                        np.multiply(self.K,
                            np.multiply(
                                np.exp(
                                    np.multiply(-r,
                                        np.subtract(self.T, t))),
                                norm.cdf(
                                    np.multiply(-1, self.d2(S, t, vol, r)))))))

    def rho(self, S, t, vol ,r):
        if t > self.T:
            return np.zeros(len(S))
        if self.op_type == 'c':
            return np.multiply(self.K, 
                    np.multiply(
                        np.subtract(self.T, t), 
                        np.multiply(
                            np.exp(
                                np.multiply(-r, 
                                    np.subtract(self.T, t))),
                            norm.cdf(self.d2(S, t, vol, r)))))
        else:
            return np.multiply(-self.K, 
                    np.multiply(
                        np.subtract(self.T, t), 
                        np.multiply(
                            np.exp(
                                np.multiply(-r, 
                                    np.subtract(self.T, t))),
                            norm.cdf(
                                np.multiply(-1, self.d2(S, t, vol, r))))))

o1 = Option(100, 100, 'c', 'l')
S = np.arange(90,110, .05)
# for t in np.arange(90,100,.1):
#     i = (t/100 - .9)*10
#     pt.plot(S, o1.rho(S, t, .1, 0), color=pt.cm.RdYlBu(i))
# pt.show()

# ax = pt.subplot(111)
# pt.subplots_adjust(left=0.15, bottom=0.25)
# t = 90
# price, = pt.plot(S, o1.price(S, t, .1, 0))
# pt.xlabel('Underlying')
# pt.ylabel('Price')
# axcolor = 'lightgoldenrodyellow'
# axtime = pt.axes([0.15, 0.1, 0.55, 0.03], axisbg=axcolor)
# stime = Slider(axtime, 'time', 90.0, 100.0, valinit=90)
# def update(val):
#     y = o1.price(S, stime.val, .1, 0)
#     price.set_ydata(y)
#     ax.set_ylim(min(y), max(y))
#     pt.draw()

# stime.on_changed(update)
# pt.show()
