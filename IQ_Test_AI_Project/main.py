import GUI
from IQAgent import AgentController
from QuestionGenerator import QuestionGeneratorDriver


def odd_one_out_Test(num):
    ### ODD ONE OUT AGENT LEARN AND TEST IN LARGE INPUT ###
    num = num / 2
    Agent = AgentController.AgentController()
    myGenerator = QuestionGeneratorDriver.QuestionGeneratorDriver(Agent.getAgent(3))
    myGenerator.learnSamples("resources\odd_one_out_country.txt", "resources\odd_one_out_country_continent.txt", 5, int(num))   # Learn countries based on continent
    myGenerator.learnSamples("resources\odd_one_out_country.txt", "resources\odd_one_out_country_region.txt", 22, int(num))     # Learn countries based on region
    print (myGenerator.testSamples("resources\odd_one_out_country.txt", "resources\odd_one_out_country_continent.txt", 5, 500)) # Print wrong answers on country continents questions
    print (myGenerator.testSamples("resources\odd_one_out_country.txt", "resources\odd_one_out_country_region.txt", 22, 500))   # Print wrong answers on country region questions


def generateQuestionFile():
    ### OUTPUT GENERATED QUESTIONS INTO FILE ###

    myGenerator = QuestionGeneratorDriver.QuestionGeneratorDriver(anAgent.getAgent(3))
    myGenerator.outputQuestions("resources\question2.txt", "answer2.txt", "resources\odd_one_out_country.txt", "resources\odd_one_out_country_continent.txt", 5, 1000, 1)   # Generate continents odd one out
    myGenerator.outputQuestions("resources\question3.txt", "answer3.txt", "resources\odd_one_out_country.txt", "resources\odd_one_out_country_region.txt", 22, 1000, 1)     # Generate regions odd one out

def agent_Learn(agent, num):
    myGenerator = QuestionGeneratorDriver.QuestionGeneratorDriver(agent)
    myGenerator.learnSamples("resources\odd_one_out_country.txt", "resources\odd_one_out_country_continent.txt", 5, int(num))   # Learn countries based on continent
    myGenerator.learnSamples("resources\odd_one_out_country.txt", "resources\odd_one_out_country_region.txt", 22, int(num))     # Learn countries based on region

def Agent_Single_Test():
    ### AGENT SINGLE TEST ###
    # Odd one out

    agent_Learn(anAgent.getAgent(3), 1000)  # Agent learning the country names

    anAgent.inputText("Odd one out: Germany, Austria, Australia, Belgium")    #Correct answer Australia
    print(anAgent.getAnswer(0))
    anAgent.inputText("Odd one out: New Zealand, South Korea, Indonesia, North Korea")    #Correct answer New Zealand
    print(anAgent.getAnswer(0))
    anAgent.inputText("Odd one out: Vietnam, China, Japan, South Korea")      #Correct answer Vietnam
    print(anAgent.getAnswer(0))

    # Number

    anAgent.inputText("What is the next number of 7 11 13 17 19 23 ?")      #Correct answer 29
    print(anAgent.getAnswer(0))

    # Direction

    anAgent.inputText("walked 15 m towards west. Turned left and walked 20 m. Turned left and walked 15 m. Turned right and walked 12 m")   #Correct answer 32 to the south
    print(anAgent.getAnswer(0))
    anAgent.inputText("walked 15 m towards west. Then, turned left, right, and left again with 10, 5, and 20 respectively.")    #Correct answer 36.05 to south west
    print(anAgent.getAnswer(0))

# MAIN FUNCTION
if __name__ == "__main__":
    myView = GUI.GUI()  # create the GUI
    anAgent = AgentController.AgentController() # Instatiating the IQ Solver agent
    myView.addAgent(anAgent)    # Add the agent into the GUI

    # Comment the line below to use debugging purposes
    myView.startApp()     # Start the application interface

    ### DEBUGGING PURPOSES ###

    # odd_one_out_Test(2000)
    # generateQuestionFile()
    # Agent_Single_Test()



