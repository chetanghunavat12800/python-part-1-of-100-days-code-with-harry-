print("Deviyon aur sajjano, aap sabhi ka bahut-bahut swagat hai. Main hoon Amitabh Bachchan, aur aap dekh rahe hain Kaun Banega Crorepati!\n\n")
print("Game Ke Rules jaanne ke liye apne keyboard par 1 dabaye aur game chalu krne ke liye 2 dabaye\n ")
while True:
  
  a=int(input("please enter your choice : "))
  match a:
   case 1:
      print("\nRules of the game are : ")
      print("1. There are 14 questions in the game. ")
      print("2. Questions from 1-5 are easy. \n And 6-10 are moderate level. \n And 11-14 are hard level.")
      print("2. You will get 4 options for each questions.\nAnd you have to correct option for prize")
      print("Ouestions from 1-5 are of 1000 rupees each and for 6-10 rupees 2000 and for 11-14 rupees 2500 each.\n ")

   case 2:
    questions = [
        [
            "Q1. Which is the smallest prime number?",
            "A. 0"
            "B. 1",
            "C. 2",
            "D. 3"
        ],
        [
            "Q2. Which blood group is known as the universal donor?",
            "A. A+",
            "B. B-",
            "C. O-",
            "D. AB+"
        ],
        [
            "Q3. Which Indian state is known as the 'Land of Five Rivers'?",
            "A. Haryana",
            "B. Punjab",
            "C. Rajasthan",
            "D. Gujarat"
        ],
        [
            "Q4. How many players are there in a cricket team on the field?",
            "A. 9",
            "B. 10",
            "C. 11",
            "D. 12"
        ],
        [
            "Q5. Which instrument is used to measure atmospheric pressure?",
            "A. Thermometer",
            "B. Hygrometer",
            "C. Barometer",
            "D. Ammeter"
        ],
        [
            "Q6. Who was the first Indian to receive the Nobel Prize?",
            "A. C. V. Raman",
            "B. Rabindranath Tagore",
            "C. Mother Teresa",
            "D. Amartya Sen"
        ],
        [
            "Q7. The SI unit of pressure is named after which scientist?",
            "A. Isaac Newton",
            "B. Blaise Pascal",
            "C. Michael Faraday",
            "D. James Watt"
        ],
        [
            "Q8. Which Mughal emperor built the Buland Darwaza?",
            "A. Shah Jahan",
            "B. Aurangzeb",
            "C. Akbar",
            "D. Humayun"
        ],
        [
            "Q9. Which layer of the Earth's atmosphere contains the ozone layer?",
            "A. Troposphere",
            "B. Stratosphere",
            "C. Mesosphere",
            "D. Thermosphere"
        ],
        [
            "Q10. Which Constitutional Amendment lowered the voting age in India from 21 to 18 years?",
            "A. 42nd Amendment",
            "B. 44th Amendment",
            "C. 61st Amendment",
            "D. 73rd Amendment"
        ],
        [
            "Q11. Which country has the longest coastline in the world?",
            "A. Russia",
            "B. Australia",
            "C. Canada",
            "D. Indonesia"
        ],
        [
            "Q12. Which vitamin is synthesized in the human skin when exposed to sunlight?",
            "A. Vitamin A",
            "B. Vitamin B12",
            "C. Vitamin D",
            "D. Vitamin K"
        ],
        [
            "Q13. Which Indian classical dance form originated in Kerala and is traditionally performed by male artists with elaborate makeup?",
            "A. Bharatanatyam",
            "B. Kathakali",
            "C. Kuchipudi",
            "D. Odissi"
        ],
        [
            "Q14. Which statement about prime numbers is correct?",
            "A. Every odd number is prime.",
            "B. Every prime number is odd.",
            "C. 2 is the only even prime number.",
            "D. Every prime number ends with 1, 3, 7, or 9."
        ]
    ]

    answers = [
        "C",  # Q1
        "C",  # Q2
        "B",  # Q3
        "C",  # Q4
        "C",  # Q5
        "B",  # Q6
        "B",  # Q7
        "C",  # Q8
        "B",  # Q9
        "C",  # Q10
        "C",  # Q11
        "C",  # Q12
        "B",  # Q13
        "C"   # Q14
    ]

    amount=[
      1000,1000,1000,1000,1000,2000,2000,2000,2000,2000,2500,2500,2500,2500
    ]
    k=0
    p=0
    amount_earned=0
    counter=0

    print("\n")

    for i in questions:
       for line in i:
         print(line)
       chosenopt=input("please choose the preffered opption: ").upper() 
       if(chosenopt==answers[k]):
           print("..... You choose the correct answer.....")
           amount_earned=amount_earned+amount[p]
           counter=counter+1

       else:
           print("----you choose the incorrect answer----")
           k=k+1
           p=p+1

      
       move=int(input("to move on next question please enter 0 "))
       if(move ==0):
           continue

       else:
           print("incorrect choice")

     

print("aapne kul",counter,"sawalo ke shai jawab diye hai")
print("toh devi aur sajjan aapki kul dhanrashi hui hai: ","₹",amount_earned)
print("\n\n\n 7 crore .........")






    

  
 