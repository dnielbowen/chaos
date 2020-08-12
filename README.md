## Logistic maps and chaos

This plays around with the basic [logistic 
map](https://en.wikipedia.org/wiki/Logistic_map), $x_{n+1}=rx_{n}(1-x_{n})$.

The code is not complicated, but that's why chaos is interesting --- a lot of 
richness and complexity out of what seems like not a lot of equation/code. If 
you play around with bounds to e.g. zoom into arbitrarily-small sections (as is 
done below) and even change the map equation to something more complicated 
(even adding hyperbolic and trig functions, higher polynomials, etc), all the 
images seem to look basically like this. This is the self-similarity and 
scale-invariance of chaos coming out --- just like how many kinds of fractals 
all seem to look Mandelbrot-like, even when similarly more-complicated 
equations are used beyond $z_{n+1}=z_{n}^2+c$. For logistc maps (probably 
"traditional" fractals, too), better mathematicians seem to explain this as 
being a family of "quadratic maps" that all yield the same properties, just 
scaled differently.

Some outputs:

![Output 1](https://raw.githubusercontent.com/eldewen/chaos/master/out/ax1-x.jpg)

![Output 2](https://raw.githubusercontent.com/eldewen/chaos/master/out/logisticSubset3.jpg)

![Output 3](https://raw.githubusercontent.com/eldewen/chaos/master/out/logisticSubset2.jpg)

![Output 4](https://raw.githubusercontent.com/eldewen/chaos/master/out/logisticSubset.jpg)
