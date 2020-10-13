#%%

import pandas as pd

#%%


df = pd.read_json("snippets.db", lines=True)


df["updated_date"] = pd.to_datetime(df["updatedAt"].apply(lambda x: x["$$date"]), unit="ms")


output = (
    df.sort_values(["_id", "updated_date"]).drop_duplicates(subset=["_id"], keep="last").drop(["updated_date"], axis=1)
)


output.to_json("snippets.db", orient="records", lines=True)
