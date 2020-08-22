# 🐎 Exploring Trends in International Dressage

I've had a passion for horses since I was a young child. What better way to dive into my first ever data project than to try and learn something new about something I love? 

I decided to scrape some data on dressage competitions from the international governing body for equestrian sport, the Fédération Equestre Internationale (FEI), using the [Scrapy](https://scrapy.org/) framework. I chose the top 100 ranked dressage horses, and traced them back two generations to their grandparents. I then worked my way back down the pedigree, collecting pedigree and competition data on each of the grandparents' descendants. Data were scraped into two tables in a SQLite database (`dressage.db`): one table for records of dressage competitions (`shows`), the other for records of horses (`pedigree`). All of my webscraping scripts can be found in the directory `horses`.

Now I had data to tame! My data cleaning journey is documented in the Jupyter notebook `dressage_data_cleaning.ipynb`. The data were not at all straightforward, given that a single horse could be referred to by multiple identifiers, and there were multiple types of webpages describing a horse depending on whether that animal had competed, or was just listed for pedigree purposes, that meant data were in a variety of formats.

Next: exploratory data analysis (`eda.ipynb`). I was most interested in dressage scores: conveniently, dressage scores are percentages. This makes them comparable between different shows. I examined the effect of different variables in my data on the mean dressage score of a horse, rider, or horse-rider combination. Below I summarise the things I found most interesting, and how I could follow up on them.

### Rider performance may be influenced by experience...

| The more horses a rider has competed on, the higher the mean dressage score for that rider tends to be    | Mean dressage score for a rider increases as the number of shows a rider has competed in increases      |
|------------|-------------|
![](../master/num_horses.png) | ![](../master/num_shows.png)

The trends illustrated above suggest that riders may be influenced by experience: the more shows a rider has under their belt, or the more horses they have experience riding in international competition, the better they tend to perform. Interestingly, I did not observe such strong correlations for horses. Instead, horses who had competed in more shows tended to regress towards the mean. Statistically, we expect this: individuals with few competitions have means that are more strongly affected by outliers. This is also clear in the scatterplot above, where the variance of riders who have competed in few shows is very high. However, in the riders data there does appear to still be an increase in score as the number of shows increases.

This made me wonder: if you were to bet money on the winner of a dressage show, would you bet money based on the rider's previous performance, or the horse's previous performance? There is potential for mixed modelling approaches to be used to try and explain how much a horse and a rider each contribute to variance in horse-rider combinations' mean dressage score. If riders explain more variance than horses, it would be a safer bet to put your money on the best performing rider, rather than the best performing horse.

**Potential for follow up: mixed model analysis to identify whether the contribution of the horse or of the rider is more important to the combination's mean dressage score**

### Dressage scores may be somewhat heritable...
|  Sires mean dressage score correlate with the scores of their offspring  |  The pedigree structure of the top 100 dressage horses: blue lines are sires, black lines are the offspring of those sires     |
|------------|-------------|
![](../master/offspring.png) | ![](../master/pedigree.PNG)

There is a strong positive correlation between the mean dressage score of a male horse with offspring (a sire) and the mean score of all of his offspring. This finding is typical of a heritable trait - that is, a trait with a genetic component. It seems likely that dressage score is likely to be somewhat affected by the genetics of the horse. For example, horses who carry genetic variants that predispose greater flexibility or strength might have a competitive edge. However, this correlation could also be explained by shared environment or other variables that covary with sire. 

**Potential for follow up: mixed model (with pedigree relationship matrix) analysis to estimate the heritability of dressage scores**
