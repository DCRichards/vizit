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
from languages import Languages
    
def main(dir, lang):
    graphs.generate(parser.parse(dir, lang))