library(UsingR)
attach(mtcars)


#---------------------------
#MPG by number of cylinders:
#---------------------------

# This method was adapted from an example on Statology:
# https://www.statology.org/r-mean-by-group/
df <- aggregate(mpg, by=list(cyl), FUN=mean)
#This is used to find average MPG by number of cylinders. 

View(df) #To determine which Columns need to be renamed.

names(df) <- c("# of Cylinders", "Average MPG") #To rename both columns.

#Graphing results, which show expected results:
barplot(df$`Average MPG`, names.arg = df$`# of Cylinders`,
        main = "Relationship Between # of Cylinders and Fuel Economy",
        xlab = "Number of Cylinders",
        ylab = "Average Fuel Economy (MPG)")



#------------------------------------------
#Which car had the largest HP/Weight Ratio?
#------------------------------------------

df2 <- mtcars[c(4,6)] #Remove Columns not needed for power-to-weight ratio
pwr.to.weight <- df2[1]/df2[2] #Calculate power-to-weight ratio

pwr.to.weight #Check Column name
?mtcars #To check the units, discovered weight is in 1000lbs units
pwr.to.weight <- pwr.to.weight/1000 #Corrected values to HP/LBS
names(pwr.to.weight) <- c("pwr-to-wt")

#Find vehicle with largest power-to-weight ratio
row.names(pwr.to.weight)[which.max(pwr.to.weight$'pwr-to-wt')]


