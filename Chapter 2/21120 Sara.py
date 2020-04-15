print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#minimize the number of print() function invocations by inserting the \n sequence into the strings
print("     *\n    * *\n   *   *\n  *     *\n ***   ***\n   *   *\n   *   *\n   *****")

#make the arrow twice as large (but keep the proportions)
print("      *")
print("     * *")
print("    *   *")
print("   *     *")
print("  *       *")
print(" *         *")
print("****     ****")
print("   *     *")
print("   *     *")
print("   *     *")
print("   *     *")
print("   *******")

#duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)

#remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?
print(    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
#EOL while scanning string literal; the error exists on the line with the missing quote
          
#do the same with some of the parentheses;
print"    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
#Invalid syntax; the error exists on the line with the missing quote

#change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
Print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
##NameError: name 'Print' is not defined

#replace some of the quotes with apostrophes; watch what happens carefully.
print('    *")
print('   * *")
print('  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
##SyntaxError: EOL while scanning string literal on first line with apostrophe
