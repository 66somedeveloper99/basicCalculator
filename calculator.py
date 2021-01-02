print('*'*20,'\n')
print('\t→\twrite the calculation in Python format (i.e \'2**3\' will result in 8 )')
while True :      
      logfile = open('.log','a') # LOG
      calc = input('insert a calculation:\t')
      logfile.write(">> "+calc+'\n') # LOG
      logfile.close()# LOG
      file = open('calculator.py','r').readlines()
      nfile = open('calculator.py','w')
      nfile.write("logfile = open(\'.log\',\'a\')\n")# LOG 
      nfile.write("logfile.write(str(float("+calc+"))+\'\\n\')\n")# LOG
      nfile.write("logfile.close()\n")# LOG
      nfile.write('import math\nresult = float('+calc+')\n')
      nfile.write('print(\"the result is:\\t\\t\",(result))')
      nfile.close()
      try:
            import os 
            os.system('python calculator.py')
      except Exception as n :
            rise(n)
      bfile = open('calculator.py','w')
      for line in file:
            bfile.write(line)
      bfile.close()