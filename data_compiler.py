
# remove the following comment line after implementing
# it is just there to temporarily suppress a warning in the unimplemented function


# noinspection PyUnusedLocal
def compile_data(stopping_voltages, photocurrents):

    # We have two data arrays. The photocurrents are the independent (y) values. The stopping voltages
    # are the dependent (x) values.

    # These need to be compiled into a single dictionary whose keys are the x values and whose values are
    # tuples containing the sum of y values, the sum of the squares of the y values, and their count.

    # NOT YET IMPLEMENTED.
    # Follow the above comments to turn the two arrays above into a single dictionary. with the keys and values
    # as described.
    combined_data = {}
    count = 1
    for x in range(len(stopping_voltages)):
        try:
            key_check = combined_data.get(stopping_voltages[x])
            if key_check == None:

                 combined_data[stopping_voltages[x]] = photocurrents[x], photocurrents[x] * photocurrents[x], count
                 count += 1

        except KeyError:
            print("Error")


    return combined_data
