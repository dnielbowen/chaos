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
equations are used beyond $z_{n+1}=z_{n}^2+c$. For logistic maps (probably 
"traditional" fractals, too), better mathematicians seem to explain this as 
being a family of "quadratic maps" that all yield the same properties, just 
scaled differently.

## A few outputs

A fully zoomed-out view of the interesting parts. The ["period 
doubling"](https://en.wikipedia.org/wiki/Period-doubling_bifurcation) whose 
frequency increases at a ratio of the [Feigenbaum 
constant](https://en.wikipedia.org/wiki/Feigenbaum_constants) can be seen in 
the branch from left-to-right.

![Output 1](https://raw.githubusercontent.com/eldewen/chaos/master/out/ax1-x.jpg)

Zooming in on one of those gaps (note the X axis bounds):

![Output 2](https://raw.githubusercontent.com/eldewen/chaos/master/out/logisticSubset3.jpg)

Zooming further into the above image, we start to repeat patterns. A miniature 
version of the whole "zoomed-out" scene was already visible in the above zoomed 
image, but scaled differently. ...like when you zoom in a Mandelbrot fractal 
and see another Mandelbrot-looking shape (and on and on, recursively).

![Output 3](https://raw.githubusercontent.com/eldewen/chaos/master/out/logisticSubset2.jpg)

Another detailed section.

![Output 4](https://raw.githubusercontent.com/eldewen/chaos/master/out/logisticSubset.jpg)

## Market prediction idea

Below was a result from playing with logistic maps in trying to yield curves 
that looked something like market data. An almost certainly wrong and very 
qualitative theory for building a quantitative financial market model idea went 
something like this:

- Markets are chaotic
- Fractals are self-similar
- When zooming in a fractal, you can see in the "distance" what's coming next 
  as you zoom

Perhaps, therefore, if you could find and match up a generated 1D fractal curve 
against real market data (via cross-correlation), by principle of 
self-similarity in fractals, perhaps the market's motion too is more 
constrained than it appears. But, there are an infinite number of curves you 
could generate to match up against market data --- isn't it a super long shot 
that you'd find one that matches? To that I say, why do so many sections of the 
Mandelbrot look the same? As you zoom in and pan around, even when it's 
different, it often feels familiar. Maybe there are a smaller number of 
"classes" of curves with variations. And, do you need to have the "right" 
model? Apparently not, they all yield basically the same result. You get 
Mandelbrot-like fractals without trying. You get logistic map-like sets without 
trying. So perhaps, just like how you can "see where you're going" when zooming 
into a fractal, you could predict e.g. the next few minutes of market data once 
you've matched one of these classes of fractal curves that you've found.

So? How did it go? I gave up trying to make the curves look like market data, 
to say nothing of going further with cross-correlation. The ones below are too 
pointy --- real market data does not look so "Alpine mountain-like" as these 
curves. Given that I highly doubt this would work in the first place I didn't 
think it was worth spending much time on. But, at least it made for kind of a 
cool picture --- to create the curves below I generated a sequence using the 
logistic map, subtracted the average (if I recall), calculated the cumulative 
sum, and tried various low-pass filters. The result is a bunch of random walks 
created with fractals that always starts and ends at 0. Granularity of the 
curve depends on the length of the logistic sequence.

One more interesting point about these curves: note how they all start out 
together for a very short time, like a tiny lightning bolt on the left. This is 
because I varied a parameter in the logistic map only very slightly to generate 
the different curves. If I varied it even more slightly, they would track 
together for longer (but not that long, because it really seems to want to go 
chaotic). This sensitivity to initial conditions is another classic character 
of chaos. But, this is similar to how you can "see where you're going" when you 
zoom into a Mandelbrot fractal, even though you can't predict what comes after 
"the next horizon" and you definitely can't begin to predict even further. 
Below is a visualization of this fact (it only converges back to zero each time 
because of how I averaged the sequence).

Worthy of mention: Mandelbrot himself has spent quite a bit of his energy, for 
decades, looking at fractal behavior in markets (for example, 
[here](https://www.amazon.com/Misbehavior-Markets-Fractal-Financial-Turbulence/dp/0465043577), 
in addition to a bunch of academic papers).

![Market sim data](https://raw.githubusercontent.com/eldewen/chaos/master/out/manyPaths.jpg)
