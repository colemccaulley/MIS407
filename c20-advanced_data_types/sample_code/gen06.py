log = open("access_log")
# Create a list containing the column where the bytes transferred should be
bytecolumn = (line.rsplit(None,1)[1] for line in log)
# Filter the bytecolumn into a list: only select numeric values, and convert to int
bytes = (int(x) for x in bytecolumn if x != '-')
# Finally, sum the bytes and print:
print('The total bytes transfered = {:,}'.format(sum(bytes)))
log.close()
