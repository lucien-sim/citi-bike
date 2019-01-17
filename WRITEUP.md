# Evaluation of Citi Bike Redistribution Policies

# Table of contents

# 1. Introduction

Citi Bike rides follow consistent patterns. For example, on workdays, Citi Bikes tend to flow from residential to commercial areas in the morning, and from commercial to residential areas in the evening. Show gif of single day to demosntrate this... point reader to migrations to and from Midtown/Upper East Side, the East Village, and Downtown Brooklyn. 

**The problem:** Consequence of this coherent migration of bikes: docking stations spend a considerable amount of time empty/full, which is inconvenient for customers. 

**My objective:**
* Provide a quantitative understanding of the problem: where are stations most frequently empty/full? Where is this emptiness/fullness most consequential? During what seasons? Consequentiality of the emptiness/fullness depends on average demand at that station at a given time, and on the level of inconvenience the emptiness/fullness poses. Explain how these two are quantified. 
* Based on these quantifications, make a few recommendations...
* Must take seasonal variation into account --> aka variation due to weather. 
* I will focus on non-holiday weekdays, when a majority of necessary travel occurs. 
* Consider doing this too: Predict how empty/full a station will be on a given day, based on the weather conditions and on the emptiness/fullness on the previous day. Use linear regression, then random forest. 

Citi Bike is New York City's dock-based bike share program. Dock-based programs, Citi Bike included, face serious challenges related to bike distribution: in the morning, bikes tend to migrate from residential to commerical areas, leading to a surplus of bikes in commerical areas and a scarcity of bikes in residential areas. This phenomenon is clearly visible in the following animation, which shows the fraction of docks that are filled at each docking station in NYC, at the beginning of each hour (EST) on May 3rd, 2018. Green dots represent docking stations that have many bikes available, while red dots represent stations that have very few bikes available. 

<center><img src=./figs/frac_full.gif width="450" height="650" /></center>

<!-- <img src=./figs/full_empty.gif width="600" height="700" /> -->

Looking at the animation you'll notice that, during business hours, most stations in commerical areas (eg. Financial District, Midtown, Downtown Brooklyn) are nearly or completely full, while most stations in some residential areas (eg. Upper East Side, Upper West Side, East Village, parts of Brooklyn) are nearly or completely empty. The opposite is true during other parts of the day. These shifts in bike distribution can be frustrating for customers: if you rely on Citi Bike to get to work but can't find a bike within a mile of your house, you might be late. If these types of problems are widespread, they might be discouraging people from participating in the Citi Bike program. 

Citi Bike is currently trying to address this issue through both [Valet stations and bike redistribution](https://help.citibikenyc.com/hc/en-us/articles/115007197887-Redistribution). Citi Bike sends employees to some of the busiest stations to provide or collect excess bikes, as necessary ("Valet" service). Citi Bike also employs people to transport bikes from full stations to empty stations using "non-motorized bike trains" (not sure what those are). Finally, Citi Bike runs a program called "[Bike Angels](https://www.npr.org/sections/money/2018/12/11/675828915/citi-bike-s-better-angels)," in which Citi Bike members can redeem prizes (discounts, free passes, gift cards) for riding bikes from full stations to empty stations. 

I know it's a problem. And Citi Bike is trying to solve it -- through redistribution, and through initiatives (eg. [BigIdeas](https://citibikefinder.splashthat.com/)) to build a tool that tells users if bikes will be available at times they need bikes. I just don't know if the problem is improving (couldn't find anything online). That's what I want to figure out. 

# 2. The data

# 3. Some data exploration

Answer the following questions: 

**Are the patterns we saw in the May 3 animation typical for weekdays?**
Animation with medians for weekday. 

**How consistent are the counts from day to day?**
Four different stations: time series with median, 5th, and 95th percentiles. How much variation is there in each stations' fullness from day to day? If there's a lot, the time of day probably isn't the only factor that affects the bike counts at a certain station on a weekday. If I wanted to build a model that predicts the station count at any given hour of the day, I'd need to take more into account. 

NOTE: Forgot to take in_service/status_key into account in driving medians and percentiles. Fixed the code, but still need to re-create the median fullness gifs. 

# 4. Understanding the problem: Jan-Jul 2018

**As a first step: plot average hours/day spent empty and full from 01/01/2018 to 07/31/2018**
Problem seems pretty severe--stations spend up to 10 hours/day empty, 7 hours/day full. Particularly bad in these neighborhoods. 

**We can quantify the problem a bit better, though...** Take activity levels and distance to nearest dock with spots/bikes available into account. It's worse to have an empty dock in the East Village during the morning rush than it is to have an empty dock in Midtown at 2am. 

**Is there seasonal variation?**

**Where and when I would focus my efforts if I wanted to improve this problem...** Does this line up with Citi Bike's Valet station initiatives? 



**Is emptiness/fullness only a problem on weekdays? Or also on weekends and holidays?** Docks can be empty and/or full on weekdays, weekends, and holidays. However, the problem appears to be the most severe on weekdays, when most docks typically spend the largest number of hours empty/full. Docks in Red Hook are an exception, in that they spend more time full on weekends than on weekdays. I'm reluctant to draw any conclusions about emptiness/fullness on holidays because only seven days from January-July 2018 are considered holidays by the Python "holidays" library: New Year's Day, MLK Day, Lincoln's Birthday, Susan B. Anthony's Birthday, Washington's Birthday, Memorial Day, and Independence Day. The sample size of holidays is small, and might not be representative of typical holiday behavior. For the remainder of the analysis, I'll focus on weekday behavior, when the problem with empty/full docking stations seems to be most severe, and when most mandatory travel occurs. 

**Which stations are most frequently empty? Full? Provide a map and a ranking of stations for both.** Stations are most frequently full on the Lower East Side and in Red Hook, and are most frequently empty in Midtown, on the Upper East Side, and on the fringes of the Citi Bike system in Brooklyn/Queens. Docks are also often empty on the Lower East Side and Upper West Side. In general and across the city, docks are more frequently empty than full. 

**Take consequence of emptiness/fullness into account.** Adjust metric so that it includes: 
   * Distance to nearest station that isn't empty (if station is empty) or full (if station is full).
   * Typical level of activity at that station, at that time. If a station is empty or full at 1am, when very few people want to use Citi Bikes, it might not be such a problem! 

# 4. Is the bike distribution problem improving? 

## a. Citywide trend
Track metric city-wide, month-to-month. 

## b. Local trends
Track metric by neighborhood, month-to-month. 

# 5. Data dashboard
Created in plotly; if I have time. 

# 6. Conclusions and Next Steps

Conclusions and recommendations: 
* At which stations is emptiness/fullness most problematic? 

Next steps: 
* google maps for distance
* analysis of tweets -> see if peoples' perceptions of the problem are improving. Probably the most business relevant! 
