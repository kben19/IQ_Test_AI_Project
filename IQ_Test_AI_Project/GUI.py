from appJar import gui
import IQAgent

class GUI:

    def __init__(self):
        self.app = gui("Login Window", "600x500")
        self.agent = None
        self.createGUI()

    def createGUI(self):
         # create a GUI variable called self.app
        self.app.setBg("white")
        self.app.setFont(18)

        # add & configure widgets - widgets get a name, to help referencing them later
        self.app.addLabel("title", "IQ Test Artificial Intelligence")

        # MAIN WINDOW
        self.app.addLabel("text1", "Question:")
        self.app.addTextArea("Question")
        self.app.addLabel("answertext", "Answer:")
        self.app.addLabel("answer", "")

        # add listener into the buttons
        self.app.addButtons(["Solve"], self.solveButton)
        self.app.addButtons(["Edit Knowledge", "Solve File"], self.subWindow1)

        # SUB WINDOW KNOWLEDGE
        self.app.startSubWindow("knowledge")
        self.app.addLabel("OddOneOut", "Odd One Out Knowledge")
        self.app.addFileEntry("file")
        self.app.addButtons(["Save", "Load"], self.knowledge)
        self.app.addButtons(["Back"], self.back1)
        self.app.stopSubWindow()

        # SUB WINDOW SOLVE FILE
        self.app.startSubWindow("solveFile")
        self.app.addLabel("sub1", "Question File:")
        self.app.addFileEntry("questions file")
        self.app.addLabel("sub2", "Answer File:")
        self.app.addFileEntry("answers file")
        self.app.addLabel("sub3", "Output File:")
        self.app.addFileEntry("output file")
        self.app.addButtons(["Run"], self.solveFileButton)
        self.app.addLabel("questions",  "Questions : 0")
        self.app.addLabel("correct",    "Correct   : 0")
        self.app.addLabel("wrong",      "Wrong     : 0")
        self.app.addButtons(["Back to Main Menu"], self.back2)
        self.app.stopSubWindow()


    def addAgent(self, anAgent):
        self.agent = anAgent

    def startApp(self):
        # start the GUI
        self.app.go()

    # Sub window button listener
    def subWindow1(self, button):
        if button == "Edit Knowledge":
            self.app.showSubWindow("knowledge")
        elif button == "Solve File":
            self.app.showSubWindow("solveFile")

    # solve button listener
    def solveButton(self):
        self.agent.inputText(self.app.getTextArea("Question"))
        self.app.setLabel("answer", self.agent.getAnswer(0))

    # Knowledge button listener
    def knowledge(self, button):
        if self.app.getEntry("file") != "":
            if button == "Save":
                self.agent.saveFile(self.app.getEntry("file"))
            elif button == "Load":
                self.agent.loadFile(self.app.getEntry("file"))
            self.app.hideSubWindow("knowledge")

    # Solve file button listener
    def solveFileButton(self):
        if self.app.getEntry("questions file") != "":
            self.agent.testQuestions(self.app.getEntry("questions file"))
            if self.app.getEntry("answers file") != "":
                correct, wrong = self.agent.checkAnswers(self.app.getEntry("answers file"))
                self.app.setLabel("questions", "Questions : " + str(correct+wrong))
                self.app.setLabel("correct",   "Correct   : " + str(correct))
                self.app.setLabel("wrong",     "Wrong     : " + str(wrong))
            if self.app.getEntry("output file") != "":
                self.agent.outputAnswers(self.app.getEntry("output file"))

    def back1(self):
        self.app.hideSubWindow("knowledge")

    def back2(self):
        self.app.hideSubWindow("solveFile")
