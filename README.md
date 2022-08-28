youtube_timestamper
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Install

``` sh
pip install youtube-timestamper
```

## How to use

In this example, we look at Sanyam Bhutani’s interview of Kaggle legend
Chris Deotte:

        <iframe
            width="700"
            height="400"
            src="https://www.youtube.com/embed/QGCvycOXs2M"
            frameborder="0"
            allowfullscreen
            
        ></iframe>
        

This interview contains a wealth of knowledge but it’s not timestamped
with chapter divisions. This library can help create timestamped
chapters by picking out the questions in Question-Answer style videos.

To start, simply import
[`YoutubeTimestamper`](https://ilangurudev.github.io/youtube-timestamper/core.html#youtubetimestamper)
from `youtube_timestamper.core` and pass in a youtube video url.

``` python
from youtube_timestamper.core import YoutubeTimestamper
```

    /home/ilangurudev/anaconda3/envs/ds/lib/python3.9/site-packages/transformers/pipelines/token_classification.py:135: UserWarning: `grouped_entities` is deprecated and will be removed in version v5.0.0, defaulted to `aggregation_strategy="none"` instead.
      warnings.warn(

``` python
yt_ts = YoutubeTimestamper("https://www.youtube.com/watch?v=QGCvycOXs2M")
```

``` python
yt_ts.suggest_question_timestamps(next_q_thresh=20)
```

    /home/ilangurudev/anaconda3/envs/ds/lib/python3.9/site-packages/transformers/pipelines/base.py:1036: UserWarning: You seem to be using the pipelines sequentially on GPU. In order to maximize efficiency please use a dataset
      warnings.warn(

    00:00:00 Introduction
    00:01:08 how did he transition into data science and cargill and his journey on kaggle?
    00:02:23 can you tell us a bit more about that, chris, now that you remember of it the secret?
    00:02:48 did you get your invite to the fight clubs yet, or can you share a bit about those?
    00:04:44 then i, um i graduated with a bachelor's degree in mathematics and then, um, immediately afterwards, i?
    00:07:19 when did kaggle come into the picture? when did you find your addiction for kagan?
    00:08:28 you know you build a model and is your model more accurate than the other guy's model?
    00:10:15 how did you go from just starting your journey to today being the forex grandmaster? how would you advise? what should they read? what should they learn? do you think there's such a list?
    00:11:49 was it part of the enjoyment process, just getting involved, or were you making a conscious effort to? you know, maybe list down points where you need to improve?
    00:12:40 and even if a competition or something looks similar to a previous one, i say to myself: you know, what new angle can i do here? you know what new thing can i learn?
    00:13:49 any favorite battle stories you that you might remember?
    00:14:33 so there's many competitions and you see the leaderboard and there's a bunch of scores and there's, you know, the top 50, they have a little bit of a jump, and there's and people in the forum say: you know magic, what's the magic?
    00:16:03 um, do you, do you have any uh, rigid approach to competitions now, or did you compete in any in parallel, or do you just stick to one? and what's your approach in general to competitions now?
    00:22:05 so, and that's something that i also enjoy very much- on the flip side, do you feel you're also losing a competitive edge?
    00:25:45 thank you, um, what advice would you have for uh, newbies who are looking to write kernels?
    00:30:58 what, what advice would you have for them? they're just chasing uh, maybe the title, since it's gamified, does it annoy you? do you have any uh advice for such people?
    00:32:51 uh, any favorite memories from discussions that you might have?
    00:34:37 and then someone says, wow, that's awesome, hey, have you thought about doing this?
    00:35:35 um, what advice would you have for people who people, many people, seek teaming up because they may be asking to just compete by themselves? but what teaming advice would you have for people in general? or what's your strategy?
    00:38:47 what's your reason for investing so much time into kagan?
    00:38:58 you know people might see it and say, why is he doing so much for the community? you know, how have i, how have i, you know, learned these ideas so well?
    00:43:49 pandas build psychic learn, okay, uh, but what, what the wrap is team doing is?
    00:45:38 is the desk data plotted on top of the train data or is the test data over here? like: is this group of images the same as this group of images?
    00:47:11 how do you, chris, how do you manage your time? what's, what's your secret to time management?
    00:49:44 but, as i said, you know, if someone's like, hey, can you? you know, can you follow the?
    00:50:30 uh, is it okay if we do a quick rapid fire questions? uh, a set of questions? so what would you like? so, would you like to me give short answers?
    00:51:12 okay, a favorite course that you've taught? uh, i'm not sure if you've taught a few or was it just a single one? oh, okay, yeah, so, uh, favorite course?
    00:52:11 do you know that? the derivative is exactly what your brain uses for you to learn something?
    00:52:38 okay, um, favorite algorithm?
    00:52:54 it's just how do you classify this guy? well, how do you class with this data point?
    00:53:55 okay, um, favorite competition that you've taken part in?
    00:55:20 you're refreshing your computer, refreshing your computer, how did i do? how did i do? it's unbelievable, right?
    01:00:28 um, what would be your favorite spot to surf? wait, favorite what sport? to windsurf?
    01:01:24 uh, your favorite way to unwind, uh, from data science or kaggle?

    Created using youtube-timestamper (https://ilangurudev.github.io/youtube-timestamper/)

------------------------------------------------------------------------

A nice starting point! As we can see,

-   The suggestions contain *all questions* - that means the
    interviewee’s questions too (*and then someone says, wow, that’s
    awesome, hey, have you thought about doing this?*).
-   Sometimes the questions don’t provide the complete context - they
    look like tarantino chapter titles. (*i mean, how does a computer
    know how to draw dogs?*)
-   The questions are too long and need to be summarized. (*how did you
    go from just starting your journey to today being the forex
    grandmaster? how would you advise? what should they read? what
    should they learn? do you think there’s such a list?*)
-   The youtube transcripts also contain a ton of typos (*kagan, forex
    grandmaster*)
-   Sometimes some questions are missed - the model is not perfect.

But I can just edit these timestamps and clean them up quickly manually
as opposed tostarting from scratch. I remove

-   Irrelevant questions
-   Summarize questions neatly (and sometimes go back to the video to
    get enough context)
-   Correct typos
-   Look for large gaps where there are no chapters and manually insert
    titles if need be.

00:00:00 Introduction<br /> 00:02:23 Secret to Kaggle Success<br />
00:02:48 Exclusive Kaggle Fight Club Invites LOL<br /> 00:04:21 Life
leading up to Kaggle<br /> 00:07:19 Beginning of addiction to
Kaggle<br /> 00:10:15 Journey to 4x Grandmaster and Tips<br /> 00:11:49
Motivation to Kaggle - Fun or Improvement<br /> 00:13:39 Favorite battle
stories<br /> 00:16:03 Approach to Competitions<br /> 00:25:45 Advice
for newbies looking to write kernels<br /> 00:30:58 Advice for people
who span kaggle forums in search of titles<br /> 00:32:51 Favorite
memories from discussions<br /> 00:35:35 Teaming Strategy and
Advice<br /> 00:38:47 Reason for investing so much time into
Kaggle<br /> 00:43:30 Rapids<br /> 00:47:11 Secret to time
management<br /> 00:50:30 Rapid Fire<br /> 00:51:12 Favorite Course that
you’ve taught<br /> 00:52:38 Favorite Algorithm<br /> 00:53:55 Favorite
Competition so far<br /> 01:00:28 Favorite spot to surf<br /> 01:01:24
Favorite way to unwind from data science and Kaggle<br />

Created using youtube-timestamper
(https://ilangurudev.github.io/youtube-timestamper/)

Now simply copy paste as a comment in the video!
