from datetime import date

"""
    According to the BMJ Journal, 2021, "The WETFLAG ('Weight, Energy, 
Tube size, Fluid, Lorazepam, Adrenaline and Glucose') mnemonic is 
an aid to emergency calculations, used extensively in Emergency Departments
and Intensive Care Units worldwide and taught as part of the EPALS (European
Paediatric Advanced Life Support) course.
	When you are presented with a collapsed child, it helps to estimate 
and write down key drugs and equipment you may need (e-safe-anaesthesia.org).
WETFLAG is one means of preparation:
	(W)eight = (age+4) x 2 : this is the estimated weight of the child
	(E)nergy = 4 x weight (Joules) : this is the energy required for defibrillation
	(T)ube   = age/4 + 4 : (approx size of endotracheal tube uncuffed for intubation)
	(FL)uids = 20ml/kg of Normal Saline bolus
	(A)drenaline = 0.1ml/kg of adrenaline 1:10,000
	(G)lucose = 2ml/kg of 10% glucose
    """


def main():
    try:
        print()
        print("WETFLAG Calculator for Pediatric Resuscitation")
        print(f"\nPlease enter the child's Date of Birth:")

        day = input("Day: ")
        month = input("Month (ex: 7 for July): ")
        year = input("Year: ")
       
        age = calculate_age(int(day), int(month), int(year))
        print(f"\nAge of child: {age} years old")  

        if age < 1 or age > 16:
            print(f"Age is invalid. This calculator is suitable for ages 1-16 years only.\n")
        
        else:
            weight = calculate_weight(age)
            energy = calculate_energy(weight)
            tube_size = calculate_tube_size(age)
            fluids = calculate_fluids(weight)
            adrenaline = calculate_adrenaline_dose(weight)
            glucose = calculate_glucose_dose(weight)

            print()
            print(f"Calculations are based on the age of {age} years and Estimated Weight of {weight} kg:")
            print(f"Weight: {weight} kg")
            print(f"Energy: {energy:.0f} Joules")
            print(f"Endotracheal Tube Size: {tube_size:.2f} cm")
            print(f"Fluids: {fluids:.0f} ml of Normal Saline bolus")
            print(f"Adrenaline: {adrenaline:.2f} ml of Adrenaline 1:10,000")
            print(f"Glucose: {glucose:.0f} ml of 10% Glucose")
            print()
           
    except ValueError as val_err:
        print("Error:", val_err,
              f"\nFailed to calculate age. Either day or month or year is invalid.")
    
    except ZeroDivisionError as zero_err:
        print("Error:", zero_err, f"\nInvalid zero division.")

def calculate_age(day, month, year):
    today = date.today()    
    birthdate = date(year, month, day)   
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))    
    return age

def calculate_weight(age):
    weight = (age + 4) * 2
    return weight

def calculate_energy(weight):
    energy = 4 * weight
    return energy

def calculate_tube_size(age):
    tube_size = (age / 4) + 4
    return tube_size

def calculate_fluids(weight):
    fluids = 20 * weight
    return fluids

def calculate_adrenaline_dose(weight):
    adrenaline = 0.1 * weight
    return adrenaline

def calculate_glucose_dose(weight):
    glucose = 2 * weight
    return glucose


if __name__ == "__main__":
    main()
