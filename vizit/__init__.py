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
    
def main(dir, regex):
    graphs.generate(parser.parse(dir, regex))