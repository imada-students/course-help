from asg4 import * 
from matplotlib import pyplot as plt

# np.set_printoptions(precision=3)

x = np.array([2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1.75, 1.91, 2.03, 2.13, 2.22, 2.30, 2.37, 2.43])

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([5.3, 7.2, 9.6, 12, 17, 23, 31])


def make_fig_error(ax, fit_func, model, x, y):
    global a,b
    ax.plot(x,y,'o')
    plt.xlim([np.amin(x),np.amax(x)])
    plt.ylim([np.amin(y),np.amax(y)])
    plt.grid(True)
    try:
        a,b = fit_func(x,y)
        ax.plot(x,f(x))
        err = training_error(f,x,y)
        ax.set_title(fit_func.__name__ + " "+ str(np.round(err,3)))
        return err
    except NotImplementedError as e:
        print(e)
    return -1


    
plt.figure(figsize=(12,2))

ax = plt.subplot(141)
f=lambda xx: a*xx + b
_lin = make_fig_error(ax, linear_model, f, x,y)


ax = plt.subplot(142)
f = lambda xx: a*np.exp(b*xx)
_exp = make_fig_error(ax, exponential_model, f, x, y)


ax = plt.subplot(143)
f = lambda xx: a*(xx**b)
_pow = make_fig_error(ax, power_model, f, x, y)


ax = plt.subplot(144)
f = lambda xx: a+b*np.log(xx)
_log = make_fig_error(ax, logarithmic_model, f, x, y)


print("Training Error: ",_lin,_exp,_pow,_log)




plt.show()

#plt.savefig("nonlin.png")
