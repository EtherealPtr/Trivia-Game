import pickle
import sys

def open_file(fileName, accessMode) :
    """Opens an external file"""
    try :
        f = open(fileName, accessMode);
    except  IOError as e:
        print("Unable to open file ", fileName, "\n ", e);
        sys.exit();
    else :
        return f;

def next_line(file) :
    """Returns next line from the trivia file"""
    line = file.readline();
    line = line.replace(" \ ", "\n");
    return line;

def read_block(file) :
     """Return the next block of data from the trivia file"""
     category = next_line(file);
     question = next_line(file);
     answers = [];
     
     for i in range(0, 4) :
            answers.append(next_line(file));

     correct = next_line(file)[8 : 14].strip();     # Read correct answer
     points = next_line(file)[7 : 14].strip();      # Read points
     next_line(file);
     
     return category, question, answers, correct, points;

def game_instructions() :
    """Introduces the game rules to the player"""
    print("\t\tWelcome to the Physics Trivia Challenge!\n", end = "");
    print("\tAttempt to select the correct answer to score some points!\n");
    
def main() :
    f = open_file("Trivia.txt", "r");
    game_instructions();
    gameOver = False;
    score = 0;
    
    while not gameOver : 
        category, question, answers, correct, points = read_block(f);
         
        if (category == "") :
            gameOver = True;
            print("Thanks for playing! Your total score is: ", score);
            continue;
            
        print("Current score is: ", score);
        print("Topic: ", category, end="");
        print("Question: ", question, end="");

        # print all the answers
        for line in answers :
            print(line, end="");

        try :
            answer = int(input("Answer: "));
        except ValueError:
            print("That's not a number!");
        else :
            if (answer == int(correct)) :
                print("Correct answer!");
                score += float(points);
            else :
                print("Incorrect answer");

        print();

    f.close();

main();
