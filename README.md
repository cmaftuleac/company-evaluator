# company-evaluator

This repository explores how to score potential B2B leads for **[Fineguide.ai](https://fineguide.ai)**, a platform that provides enterprise-grade AI agents for customer service. The goal is to estimate how likely a given company is to purchase or trial Fineguide's services.

## Fineguide snapshot
- Website title: *"Fineguide.ai | AI platform for customer service"*
- Tagline: *"Smarter AI Agents for Real Results"*
- Description: *"Fineguide.ai delivers enterprise-grade AI agents that understand complex customer inquiries, provide accurate responses and drive measurable outcomes."*

_Source: [fineguide.ai](https://fineguide.ai)_

## Scoring approach
1. **Target** – Predict whether a company will meaningfully trial or buy Fineguide within the next 6 months.
2. **Signals** – Extract signals across six buckets:
   - Fit to ICP (industry, company size, traffic, support team size)
   - Pain indicators (support job posts, help center size)
   - AI/digital maturity (mentions of chatbots, existing support tech)
   - Buying intent (funding events, AI webinars, search activity)
   - Budget & authority (revenue, decision makers)
   - Timing triggers (seasonal peaks, new launches)
3. **Pipeline** – For each company:
   - Enrich data via web scraping and APIs (BuiltWith, SERP search, LinkedIn).
   - Use an OpenAI model (via LangChain) to score each bucket 0‑5 based on gathered context.
   - Aggregate weighted scores into a 0‑100 likelihood to buy.
   - Store results for sales review and feedback.

See `scorer.py` for a minimal LangChain prototype.
