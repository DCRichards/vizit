"""

#    # # ###### # ##### 
#    # #     #  #   #   
#    # #    #   #   #   
#    # #   #    #   #   
 #  #  #  #     #   #   
  ##   # ###### #   #  
  
Simple dependency visualisation
by DCRichards

"""

import os

import parser
import graphs
import cli
import languages

def _create_graph(directory, lang):
    graphs.generate(parser.parse(directory, lang))
    
def main():
    cli_args = cli.get_args()
    _create_graph(cli_args[0], languages.get(cli_args[1]))
    
main()