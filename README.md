# TSP Implementation

This project is the culminations of my attempts to solve the Traveling Salesman Problem (TSP). So far, I have experimented with 2-opt, simulated annealing, and a 2-approximation algorithm based on walking through the walls of the Minimum Spanning Tree. The 2-approximation algorithm portion is not included in the final algorithm, but I might add it back since it is good at dealing with certain datasets of TSP problem.

# Requirements
Here are the python version that you would need:
* Python 3.6.7
* virtualenv or anaconda package manager

# Virtual Environment and Setup:
Although this project is created using only the base Python 3.6.7, you may be wondering how to setup the virtual environment. Here are the instructions:

```
1. python3 -m pip install virtualenv
2. virtualenv tsp
3. source tsp/bin/activate
4. python3 -m pip install -r requirements.txt
```
or if you have conda run:
```
conda env create -f environment.yml
source activate tsp
```

# Instructions to run application
To run the application, you need to pass in arguments:
* '-i', the input file (for reading in the TSP Graph)
* '-o', the output file (for writing the final tour)
* '-t', the allotted time to complete tour search
(for when you want to do more in the world than just waiting for the most optimal tour)
```markdown
python tsp-3510.py -i 'dataset/tsp1000.txt' -o 'output_tour.txt' -t 20
```
All of the field are necessary, so do not skip any inputs!
