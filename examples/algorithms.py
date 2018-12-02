def get_missing_numbers(array, count):

    print("Elenco %s, dimensione %d" % (array, count))
    
    if len(array) == count - 1:
        missing = sum(range(1, count+1)) - sum(array)
        print("Numero mancante: %s" % missing)
    
    else:
        missing = sorted(set(range(1, count+1)) - set(array))
        print("Numeri mancanti: %s" % missing)

    return missing


if __name__ == "__main__":
    get_missing_numbers([1, 2, 4, 5, 6], 6)
    get_missing_numbers([1, 3, 5, 6, 7, 9], 10)