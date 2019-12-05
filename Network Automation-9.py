
    # -------Write output to a file-------------------

    router
    # friendly
    RN=['R1','R2','R3','R4','R5']
        time.sleep(wait)
        output = connection.read_very_eager()
        RN[router] = open("RN", "w")
        RN[router].write(output)
        RN[router].close 


    



