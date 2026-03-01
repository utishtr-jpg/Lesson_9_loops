num=int(input("Enter a number"))
expo= int(input("Please enter the exponent"))
result=1
for i in range(expo):
    result= result*num
    print("The number power exponent in loop {} is {}".format(i,result))
#Alternate ending: using pow function
end_result= pow(num,expo)
print("The answer using the inbuilt pow function is", end_result)

#end