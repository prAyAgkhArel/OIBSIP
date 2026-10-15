class BMICalculator:
    def calculate_bmi(self, weight, height):
        return weight/(height**2)
    
    def get_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese" 