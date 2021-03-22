# gpt_launcher
python function ables to process any *xml file whose is created by SNAP

Identify the path to the gpt in your machine. This is the path in my windows 10 "C:\Program Files\snap\bin\gpt'"
gpt_path = r'C:\Program Files\snap\bin\gpt' # If it is in your PATH environment variable you can just use 'gpt'

Identify the path to the *.xml file whose is created by you to implement any process. 
graph_path = r'D:\pyrosar_test\outname_proc.xml'
# applying the function needs both the gpt path and the *.xml file path
SentinelGraph(gpt_path, graph_path)
