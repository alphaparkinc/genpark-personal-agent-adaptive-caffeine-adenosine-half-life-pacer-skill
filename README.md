# Adaptive Caffeine Adenosine Half-Life & Sleep Latency Pacer Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Pharmacokinetic caffeine clearance half-life curve (CYP1A2 enzyme rate), bedtime adenosine sleep latency guard, and caffeine cutoff hour optimizer. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_circulating_caffeine_at_bedtime`: Calculate residual bloodstream caffeine mg at bedtime based on doses, timestamps, and CYP1A2 metabolic rate.
- `prescribe_caffeine_curfew`: Compute absolute caffeine curfew hour to keep residual caffeine < 25mg at bedtime.

## 🚀 Installation & Usage
```bash
python -m genpark_personal_agent_adaptive_caffeine_adenosine_half_life_pacer_skill.server --test
```
