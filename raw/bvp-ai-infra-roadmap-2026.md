---
title: "AI Infrastructure Roadmap: Five frontiers for 2026"
source: "https://www.bvp.com/atlas/ai-infrastructure-roadmap-five-frontiers-for-2026"
author:
  - "[[Taj Shorter]]"
published: 2026-03-30
created: 2026-04-15
description: "The first generation of AI infrastructure companies unlocked the “brains” for intelligence. The next generation will unleash these engines of intelligence into the real-world."
tags:
  - "clippings"
---
## The first generation of AI infrastructure companies unlocked the “brains” for intelligence. The next generation will unleash these engines of intelligence into the real-world.

![Untitled 1600 X 900 Px 1](https://www.bvp.com/assets/themes/bvp-24/img/clear-post-banner.gif)

The first generation of AI was built for a world where the model was the product, and progress meant bigger weights, more data, and stellar benchmarks. AI infrastructure mirrored this reality, fueling the rise of giants in foundation models, compute capacity, training techniques, and data ops. This was the focus of our [2024 AI Infrastructure Roadmap](https://www.bvp.com/atlas/roadmap-ai-infrastructure), which drove our investments in companies such as [Anthropic](https://anthropic.com/), [Fal AI](https://fal.ai/), [Supermaven](https://supermaven.com/) (acquired by [Cursor](https://cursor.com/)), and [VAPI](https://vapi.ai/) as the AI infrastructure revolution unfolded.

But the landscape has changed. Big labs are moving beyond chasing benchmark gains to designing AI that interfaces with the real world, and enterprises are graduating from POCs to production. The infrastructure that got us here — which was optimized for scale and efficiency — won’t get us to the next phase. What’s needed now is infrastructure for grounding AI in operational contexts, real-world experience, and continuous learning.

The stage is being set for a new wave of AI infrastructure tools to enable AI to operate in the real world. We’ve identified five frontiers that will define this next wave, each addressing a structural limitation that needs to be solved beyond model scaling.

## Five cutting-edge frontiers for next gen AI infrastructure

![](https://www.bvp.com/assets/uploads/2026/03/AI-Infra-2nd-act_DESIGN-V7.png)

### 1\. “Harness” infrastructure

==As AI deployments shift from single models to compound systems, infrastructure designed to "harness" models — unlocking their full potential — becomes more important than ever.==

Take memory and context management. Most enterprise AI systems suffer from organizational amnesia. While basic Retrieval-Augmented Generation (RAG) solved the connection problem between models and data sources, compound AI systems now require more sophisticated memory infrastructure. Enterprises hold vast amounts of historical data and organizational knowledge — from proprietary documents to CRM records — that AI systems must access to avoid hallucinations and stay grounded in company-specific reality.

Reliable AI deployment depends not just on raw model horsepower, but on orchestrating components like knowledge retrieval, cross-session context management, and planning. As models become commoditized, differentiation shifts to the memory and context layer. What developers once built from scratch — custom vector databases and retrieval systems — is now emerging as its own infrastructure category. Startups and [Big Tech alike](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) now offer plug-and-play semantic layers that maintain conversation context, user preferences, and long-term memory across sessions.

==Novel evaluation and observability present another critical infrastructure challenge — one that didn’t exist in prior software development paradigms. Consider teams shipping conversational AI agents to production. Traditional monitoring tracks completion rates, latency, error codes, and thumbs up/down feedback. But conversational AI fails differently. When a chatbot gives a confident wrong answer, gradually drifts from the user's actual question, or misunderstands the request while producing something plausible, users often don’t react. No complaint, no thumbs down, no error signal. The conversation looks fine in dashboards, and AI just quietly failed.==

==An estimated [**78% of AI failures are invisible**](https://arxiv.org/abs/2603.15423) — AI gets something wrong, but no one catches it. Not the user, not traditional monitoring, not even a sentiment analysis. These failures cluster into recurring patterns:==

- **The confidence trap** — AI is confidently wrong, and the user accepts it
- **The drift** — AI gradually answers a different question than what was asked
- **The silent mismatch** — AI misunderstands but produces something plausible enough that the user doesn't push back

These patterns persist across 93% of cases even with more powerful models, because they stem from interaction dynamics — how models present outputs and how users communicate intent — not capability gaps.

New infrastructure is emerging to address this. Platforms like [Bigspin.ai](http://bigspin.ai/) provide not just pre-deployment testing but real-time production monitoring of model outputs against golden datasets and user feedback. We’re also moving beyond traditional analytics toward semantic metrics, with new platforms such as [Braintrust](https://www.braintrust.dev/) and [Judgment Labs](https://judgmentlabs.ai/), as well as techniques such as LLM-as-a-judge, that are emerging for high-quality evals and metrics definition.

**These examples illustrate evolving needs for AI harness infrastructure. For more on environments, runtime, orchestration, protocols, and frameworks, see our** [**Software 3.0 roadmap**](https://www.bvp.com/atlas/roadmap-developer-tooling-for-software-3-0)**.**

### 2\. Continual learning systems

==Today’s AI models face a fundamental constraint: frozen weights prevent true learning after deployment. While context management strategies like compaction are powerful, and we see many big labs use them for long-running agents, in-context learning enables only surface-level adaptation through rote memorization, not the acquisition of new skills. It also becomes prohibitively expensive as contexts grow, since the KV cache scales linearly with added context. From both technical and economic perspectives, it’s infeasible to build AI systems that remember everything and continuously improve over years of use.==

This is where continual learning offers a solution. It enables AI to accumulate knowledge and skills across tasks over time, maintaining earlier capabilities while acquiring new ones. Unlike traditional models trained once and deployed statically, continual learning systems evolve in production — getting smarter with each interaction while avoiding catastrophic forgetting. Researchers and practitioners are pursuing this through innovations at both pre-training and post-training stages.

Architectural approaches fundamentally rethink how models learn:

- [Learning Machine](https://learning-machine.ai/) is building models that continuously learn during inference, as humans do. Through a new architecture and training paradigm, models will master the meta skill of "how to learn", enabling adaptation to individual users and enterprises post-deployment
- Core Automation is fundamentally rethinking transformer architecture to build systems where memory emerges naturally from novel attention mechanisms
- [Stanford and Nvidia’s TTT-E2E](https://arxiv.org/pdf/2512.23675) uses a sliding-window Transformer that continues learning at test time through next-token prediction on its context – compressing that context into its weights. During training, the model learns how to better update its own weights at inference, making the approach end-to-end

Near-term, production-ready solutions are also emerging:

- [“Cartridges” methodology](https://scalingintelligence.stanford.edu/pubs/cartridges/) stores long contexts in small KV caches trained offline once, then reused across different user requests during inference
- Sublinear Systems and foundation model labs are racing to address context limitations through novel techniques

**The spectrum of approaches we’ve seen for continual learning ranges from high-risk architectural moonshots that could redefine the field entirely to production-ready techniques that incrementally improve existing transformers. We’re eager to meet founders across this spectrum.**

Production deployment of continual learning requires new governance primitives that don’t yet exist in standard ML workflows. Rollback mechanisms enable reversion to stable checkpoints when updates introduce regressions, requiring full lineage tracking of weights, data, and hyperparameters. Isolation techniques allow safe experimentation without affecting core capabilities. Creating benchmarks, beyond needle-in-the-haystack tests, to gauge the performance of continual learning systems versus in-context learning will also be critical.

### 3\. Reinforcement learning platforms

With data quality fundamentally determining AI capabilities, the old machine learning axiom of “garbage in, garbage out” has never been more relevant. Data platforms such as [Mercor](https://www.mercor.com/), [Turing](https://www.turing.com/), and [micro1](https://www.micro1.ai/) have been instrumental in the AI revolution’s first wave by mobilizing human expertise to create high-quality datasets. But we believe that as AI systems evolve from pattern recognition to autonomous decision-making, a critical limitation has emerged: human-generated labeled data is no longer enough to enable production-grade AI. It cannot teach AI systems how to navigate complex, multi-step tasks with delayed consequences and compounding decisions.

This is where reinforcement learning (RL) becomes essential, as AI must learn through interaction rather than static datasets to ground the AI in “experience.” Leveraging an RL stack is now a cornerstone of AI infra tooling to teach agents complex behaviors without the cost and risk of real-world trial and error. Platforms in this emerging stack include:

| Environment building and experience curation | [Bespoke Labs](https://www.bespokelabs.ai/), [Deeptune](https://deeptune.com/), [Fleet](http://fleet.so/), [Habitat](https://www.habitat.inc/), [Matrices](https://matrices.ai/), [Mechanize,](https://www.mechanize.work/) [OpenReward](https://openreward.ai/), [Phinity](https://www.phinity.ai/), [Preference Model](https://www.preferencemodel.com/), [Proximal,](https://proximal.ai/) [SepalAI](https://www.sepalai.com/), [Steadyworks,](https://steadyworks.ai/) [Veris](https://veris.ai/), [VMax](https://vmax.ai/) |
| --- | --- |
| RL-as-a-service | [Applied Compute](https://appliedcompute.com/), [cgft](https://cgft.io/), [Metis](https://www.withmetis.ai/), [osmosis,](https://osmosis.ai/) [Trajectory](https://trajectory.ai/) |
| Platform infrastructure | [AgileRL](https://www.agilerl.com/), [Hud](https://www.hud.ai/), [Isidor](https://www.isidor.ai/), [OpenPipe](https://openpipe.ai/blog/announcing-6-7m-seed-raise), [Prime Intellect](https://www.primeintellect.ai/), [Tinker](https://thinkingmachines.ai/tinker/) |

### 4\. Inference inflection point

Model deployment and inference optimization emerged as a critical infrastructure layer in our 2024 roadmap, when vendors like [Fal](https://fal.ai/), [Together](https://www.together.ai/), [Baseten](https://www.baseten.co/), and [Fireworks](https://fireworks.ai/) ==pioneered efficient serving solutions. At that time, capital-intensive model training consumed the majority of compute resources across the AI stack. Today, we’re witnessing a fundamental shift in the compute center of gravity. As AI agents and applications transition from prototype to production at scale, inference workloads now rival — and in many cases exceed — training in both compute demand and economic importance. As NVIDIA’s== [Jensen Huang stated in his GTC 2026 keynote](https://www.youtube.com/watch?v=jw_o0xr8MWU), “Finally, AI is able to do productive work, and therefore the inflection point of inference has arrived.”

**This inflection point reflects a maturing market where the cost and performance of running AI systems continuously matter just as much as the initial investment in building them.**

A new generation of infrastructure startups is addressing this production imperative through specialized optimization across the inference stack. Companies like [TensorMesh](https://www.tensormesh.ai/) are leveraging [LMCache](https://lmcache.ai/) to eliminate redundant re-computation, [RadixArk](https://www.radixark.ai/) is advancing SGLang-based routing and scheduling for multi-turn conversations, and [Inferact](https://inferact.ai/) is pushing vLLM performance boundaries for high-throughput serving. [Gimlet Labs](https://gimletlabs.ai/) and even hyperscalers like [NVIDIA](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) are working on heterogeneous inference innovations purpose-built for complex agentic systems. These innovations translate cutting-edge systems research into measurable production gains: faster response times and lower costs.

We’re also seeing innovations in inference for novel deployments, with edge and on-device as one prime example. As AI proliferates all sectors of the economy, from robotics to consumer, AI deployments need to meet users where they are, which isn’t always cloud-based. We’re seeing companies such as [WebAI](https://www.webai.com/), [FemtoAI](https://femto.ai/), [PolarGrid](https://www.polargrid.ai/), [Aizip Mirai](https://aizip.ai/), and [OpenInfer](https://openinfer.io/) build at the very “edge” of what’s possible for on-device AI deployments in consumer devices. On-device innovations from model vendors such as [Perceptron](https://www.perceptron.inc/) are also important for physical AI, and we expect more in the space as we outlined in [our thinking on intelligent robotics](https://www.bvp.com/atlas/intelligent-robotics-the-new-era-of-physical-ai).

[Edge AI is also critical for industries such as defense](https://www.bvp.com/atlas/defense-tech-roadmap-five-frontiers-for-2026), where comms are jammed or denied; companies such as [TurbineOne](https://www.turbineone.com/), [Dominion Dynamics](https://www.bvp.com/news/dominion-dynamics-forging-the-future-of-interoperable-attritable-systems-for-arctic-and-allied-defense), [Picogrid](https://picogrid.com/), and [Breaker](https://breakerindustries.com/) are leading the charge on providing the infrastructure tooling for warfighters to harness the power of AI even in the most austere environments.

### 5\. World models

[The model layer is one of the most dynamic and hotly contested layers within the AI infrastructure stack](https://www.bvp.com/atlas/roadmap-ai-infrastructure#1-Innovations-in-scaling-novel-model-architectures-and-specialized-purpose-foundation-models). While LLMs have taken over language intelligence, a new class of models — world models — has emerged to deliver intelligence for the physical world.

As AI moves from our screens to our physical realities, new challenges arise: how does an AI "brain" develop intuition for physics and the world if it has no "body"? World models offer a solution. At the core, these are AI systems trained on real-world data — video, sensors, GPS, and more — that learn to predict how the world evolves given a current situation and action. Rather than describing reality, they simulate it.

Out of this newer research, three broad architectural paradigms have emerged. In practice, companies are also beginning to explore hybrids that combine elements of each:

- **Video-based world models** from companies such as [Reka](https://reka.ai/) and [Decart](https://decart.ai/) frame the problem as one of video generation, predicting future frames directly in pixel space. Because they generate outputs step-by-step, they can operate in real time and respond dynamically to new inputs, making them well-suited for interactive environments. Though they still struggle with maintaining physical consistency over longer horizons, they produce visually compelling outputs
- **Explicit 3D representation models** from companies such as [World Labs](https://www.worldlabs.ai/) take a different path, constructing persistent 3D scene representations that deliver strong spatial coherence at a lower inference cost. For now, these environments are pre-generated and static, but World Labs has signaled that real-time interactivity is on its roadmap
- **Latent predictive models**, based on Joint Embedding Predictive Architectures (JEPA) pioneered by [AMI Labs](https://amilabs.xyz/), avoid pixel generation altogether by forecasting future states in a compressed latent space. This approach is significantly more compute-efficient and sidesteps many visual failure modes, but comes with reduced interpretability. While each paradigm has seen meaningful progress, important gaps remain — how these are resolved will shape the path to the broader commercialization of world models

This commercial opportunity for world models is expansive. We recently shared our view of [world models in robotics](https://www.bvp.com/atlas/can-world-models-unlock-general-purpose-robotics), as this sector has been among the most visible early applications. By generating unlimited synthetic training environments, world models solve the data scarcity problem that has bottlenecked physical AI for decades. Autonomous driving is proving this as Waymo and Wayve use world models to simulate rare edge cases that no real-world test program could economically replicate. The same core capability unlocks even more, such as high-stakes simulation in defense, healthcare, industrial operations, and enterprise planning.

World models are not a vertical-specific kind of tool — they’re a new substrate for machine intelligence, analogous to what LLMs did for text-based reasoning. The industries that build on top of them early will have a significant head start on deploying agents that work in the real world. We’re excited about companies building the architectures and simulators that make world models possible across industries.

## Building infrastructure for AI to experience and enter the real world

While the first generation of AI infrastructure companies built the engines of intelligence — the models, compute clusters, and training pipelines that proved AI’s capability — the next generation must build the nervous system and harnesses that allow AI to sense, remember, adapt, and operate continuously in the real world. These frontiers represent more than incremental improvements to existing infrastructure. The companies building in these spaces aren’t just optimizing latency or reducing costs; they’re solving the fundamental challenges that separate impressive demos from reliable systems that create enduring value.

We believe 2026 will be the year when AI infrastructure’s center of gravity definitively shifts, reimagining what AI-native operations look like for this year and beyond. **We’re particularly excited to work with founders who are pursuing these endeavors. To get in touch with us, please contact aiinfra@bvp.com.**

<sup><b>Disclaimer</b>: The information presented here is for general informational and educational purposes only and does not constitute investment advice, a recommendation, or an offer or solicitation to buy or sell any securities or investment products. The information presented is also not intended as advertising material under the Investment Advisers Act. Certain companies discussed may be current or former portfolio companies. BVP may still have a financial interest in these companies. Any discussion of specific companies, securities, or investment strategies should not be considered a recommendation to take any particular action. Past performance is not indicative of future results. All investments involve risk, including possible loss of principal. Market conditions and investment returns can fluctuate significantly. Please visit <a href="https://www.bvp.com/legal">https://www.bvp.com/legal</a> for more information.</sup>