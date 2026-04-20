#SyHeart
#This is a demo of a virtual doctor that evaluates blood pressure and gives medical recommendations 

#Features:
# - checks systolic and diastolic pressure
# - detects hypertensive crisis, stage 1 and stage 2 hypertension
# - suggests what to do

#This is a product by Kosmoxia Labs

CLASSIFY_PRESSURE_VALUES = {
    "hypertensive_crisis" : "This is an emergency. You are in a hypertensive crisis. You must call an ambulance immediately.",
    "stage_2" : "You suffer from stage 2 hypertension. I strongly recommend to go to the hospital as soon as possible",
    "stage_1" : "You suffer from stage 1 hypertension. I recommend to see your doctor in a few days",
    "elevated" : "Your pressure is slightly elevated. "
                  "\nIf I were you, I would see my doctor to understand if I must take some kind of medicine",
    "normal" : "Your pressure is normal!",
    "low" : "Your pressure is quite low. I recommend to eat something sweet",
    "hypotension" : "Your pressure is definitely too low. I strongly recommend to consult your doctor"
    }


#Define a function which ask user's menu choice
def menu_option():
    while True:
     menu()
     choice = input("\n What do you want to do? ")
     if choice == "1":
        check_blood_pressure()
        break
     elif choice == "2":
        print("That's not available yet. Try next time")
        break     
     elif choice == "3":
        print("Ok, goodbye!")
        break
     else:
        print("Please, insert 1, 2 or 3")
        continue


#Define a function that ask to user if his answer is yes or no
def ask_yes_or_no(question):
    while True:
        answer = input(question).lower().strip()
        if "yes" in answer:
            return True
        elif "no" in answer:
            return False
        else: 
            print("Please, insert yes or no")
            continue


def menu():
    print("\n" + "="*40)
    print("SYHEART")
    print("="*40)
    print("\n 1. Check your blood pressure")
    print("\n 2. Check your BMI (coming soon!)")
    print("\n 3. Exit")


#Define a function to ask user's pressure values
def correct_pressure_values(pressure):
    while True:
        try:
            value = int(input(pressure))
            if 30 <= value <= 280: #Define a realistic range of values
               return value
            else:
                print("Please, insert realistic values") 
        except ValueError: #Correct any user's error
            print("Please, insert a valid number") 


#Define a function that classify the pressure values
def classify_pressure_values(systolic : int, diastolic : int):
    if systolic >= 180 or diastolic >= 120:
        return "hypertensive_crisis"
    elif 140 <= systolic < 180 or 90 <= diastolic < 120:
        return "stage_2"
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        return "stage_1"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "elevated"
    elif 110 <= systolic < 120 and 70 <= diastolic < 80:
        return "normal"
    elif 90 <= systolic < 110 and 60 <= diastolic < 70:
        return "low"
    else:
        return "hypotension"

def check_blood_pressure():
     systolic = correct_pressure_values("Ok, now I have to ask you two questions. First of all, what's the systolic blood pressure value? ")
     diastolic = correct_pressure_values("What's the diastolic blood pressure value? ")
     category = classify_pressure_values(systolic, diastolic)

    #Recommend what to do in case of a hypertensive crisis
     if category == "hypertensive_crisis":
        while True:
            print(CLASSIFY_PRESSURE_VALUES["hypertensive_crisis"])
            ask_symtomps = ask_yes_or_no("Do you have any symtomps at the moment? ")
            if  ask_symtomps:
                symtomps = input("Ok, don't panic. May I know which ones? ").lower().strip()
                if "headache" in symtomps or "chest pain" in symtomps or "tachycardia" in symtomps:
                   print(f"This is a serious situation. I strongly recommend to call {emergency_number} right now")
                else: 
                    print(f"Even if I don't recognize these symptoms as the hypertensive crisis ones, your pressure is too high. Please call {emergency_number} immediately")
                break
            else:
                print("Ok, that's good. However you still must go to the hospital immediately")
                break
           
    #Recommend what to do in case of stage 2 hypertension
     elif category == "stage_2":
        print(CLASSIFY_PRESSURE_VALUES["stage_2"])
    
    #Recommend what to do in case of stage 1 hypertension
     elif category == "stage_1":
        while True:
            print(CLASSIFY_PRESSURE_VALUES["stage_1"])
            ask_stage1_advices = ask_yes_or_no("Would you like some advices to keep your blood pressure low? ")
            if ask_stage1_advices:
                print("Ok, here some advices! \nFirst of all, reduce alcohol and abolish tobacco." \
                "\nThen, you have to drastically limit the added salt" \
                "\nEventually, practice aerobic activity regularly")
                break
            else:
                print("Ok, goodbye then! See you next time!")
                break
           
    #Checking if the user's blood pression is elevated
     elif category == "elevated":
        print(CLASSIFY_PRESSURE_VALUES["elevated"])
        elevated_advices = ask_yes_or_no("Would you fancy some advices to keep the blood pressure low? ")
        if elevated_advices:
            print("Here my advices:\n" \
            "1. Don't exceed 5 grams of salt per day\n" \
            "2. Avoid smoking and drastically limit alcohol consumption")
        else:
            print("Ok, see you soon!")
 
    #Checking if the user's blood pression is normal
     elif category == "normal":
        print(CLASSIFY_PRESSURE_VALUES["normal"])
    
    #Checking if the user's blood pressure is low
     elif category == "low":
         print(CLASSIFY_PRESSURE_VALUES["low"])

    #Recommend what to do in case of hypotension
     else:
         print(CLASSIFY_PRESSURE_VALUES["hypotension"])
         hypotension_advices = ask_yes_or_no("Would you like some advices to raise the blood pressure? ")
         if hypotension_advices:
             print("Here my advices!\n" \
             "1. First of all, drink some water immediately. If you want add salt\n" \
             "2. Lie down and raise your legs to promote venous return\n" \
             "3. Increase your water intake and consume fruits and vegetables, especially during the warmer months. " \
             "\nPure licorice can help thanks to its glycyrrhizin content.")
         else:
             print("Ok, see you next time!")


print("Hi, welcome to SyHeart! (v01)")
print("WARNING: This is a prototype only and is not a substitute for the advice of a real doctor. " \
      "\nIf you need help, please consult your doctor.")

#Ask user's name
name = input("Hi! What's your name? ")

#Asking about the country's emergency number
emergency_number = input("What's your country's emergency number? ")

menu_option()

#Ask to the user if he wants to try again SyHeart
while True:
    final_answer = ask_yes_or_no("Would you like to try SyHeart again? ")
    if final_answer:
        menu_option()
    else:
        print("Thank you for using SyHeart!")
        break