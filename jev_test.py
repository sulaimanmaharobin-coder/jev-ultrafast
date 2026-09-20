from typesafe_sdk import TypeSafeClient, Noul

with TypeSafeClient() as client:
    response = client.system_one(
        state={"document": "I was charged twice. Please fix this ASAP."},
        questions={
            "billing": Noul(instructions="Is this ticket about billing?"),
        },
    )
    print("P(billing) =", response.nouls["billing"].noul)
