from agents.agriculture_agent import AgricultureAgent

agent = AgricultureAgent()

crop = agent.recommend_crop(
    90,
    42,
    43,
    20.8,
    82,
    6.5,
    202
)

print("Recommended Crop:", crop)