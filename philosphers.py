# this program writes three lines of data
# to a file.
def main():
    outfile = open("philosophers.txt",'w')

#write the names of three philosphers to the file.
    outfile.write('John Locke' + '\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke')
    # Close the file
    outfile.close()
# Call the main function
main()