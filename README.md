# VizIt

A simple dependency visualisation project

## About

VizIt represents dependencies in programming languages using a network graph. This project exists for a number of reasons:

* To help me learn Python
* To actually be useful in visualising dependencies 
* ...um, because I just like programming

## Examples

Usage and more detailed information coming soon. For now, here's an example from the prototype:

![](https://raw.githubusercontent.com/DCRichards/vizit/master/examples/example_graph.png)

## Setup

Installation using pip:

    git clone https://github.com/DCRichards/vizit.git
    cd vizit
    sudo pip install -e vizit/
    
# Usage

    -h, --help    show this help message and exit
    -v            display version information
    -d dir        root directory to search, by default this is the current directory
    -l language   programming language (*required)
    -j json       location of a .json file to export graph data to for external display    

Examples:

    vizit -l python -d ~/Downloads/vizit
    vizit -l c
    
Supported Languages:

* Python (python)
* C (c)
* Objective-C (objectivec)

## Libraries

* [NetworkX](http://networkx.github.io/documentation/latest/overview.html)

## Contributing

Python isn't my main language so if you think you've found a bug or just want to help me improve then submit an issue or pull request.
