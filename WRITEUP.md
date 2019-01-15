# Evaluation of Citi Bike Redistribution Policies

# Table of contents

# 1. Introduction

Citi Bike is New York City's dock-based bike share program. Dock-based programs, Citi Bike included, face serious challenges related to bike distribution: in the morning, bikes tend to migrate from residential to commerical areas, leading to a surplus of bikes in commerical areas and a scarcity of bikes in residential areas. This phenomenon is clearly visible in the following animation, which shows the fraction of docks that are filled at each docking station in NYC, at the beginning of each hour (EST) on May 3rd, 2018. Green dots represent docking stations that have many bikes available, while red dots represent stations that have very few bikes available. 

<img src=./figs/frac_full.gif width="450" height="650" />
<!-- <img src=./figs/full_empty.gif width="600" height="700" /> -->

Looking at the animation you'll notice that, during business hours, most stations in commerical areas (eg. Financial District, Midtown, Downtown Brooklyn) are nearly or completely full, while most stations in some residential areas (eg. Upper East Side, Upper West Side, East Village, parts of Brooklyn) are nearly or completely empty. The opposite is true during other parts of the day. These shifts in bike distribution can be frustrating for customers: if you rely on Citi Bike to get to work but can't find a bike within a mile of your house, you might be late. If these types of problems are widespread, they might be discouraging people from participating in the Citi Bike program. 

Citi Bike is currently trying to address this issue through both [Valet stations and bike redistribution](https://help.citibikenyc.com/hc/en-us/articles/115007197887-Redistribution). Citi Bike sends employees to some of the busiest stations to provide or collect excess bikes, as necessary ("Valet" service). Citi Bike also employs people to transport bikes from full stations to empty stations using "non-motorized bike trains" (not sure what those are). Finally, Citi Bike runs a program called "[Bike Angels](https://www.npr.org/sections/money/2018/12/11/675828915/citi-bike-s-better-angels)," in which Citi Bike members can redeem prizes (discounts, free passes, gift cards) for riding bikes from full stations to empty stations. 

I know it's a problem. And Citi Bike is trying to solve it -- through redistribution, and through initiatives (eg. [BigIdeas](https://citibikefinder.splashthat.com/)) to build a tool that tells users if bikes will be available at times they need bikes. I just don't know if the problem is improving (couldn't find anything online). That's what I want to figure out. 

# 2. The Data 

# 3. Data Exploration

NOTE: Forgot to take in service/out of service into account in driving medians and percentiles. 

Look at animations of median trends, for weekdays, weekends, and holidays--make sure the trends we saw in the animation above aren't anomalies. They're not. Weekends don't see the same problems. 

Build some intuition -- weekday, weekend, holiday time series of median, p05, p95 for three stations. One -> canoncially commerical, Another -> canonically residential, a third -> doesn't fit either category. How much variation is there in each stations' fullness from day to day? If there's a lot, the time of day probably isn't the only factor that affects the bike counts at a certain station on a weekday. 

Alright, now we've built some intuition on the movement of bikes, the daily cycles at individual stations, and on how consistent the daily counts are. Now, start looking at how prevalent the issue with empty/full stations actually is. 

(there's anecdotal evidence but I haven't found any numbers online)

It's clear that there's a daily migration of bikes from residential to commerical areas. It's also clear that there's anecdotal evidence that bike stations are frequently completely empty or full. But how widespread is the issue, in reality? 
* Plot average hours/day each station spends either completely empty/completely full. 
* Show distributions of hours/day for a few stations. 
* Removal of outliers --> in service/out of service

# 4. Is the bike distribution problem improving? 

## a. Metric development
Important things to consider: 
* How much time a station is empty/full
* How far it is to the next station with bikes/docks available, when the station is empty/full. 
* How active is the station, typically, at the time the station is empty/full? If a station is empty at 1am when very few people are trying to ride Citi Bikes, it might not be such a big deal. Or, it might be a big deal if a central part of the mission's business is to ensure that it's convenient to use the system at any time of day. 
* Other things? 

## b. Citywide trends

## c. Local trends

## d. Problem areas

# 5. Conclusions, Next Steps, and Recommendations

* google maps for distance
* analysis of tweets -> see if peoples' perceptions of the problem are improving. Probably the most business relevant! 
