from openai import OpenAI
client = OpenAI()

article_origin = input("Enter where the artical is from")
prompt = """Write a summary of the following article from the {ARTICLE}, then create a Conservative political take, a Moderate political take, and a Liberal political take:

Santa Claus may be running out of steam.

The year-end rally that was amplified after the Federal Reserve hinted at imminent rate cuts showed signs of fading on the final trading day of the year.

But 2023 still came with many gifts for investors.

S&P 500: While the broadest measure of the US stock market closed 0.28% lower on Friday, leaving it just under 30 points away from a record-high close, it gained 24% this year, ending 2023 with a bang. It also notched its ninth-straight weekly gain — the longest streak since January 2004. This year has been much kinder to the market than last: The benchmark index fell by about 20% in 2022.

Dow Jones Industrial Average: The Dow reached multiple record highs in December, including notching records in each of the past five trading sessions. It was down 0.05% Friday, closing at 37,689. In 202﻿3, the Dow gained 14%.

Nasdaq Composite: The tech-heavy Nasdaq index was the year’s biggest star, however. Although it was down 0.56% Friday, closing at around 4769, it rose by 43% in 2023 — its best performance since 2020. It remains about 1,000 points below the all-time high it reached in November 2021, demonstrating what a horrendous year tech had in 2022 — and how much room it still has left to recover.

The US dollar: The world’s reserve currency is on track for its worst year since 2020. The US dollar index, a measure of how the currency is performing against six other currencies, is down over 2% for the year. The dollar has been weakened by the prospect of rate cuts next year.

US Treasuries: After nearly hitting 5%, the yield on the 10-year US Treasury note ended the year below 4%. Yields on longer-dated US Treasuries retreated beginning around November and closed near the levels they were at this summer.

Stocks surged this year as the US economy remained remarkably strong in the face of interest rate intervention by the Fed. CNN Business’ Fear and Greed Index ended the year in “Extreme Greed” territory.

At this point in 2022, inflation was running at about 6.5%. Today, that number has more than halved and sits at 3.1%. US consumers, meanwhile, are still spending and economic data is resilient. Unemployment is at a healthy 3.7%.

But that’s not to say it was all rainbows and butterflies in 2023.

The so-called “wall of worry” followed investors through the year as recession risk and the Fed’s higher-for-longer interest rate policy kept them on their toes. China’s miserable economy also didn’t help.

Geopolitical uncertainties — conflict in the Middle East and Eastern Europe and rising tensions with China — also spooked Wall Street.

And even when the overall market is winning, there are still losers.

Here are the big winners, and losers, of the year.

The winners
It’s been a strong year for supersized tech and AI stocks.

Apple, Microsoft, Alphabet, Amazon, Nvidia, Meta Platforms and Tesla, known collectively as the ‘Magnificent 7,’ dominated the S&P 500 and soared well over 100% in 2023.

Nvidia (NVDA) gained 246%, Meta (META) gained 184% and Tesla (TSLA) soared 130%. Each of those stocks slumped by more than 50% in 2022.

And while these mega-cap stocks dominated in 2023, there were some surprising mid-cap winners as well.

Duolingo (DUOL) shares rose 220% for the year.

The language-learning app saw hyper growth during the pandemic that hasn’t slowed down since the company went public in July 2021. Revenue is 43% higher than it was last year and the Pittsburgh-based company has been profitable for the past two quarters, a first for Duolingo.

Shares of Abercrombie & Fitch (ANF) are closed 274% higher, its best year ever. Net sales are up 30% year over year as of third-quarter earnings, and the retailer forecasted more growth in the final quarter of the year.

Cancer drug developer ImmunoGen (IMGN), meanwhile, closed 522% higher for the year after AbbVie announced in late November it would acquire the company for $10 billion.

The losers
One of the worst-performing stocks in the S&P 500 this year was Enphase Energy (ENPH), which shed 48% for the year.

The energy technology company has been dealing with an excess of inventory as new metering regulations in California and increased lending rates have led to a drop in demand for solar panels in the United States. Enphase announced in December that it would restructure its company.

Drugmaker Moderna (MRNA), meanwhile, fell by 44% as demand for its Covid vaccine wanes.

The company announced that its 2023 sales would reach the lower end of its target. The drugmaker also pushed the expected launch of its new flu shot back a year, from 2024 to 2025.

Much like Moderna, Pfizer (PFE) also suffered this year. Shares of the stock were down 44%. This was the worst year on record for both stocks.

Discount retailer Dollar General (DG) dropped 45% in 2023, its first annual decline since going public in 1968.

Increased labor costs, inventory management issues, increased competition from Dollar Tree and other discount stores like Walmart and the growing economic constraints on lower-income consumers have all hurt the company this year.

In October, the company announced it would bring back its former CEO Todd Vasos from retirement to replace current CEO Jeff Owen.

“At this time the Board has determined that a change in leadership is necessary to restore stability and confidence in the Company moving forward,” said Michael Calbert, chair of Dollar General’s board of directors, in a statement.

As a year of volatility and surprises draws to a close, investors are looking ahead to yet another year of twists and turns.

RELATED


""".format(ARTICLE = article_origin)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful research assistant for extemporaneous speakers in the NSDA."},
    {"role": "user", "content": str(prompt)},
    {"role": "assistant", "content": str(article_origin)}
  ]
)

print(completion.choices[0].message)