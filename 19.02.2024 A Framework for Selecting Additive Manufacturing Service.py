#!/usr/bin/env python
# coding: utf-8

# In[19]:


def ask_question(question):
    while True:
        response = input(question + " (yes/no): ").lower()
        if response in ['yes', 'no']:
            return response
        else:
            print("Error: Please enter 'yes' or 'no'.")

 

questions = [ 

    "Have you identified the parts for AM?", 

    "Do you want to select 3D-CAD models from 3D Printing Service Bureau Database?", 

    "Are you looking to identify suitable parts for 3D printing through a 3D printing service bureau?", 

    "Do you have a 3D model of part?", 

    "Do you have a 2D Data of the part?", 

    "Do you have a physical part?", 

    "Do you have a Conceptual (idea or concept) model?", 

    "Do you need optimization in your design?", 

    "Do you want to 3D print the part?", 

    "Does your part require accuracy < 0.20 mm?", 

    "Does your part require surface finish < 10 Ra?", 

    "Does your part have the requirement of heat treatment?", 

    "Does your part have specific requirements like surface treatment, coating, etc.?", 

    "Does your part have the specific inspection or testing requirements?", 

    "Does your part have Specific Functional, Application etc. requirements?" 

] 

 

# Define the services 

services = ["Evaluative service", "Generative service", "Selective service","Facilitative service"] 

 

# Initialize a dictionary to keep track of the counts 

service_counts = {service: 0 for service in services} 

 

# Define the Sub_services 

Sub_services = ["Explorative service", "Constructive service", "Decisive service"] 

 

# Initialize a dictionary to keep track of the counts 

Sub_service_counts = {Sub_service: 0 for Sub_service in Sub_services} 

 

# Start with the first question 

current_question_index = 0 

 

while current_question_index < len(questions): 

    current_question = questions[current_question_index] 

 

    if current_question_index == 0: 

        response = ask_question(current_question) 

        if response == "yes": 

            current_question_index = 3 

        else: 

            current_question_index = 1 

    elif current_question_index == 1: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("Selection and Customization of an existing 3D-CAD model from database") 

            selected_service = "Selective service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 

            current_question_index = 7 

        else: 

            current_question_index = 2 

    elif current_question_index == 2: 

        response = ask_question(current_question) 

        if response == "no": 

            break 

        else: 

            print("Part Evaluation") 

            selected_service = "Evaluative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 

            current_question_index = 3 

    elif current_question_index == 3: 

        response = ask_question(current_question) 

        if response == "yes": 

            current_question_index = 7 

        else: 

            current_question_index = 4 

    elif current_question_index == 4: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("3D-CAD model creation from 2D data") 

            selected_service = "Generative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 

            current_question_index = 7 

        else: 

            current_question_index = 5 

    elif current_question_index == 5: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("3D-CAD model creation through reverse engineering") 

            selected_service = "Generative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 

            current_question_index = 7 

        else: 

            current_question_index = 6 

    elif current_question_index == 6: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("3D-CAD model creation from the concept or idea") 

            selected_service = "Generative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 

            current_question_index = 7 

        else: 

            break 

    elif current_question_index == 7: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("Design Optimization") 

            selected_service = "Generative service" 

            if selected_service in services: 

                if service_counts[selected_service] > 0: 

                    service_counts[selected_service] += 1 

            selected_service = "Selective service" 

            if selected_service in services: 

                if service_counts[selected_service] > 0: 

                    service_counts[selected_service] += 1 

            current_question_index = 8 

        else: 

            current_question_index = 8 

    elif current_question_index == 8: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("Part printing (Fabrication) & Support Removal") 

            selected_service = "Facilitative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 

            current_question_index = 9 

        else: 

            break 

    elif current_question_index == 9: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("Machining or Surface Finishing and Polishing") 

            selected_service = "Facilitative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 

            current_question_index = 10 

        else: 

            current_question_index = 10 

    elif current_question_index == 10: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("Machining or Surface Finishing and Polishing") 

            selected_service = "Facilitative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 

            current_question_index = 11 

        else: 

            current_question_index = 11 

    elif current_question_index == 11: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("Heat Treatment and Post Curing") 

            selected_service = "Facilitative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 

            current_question_index = 12 

        else: 

            current_question_index = 12 

    elif current_question_index == 12: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("Painting and Coating") 

            selected_service = "Facilitative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 

            current_question_index = 13 

        else: 

            current_question_index = 13 

    elif current_question_index == 13: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("Quality Inspection and Testing") 

            selected_service = "Facilitative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1 
          
            current_question_index = 14 

        else: 

            current_question_index = 14 

    elif current_question_index == 14: 

        response = ask_question(current_question) 

        if response == "yes": 

            print("Specific Functional, Application etc. requirements") 

            selected_service = "Facilitative service" 

            if selected_service in services: 

                service_counts[selected_service] += 1
                
        print("Packaging and Shipping")         

        break 
        

#print(service_counts)  

#Result Printing Logic


# Check and print results
non_zero_count_services = [service for service, count in service_counts.items() if count > 0]

if len(non_zero_count_services) == 1:
    
    print(non_zero_count_services[0])
    
elif len(non_zero_count_services) > 1:
    
    # Check if both Evaluative service and Generative service counts are greater than 0 

    if service_counts["Evaluative service"] > 0 and service_counts["Generative service"] > 0: 

        Sub_selected_service = "Explorative service" 

        #print(Sub_selected_service) 

        if Sub_selected_service in Sub_services: 

            Sub_service_counts[Sub_selected_service] += 1 

    # Check if Generative service and Facilitative services counts are greater than 0 

    if service_counts["Generative service"] > 0 and service_counts["Facilitative service"] > 0: 

        Sub_selected_service = "Constructive service" 

        #print(Sub_selected_service) 

        if Sub_selected_service in Sub_services: 

            Sub_service_counts[Sub_selected_service] += 1   

    if service_counts["Evaluative service"] > 0 and service_counts["Facilitative service"] > 0: 

        Sub_selected_service = "Decisive service" 

        #print(Sub_selected_service) 

        if Sub_selected_service in Sub_services: 

            Sub_service_counts[Sub_selected_service] += 1  

    if service_counts["Selective service"] > 0 and service_counts["Facilitative service"] > 0: 

        print("Selective service") 
       

    non_zero_count_Sub_services = [Sub_service for Sub_service, count in Sub_service_counts.items() if count > 0]
    
    if len(non_zero_count_Sub_services) == 1:
    
        print(non_zero_count_Sub_services[0])
    
    elif len(non_zero_count_services) > 1:
    
    # Check if both Evaluative service and Generative service counts are greater than 0 

        if Sub_service_counts["Explorative service"] > 0 and Sub_service_counts["Constructive service"] > 0: 

            print("Assistive service")


#print(Sub_service_counts)

# End of code 

print("End of the process")


# In[ ]:





# In[ ]:




