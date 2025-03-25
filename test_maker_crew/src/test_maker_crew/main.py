import sys
import yaml
from test_maker_crew.crew import TestWriterCrew
from crewai_tools import FileWriterTool,FileReadTool

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Test making Crew")
    print('-------------------------------')

    # with open('src/test_maker_crew/config/gamedesign.yaml', 'r', encoding='utf-8') as file:
    #     examples = yaml.safe_load(file)
    topic = "the topic is the history of Tea  - the test must include what kind of different Teas there were, " \
    "what ways did people make their tea before and more that you will think of"
    main_topic = "History of Tea"
    inputs = {
        'game' :  "hangman hame with inputs from the console",
        "topic":topic,
        "main_topic":main_topic
    }
    test= TestWriterCrew().crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## Here is the test")
    print("########################\n")
    print("Test: ")
    print(test)
    with open(f"tests/{main_topic}.txt", "w") as file:
        file.write(test.raw)
    # file_writer_tool = FileWriterTool()
    # res= file_writer_tool._run(filename='gamecode0102.txt',content= game,directory = 'result')
    # print(res)
    # file_read_tool = FileReadTool(file_path='result/gamecode0102.txt')
    # print(file_read_tool)

# def train():
#     """
#     Train the crew for a given number of iterations.
#     """

