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

#deframe from: 
#https://stackoverflow.com/questions/73934726/turn-a-data-frame-column-into-vector-with-names-as-row-names

df2 <- mtcars[c(4,6)] #Remove Columns not needed for power-to-weight ratio
pwr.to.weight <- df2[1]/df2[2] #Calculate power-to-weight ratio
pwr.to.weight <- pwr.to.weight/1000 #Corrected values to HP/LBS
names(pwr.to.weight) <- c("pwr-to-wt")

#Find vehicle with largest power-to-weight ratio
row.names(pwr.to.weight)[which.max(pwr.to.weight$'pwr-to-wt')]



#----------------------------------------------------------------
#Plot the top five vehicles with the best power-to-weight ratios.
#----------------------------------------------------------------

#Using (https://www.programmingr.com/examples/r-dataframe/sort-r-data-frame/),
#Find the top five vehicles with largest pwr/wt ratio:
top.five<-pwr.to.weight[order(-pwr.to.weight$'pwr-to-wt'),][1:5]#From website

#Adding in vehicle model names:
names(top.five)<-row.names(pwr.to.weight)[order(-pwr.to.weight$'pwr-to-wt')[1:5]]

#Plotting the Top Five Vehicles:
barplot(top.five, names.arg = names(top.five), )

