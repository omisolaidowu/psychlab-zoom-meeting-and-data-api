from datetime import datetime

class ConvertTime:
    def convert_date_format(self, date_string):
        date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")

        formatted_date = date.strftime("%a, %d %b, %Y")
        
        return formatted_date