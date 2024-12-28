# Self-Organized Criticality in Artificial Neural Networks 
This is an entirely new and unique approach mimicking artificial neural networks from a brain-inspired model's point of view. I have used advanced mathematical frameworks from statistical physics and unique simulation techniques. So, this is a neve-forseen interplay between statistical physics and artificial neural networks.

# Introduction to First Passage Processes
The first passage process is a special type of random walk, i.e., a stochastic process. It serves as a fundamental framework in stochastic dynamics, enabling the analysis of probabilities and typical times for particles or complex systems to reach specific thresholds. This model finds widespread application across diverse disciplines, ranging from physics, mathematics to neuroscience and financial markets. The applicability of first passage processes extends into the realm of financial markets, where it finds resonance in stock market trading strategies. For instance, the execution of buy/sell orders hinges on the moment when stock prices initially breaches a predefined threshold. In modern trading practices, algorithms that take advantage of the principles of first passage processes, such as trade bots, captilalize on such fluctuations. 

The first passage probability, F(r, t), represents the probability that a random walk or a diffusing particle arrives at a particular site (or set of sites) for the first time during a specified time frame t, starting from the origin. In essence, it quantifies the probability of zero crossings and captures the probability distribution of the first arrival times of a random walk. On the other hand, the occupation probability, P(r, t), represents the probability that a random walk occupies a particular site r at time t, given that it started from the origin. F(r, t) accounts for the cumulative probability of the random walks being present at the site r at any given time t.

# FP process analogy in the neural network 
In artificial neural networks, we have neurons connected to each other that transmits information from one neuron to another. Now, if the potential of the network or the neuron in question crosses a specific potential threshold then it fires, i.e., all the neurons in the network starts firing. Now, if we restrict our focus to one synaptic end and consider rest of the network on both the sides as two blocks, then we will calculate the typical time for the network potential to cross that the threshold value, i.e., first passage time. 

Now, we restrict our focus to the synaptic ends of the neural network. We have an n-n connection between receptors and transmitters at these synaptic ends. To study this interaction picture, we implement this molecular dynamics simulation. We can initialize those receptors and transmitters using the random number generator and then use the MD simulation to establish the interaction picture. 

We want to examine how good of a neural network we can create if we implement these ideas from non-equilibrium statistical physics. We want to investigate whether these techniques enhance computational power or time efficiency. So, from a physicist's point of view, this is a great adventure for our intuitions and existing empirical models to extrapolate in these domains.

So, this is how we are integrating the idea of FP process into the neural network.

# Findings and yields
