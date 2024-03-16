# Make a function so that it can be called from other scripts
def getlatlon(city, country):
    import csv

    # Complicated - opens the file and stores it as 'file'
    with open('cities.csv', 'r', encoding='utf8') as file:

        # Reads the files data
        reader = csv.reader(file)

        for line in reader:

            # Makes both the input city and the csv city lowercase and removes whitespaces (e.g. space)
            csv_city = line[1].strip().lower()
            input_city = city.strip().lower()

            # Makes both the input country and the csv country lowercase and removes whitespaces (e.g. space)
            csv_country = line[7].strip().lower()
            input_country = country.strip().lower()

            if input_city == csv_city and input_country == csv_country:

                lat = float(line[8])
                lon = float(line[9])

                return lat, lon
            
    
    #return None, None