library(vdemdata)
library(scales)
library(ggrepel)
library(readr)
library(plotly)
library(dplyr)
library(ggplot2)
library(ggridges)
library(ggthemes)
library(maps)
library(viridis)
library(tidyverse)
library(reshape2)


# covid -------------------------------------------------------------------

owid_covid_data <- read_csv("C:/Users/inesr/Downloads/owid-covid-data.csv")
colnames(owid_covid_data)

owid_covid_data <- owid_covid_data %>% map_if(is.numeric,~ifelse(is.na(.x),0,.x)) %>% as.data.frame()
owid_covid_data$date <- as.Date(owid_covid_data$date, format= "%Y-%m-%d")
owid_covid_data_original <- owid_covid_data

#correlation heatmap

#Prepare the data covid data are used :
owid_covid_data = owid_covid_data_original %>% filter(date>= "2021-01-01",total_deaths>0, total_cases>0,
                                                      location !="World", location!="Upper middle income", 
                                                      location!="Lower middle income", location !="Asia" , location !="Oceania",
                                                      location!="Europe", location!="High income", location !="European Union",
                                                      location !="North America", location !="South America" , 
                                                      location !="Gibraltar") %>% group_by(date) %>%
  summarise( vac_pop=mean(people_fully_vaccinated),
                     deaths_pop=sum(new_deaths), 
                     cases_pop = sum(new_cases)/max(population))
mydata <- owid_covid_data[, c(2,3,4)]
head(mydata)
#Correlation matrix can be created using the R function cor() :
cormat <- round(cor(mydata),2)
head(cormat) 


library(reshape2)
melted_cormat <- melt(cormat)
head(melted_cormat)
ggplot(data = melted_cormat, aes(x=Var1, y=Var2, fill=value)) + 
  geom_tile()

# Get lower triangle of the correlation matrix
get_lower_tri<-function(cormat){
  cormat[upper.tri(cormat)] <- NA
  return(cormat)
}
# Get upper triangle of the correlation matrix
get_upper_tri <- function(cormat){
  cormat[lower.tri(cormat)]<- NA
  return(cormat)
}

upper_tri <- get_upper_tri(cormat)

# Melt the correlation matrix
melted_cormat <- melt(upper_tri, na.rm = TRUE)

# Heatmap
ggplot(data = melted_cormat, aes(Var2, Var1, fill = value))+
  geom_tile(color = "white")+
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                       midpoint = 0, limit = c(-1,1), space = "Lab", 
                       name="Pearson\nCorrelation") +
  theme_minimal()+ 
  theme(axis.text.x = element_text(angle = 45, vjust = 1, 
                                   size = 12, hjust = 1))+
  coord_fixed()

# Helper function to reorder the correlation matrix :

reorder_cormat <- function(cormat){
  # Use correlation between variables as distance
  dd <- as.dist((1-cormat)/2)
  hc <- hclust(dd)
  cormat <-cormat[hc$order, hc$order]
}

# Reorder the correlation matrix
cormat <- reorder_cormat(cormat)
upper_tri <- get_upper_tri(cormat)
# Melt the correlation matrix
melted_cormat <- melt(upper_tri, na.rm = TRUE)
# Create a ggheatmap
ggheatmap <- ggplot(melted_cormat, aes(Var2, Var1, fill = value))+
  geom_tile(color = "white")+
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                       midpoint = 0, limit = c(-1,1), space = "Lab", 
                       name="Pearson\nCorrelation") +
  theme_minimal()+ # minimal theme
  theme(axis.text.x = element_text(angle = 45, vjust = 1, 
                                   size = 12, hjust = 1))+
  coord_fixed()
# Print the heatmap
print(ggheatmap)

# Add correlation coefficients on the heatmap
ggheatmap + 
  geom_text(aes(Var2, Var1, label = value), color = "black", size = 4) +
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    panel.grid.major = element_blank(),
    panel.border = element_blank(),
    panel.background = element_blank(),
    axis.ticks = element_blank(),
    legend.justification = c(1, 0),
    legend.position = c(0.6, 0.7),
    legend.direction = "horizontal")+
  guides(fill = guide_colorbar(barwidth = 7, barheight = 1,
                               title.position = "top", title.hjust = 0.5))
