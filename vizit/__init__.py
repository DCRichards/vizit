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

def _create_graph(directory, lang, js):
    graphs.generate(parser.parse(directory, lang), js)
    
def main():
    cli_args = cli.get_args()
    _create_graph(cli_args[0], languages.get(cli_args[1]), cli_args[2])
    
main()