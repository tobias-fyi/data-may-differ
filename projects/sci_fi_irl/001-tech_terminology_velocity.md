Title: Technology Terminology Velocity
Date: 2019-09-27
Modified: 2019-09-27
Category: Tech, Mass Media, Popular Culture
Tags: Reddit, PushShift, Python, Data Storytelling
Slug: technology-terminology-velocity
Author: Tobias Reaper
Summary: A brief data story about varying velocities of technology terminology across different online communities.

![tobias fyi logo]({static}/images/19-09-tobias-fyi-logo.png)

## Sci-fi, IRL

This essay is the first in a series of data-driven essays, Sci-fi IRL, that will explore the relationship between science-fiction and IRL (in real life) science, technology, and philosophy.

## Introduction

I love reading and writing science-fiction for many reasons. At the top of that list is how the format of the genre can open doors to the exploration of important concepts and technology in ways that, in my view, no other genre of storytelling, fictional or not, can.

Of particular interest to me is the opportunity sci-fi presents for preemptively exploring near-to-mid-future ideas that have the potential to drastically affect our existence in the "real" world (I won't get into the weeds with that term right now—I hope you know what I mean). 

One great example of this that immediately comes to mind is traveling through and living in outer space. (You thought I was going to say artificial intelligence, weren't you?)

Of course there are many stories set in space that do not pay much attention to the minute or day-to-day details of life in zero-gravity. However, as a powerful literary or plot device that can give a story depth and realism, it is usually addressed at some level. Although vast majority of the sci-fi I consume nowadays comes in the form of books, the most vivid portrayal of life in the void also happens to be one of my favorite book and television series, The Expanse. If you don't know what that is or have not read or watched it, I'd very highly recommend it.

The reason for it being high up on my list is not solely due to this portrayal and the fact that I enjoy hard sci-fi when it's done well. To go back to what I stated earlier, it gives me a new lens through which I can consider the concept. I believe it's likely that humans will start living in space sometime in the next several decades.

The fact is that living in space without natural gravity and being surrounded by vacuum changes almost everything about day to day life, and indeed much more than that.

My point is that we can and should explore as many of the possible ramifications of these types of things *now*, before we're on our way past the stratosphere

The Sci-Fi IRL series is my first attempt at connecting the various science-fiction universes with our own. 

## Part 1: Technology Terminology Velocity

The goal of this particular piece is to make the smallest baby step possible toward the overarching goal of the project, which is to answer the question, "What is the relationship, if any, between the ideas and technology in science-fiction and those of the real world?"

In order to take this first small step for mankind, I will be using data to illustrate one potential point of relation between the science of fiction and the non—the terminology of technology.

My hypothesis is that there is a distinct, and to some degree regular, time lag between when the terminology describing some important new technology is introduced into popular discourse and when it begins to show up in popular culture. I'm using the term "popular culture" to refer to the overall, ever-changing corpus of (science-fiction) books, series, and video games.

I decided to call the measure of this relationship the Velocity of Technology Terminology.

## Next Steps

The next step after (hopefully) establishing the velocity of intellectual interchange from the real world to popular culture will be to test the hypothesis that a similar, complementary relationship exists going the other direction. 

One way to phrase that line of inquiry as a question could be, "When popular culture introduces some new terminology, how long does it take to spread into the fields of science, technology, and philosophy?

However, I don't want to get ahead of myself. I'll save the latter half for next time.

## Velocity Methodology

### A Bit of Backstory

While considering how to go about testing this hypothesis, I ran across the somewhat-infamous [Reddit Dataset](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/), which supposedly held every single publicly-available Reddit comment, totaling almost 2 billion. 

As an on-and-off Redditor over the past decade or so, I immediately recognized the huge potential provided by this type of data source.

However, I held back at first because I did not necessarily want (let alone was even able) to download many hundreds of gigabytes of data. In reality, I would only be using a miniscule fraction of that in my analysis, at least at this early stage in my data science career—once I get into more advanced topics like machine learning, who knows?—if I could even figure out how to parse something that incredibly large.

I felt optimistic; up to the task. I stumbled on the [PushShift file directory](https://files.pushshift.io/reddit/), which is an actively-updated archive of that same data. Once I realized I could download the data month-by-month, I decided to go for it.

I spent a week or two downloading from the PushShift server, raking in around 200GB of data during that time. Several days ago, I happened to be poking around on the PushShift site and found out that along with providing all of the data for download, the maintainer, [Jason](https://pushshift.io/donations/) built and hosts [a public API](https://github.com/pushshift/api) for [querying the entire dataset](https://pushshift.io/api-parameters/) *without downloading all of it to my local storage*.

That benefitted me in a couple of very important ways. First, I no longer had to fill up the majority of my total digital storage capacity (quite literally—all of my externals and everything). Second, the data is already cleaned and organized, with infrastructure already in place to run the kinds of queries that I wanted to run for this essay.  

I want to give a huge shoutout to Jason [AKA `u/Stuck_in_the_Matrix`](https://www.reddit.com/u/Stuck_In_the_Matrix/) for providing such a valuable service, and allowing free and open access.

### For Key in Words

To start, I spent some time coming up with a list of words and phrases that I could use to test my hypothesis. In order to find anything interesting, it was *very* important to come up with effective criteria that was aligned with the goals of this research. 

The fundamental criteria I used while creating the list were that the word or phrase should: 

1. Be, or have been at some point in the last decade, popular enough to be considered a "normal" part of popular lexicon; 
2. Describe a distinct technology, field, and/or ideology; and 
3. Not be so specific as to prevent it from being explored in non-technical media.

#### Keywords

- algorithms
- artificial intelligence
- augmented reality
- genetic engineering
- universal basic income
- quantum computing
- cryptocurrency
- facial recognition

### Equal Representation

Once I had my first basic list of around 10 terms (for the first run-through I ended up using 9 of them), the next step was to find or create a method of representing the groups I want to test. Of course, since I am using Reddit data, the obvious thing to do is find subreddits that fit into those groups. 

With that in mind, I spent a while combing through the massive list of subreddits, adding to my list, grouping and re-grouping, pruning from the list...you get the point. In case I didn't make it clear enough already, the general criteria I used to group the subreddits are: 

1. Science, technology, philosophy; and
2. Entertainment and media.

#### Subreddits

- Science / Technology
    - Futurology, 14.2m
    - technology, 8.2m
    - science, 22.4m
    - askscience, 18.1m
- Entertainment
    - books, 17.1m
    - scifi, 1.2m
    - movies, 21.5m
    - gaming, 23.7m
- Media / General
    - worldnews, 22.2m
    - news, 19m
    - politics, 5.4m
    - AskReddit, 24.6m

### The Data is in the Details

I used the API to aggregate the number of comments that contain the keywords, and explore the data across time and across different online communities (subreddits).

    #!python
    from django.db import models

    from wagtail.core.models import Page
    from wagtail.core.fields import RichTextField
    from wagtail.admin.edit_handlers import FieldPanel


    class HomePage(Page):
        body = RichTextField(blank=True)

        content_panels = Page.content_panels + [FieldPanel("body", classname="full")]

### Considerations, Assumptions, Shortfalls, Improvements


## Visual Exploration



## Re(Sources)


